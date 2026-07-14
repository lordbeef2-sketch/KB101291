# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=2751 end=3000 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-module.html language=enus -->
## TOPIC 02751: Step.Module

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-module.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-module.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Module Data Type Module Purpose Returns a reference to the Module object related to the current step. Remarks You must acquire the module interface for the specific adapter from the object this property returns to specify the code module name, location, and parameters for the Module obje

### Step.Module

#### Syntax

[Step](step.html).Module

#### Data Type

[Module](module.html)

#### Purpose

Returns a reference to the Module object related to the current step.

#### Remarks

You must acquire the module interface for the specific adapter from the object this property returns to specify the code module name, location, and parameters for the Module object.

#### See Also

[Module](module.html)

[Module.Adapter](module-adapter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-moduleloadoption.html language=enus -->
## TOPIC 02752: Step.ModuleLoadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-moduleloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-moduleloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ModuleLoadOption Data Type ModuleLoadOptions Use the following constants with this data type: LoadOption_DynamicLoad –(Value: 3) Does not load the code module for a step until the step is ready to call it. LoadOption_PreloadWhenExecuted –(Value: 2) Loads the code module for a step when a

### Step.ModuleLoadOption

#### Syntax

[Step](step.html).ModuleLoadOption

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

Specifies the option that determines when TestStand loads the code module for the step.

#### Remarks

The
 SequenceFile.ModuleLoadOption
 property takes precedence over this property, unless the value of the
 SequenceFile.ModuleLoadOption
 property is
 LoadOption_UseStepLoadOption
 .

#### See Also

[SequenceFile.ModuleLoadOption](sequencefile-moduleloadoption.html)

[Step.ModuleUnloadOption](step-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-moduleunloadoption.html language=enus -->
## TOPIC 02753: Step.ModuleUnloadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-moduleunloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-moduleunloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ModuleUnloadOption Data Type ModuleUnloadOptions Use the following constants with this data type: UnloadOption_AfterSequenceExecution –(Value: 3) Unloads the code module for a step after the sequence containing the step finishes executing. UnloadOption_AfterStepExecution –(Value: 2) Unlo

### Step.ModuleUnloadOption

#### Syntax

[Step](step.html).ModuleUnloadOption

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

Specifies the option that determines when TestStand unloads the code module for the step.

#### Remarks

The
 SequenceFile.ModuleUnloadOption
 property takes precedence over this property, unless the value of the
 SequenceFile.ModuleUnloadOption
 property is
 UnloadOption_UseStepUnloadOption
 .

#### See Also

[SequenceFile.ModuleUnloadOption](sequencefile-moduleunloadoption.html)

[Step.ModuleLoadOption](step-moduleloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-mutexnameorrefexpr.html language=enus -->
## TOPIC 02754: Step.MutexNameOrRefExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-mutexnameorrefexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-mutexnameorrefexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.MutexNameOrRefExpr Data Type String Purpose Specifies which lock the step acquires and releases. This property is ignored if the Step.UseMutex property is False . Remarks Enter a string expression to specify the name of an existing lock. You can also enter an expression that evaluates an

### Step.MutexNameOrRefExpr

#### Syntax

[Step](step.html).MutexNameOrRefExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies which lock the step acquires and releases. This property is ignored if the
 [Step.UseMutex](step-usemutex.html)
 property is
 False
 .

#### Remarks

Enter a string expression to specify the name of an existing lock. You can also enter an expression that evaluates an ActiveX reference to an existing Lock object.

Pass an empty string to specify that TestStand uses a lock unique to the step.

#### See Also

[Step.BatchSyncOption](step-batchsyncoption.html)

[Step.UseMutex](step-usemutex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-name.html language=enus -->
## TOPIC 02755: Step.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Name Data Type String Purpose Specifies the name of the step. Remarks You can use the following code snippet to set the default name of the new step: Step.Name = Step.StepType.AsPropertyObject.EvaluateEx(Step.StepType.DefaultNameExpr, EvalOption_DoNotAlterValues).GetValString("", 0) Test

### Step.Name

#### Syntax

[Step](step.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the step.

#### Remarks

You can use the following code snippet to set the default name of the new step:

Step.Name = Step.StepType.AsPropertyObject.EvaluateEx(Step.StepType.DefaultNameExpr, EvalOption_DoNotAlterValues).GetValString("", 0)

Note

PropertyObject.ValidateNewName

#### See Also

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[Step.GetDescriptionEx](step-getdescriptionex.html)

[Step.GetStepSettingsString](step-getstepsettingsstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-passaction.html language=enus -->
## TOPIC 02756: Step.PassAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-passaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-passaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.PassAction Data Type String Purpose Specifies the type of post action you want to occur if the step passes. Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues Step.PassActionTargetByExpr

### Step.PassAction

#### Syntax

[Step](step.html).PassAction

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of post action you want to occur if the step passes.

#### Remarks

Assign a
 [PostActionValues](postactionvalues.html)
 string constant to the property to specify the type of post action to perform.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.PassActionTargetByExpr](step-passactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-passactiontarget.html language=enus -->
## TOPIC 02757: Step.PassActionTarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-passactiontarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-passactiontarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.PassActionTarget Data Type String Purpose This property is obsolete. Use the Step.PassActionTargetByExpr property instead. Remarks Specifies the target for the post action the Step.PassAction property specifies. Post action targets are now expressions. If you set the target using this pr

### Step.PassActionTarget

#### Syntax

[Step](step.html).PassActionTarget

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.PassActionTargetByExpr

#### Remarks

Specifies the target for the post action the
 [Step.PassAction](step-passaction.html)
 property specifies. Post action targets are now expressions. If you set the target using this property, TestStand converts the target into a string constant expression before storing it. If you attempt to obtain the target using this property and it is a string constant expression, TestStand converts the target back into the string it represents and returns the string to you. If the target is not a string constant but is a more complex expression, TestStand returns an error if you try to obtain the value using this property.

If the
 Step.PassAction
 property is
 [PostAction_GotoStep](postactionvalues.html)
 , the target is the name of the step. If the
 Step.PassAction
 property is
 [PostAction_CallCallback](postactionvalues.html)
 , the target is the name of the callback sequence. For all other types of post actions, the target property is not used.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.PassAction](step-passaction.html)

[Step.PassActionTargetByExpr](step-passactiontargetbyexpr.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-passactiontargetbyexpr.html language=enus -->
## TOPIC 02758: Step.PassActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-passactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-passactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.PassActionTargetByExpr Data Type String Purpose Specifies the target for the post action the Step.PassAction property specifies. Remarks If the Step.PassAction property is PostAction_GotoStep , the target is the name of the step. If the Step.PassAction property is PostAction_CallCallback

### Step.PassActionTargetByExpr

#### Syntax

[Step](step.html).PassActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [Step.PassAction](step-passaction.html)
 property specifies.

#### Remarks

If the
 Step.PassAction
 property is
 [PostAction_GotoStep](postactionvalues.html)
 , the target is the name of the step. If the
 Step.PassAction
 property is
 [PostAction_CallCallback](postactionvalues.html)
 , the target is the name of the callback sequence. For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant (the name of the target in quotation marks).

#### See Also

[PostActionValues](postactionvalues.html)

[Step.PassAction](step-passaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-postexpression.html language=enus -->
## TOPIC 02759: Step.PostExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-postexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-postexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.PostExpression Data Type String Purpose Specifies the Post expression for the step. Remarks TestStand evaluates the Post expression after calling the code module and Post-Step substep for the step. See Also Step.PreExpression Step.StatusExpression

### Step.PostExpression

#### Syntax

[Step](step.html).PostExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Post expression for the step.

#### Remarks

TestStand evaluates the Post expression after calling the code module and Post-Step substep for the step.

#### See Also

[Step.PreExpression](step-preexpression.html)

[Step.StatusExpression](step-statusexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-precondition.html language=enus -->
## TOPIC 02760: Step.Precondition

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-precondition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-precondition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Precondition Data Type String Purpose Specifies an expression that must evaluate to True or be empty to execute the step. Remarks This string is an expression with a Boolean result. Use the AnyOf() and AllOf() expression functions to specify more than one expression. The following is an

### Step.Precondition

#### Syntax

[Step](step.html).Precondition

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression that must evaluate to
 True
 or be empty to execute the step.

#### Remarks

This string is an expression with a Boolean result. Use the AnyOf() and AllOf() expression functions to specify more than one expression. The following is an example of an expression for a precondition based on the results of another step:

RunState.Sequence.Main["NameOfAnotherStep"].Result.Status == "Passed"

#### See Also

[Engine.DisplayPreconditionDialog](engine-displaypreconditiondialog.html)

[Step.EvalPrecondForInteractiveExecution](step-evalprecondforinteractiveexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-preexpression.html language=enus -->
## TOPIC 02761: Step.PreExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-preexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-preexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.PreExpression Data Type String Purpose Specifies the Pre expression for the step. Remarks TestStand evaluates the Pre expression before it calls the Pre-Step substep and code module for the step. See Also Step.PostExpression Step.StatusExpression

### Step.PreExpression

#### Syntax

[Step](step.html).PreExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Pre expression for the step.

#### Remarks

TestStand evaluates the Pre expression before it calls the Pre-Step substep and code module for the step.

#### See Also

[Step.PostExpression](step-postexpression.html)

[Step.StatusExpression](step-statusexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-recordloopiterationresults.html language=enus -->
## TOPIC 02762: Step.RecordLoopIterationResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-recordloopiterationresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-recordloopiterationresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.RecordLoopIterationResults Data Type Boolean Purpose Specifies whether to add the step results to the sequence results list after each loop iteration. Remarks TestStand also adds the final result it computes for the step loop as a whole if you enable the Step.ResultRecordingOption proper

### Step.RecordLoopIterationResults

#### Syntax

[Step](step.html).RecordLoopIterationResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to add the step results to the sequence results list after each loop iteration.

#### Remarks

TestStand also adds the final result it computes for the step loop as a whole if you enable the
 [Step.ResultRecordingOption](step-resultrecordingoption.html)
 property for the step.

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopType](step-looptype.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-recordresult.html language=enus -->
## TOPIC 02763: Step.RecordResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-recordresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-recordresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.RecordResult Data Type Boolean Purpose This property is obsolete. Use the Step.ResultRecordingOption property instead. Remarks Specifies whether to record the Result properties of the step. If you set this property to True , TestStand records the result of the step, unless the Engine.Dis

### Step.RecordResult

#### Syntax

[Step](step.html).RecordResult

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Step.ResultRecordingOption

#### Remarks

Specifies whether to record the Result properties of the step. If you set this property to
 True
 , TestStand records the result of the step, unless the
 [Engine.DisableResults](engine-disableresults.html)
 property is
 True
 or the
 [Sequence.DisableResults](sequence-disableresults.html)
 property is
 True
 .

For steps that loop, use the
 [Step.RecordLoopIterationResults](step-recordloopiterationresults.html)
 property to specify to add step results to the sequence result list after each loop iteration.

#### See Also

[Engine.DisableResults](engine-disableresults.html)

[Sequence.DisableResults](sequence-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[Step.RecordLoopIterationResults](step-recordloopiterationresults.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-requirements.html language=enus -->
## TOPIC 02764: Step.Requirements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-requirements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-requirements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Requirements Data Type PropertyObject Purpose Returns the Requirements property for the step. The Links subproperty of the Requirements property is an array of string values that represents the product and unit requirements the step covers. Remarks You can use the following pseudocode to

### Step.Requirements

#### Syntax

[Step](step.html).Requirements

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the Requirements property for the step. The Links subproperty of the Requirements property is an array of string values that represents the product and unit requirements the step covers.

#### Remarks

You can use the following pseudocode to add a new element to the list of requirements:

PropertyObject links = step.Requirements.GetPropertyObject("Links", 0);
 int nextAvailableIndex = links.GetNumElements();
 links.SetValStringByOffset(nextAvailableIndex, PropertyOptions.PropOption_InsertElement, "REQ_ABC");

#### See Also

[PropertyObject](propertyobject.html)

[PropertyObjectFile.Requirements](propertyobjectfile-requirements.html)

[Sequence.Requirements](sequence-requirements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-resultrecordingoption.html language=enus -->
## TOPIC 02765: Step.ResultRecordingOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-resultrecordingoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-resultrecordingoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ResultRecordingOption Data Type ResultRecordingOptions Use the following constants with this data type: ResultRecordingOption_Disabled –(Value: 0) Specifies that the step does not record results. ResultRecordingOption_Enabled –(Value: 1) Specifies that the step records results unless the

### Step.ResultRecordingOption

#### Syntax

[Step](step.html).ResultRecordingOption

#### Data Type

[ResultRecordingOptions](resultrecordingoptions.html)

Use the following constants with this data type:

- ResultRecordingOption_Disabled 
 –(Value: 0) Specifies that the step does not record results.
- ResultRecordingOption_Enabled 
 –(Value: 1) Specifies that the step records results unless the
 Sequence.DisableResults 
 or
 StationOptions.DisableResults 
 property is
 True 
 .
- ResultRecordingOption_EnabledAndOverrideSequenceSetting 
 –(Value: 2) Specifies that the step records results unless the
 StationOptions.DisableResults 
 property is
 True 
 .

#### Purpose

Specifies whether to record the result properties of the step.

#### Remarks

For steps that loop, use the
 [Step.RecordLoopIterationResults](step-recordloopiterationresults.html)
 property to specify to add step results to the sequence result list after each loop iteration.

#### See Also

[Sequence.DisableResults](sequence-disableresults.html)

[Step.RecordLoopIterationResults](step-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-resultstatus.html language=enus -->
## TOPIC 02766: Step.ResultStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-resultstatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-resultstatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ResultStatus Data Type String Purpose Specifies the status string for the step. Remarks Although you can define custom status strings, you usually set this property to one of the ResultStatus_ constants of StepProperties . See Also Step.GetResultStatusDisplayString Step.StatusExpression

### Step.ResultStatus

#### Syntax

[Step](step.html).ResultStatus

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the status string for the step.

#### Remarks

Although you can define custom status strings, you usually set this property to one of the
 ResultStatus_
 constants of
 [StepProperties](stepproperties.html)
 .

#### See Also

[Step.GetResultStatusDisplayString](step-getresultstatusdisplaystring.html)

[Step.StatusExpression](step-statusexpression.html)

[StepProperties](stepproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-runmode.html language=enus -->
## TOPIC 02767: Step.RunMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-runmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-runmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.RunMode Data Type String Purpose This property is obsolete. Use the Step.GetRunModeEx and Step.SetRunModeEx methods instead. Remarks Specifies the run mode of the step. Although you can use this property, it is now equivalent to setting or getting the sequence file version of the run mod

### Step.RunMode

#### Syntax

[Step](step.html).RunMode

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.GetRunModeEx

Step.SetRunModeEx

#### Remarks

Specifies the run mode of the step. Although you can use this property, it is now equivalent to setting or getting the sequence file version of the run mode.

The
 [RunModes](runmodes.html)
 constants define the valid values for this property.

This property is the run mode TestStand stores for the step in the sequence file. To set the run mode temporarily, set the
 Step.RunTimeRunMode
 property instead. Setting this property also sets the
 Step.RunTimeRunMode
 property. In the sequence editor, the Sequence File window shows this property for the steps, and the Execution window shows the
 Step.RunTimeRunMode
 property for the steps.

Note

Step.RunTimeRunMode

Step.GetRunModeEx

Step.SetRunModeEx

#### See Also

[RunModes](runmodes.html)

[Step.GetRunModeEx](step-getrunmodeex.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-runtimerunmode.html language=enus -->
## TOPIC 02768: Step.RunTimeRunMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-runtimerunmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-runtimerunmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.RunTimeRunMode Data Type String Purpose This property is obsolete. Use the Step.GetRunModeEx and Step.SetRunModeEx methods instead. Remarks Specifies the run-time run mode of the step. Although you can use this property, it is now equivalent to setting or getting the sequence file versio

### Step.RunTimeRunMode

#### Syntax

[Step](step.html).RunTimeRunMode

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.GetRunModeEx

Step.SetRunModeEx

#### Remarks

Specifies the run-time run mode of the step. Although you can use this property, it is now equivalent to setting or getting the sequence file version of the run mode.

The
 [RunModes](runmodes.html)
 constants define the valid values for this property.

This property is the run mode TestStand uses when it executes the sequence file. When running a step, TestStand copies the value of the
 Step.RunMode
 property to this property if you have not already explicitly set this property. Unlike the
 Step.RunMode
 property, the value of this property is not saved but is discarded when the sequence file is unloaded. Setting this property has no effect on the
 Step.RunMode
 property. In the sequence editor, the Sequence File window shows the
 Step.RunMode
 property for the steps, and the Execution window shows the
 Step.RunTimeRunMode
 property for the steps.

Note

Step.RunMode

Step.GetRunModeEx

Step.SetRunModeEx

#### See Also

[RunModes](runmodes.html)

[Step.GetRunModeEx](step-getrunmodeex.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-sequence.html language=enus -->
## TOPIC 02769: Step.Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Sequence Data Type Sequence Purpose Returns a reference to the sequence in which the step resides. Remarks Returns a NULL reference if the step is not currently inserted into a sequence. This property returns the run-time copy of a sequence if called on the run-time copy of a step. See A

### Step.Sequence

#### Syntax

[Step](step.html).Sequence

#### Data Type

[Sequence](sequence.html)

#### Purpose

Returns a reference to the sequence in which the step resides.

#### Remarks

Returns a
 NULL
 reference if the step is not currently inserted into a sequence. This property returns the run-time copy of a sequence if called on the run-time copy of a step.

#### See Also

[Sequence](sequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-setbreakonstepex.html language=enus -->
## TOPIC 02770: Step.SetBreakOnStepEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-setbreakonstepex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-setbreakonstepex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SetBreakOnStepEx( newBreakSetting, [executionParam]) Purpose This method is obsolete. Use the Step.SetBreakSettings method instead. Remarks Sets or unsets a breakpoint on the step. Parameters newBreakSetting As Boolean [In] Pass True to set a breakpoint on the step or False to unset a br

### Step.SetBreakOnStepEx

#### Syntax

[Step](step.html).SetBreakOnStepEx( newBreakSetting, [executionParam])

#### Purpose

Note

Step.SetBreakSettings

#### Remarks

Sets or unsets a breakpoint on the step.

#### Parameters

newBreakSetting
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to set a breakpoint on the step or
 False
 to unset a breakpoint.

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object to obtain the breakpoint settings on a step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method sets the breakpoint setting on the step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Step.GetBreakSettings](step-getbreaksettings.html)

[Step.SetBreakSettings](step-setbreaksettings.html)

Parent topic:

Obsolete Step Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-setbreaksettings.html language=enus -->
## TOPIC 02771: Step.SetBreakSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-setbreaksettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-setbreaksettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SetBreakSettings( isSet, enabled, passCount, Condition, [executionParam]) Purpose Specifies if the step of the sequence is set to break. Parameters isSet As Boolean [In] Specifies if the breakpoint is set. enabled As Boolean [In] Specifies if the breakpoint is enabled. TestStand ignores

### Step.SetBreakSettings

#### Syntax

[Step](step.html).SetBreakSettings( isSet, enabled, passCount, Condition, [executionParam])

#### Purpose

Specifies if the step of the sequence is set to break.

#### Parameters

isSet
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies if the breakpoint is set.

enabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies if the breakpoint is enabled. TestStand ignores disabled breakpoints during execution.

passCount
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the number of iterations the execution skips the breakpoint before suspending execution. Pass
 0
 if you do not want to use a conditional pass count.

Condition
 As
 [String](data-types-for-teststand.html)

[In] Specifies the expression that must evaluate to
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
 ] Specifies a reference to an Execution object to update the breakpoint settings on a step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method sets the breakpoint setting on the step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.GetBreakOnEndSettings](sequence-getbreakonendsettings.html)

[Sequence.SetBreakOnEndSettings](sequence-setbreakonendsettings.html)

[Step.GetBreakSettings](step-getbreaksettings.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-setrunmodeex.html language=enus -->
## TOPIC 02772: Step.SetRunModeEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-setrunmodeex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-setrunmodeex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SetRunModeEx( newRunMode, [executionParam]) Purpose Sets the run mode of a step. Remarks You can set the run mode either for the sequence file or for a particular execution. If you pass an Execution object for the executionParam parameter, the run mode change applies only to that executi

### Step.SetRunModeEx

#### Syntax

[Step](step.html).SetRunModeEx( newRunMode, [executionParam])

#### Purpose

Sets the run mode of a step.

#### Remarks

You can set the run mode either for the sequence file or for a particular execution. If you pass an Execution object for the
 executionParam
 parameter, the run mode change applies only to that execution and is lost when the execution is destroyed. If you do not pass an Execution object, the run mode change effects all current and future executions and is saved when you save the sequence file.

#### Parameters

newRunMode
 As
 [String](data-types-for-teststand.html)

[In] The
 [RunModes](runmodes.html)
 constants define the valid values for this parameter.

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you want to set the run mode for a particular execution only, pass a reference to an Execution object.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[RunModes](runmodes.html)

[Step.GetRunModeEx](step-getrunmodeex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-smallicon.html language=enus -->
## TOPIC 02773: Step.SmallIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-smallicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-smallicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SmallIcon Data Type Picture Purpose Returns the small version of the icon that represents the step. Remarks The step type defines the icon the property returns. If the step type does not specify an icon, the property returns the icon the Adapter of the step specifies. See Also Adapter En

### Step.SmallIcon

#### Syntax

[Step](step.html).SmallIcon

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns the small version of the icon that represents the step.

#### Remarks

The step type defines the icon the property returns. If the step type does not specify an icon, the property returns the icon the
 [Adapter](adapter.html)
 of the step specifies.

#### See Also

[Adapter](adapter.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[Step.IconName](step-iconname.html)

[Step.LargeIcon](step-largeicon.html)

[Step.SmallIconIndex](step-smalliconindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-smalliconindex.html language=enus -->
## TOPIC 02774: Step.SmallIconIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-smalliconindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-smalliconindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SmallIconIndex Data Type Long Purpose Returns a unique index for the small version of the icon that represents the step. You can use this index to retrieve the icon image from the image list you obtain with the Engine.SmallImageList property. See Also Engine.SmallImageList Step.IconName

### Step.SmallIconIndex

#### Syntax

[Step](step.html).SmallIconIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique index for the small version of the icon that represents the step. You can use this index to retrieve the icon image from the image list you obtain with the
 [Engine.SmallImageList](engine-smallimagelist.html)
 property.

#### See Also

[Engine.SmallImageList](engine-smallimagelist.html)

[Step.IconName](step-iconname.html)

[Step.LargeIconIndex](step-largeiconindex.html)

[Step.SmallIcon](step-smallicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-specifymodule.html language=enus -->
## TOPIC 02775: Step.SpecifyModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-specifymodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-specifymodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SpecifyModule( specModOptions = SpecMod_NoOptions) Return Value Boolean Returns True if the Specify Module dialog box modifies the step. Purpose Launches the Specify Module dialog box for the step, if one exists. Remarks Check the Step.CanSpecifyModule property to verify that you can cal

### Step.SpecifyModule

#### Syntax

[Step](step.html).SpecifyModule( specModOptions = SpecMod_NoOptions)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the
 [Specify Module](../tsref/edit-activex-com-call-dialog-box.html)
 dialog box modifies the step.

#### Purpose

Launches the Specify Module dialog box for the step, if one exists.

#### Remarks

Check the
 [Step.CanSpecifyModule](step-canspecifymodule.html)
 property to verify that you can call this method.

The current version of TestStand does not support all
 [SpecifyModuleOptions](specifymoduleoptions.html)
 options for all adapters, as the following list indicates:

- LabVIEW Adapter 
 —Only supports
 SpecMod_ReadOnly 
 .
- LabWindows/CVI Adapter 
 —Supports all options.
- C/C++ DLL Adapter 
 —Supports all options.
- .NET 
 —Only supports
 SpecMod_ReadOnly 
 .
- ActiveX/COM Adapter 
 —Only supports
 SpecMod_ReadOnly 
 .
- Sequence Adapter 
 —Supports all options.
- HTBasic Adapter 
 —Only supports
 SpecMod_ReadOnly 
 .

#### Parameters

specModOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [SpecifyModuleOptions](specifymoduleoptions.html)
 to modify the behavior of the dialog box.

This parameter has a default value of
 SpecMod_NoOptions
 .

#### See Also

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

[SpecifyModuleOptions](specifymoduleoptions.html)

[Step.CanSpecifyModule](step-canspecifymodule.html)

[Step.CreateCode](step-createcode.html)

[Step.EditCode](step-editcode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-statusexpression.html language=enus -->
## TOPIC 02776: Step.StatusExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-statusexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-statusexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.StatusExpression Data Type String Purpose Specifies the status expression for the step. Remarks Use this expression to set the ResultStatus property of the step. TestStand executes this expression after executing all other substeps and expressions for the step. The expression must evalua

### Step.StatusExpression

#### Syntax

[Step](step.html).StatusExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the status expression for the step.

#### Remarks

Use this expression to set the ResultStatus property of the step. TestStand executes this expression after executing all other substeps and expressions for the step. The expression must evaluate to a string.

#### See Also

[Step.PostExpression](step-postexpression.html)

[Step.PreExpression](step-preexpression.html)

[Step.ResultStatus](step-resultstatus.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-stepfailcausessequencefail.html language=enus -->
## TOPIC 02777: Step.StepFailCausesSequenceFail

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-stepfailcausessequencefail.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-stepfailcausessequencefail.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.StepFailCausesSequenceFail Data Type Boolean Purpose Specifies if failure of the step causes the sequence to fail. Remarks If this property is True and the step fails, TestStand sets the internal status property of the sequence that contains the step to Failure . If the Sequence.FailureA

### Step.StepFailCausesSequenceFail

#### Syntax

[Step](step.html).StepFailCausesSequenceFail

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if failure of the step causes the sequence to fail.

#### Remarks

If this property is
 True
 and the step fails, TestStand sets the internal status property of the sequence that contains the step to
 Failure
 . If the
 [Sequence.FailureAction](sequence-failureaction.html)
 property is
 True
 for the sequence, the execution then jumps to the Cleanup step group of the sequence.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[Step.CausedSequenceFailure](step-causedsequencefailure.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-stepgroup.html language=enus -->
## TOPIC 02778: Step.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose Returns the step g

### Step.StepGroup

#### Syntax

[Step](step.html).StepGroup

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

Returns the step group in which the step currently resides.

#### Remarks

If the step is not currently inserted in a sequence, accessing this property returns an error.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-stepindex.html language=enus -->
## TOPIC 02779: Step.StepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-stepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-stepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.StepIndex Data Type Long Purpose Returns the zero-based index that indicates where in the step group the step resides. Remarks If the step is not currently inserted in a sequence, accessing this property returns an error. See Also Step.Sequence Step.StepGroup

### Step.StepIndex

#### Syntax

[Step](step.html).StepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the zero-based index that indicates where in the step group the step resides.

#### Remarks

If the step is not currently inserted in a sequence, accessing this property returns an error.

#### See Also

[Step.Sequence](step-sequence.html)

[Step.StepGroup](step-stepgroup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-steptype.html language=enus -->
## TOPIC 02780: Step.StepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-steptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-steptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.StepType Data Type StepType Purpose Returns the step type for this step. See Also StepType

### Step.StepType

#### Syntax

[Step](step.html).StepType

#### Data Type

[StepType](steptype.html)

#### Purpose

Returns the step type for this step.

#### See Also

[StepType](steptype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecconnectionlifetime.html language=enus -->
## TOPIC 02781: Step.SwitchExecConnectionLifetime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecconnectionlifetime.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecconnectionlifetime.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecConnectionLifetime Data Type SwitchExecLifetimes Use the following constants with this data type: SwitchExecLifetime_Execution –(Value: 1) Specifies that the route is connected until the execution completes. SwitchExecLifetime_Manual –(Value: 0) Specifies that the route is conn

### Step.SwitchExecConnectionLifetime

#### Syntax

[Step](step.html).SwitchExecConnectionLifetime

#### Data Type

[SwitchExecLifetimes](switchexeclifetimes.html)

Use the following constants with this data type:

- SwitchExecLifetime_Execution 
 –(Value: 1) Specifies that the route is connected until the execution completes.
- SwitchExecLifetime_Manual 
 –(Value: 0) Specifies that the route is connected until manually disconnected.
- SwitchExecLifetime_Sequence 
 –(Value: 3) Specifies that the route is connected until the sequence completes executing.
- SwitchExecLifetime_Step 
 –(Value: 4) Specifies that the route is connected until the step completes executing.
- SwitchExecLifetime_Thread 
 –(Value: 2) Specifies that the route is connected until the thread completes.

#### Purpose

Specifies the lifetime that TestStand applies to routes when the value of the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property is
 Connect
 or
 ConnectDisconnect
 . You can specify whether you want the route to exist until manually disconnected later or until the step, sequence, thread, or execution completes.

Note

Step.SwitchExecMulticonnectMode

Multiconnect

Manual

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecMulticonnectMode](step-switchexecmulticonnectmode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecenabled.html language=enus -->
## TOPIC 02782: Step.SwitchExecEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecEnabled Data Type Boolean Purpose Specifies whether to perform a switching operation for the step. The step performs the switching operation the Step.SwitchExecOperation property specifies for the virtual device the Step.SwitchExecVirtualDevice property specifies. This feature

### Step.SwitchExecEnabled

#### Syntax

[Step](step.html).SwitchExecEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to perform a switching operation for the step. The step performs the switching operation the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property specifies for the virtual device the
 [Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)
 property specifies.

Note

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecmulticonnectmode.html language=enus -->
## TOPIC 02783: Step.SwitchExecMulticonnectMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecmulticonnectmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecmulticonnectmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecMulticonnectMode Data Type SwitchExecMulticonnectModes Use the following constants with this data type: SwitchExecMulticonnectMode_Default –(Value: -1) Defaults to the multiconnect mode as predefined for each route in the NI Switch Executive. SwitchExecMulticonnectMode_Multicon

### Step.SwitchExecMulticonnectMode

#### Syntax

[Step](step.html).SwitchExecMulticonnectMode

#### Data Type

[SwitchExecMulticonnectModes](switchexecmulticonnectmodes.html)

Use the following constants with this data type:

- SwitchExecMulticonnectMode_Default 
 –(Value: -1) Defaults to the multiconnect mode as predefined for each route in the NI Switch Executive.
- SwitchExecMulticonnectMode_Multiconnect 
 –(Value: 1) A route can connect multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple Connect operations for a specific route, the route is not physically disconnected until an equal number of Disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
- SwitchExecMulticonnectMode_None 
 –(Value: 0) A route can connect only once.

#### Purpose

Specifies the behavior when more than one connection operation occurs on a specific route.

Note

Multiconnect

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecoperation.html language=enus -->
## TOPIC 02784: Step.SwitchExecOperation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecoperation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecoperation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecOperation Data Type SwitchExecOperations Use the following constants with this data type: SwitchExecOperation_Connect –(Value: 1) Creates the paths for the specified routes in the Step.SwitchExecRoutesToConnect property. SwitchExecOperation_ConnectDisconnect –(Value: 4) Creates

### Step.SwitchExecOperation

#### Syntax

[Step](step.html).SwitchExecOperation

#### Data Type

[SwitchExecOperations](switchexecoperations.html)

Use the following constants with this data type:

- SwitchExecOperation_Connect 
 –(Value: 1) Creates the paths for the specified routes in the
 Step.SwitchExecRoutesToConnect 
 property.
- SwitchExecOperation_ConnectDisconnect 
 –(Value: 4) Creates the paths for the routes specified in the
 Step.SwitchExecRoutesToConnect 
 property and destroys the paths for the routes specified in the
 Step.SwitchExecRoutesToDisconnect 
 property. Use the
 Step.SwitchExecOperationOrder 
 property to specify whether the Disconnect operation occurs before or after the Connect operation.
- SwitchExecOperation_Disconnect 
 –(Value: 2) Destroys the paths the specified routes define in the
 Step.SwitchExecRoutesToDisconnect 
 property.
- SwitchExecOperation_DisconnectAll 
 –(Value: 3) Disconnects all previously created paths.

#### Purpose

Specifies whether to connect or disconnect the routes the
 Step.SwitchExecRoutesToConnect
 and
 Step.SwitchExecRoutesToDisconnect
 properties specify, or disconnect all previously connected routes for a virtual device.

Note

Step.SwitchExecWaitForDebounce

#### See Also

[Step.SwitchExecOperationOrder](step-switchexecoperationorder.html)

[Step.SwitchExecRoutesToConnect](step-switchexecroutestoconnect.html)

[Step.SwitchExecRoutesToDisconnect](step-switchexecroutestodisconnect.html)

[Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)

[Step.SwitchExecWaitForDebounce](step-switchexecwaitfordebounce.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecoperationorder.html language=enus -->
## TOPIC 02785: Step.SwitchExecOperationOrder

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecoperationorder.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecoperationorder.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecOperationOrder Data Type SwitchExecOperationOrders Use the following constants with this data type: SwitchExecOperationOrder_DisconnectAfterConnect –(Value: 2) Specifies to connect routes before disconnecting any routes. Use this mode of operation when you are switching electri

### Step.SwitchExecOperationOrder

#### Syntax

[Step](step.html).SwitchExecOperationOrder

#### Data Type

[SwitchExecOperationOrders](switchexecoperationorders.html)

Use the following constants with this data type:

- SwitchExecOperationOrder_DisconnectAfterConnect 
 –(Value: 2) Specifies to connect routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to the source.
- SwitchExecOperationOrder_DisconnectBeforeConnect 
 –(Value: 1) Specifies to disconnect routes before connecting any routes. This is the typical mode of operation.

#### Purpose

Specifies whether the Disconnect operation occurs before or after the Connect operation when the value of the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property is
 ConnectDisconnect
 .

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecroutestoconnect.html language=enus -->
## TOPIC 02786: Step.SwitchExecRoutesToConnect

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecroutestoconnect.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecroutestoconnect.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecRoutesToConnect Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the routes to connect when the value of the Step.SwitchExecOperation property is Connect or ConnectDisconnect . The expression must be a valid route specification strin

### Step.SwitchExecRoutesToConnect

#### Syntax

[Step](step.html).SwitchExecRoutesToConnect

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the routes to connect when the value of the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property is
 Connect
 or
 ConnectDisconnect
 .

Note

route specification string

Step.SwitchExecVirtualDevice

#### See Also

[Route Specification String](/csh?context=ts_tsref_route_spec_string)

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecroutestodisconnect.html language=enus -->
## TOPIC 02787: Step.SwitchExecRoutesToDisconnect

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecroutestodisconnect.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecroutestodisconnect.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecRoutesToDisconnect Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the routes to disconnect when the value of the Step.SwitchExecOperation property is Disconnect or ConnectDisconnect . The expression must be a valid route specificat

### Step.SwitchExecRoutesToDisconnect

#### Syntax

[Step](step.html).SwitchExecRoutesToDisconnect

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the routes to disconnect when the value of the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property is
 Disconnect
 or
 ConnectDisconnect
 .

Note

route specification string

Step.SwitchExecVirtualDevice

#### See Also

[Route Specification String](/csh?context=ts_tsref_route_spec_string)

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecVirtualDevice](step-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecvirtualdevice.html language=enus -->
## TOPIC 02788: Step.SwitchExecVirtualDevice

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecvirtualdevice.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecvirtualdevice.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecVirtualDevice Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the virtual device name on which to perform the switching operation. Remarks NI Switch Executive software in Measurement & Automation Explorer defines the virtual device

### Step.SwitchExecVirtualDevice

#### Syntax

[Step](step.html).SwitchExecVirtualDevice

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the virtual device name on which to perform the switching operation.

#### Remarks

Note

#### See Also

[Step.SwitchExecEnabled](step-switchexecenabled.html)

[Step.SwitchExecOperation](step-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-switchexecwaitfordebounce.html language=enus -->
## TOPIC 02789: Step.SwitchExecWaitForDebounce

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-switchexecwaitfordebounce.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-switchexecwaitfordebounce.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.SwitchExecWaitForDebounce Data Type Boolean Purpose Specifies if the operation the Step.SwitchExecOperation property specifies waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after both the Connect and Disconnect operations are complete. See

### Step.SwitchExecWaitForDebounce

#### Syntax

[Step](step.html).SwitchExecWaitForDebounce

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the operation the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 property specifies waits for all switches to debounce before returning to TestStand.

Note

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-uniquestepid.html language=enus -->
## TOPIC 02790: Step.UniqueStepId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-uniquestepid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-uniquestepid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.UniqueStepId Data Type String Purpose Returns an identification string unique among all steps TestStand has created or will create. Sequence editors you create with TestStand assign new unique IDs to steps that you duplicate in the editor. However, the value of Step.UniqueStepId is not u

### Step.UniqueStepId

#### Syntax

[Step](step.html).UniqueStepId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an identification string unique among all steps TestStand has created or will create.

Note

Step.UniqueStepId

Step.CreateNewUniqueStepId

Step.UniqueStepId

Step.Sequence.SequenceFile.Id

Step.UniqueStepId

#### Remarks

An example of a UniqueStepId is
 ID#:aXPIZYIPFEWM/Jsuxx0FAD
 .

#### See Also

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[Step.Name](step-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-unloadmodule.html language=enus -->
## TOPIC 02791: Step.UnloadModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-unloadmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-unloadmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.UnloadModule Return Value Boolean Indicates if the module was successfully unloaded. Purpose Unloads the code module for the step. Remarks The module is not unloaded if the step is currently executing. See Also LoadModule

### Step.UnloadModule

#### Syntax

[Step](step.html).UnloadModule

#### Return Value

[Boolean](data-types-for-teststand.html)

Indicates if the module was successfully unloaded.

#### Purpose

Unloads the code module for the step.

#### Remarks

The module is not unloaded if the step is currently executing.

#### See Also

[LoadModule](step-loadmodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-usemutex.html language=enus -->
## TOPIC 02792: Step.UseMutex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-usemutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-usemutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.UseMutex Data Type Boolean Purpose Specifies that the step acquires a lock before it executes and releases the lock after it completes. Remarks Use the Step.MutexNameOrRefExpr property to specify which lock the step uses. See Also Step.BatchSyncOption Step.MutexNameOrRefExpr

### Step.UseMutex

#### Syntax

[Step](step.html).UseMutex

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the step acquires a lock before it executes and releases the lock after it completes.

#### Remarks

Use the
 [Step.MutexNameOrRefExpr](step-mutexnameorrefexpr.html)
 property to specify which lock the step uses.

#### See Also

[Step.BatchSyncOption](step-batchsyncoption.html)

[Step.MutexNameOrRefExpr](step-mutexnameorrefexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-windowactivation.html language=enus -->
## TOPIC 02793: Step.WindowActivation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-windowactivation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-windowactivation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.WindowActivation Data Type WindowActivationOptions Use the following constants with this data type: WinActOption_ActivateWhenStepCompletes –(Value: 2) Activate when the step completes. WinActOption_IfActiveReactivateWhenStepCompletes –(Value: 3) If initially active, reactivate when the s

### Step.WindowActivation

#### Syntax

[Step](step.html).WindowActivation

#### Data Type

[WindowActivationOptions](windowactivationoptions.html)

Use the following constants with this data type:

- WinActOption_ActivateWhenStepCompletes 
 –(Value: 2) Activate when the step completes.
- WinActOption_IfActiveReactivateWhenStepCompletes 
 –(Value: 3) If initially active, reactivate when the step completes.
- WinActOption_None 
 –(Value: 1) No activation.

#### Purpose

Determines if the TestStand application activates its window when the step completes.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step.html language=enus -->
## TOPIC 02794: Step

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the Step class represent steps in TestStand sequences. A step can perform many tasks, such as initializing an instrument, performing a complex test, or making a decision that affects the flow of execution in a sequence. You can obtain a reference to a step in a sequence by calling the Seq

### Step

Objects of the Step class represent steps in TestStand sequences. A step can perform many tasks, such as initializing an instrument, performing a complex test, or making a decision that affects the flow of execution in a sequence. You can obtain a reference to a step in a sequence by calling the
 [Sequence.GetStep](sequence-getstep.html)
 method. Create new steps with the
 [Engine.NewStep](engine-newstep.html)
 method.

Note

#### Properties

| AdapterKeyName (Read Only) |
| --- |
| AdditionalResults (Read Only) |
| AdditionalResultsHints (Read Only) |
| BatchSyncOption |
| BlockEndIndex |
| BlockFlags |
| BlockLevel |
| BlockLevelsUnmatched |
| BlockNextIndex |
| BlockParentIndex |
| BlockPreviousIndex |
| BlockStartIndex |
| CancelCurrentExecution |
| CancelCurrentModuleExecution |
| CancelStepCallback |
| CanCreateCode (Read Only) |
| CanEditCode (Read Only) |
| CanSpecifyModule (Read Only) |
| CausedSequenceFailure |
| CurrentLoopResult |
| CustomActionExpression |
| CustomFalseAction |
| CustomFalseActionTargetByExpr |
| CustomTrueAction |
| CustomTrueActionTargetByExpr |
| EditAsReadOnly |
| EvalPrecondForInteractiveExecution |
| FailAction |
| FailActionTargetByExpr |
| IconName |
| IgnoreRTE |
| IsSequenceCall (Read Only) |
| LargeIcon (Read Only) |
| LargeIconIndex (Read Only) |
| LastStepResult |
| LoopIncExpression |
| LoopInitExpression |
| LoopStatusExpression |
| LoopType |
| LoopWhileExpression |
| Module (Read Only) |
| ModuleLoadOption |
| ModuleUnloadOption |
| MutexNameOrRefExpr |
| Name |
| PassAction |
| PassActionTargetByExpr |
| PostExpression |
| Precondition |
| PreExpression |
| RecordLoopIterationResults |
| Requirements (Read Only) |
| ResultRecordingOption |
| ResultStatus |
| Sequence (Read Only) |
| SmallIcon (Read Only) |
| SmallIconIndex (Read Only) |
| StatusExpression |
| StepFailCausesSequenceFail |
| StepGroup (Read Only) |
| StepIndex (Read Only) |
| StepType (Read Only) |
| SwitchExecConnectionLifetime |
| SwitchExecEnabled |
| SwitchExecMulticonnectMode |
| SwitchExecOperation |
| SwitchExecOperationOrder |
| SwitchExecRoutesToConnect |
| SwitchExecRoutesToDisconnect |
| SwitchExecVirtualDevice |
| SwitchExecWaitForDebounce |
| UniqueStepId (Read Only) |
| UseMutex |
| WindowActivation |

#### Methods

| AsPropertyObject |
| --- |
| CanChangeAdapter |
| CanChangeStepType |
| CanExecuteSubstep |
| ChangeAdapter |
| ChangeStepType |
| CreateCode |
| CreateNewUniqueStepId |
| DisplayAdditionalResultsDialog |
| EditCode |
| ExecuteSubstep |
| GetBreakSettings |
| GetDescriptionEx |
| GetEditSubstepMenuStructure |
| GetResultStatusDisplayString |
| GetRunModeEx |
| GetStepSettingsString |
| LoadModule |
| LogAdditionalResult |
| SetBreakSettings |
| SetRunModeEx |
| SpecifyModule |
| UnloadModule |

#### See Also

[Engine.NewStep](engine-newstep.html)

[Sequence](sequence.html)

[Sequence.GetStep](sequence-getstep.html)

[StepType](steptype.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepadditionalresults-customresults.html language=enus -->
## TOPIC 02795: StepAdditionalResults.CustomResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepadditionalresults-customresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepadditionalresults-customresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepAdditionalResults.CustomResults Data Type AdditionalResults Purpose Returns the custom additional results for a step. See Also AdditionalResults StepAdditionalResults.ParameterResults

### StepAdditionalResults.CustomResults

#### Syntax

[StepAdditionalResults](stepadditionalresults.html).CustomResults

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

Returns the custom additional results for a step.

#### See Also

[AdditionalResults](additionalresults.html)

[StepAdditionalResults.ParameterResults](stepadditionalresults-parameterresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepadditionalresults-parameterresults.html language=enus -->
## TOPIC 02796: StepAdditionalResults.ParameterResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepadditionalresults-parameterresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepadditionalresults-parameterresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepAdditionalResults.ParameterResults Data Type AdditionalResults Purpose Returns the parameter results for a step. You cannot directly add or remove additional results in this collection. The parameters in the step module determine the items in this collection. Remarks This collection conta

### StepAdditionalResults.ParameterResults

#### Syntax

[StepAdditionalResults](stepadditionalresults.html).ParameterResults

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

Returns the parameter results for a step. You cannot directly add or remove additional results in this collection. The parameters in the step module determine the items in this collection.

#### Remarks

This collection contains an item for every [In] parameter and for every [Out] parameter. For every [In/Out] parameter, this collection contains one item for the [In] value and another item for the [Out] value.

#### See Also

[AdditionalResults](additionalresults.html)

[CustomResults](stepadditionalresults-customresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepadditionalresults.html language=enus -->
## TOPIC 02797: StepAdditionalResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepadditionalresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepadditionalresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Step.AdditionalResults property to obtain an instance of this class, which contains collections for the parameter additional results and custom additional results of a step. Properties CustomResults (Read Only) ParameterResults (Read Only) See Also Step.AdditionalResults

### StepAdditionalResults

Use the
 [Step.AdditionalResults](step-additionalresults.html)
 property to obtain an instance of this class, which contains collections for the parameter additional results and custom additional results of a step.

#### Properties

| CustomResults (Read Only) |
| --- |
| ParameterResults (Read Only) |

#### See Also

[Step.AdditionalResults](step-additionalresults.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepdescriptionoptions.html language=enus -->
## TOPIC 02798: StepDescriptionOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepdescriptionoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepdescriptionoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Step.GetDescriptionEx and Step.GetStepSettingsString methods. StepDescOption_IncludeBreakpoint –(Value: 0x02) Returns the available breakpoint description with the step description. Use this option with the Step.GetE

### StepDescriptionOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Step.GetDescriptionEx](step-getdescriptionex.html)
 and
 [Step.GetStepSettingsString](step-getstepsettingsstring.html)
 methods.

- StepDescOption_IncludeBreakpoint 
 –(Value: 0x02) Returns the available breakpoint description with the step description. Use this option with the
 Step.GetExecutionFlowString 
 method.
 Note 
 Only conditional breakpoints provide a description.
- StepDescOption_Long 
 –(Value: 0x1) Returns the longest description available for the step. If you do not specify this option, the adapter settings determine whether to return a long description.
- StepDescOption_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[Step.GetDescriptionEx](step-getdescriptionex.html)

[Step.GetExecutionFlowString](step-getexecutionflowstring.html)

[Step.GetStepSettingsString](step-getstepsettingsstring.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepgroups.html language=enus -->
## TOPIC 02799: StepGroups

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepgroups.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepgroups.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the step group of a sequence. StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. See Also Sequence.GetStep Sequence.InsertSte

### StepGroups

This data type contains values that specify the step group of a sequence.

- StepGroup_Cleanup 
 –(Value: 2) Specifies the Cleanup step group.
- StepGroup_Main 
 –(Value: 1) Specifies the Main step group.
- StepGroup_Setup 
 –(Value: 0) Specifies the Setup step group.

#### See Also

[Sequence.GetStep](sequence-getstep.html)

[Sequence.InsertStep](sequence-insertstep.html)

[SequenceContext.StepGroup](sequencecontext-stepgroup.html)

[Step.StepGroup](step-stepgroup.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steplooptypes.html language=enus -->
## TOPIC 02800: StepLoopTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steplooptypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steplooptypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify the valid values for the Step.LoopType property. LoopType_Custom –(Value: "Custom") LoopType_FixedNumLoops –(Value: "FixedNumLoops") LoopType_NoLoop –(Value: "NoLooping") LoopType_PassFailCount –(Value: "PassFailCount") See Also Step.LoopIncExpression Step.LoopInitExpression

### StepLoopTypes

These constants specify the valid values for the
 [Step.LoopType](step-looptype.html)
 property.

- LoopType_Custom 
 –(Value: "Custom")
- LoopType_FixedNumLoops 
 –(Value: "FixedNumLoops")
- LoopType_NoLoop 
 –(Value: "NoLooping")
- LoopType_PassFailCount 
 –(Value: "PassFailCount")

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopType](step-looptype.html)

[Step.LoopWhileExpression](step-loopwhileexpression.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stepproperties.html language=enus -->
## TOPIC 02801: StepProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stepproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stepproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these string constants to create lookup strings to access properties of the built-in step types using the PropertyObject class. Notice that some of the constants refer to properties, whereas other constants refer to property values. Limits_HighProp –(Value: "High") Limits_LowProp –(Value: "Low")

### StepProperties

Use these string constants to create lookup strings to access properties of the built-in step types using the PropertyObject class. Notice that some of the constants refer to properties, whereas other constants refer to property values.

- Limits_HighProp 
 –(Value: "High")
- Limits_LowProp 
 –(Value: "Low")
- Limits_NominalValueProp 
 –(Value: "Nominal")
- Limits_StringProp 
 –(Value: "String")
- Limits_ThresholdTypeProp 
 –(Value: "ThresholdType")
- NumMeasComp_EQ 
 –(Value: "EQ")
- NumMeasComp_EQTHRESHOLD 
 –(Value: "EQT")
- NumMeasComp_GE 
 –(Value: "GE")
- NumMeasComp_GELE 
 –(Value: "GELE")
- NumMeasComp_GELT 
 –(Value: "GELT")
- NumMeasComp_GT 
 –(Value: "GT")
- NumMeasComp_GTLE 
 –(Value: "GTLE")
- NumMeasComp_GTLT 
 –(Value: "GTLT")
- NumMeasComp_LE 
 –(Value: "LE")
- NumMeasComp_LOG 
 –(Value: "LOG")
- NumMeasComp_LT 
 –(Value: "LT")
- NumMeasComp_NE 
 –(Value: "NE")
- NumMeasRadix 
 –(Value: "DisplayRadix") This constant is obsolete. In TestStand 2.0, set the numeric format using the
 PropertyObject.NumericFormat 
 property of the following step properties:
 Limits.High 
 ,
 Limits.Low 
 , and
 Result.Numeric 
 .
- NumMeasThresholdType_DELTA 
 –(Value: "DELTA")
- NumMeasThresholdType_PERCENTAGE 
 –(Value: "PERCENTAGE")
- NumMeasThresholdType_PPM 
 –(Value: "PPM")
- Result_NumericProp 
 –(Value: "Numeric")
- Result_PassFailProp 
 –(Value: "PassFail")
- Result_StatusProp 
 –(Value: "Status")
- Result_StringProp 
 –(Value: "String")
- ResultStatus_Done 
 –(Value: "Done")
- ResultStatus_Error 
 –(Value: "Error")
- ResultStatus_Failed 
 –(Value: "Failed")
- ResultStatus_Looping 
 –(Value: "Looping")
- ResultStatus_NoStatus 
 –(Value: "")
- ResultStatus_Passed 
 –(Value: "Passed")
- ResultStatus_Running 
 –(Value: "Running")
- ResultStatus_Skipped 
 –(Value: "Skipped")
- ResultStatus_Terminated 
 –(Value: "Terminated")
- ResultStatus_Waiting 
 –(Value: "Waiting")
- Step_InBufProp 
 –(Value: "InBuf")
- Step_LimitsProp 
 –(Value: "Limits")
- Step_MeasComparisonType 
 –(Value: "Comp")
- Step_MeasThresholdType 
 –(Value: "ThresholdType")
- Step_ResultProp 
 –(Value: "Result")
- Step_TSInfoProp 
 –(Value: "TS")
- StrMeasComp_CaseSensitive 
 –(Value: "CaseSensitive")
- StrMeasComp_IgnoreCase 
 –(Value: "IgnoreCase")
- TSInfo_StepAdditions 
 –(Value: "SData") Do not use this constant to access the adapter-specific properties of a step. Instead, use the specific module interface for the Module object for the step. Use the
 Step.Module 
 property to acquire a reference to a Module object.

#### See Also

[CVIModule](cvimodule.html)

[DllModule](dllmodule.html)

[LabVIEWModule](labviewmodule.html)

[PropertyObject](propertyobject.html)

[PropertyObject.NumericFormat](propertyobject-numericformat.html)

[SequenceCallModule](sequencecallmodule.html)

[Step.Module](step-module.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-additionalresultshints.html language=enus -->
## TOPIC 02802: StepType.AdditionalResultsHints

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-additionalresultshints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-additionalresultshints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.AdditionalResultsHints Data Type AdditionalResults Purpose Returns a list of additional result hints associated with a step type. Remarks The combined members of StepType.AdditionalResultsHints and Step.AdditionalResultsHints define a list of preconfigured custom additional results y

### StepType.AdditionalResultsHints

#### Syntax

[StepType](steptype.html).AdditionalResultsHints

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

Returns a list of additional result hints associated with a step type.

#### Remarks

The combined members of
 StepType.AdditionalResultsHints
 and
 [Step.AdditionalResultsHints](step-additionalresultshints.html)
 define a list of preconfigured custom additional results you can choose to log when you edit the additional results of a step in a user interface.

#### See Also

[AdditionalResults](additionalresults.html)

[Step.AdditionalResultsHints](step-additionalresultshints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-addsubstep.html language=enus -->
## TOPIC 02803: StepType.AddSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-addsubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-addsubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.AddSubstep( newSubstep) Purpose Adds a new substep to the step type. Remarks Use substeps to define standard actions, other than calling the step module, TestStand performs for all instances of the step type. You can specify one of the following four categories for a step type: Pre-S

### StepType.AddSubstep

#### Syntax

[StepType](steptype.html).AddSubstep( newSubstep)

#### Purpose

Adds a new substep to the step type.

#### Remarks

Use substeps to define standard actions, other than calling the step module, TestStand performs for all instances of the step type. You can specify one of the following four categories for a step type:

- Pre-Step substeps 
 —TestStand calls the Pre-Step substeps before calling the step module. You can implement a Pre-Step substep to retrieve and store measurement configuration parameters into custom step properties the step module can access.
- Post-Step substeps 
 —TestStand calls the Post-Step substeps after calling the step module. You can implement a Post-Step substep to compare the values the step module stores in custom step properties against limit values the Edit substep stores in other custom step properties.
- Edit substeps 
 —An Edit substep launches a dialog box in which you can edit the values of custom step properties. For example, an Edit substep can launch a dialog box in which you specify the high and low limits for a test. The Edit substep can then store the high and low limit values as step properties. Dialog boxes that the specified Edit substep code module launch must be modal. For all dialog boxes except the Microsoft Foundation Classes dialog boxes, use the
 Engine.NotifyStartOfModalDialogEx 
 and
 Engine.NotifyEndOfModalDialog 
 methods of the TestStand API. Refer to the examples in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Examples\Fundamentals\Launching a Modal Dialog 
 directory for more information about how to use modal dialog boxes.
- Custom substeps 
 —TestStand does not call Custom substeps. You can use the TestStand API to invoke a Custom substep from a test module, user interface, or other code module.

#### Parameters

newSubstep
 As
 [Step](step.html)

[In] Specifies the new step to be added as a substep for the current step type. Create a new step to pass for this parameter by calling the
 [Engine.NewStep](engine-newstep.html)
 method and specifying
 Substep
 ,
 EditSubstep
 ,
 PreSubstep
 , or
 PostSubstep
 as the value for the
 stepTypeName
 parameter of the
 Engine.NewStep
 method.

#### See Also

[Engine.NewStep](engine-newstep.html)

[Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Step](step.html)

[StepType.GetSubstep](steptype-getsubstep.html)

[StepType.NumSubsteps](steptype-numsubsteps.html)

[StepType.RemoveSubstep](steptype-removesubstep.html)

[StepType.SwapSubsteps](steptype-swapsubsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-appliestoblockstructure.html language=enus -->
## TOPIC 02804: StepType.AppliesToBlockStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-appliestoblockstructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-appliestoblockstructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.AppliesToBlockStructure Data Type Boolean Purpose Specifies whether this step defines or operates according to the block structure of the sequence. If this property is not set, the step type ignores the values of the StepType.BlockStartTypes and StepType.BlockEndTypes properties. See

### StepType.AppliesToBlockStructure

#### Syntax

[StepType](steptype.html).AppliesToBlockStructure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether this step defines or operates according to the block structure of the sequence. If this property is not set, the step type ignores the values of the
 [StepType.BlockStartTypes](steptype-blockstarttypes.html)
 and
 [StepType.BlockEndTypes](steptype-blockendtypes.html)
 properties.

#### See Also

[StepType.BlockEndTypes](steptype-blockendtypes.html)

[StepType.BlockStartTypes](steptype-blockstarttypes.html)

[StepType.CanEncapsulate](steptype-canencapsulate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-aspropertyobject.html language=enus -->
## TOPIC 02805: StepType.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the StepType object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### StepType.AsPropertyObject

#### Syntax

[StepType](steptype.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the StepType object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-batchsyncoption.html language=enus -->
## TOPIC 02806: StepType.BatchSyncOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-batchsyncoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-batchsyncoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.BatchSyncOption Data Type BatchSynchronizationOptions Use the following constants with this data type: BatchSyncOption_NoSync –(Value: 2) No batch synchronization is used on this step. BatchSyncOption_OneThreadOnly –(Value: 5) Use a One Thread Only section to specify that only one th

### StepType.BatchSyncOption

#### Syntax

[StepType](steptype.html).BatchSyncOption

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

Specifies the Batch Synchronization operation the step enters before it executes and exits after it completes.

#### See Also

[StepType.MutexNameOrRefExpr](steptype-mutexnameorrefexpr.html)

[StepType.UseMutex](steptype-usemutex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-blockendtypes.html language=enus -->
## TOPIC 02807: StepType.BlockEndTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-blockendtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-blockendtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.BlockEndTypes Data Type String Purpose Specifies a comma-separated list of step type names. Steps of any type in the list end blocks started by steps of this type.

### StepType.BlockEndTypes

#### Syntax

[StepType](steptype.html).BlockEndTypes

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a comma-separated list of step type names. Steps of any type in the list end blocks started by steps of this type.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-blockstarttypes.html language=enus -->
## TOPIC 02808: StepType.BlockStartTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-blockstarttypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-blockstarttypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.BlockStartTypes Data Type String Purpose Specifies a comma-separated list of step type names. Steps of this type end blocks started by steps of any type in the list.

### StepType.BlockStartTypes

#### Syntax

[StepType](steptype.html).BlockStartTypes

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a comma-separated list of step type names. Steps of this type end blocks started by steps of any type in the list.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-canencapsulate.html language=enus -->
## TOPIC 02809: StepType.CanEncapsulate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-canencapsulate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-canencapsulate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CanEncapsulate Data Type Boolean Purpose Specifies whether this step and a corresponding end step can surround a block of contiguous steps.

### StepType.CanEncapsulate

#### Syntax

[StepType](steptype.html).CanEncapsulate

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether this step and a corresponding end step can surround a block of contiguous steps.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-canspecifymodule.html language=enus -->
## TOPIC 02810: StepType.CanSpecifyModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-canspecifymodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-canspecifymodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CanSpecifyModule Data Type Boolean Purpose Returns a value that indicates whether the adapter for the default module of the step type supports the StepType.SpecifyModule method. See Also StepType.SpecifyModule

### StepType.CanSpecifyModule

#### Syntax

[StepType](steptype.html).CanSpecifyModule

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the adapter for the default module of the step type supports the
 [StepType.SpecifyModule](steptype-specifymodule.html)
 method.

#### See Also

[StepType.SpecifyModule](steptype-specifymodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-changedesignatedadapter.html language=enus -->
## TOPIC 02811: StepType.ChangeDesignatedAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-changedesignatedadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-changedesignatedadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.ChangeDesignatedAdapter( adapterName) Purpose Specifies the module adapter assigned to the step type. Remarks To obtain the current designated adapter, use the StepType.DesignatedAdapter property. Parameters adapterName As String [In] Corresponds to the key name of the adapter assign

### StepType.ChangeDesignatedAdapter

#### Syntax

[StepType](steptype.html).ChangeDesignatedAdapter( adapterName)

#### Purpose

Specifies the module adapter assigned to the step type.

#### Remarks

To obtain the current designated adapter, use the
 [StepType.DesignatedAdapter](steptype-designatedadapter.html)
 property.

#### Parameters

adapterName
 As
 [String](data-types-for-teststand.html)

[In] Corresponds to the key name of the adapter assigned to the specific step type. If the Step Type does not require a module adapter, set this parameter to an empty string.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Module.Adapter](module-adapter.html)

[StepType.CanSpecifyModule](steptype-canspecifymodule.html)

[StepType.DesignatedAdapter](steptype-designatedadapter.html)

[StepType.Module](steptype-module.html)

[StepType.SpecifyModule](steptype-specifymodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-codetemplates.html language=enus -->
## TOPIC 02812: StepType.CodeTemplates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-codetemplates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-codetemplates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CodeTemplates Data Type CodeTemplates Purpose Returns the code templates for this step type. See Also CodeTemplate CodeTemplates

### StepType.CodeTemplates

#### Syntax

[StepType](steptype.html).CodeTemplates

#### Data Type

[CodeTemplates](codetemplates.html)

#### Purpose

Returns the code templates for this step type.

#### See Also

[CodeTemplate](codetemplate.html)

[CodeTemplates](codetemplates.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-createcombinedsteptype.html language=enus -->
## TOPIC 02813: StepType.CreateCombinedStepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-createcombinedsteptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-createcombinedsteptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CreateCombinedStepType( combineWith) Return Value StepType Returns the new combined step type. Purpose Combines two step types to create a new step type. Remarks If both step types have the same properties but have different values, the values associated with the step type you invoke

### StepType.CreateCombinedStepType

#### Syntax

[StepType](steptype.html).CreateCombinedStepType( combineWith)

#### Return Value

[StepType](steptype.html)

Returns the new combined step type.

#### Purpose

Combines two step types to create a new step type.

#### Remarks

If both step types have the same properties but have different values, the values associated with the step type you invoke this method upon take precedence.

#### Parameters

combineWith
 As
 [StepType](steptype.html)

[In] Specifies the step type to combine with this one.

#### See Also

[StepType](steptype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-customactionexpression.html language=enus -->
## TOPIC 02814: StepType.CustomActionExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-customactionexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-customactionexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CustomActionExpression Data Type String Purpose Specifies the custom post action condition expression for the step. See Also StepType.CustomFalseAction StepType.CustomFalseActionTargetByExpr StepType.CustomTrueAction StepType.CustomTrueActionTargetByExpr

### StepType.CustomActionExpression

#### Syntax

[StepType](steptype.html).CustomActionExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the custom post action condition expression for the step.

#### See Also

[StepType.CustomFalseAction](steptype-customfalseaction.html)

[StepType.CustomFalseActionTargetByExpr](steptype-customfalseactiontargetbyexpr.html)

[StepType.CustomTrueAction](steptype-customtrueaction.html)

[StepType.CustomTrueActionTargetByExpr](steptype-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-customfalseaction.html language=enus -->
## TOPIC 02815: StepType.CustomFalseAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-customfalseaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-customfalseaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CustomFalseAction Data Type String Purpose Specifies the type of action you want to occur when the custom post action expression evaluates to False . Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionVa

### StepType.CustomFalseAction

#### Syntax

[StepType](steptype.html).CustomFalseAction

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

[StepType.CustomActionExpression](steptype-customactionexpression.html)

[StepType.CustomFalseActionTargetByExpr](steptype-customfalseactiontargetbyexpr.html)

[StepType.CustomTrueAction](steptype-customtrueaction.html)

[StepType.CustomTrueActionTargetByExpr](steptype-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-customfalseactiontargetbyexpr.html language=enus -->
## TOPIC 02816: StepType.CustomFalseActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-customfalseactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-customfalseactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CustomFalseActionTargetByExpr Data Type String Purpose Specifies the target for the post action the StepType.CustomFalseAction property specifies. Remarks If the StepType.CustomFalseAction property is PostAction_GotoStep , the target is the name of the step or the ID of the step. If

### StepType.CustomFalseActionTargetByExpr

#### Syntax

[StepType](steptype.html).CustomFalseActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [StepType.CustomFalseAction](steptype-customfalseaction.html)
 property specifies.

#### Remarks

- If the
 StepType.CustomFalseAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 StepType.CustomFalseAction 
 property is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[PostActionValues](postactionvalues.html)

[StepType.CustomActionExpression](steptype-customactionexpression.html)

[StepType.CustomFalseAction](steptype-customfalseaction.html)

[StepType.CustomTrueAction](steptype-customtrueaction.html)

[StepType.CustomTrueActionTargetByExpr](steptype-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-customtrueaction.html language=enus -->
## TOPIC 02817: StepType.CustomTrueAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-customtrueaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-customtrueaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CustomTrueAction Data Type String Purpose Specifies the type of action you want to occur when the custom post action expression evaluates to True . Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValu

### StepType.CustomTrueAction

#### Syntax

[StepType](steptype.html).CustomTrueAction

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

[StepType.CustomActionExpression](steptype-customactionexpression.html)

[StepType.CustomFalseAction](steptype-customfalseaction.html)

[StepType.CustomFalseActionTargetByExpr](steptype-customfalseactiontargetbyexpr.html)

[StepType.CustomTrueActionTargetByExpr](steptype-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-customtrueactiontargetbyexpr.html language=enus -->
## TOPIC 02818: StepType.CustomTrueActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-customtrueactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-customtrueactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.CustomTrueActionTargetByExpr Data Type String Purpose Specifies the target for the post action the StepType.CustomTrueAction property specifies. Remarks If the StepType.CustomTrueAction property is PostAction_GotoStep , the target is the name of the step or the ID of the step. If you

### StepType.CustomTrueActionTargetByExpr

#### Syntax

[StepType](steptype.html).CustomTrueActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [StepType.CustomTrueAction](steptype-customtrueaction.html)
 property specifies.

#### Remarks

- If the
 StepType.CustomTrueAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 StepType.CustomTrueAction 
 is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[PostActionValues](postactionvalues.html)

[StepType.CustomActionExpression](steptype-customactionexpression.html)

[StepType.CustomFalseAction](steptype-customfalseaction.html)

[StepType.CustomFalseActionTargetByExpr](steptype-customfalseactiontargetbyexpr.html)

[StepType.CustomTrueAction](steptype-customtrueaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-defaultnameexpr.html language=enus -->
## TOPIC 02819: StepType.DefaultNameExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-defaultnameexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-defaultnameexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.DefaultNameExpr Data Type String Purpose Specifies a string expression TestStand evaluates and uses as the name of the step when you create a new step with the step type. Remarks If a step with the same name already exists in the sequence and the Make step names unique when inserting

### StepType.DefaultNameExpr

#### Syntax

[StepType](steptype.html).DefaultNameExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string expression TestStand evaluates and uses as the name of the step when you create a new step with the step type.

#### Remarks

If a step with the same name already exists in the sequence and the
 Make step names unique when inserting steps
 sequence editor option is enabled, TestStand appends an underscore followed by a number to the step name to make it unique.

If you want to store the name in a
 [string resource file](/csh?context=ts_tsfundamentals_resource_strings)
 , use the
 Restr
 expression function to retrieve the name from the file. Storing the name in a string resource file is useful when you want to display the name in different languages.

#### See Also

[StepType.DescriptionExpr](steptype-descriptionexpr.html)

[StepType.DesignatedAdapter](steptype-designatedadapter.html)

[StepType.IconName](steptype-iconname.html)

[StepType.Precondition](steptype-precondition.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-descriptionexpr.html language=enus -->
## TOPIC 02820: StepType.DescriptionExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-descriptionexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-descriptionexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.DescriptionExpr Data Type String Purpose Specifies a string expression TestStand evaluates and uses as the contents of the Description field for a step of the step type. Remarks If you include the %ModuleDescription macro in a string you surround with double quotes, TestStand replace

### StepType.DescriptionExpr

#### Syntax

[StepType](steptype.html).DescriptionExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string expression TestStand evaluates and uses as the contents of the Description field for a step of the step type.

#### Remarks

If you include the
 %ModuleDescription
 macro in a string you surround with double quotes, TestStand replaces the
 %ModuleDescription
 macro text with text the module adapter provides, which describes the code module the step uses.

#### See Also

[StepType.DefaultNameExpr](steptype-defaultnameexpr.html)

[StepType.DesignatedAdapter](steptype-designatedadapter.html)

[StepType.Precondition](steptype-precondition.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-designatedadapter.html language=enus -->
## TOPIC 02821: StepType.DesignatedAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-designatedadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-designatedadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.DesignatedAdapter Data Type String Purpose Returns the module adapter for the step type. The module adapter for any instance created from this type defaults to this setting. Remarks Use the StepType.ChangeDesignatedAdapter method to change this setting. If the step type does not spec

### StepType.DesignatedAdapter

#### Syntax

[StepType](steptype.html).DesignatedAdapter

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the module adapter for the step type. The module adapter for any instance created from this type defaults to this setting.

#### Remarks

Use the
 [StepType.ChangeDesignatedAdapter](steptype-changedesignatedadapter.html)
 method to change this setting. If the step type does not specify a default module adapter, this property returns an empty string.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.NewStep](engine-newstep.html)

[StepType.CanSpecifyModule](steptype-canspecifymodule.html)

[StepType.ChangeDesignatedAdapter](steptype-changedesignatedadapter.html)

[StepType.SpecifyModule](steptype-specifymodule.html)

[StepType.Module](steptype-module.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-dimmablepropertykeynames.html language=enus -->
## TOPIC 02822: StepType.DimmablePropertyKeyNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-dimmablepropertykeynames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-dimmablepropertykeynames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.DimmablePropertyKeyNames Data Type String Array Purpose Returns the key names from the step type-modifiable properties. These properties are disabled to prevent you from modifying the settings of built-in instance properties in individual steps. In this way, the settings specified fo

### StepType.DimmablePropertyKeyNames

#### Syntax

[StepType](steptype.html).DimmablePropertyKeyNames

#### Data Type

[String Array](data-types-for-teststand.html)

#### Purpose

Returns the key names from the step type-modifiable properties.

These properties are disabled to prevent you from modifying the settings of built-in instance properties in individual steps. In this way, the settings specified for the step type remain permanent for all step instances.

#### Remarks

A key name is an internal name assigned to a specific property. To obtain the property display name, use the
 [StepType.GetDimmablePropertyDisplayName](steptype-getdimmablepropertydisplayname.html)
 method.

#### See Also

[StepType.DimProperty](steptype-dimproperty.html)

[StepType.GetDimmablePropertyDisplayName](steptype-getdimmablepropertydisplayname.html)

[StepType.IsPropertyDimmed](steptype-ispropertydimmed.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-dimproperty.html language=enus -->
## TOPIC 02823: StepType.DimProperty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-dimproperty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-dimproperty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.DimProperty( propertyKeyName, newValue) Purpose Specifies if the control(s) for the specified property are disabled in the Step Properties dialog box. Parameters propertyKeyName As String [In] Specifies the corresponding property key name. newValue As Boolean [In] If this parameter i

### StepType.DimProperty

#### Syntax

[StepType](steptype.html).DimProperty( propertyKeyName, newValue)

#### Purpose

Specifies if the control(s) for the specified property are disabled in the
 [Step Properties](../tsref/step-properties-dialog-box.html)
 dialog box.

#### Parameters

propertyKeyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the corresponding property key name.

newValue
 As
 [Boolean](data-types-for-teststand.html)

[In] If this parameter is
 True
 , the control for the corresponding property is disabled.

#### See Also

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

[StepType.DimmablePropertyKeyNames](steptype-dimmablepropertykeynames.html)

[StepType.GetDimmablePropertyDisplayName](steptype-getdimmablepropertydisplayname.html)

[StepType.IsPropertyDimmed](steptype-ispropertydimmed.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-evalprecondforinteractiveexecution.html language=enus -->
## TOPIC 02824: StepType.EvalPrecondForInteractiveExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-evalprecondforinteractiveexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-evalprecondforinteractiveexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.EvalPrecondForInteractiveExecution Data Type EvalPrecondOptions Use the following constants with this data type: EvalPrecondOption_EvaluatePrecond –(Value: 1) Evaluates the precondition. EvalPrecondOption_NoEvaluatePrecond –(Value: 2) Does not evaluate the precondition. EvalPrecondOp

### StepType.EvalPrecondForInteractiveExecution

#### Syntax

[StepType](steptype.html).EvalPrecondForInteractiveExecution

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

Specifies whether TestStand evaluates the step precondition when you run the step interactively.

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StepType.Precondition](steptype-precondition.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-failaction.html language=enus -->
## TOPIC 02825: StepType.FailAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-failaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-failaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.FailAction Data Type String Purpose Specifies the type of post action you want to occur if the step fails. Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues StepType.FailActionTargetByExpr

### StepType.FailAction

#### Syntax

[StepType](steptype.html).FailAction

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

[StepType.FailActionTargetByExpr](steptype-failactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-failactiontargetbyexpr.html language=enus -->
## TOPIC 02826: StepType.FailActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-failactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-failactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.FailActionTargetByExpr Data Type String Purpose Specifies the target for the post action the StepType.FailAction property specifies. Remarks If the StepType.FailAction is PostAction_GotoStep , the target is the name of the step. If the StepType.FailAction is PostAction_CallCallback ,

### StepType.FailActionTargetByExpr

#### Syntax

[StepType](steptype.html).FailActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [StepType.FailAction](steptype-failaction.html)
 property specifies.

#### Remarks

- If the
 StepType.FailAction 
 is
 PostAction_GotoStep 
 , the target is the name of the step.
- If the
 StepType.FailAction 
 is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[StepType.FailAction](steptype-failaction.html)

[StepType.PassAction](steptype-passaction.html)

[StepType.PassActionTargetByExpr](steptype-passactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-getdefaultname.html language=enus -->
## TOPIC 02827: StepType.GetDefaultName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-getdefaultname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-getdefaultname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.GetDefaultName Return Value String Purpose Returns the default step name to use when creating new steps of this type. See Also StepType.DescriptionExpr StepType.Name

### StepType.GetDefaultName

#### Syntax

[StepType](steptype.html).GetDefaultName

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the default step name to use when creating new steps of this type.

#### See Also

[StepType.DescriptionExpr](steptype-descriptionexpr.html)

[StepType.Name](steptype-name.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-getdimmablepropertydisplayname.html language=enus -->
## TOPIC 02828: StepType.GetDimmablePropertyDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-getdimmablepropertydisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-getdimmablepropertydisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.GetDimmablePropertyDisplayName( propertyKeyName) Return Value String Purpose Obtains the display name for the key name. Remarks The display name depends on localization. Parameters propertyKeyName As String [In] Specifies a property key name. See Also StepType.DimmablePropertyKeyName

### StepType.GetDimmablePropertyDisplayName

#### Syntax

[StepType](steptype.html).GetDimmablePropertyDisplayName( propertyKeyName)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Obtains the display name for the key name.

#### Remarks

The display name depends on localization.

#### Parameters

propertyKeyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies a property key name.

#### See Also

[StepType.DimmablePropertyKeyNames](steptype-dimmablepropertykeynames.html)

[StepType.DimProperty](steptype-dimproperty.html)

[StepType.IsPropertyDimmed](steptype-ispropertydimmed.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-getsubstep.html language=enus -->
## TOPIC 02829: StepType.GetSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-getsubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-getsubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.GetSubstep( substepIndex) Return Value Step Purpose Returns the specified substep. Parameters substepIndex As Long [In] Specifies the zero-based index of the substep. See Also Step Step.CanExecuteSubstep Step.ExecuteSubstep StepType.AddSubstep StepType.NumSubsteps StepType.RemoveSubs

### StepType.GetSubstep

#### Syntax

[StepType](steptype.html).GetSubstep( substepIndex)

#### Return Value

[Step](step.html)

#### Purpose

Returns the specified substep.

#### Parameters

substepIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the substep.

#### See Also

[Step](step.html)

[Step.CanExecuteSubstep](step-canexecutesubstep.html)

[Step.ExecuteSubstep](step-executesubstep.html)

[StepType.AddSubstep](steptype-addsubstep.html)

[StepType.NumSubsteps](steptype-numsubsteps.html)

[StepType.RemoveSubstep](steptype-removesubstep.html)

[StepType.SwapSubsteps](steptype-swapsubsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-iconname.html language=enus -->
## TOPIC 02830: StepType.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.IconName Data Type String Purpose Specifies the icon filename assigned to the step type. Remarks The engine maintains a list of images that contain all the icons located in the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons directories and images you add using

### StepType.IconName

#### Syntax

[StepType](steptype.html).IconName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the icon filename assigned to the step type.

#### Remarks

The engine maintains a list of images that contain all the icons located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method.

TestStand displays the icon next to the names of the steps that use the step type. If you assign an empty string to this property or assign the name of an icon that is not part of the engine images list, TestStand displays the icon of the module adapter the step uses next to the name of the step.

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.NumImages](engine-numimages.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[StepType.MenuIcon](steptype-menuicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-ignorerte.html language=enus -->
## TOPIC 02831: StepType.IgnoreRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-ignorerte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-ignorerte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.IgnoreRTE Data Type Boolean Purpose Specifies to prevent the step from reporting a run-time error to the sequence. Remarks When a step causes a run-time error, the step stops executing and TestStand sets the status of the step to Error . If you set this property to False , TestStand

### StepType.IgnoreRTE

#### Syntax

[StepType](steptype.html).IgnoreRTE

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to prevent the step from reporting a run-time error to the sequence.

#### Remarks

When a step causes a run-time error, the step stops executing and TestStand sets the status of the step to
 Error
 . If you set this property to
 False
 , TestStand also sets the internal status of the sequence to
 Error
 , and execution branches to the Cleanup step group for the sequence.

If you set this property to
 True
 , TestStand does not set the internal status of the sequence to
 Error
 . Instead, TestStand resets the
 Error.Occurred
 property of the step to
 False
 and execution continues normally with the next step.

The value for the
 Result.Status
 property remains set to
 Error
 for the step.

#### See Also

[StationOptions.RTEOption](stationoptions-rteoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-ispropertydimmed.html language=enus -->
## TOPIC 02832: StepType.IsPropertyDimmed

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-ispropertydimmed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-ispropertydimmed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.IsPropertyDimmed( propertyKeyName) Return Value Boolean Purpose Indicates whether the control for the specified property is dimmed in the Step Properties dialog box. Parameters propertyKeyName As String [In] Specifies the corresponding property key name. See Also Step Properties dial

### StepType.IsPropertyDimmed

#### Syntax

[StepType](steptype.html).IsPropertyDimmed( propertyKeyName)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether the control for the specified property is dimmed in the
 [Step Properties](../tsref/step-properties-dialog-box.html)
 dialog box.

#### Parameters

propertyKeyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the corresponding property key name.

#### See Also

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

[StepType.DimmablePropertyKeyNames](steptype-dimmablepropertykeynames.html)

[StepType.DimProperty](steptype-dimproperty.html)

[StepType.GetDimmablePropertyDisplayName](steptype-getdimmablepropertydisplayname.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-loopincexpression.html language=enus -->
## TOPIC 02833: StepType.LoopIncExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-loopincexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-loopincexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.LoopIncExpression Data Type String Purpose Specifies the loop increment expression for the step. See Also StepType.LoopInitExpression StepType.LoopStatusExpression StepType.LoopType StepType.LoopWhileExpression StepType.RecordLoopIterationResults

### StepType.LoopIncExpression

#### Syntax

[StepType](steptype.html).LoopIncExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop increment expression for the step.

#### See Also

[StepType.LoopInitExpression](steptype-loopinitexpression.html)

[StepType.LoopStatusExpression](steptype-loopstatusexpression.html)

[StepType.LoopType](steptype-looptype.html)

[StepType.LoopWhileExpression](steptype-loopwhileexpression.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-loopinitexpression.html language=enus -->
## TOPIC 02834: StepType.LoopInitExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-loopinitexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-loopinitexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.LoopInitExpression Data Type String Purpose Specifies the loop initialization expression for the step. See Also StepType.LoopIncExpression StepType.LoopStatusExpression StepType.LoopType StepType.LoopWhileExpression StepType.RecordLoopIterationResults

### StepType.LoopInitExpression

#### Syntax

[StepType](steptype.html).LoopInitExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop initialization expression for the step.

#### See Also

[StepType.LoopIncExpression](steptype-loopincexpression.html)

[StepType.LoopStatusExpression](steptype-loopstatusexpression.html)

[StepType.LoopType](steptype-looptype.html)

[StepType.LoopWhileExpression](steptype-loopwhileexpression.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-loopstatusexpression.html language=enus -->
## TOPIC 02835: StepType.LoopStatusExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-loopstatusexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-loopstatusexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.LoopStatusExpression Data Type String Purpose Specifies the loop status result expression for the step. See Also StepType.LoopIncExpression StepType.LoopInitExpression StepType.LoopType StepType.LoopWhileExpression StepType.RecordLoopIterationResults

### StepType.LoopStatusExpression

#### Syntax

[StepType](steptype.html).LoopStatusExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop status result expression for the step.

#### See Also

[StepType.LoopIncExpression](steptype-loopincexpression.html)

[StepType.LoopInitExpression](steptype-loopinitexpression.html)

[StepType.LoopType](steptype-looptype.html)

[StepType.LoopWhileExpression](steptype-loopwhileexpression.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-looptype.html language=enus -->
## TOPIC 02836: StepType.LoopType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-looptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-looptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.LoopType Data Type String Purpose Specifies the type of looping for the step. Remarks Use the StepLoopTypes constants to specify the value of the property. See Also StepLoopTypes StepType.LoopIncExpression StepType.LoopInitExpression StepType.LoopStatusExpression StepType.LoopWhileEx

### StepType.LoopType

#### Syntax

[StepType](steptype.html).LoopType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of looping for the step.

#### Remarks

Use the
 [StepLoopTypes](steplooptypes.html)
 constants to specify the value of the property.

#### See Also

[StepLoopTypes](steplooptypes.html)

[StepType.LoopIncExpression](steptype-loopincexpression.html)

[StepType.LoopInitExpression](steptype-loopinitexpression.html)

[StepType.LoopStatusExpression](steptype-loopstatusexpression.html)

[StepType.LoopWhileExpression](steptype-loopwhileexpression.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-loopwhileexpression.html language=enus -->
## TOPIC 02837: StepType.LoopWhileExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-loopwhileexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-loopwhileexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.LoopWhileExpression Data Type String Purpose Specifies the While Loop expression for the step. See Also StepType.LoopIncExpression StepType.LoopInitExpression StepType.LoopStatusExpression StepType.LoopType StepType.RecordLoopIterationResults

### StepType.LoopWhileExpression

#### Syntax

[StepType](steptype.html).LoopWhileExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the While Loop expression for the step.

#### See Also

[StepType.LoopIncExpression](steptype-loopincexpression.html)

[StepType.LoopInitExpression](steptype-loopinitexpression.html)

[StepType.LoopStatusExpression](steptype-loopstatusexpression.html)

[StepType.LoopType](steptype-looptype.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-menugroupname.html language=enus -->
## TOPIC 02838: StepType.MenuGroupName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-menugroupname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-menugroupname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.MenuGroupName Data Type String Purpose This property is obsolete. Remarks Specifies the step type menu group to which the step type belongs. This property corresponds to the default group name of the step type in the Groups and Step Types control of the Step Type Menu Editor dialog b

### StepType.MenuGroupName

#### Syntax

[StepType](steptype.html).MenuGroupName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

#### Remarks

Specifies the step type menu group to which the step type belongs.

This property corresponds to the default group name of the step type in the Groups and Step Types control of the
 [Step Type Menu Editor](../tsref/step-type-menu-editor-dialog-box.html)
 dialog box. Instead of using this property, use the Step Type Menu Editor dialog box and save the step type in a type palette file. TestStand uses this value for the initial group for a step type if no Step Type menu data for the step type exists in TestExec.ini or in a type palette file. TestStand saves Step Type menu data with type palette files automatically and also saves the current configuration in TestExec.ini. When you redistribute a type palette file, TestStand merges the Step Type menu data with the current Step Type menu data stored in the TestExec.ini file of the station. Sequence files do not store Step Type menu data. However, because TestStand stores data for step types stored in sequence files in the TestExec.ini of the station on which the step types have been loaded, you can configure the location of those step types.

#### See Also

[Step Type Menu Editor](../tsref/step-type-menu-editor-dialog-box.html)

[StepType.MenuItemNameExpr](steptype-menuitemnameexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-menuicon.html language=enus -->
## TOPIC 02839: StepType.MenuIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-menuicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-menuicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.MenuIcon Data Type Picture Purpose Returns the icon TestStand displays in the context menu for new steps. See Also StepType.IconName

### StepType.MenuIcon

#### Syntax

[StepType](steptype.html).MenuIcon

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns the icon TestStand displays in the context menu for new steps.

#### See Also

[StepType.IconName](steptype-iconname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-menuiconindex.html language=enus -->
## TOPIC 02840: StepType.MenuIconIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-menuiconindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-menuiconindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.MenuIconIndex Data Type Long Purpose Returns the icon index in the small image list of the engine to display in menus for creating new steps of this type. See Also Engine.SmallImageListEx

### StepType.MenuIconIndex

#### Syntax

[StepType](steptype.html).MenuIconIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the icon index in the small image list of the engine to display in menus for creating new steps of this type.

#### See Also

[Engine.SmallImageListEx](engine-smallimagelistex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-menuitemnameexpr.html language=enus -->
## TOPIC 02841: StepType.MenuItemNameExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-menuitemnameexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-menuitemnameexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.MenuItemNameExpr Data Type String Purpose Specifies an expression for the step type name that appears in the Insert Step submenu. Remarks This property corresponds to the Item Name Expression control on the Menu tab of the Step Type Properties dialog box. TestStand uses this expressi

### StepType.MenuItemNameExpr

#### Syntax

[StepType](steptype.html).MenuItemNameExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression for the step type name that appears in the Insert Step submenu.

#### Remarks

This property corresponds to the Item Name Expression control on the
 [Menu tab](../tsref/menu-tab-step-type-properties-dialog-box.html)
 of the
 [Step Type Properties](../tsref/step-type-properties-dialog-box.html)
 dialog box. TestStand uses this expression for the display name of the step type in the
 [Insertion Palette](../tsref/insertion-palette-pane.html)
 or the
 [Insert Step submenu](../tsref/steps-pane-context-menu-sequence-file-window.html)
 of the Steps pane context menu.

Note

string resource file

Restr

#### See Also

[Insert Step submenu](../tsref/steps-pane-context-menu-sequence-file-window.html)

[Insertion Palette](../tsref/insertion-palette-pane.html)

[Menu tab](../tsref/menu-tab-step-type-properties-dialog-box.html)

[Step Type Properties](../tsref/step-type-properties-dialog-box.html)

[StepType.MenuGroupName](steptype-menugroupname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-module.html language=enus -->
## TOPIC 02842: StepType.Module

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-module.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-module.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.Module Data Type Module Purpose Returns a reference to the Module object related to the current step type. Remarks You must acquire the module interface for the specific adapter from the object this property returns to specify the code module name, location and parameters for the Mod

### StepType.Module

#### Syntax

[StepType](steptype.html).Module

#### Data Type

[Module](module.html)

#### Purpose

Returns a reference to the Module object related to the current step type.

#### Remarks

You must acquire the module interface for the specific adapter from the object this property returns to specify the code module name, location and parameters for the Module object.

#### See Also

[Module](module.html)

[Module.Adapter](module-adapter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-moduleloadoption.html language=enus -->
## TOPIC 02843: StepType.ModuleLoadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-moduleloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-moduleloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.ModuleLoadOption Data Type ModuleLoadOptions Use the following constants with this data type: LoadOption_DynamicLoad –(Value: 3) Does not load the code module for a step until the step is ready to call it. LoadOption_PreloadWhenExecuted –(Value: 2) Loads the code module for a step wh

### StepType.ModuleLoadOption

#### Syntax

[StepType](steptype.html).ModuleLoadOption

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

Specifies the option that determines when TestStand loads the code module for the steps of this type.

#### Remarks

The
 SequenceFile.ModuleLoadOption
 property takes precedence over this property, unless the value of the
 SequenceFile.ModuleLoadOption
 property is
 LoadOption_UseStepLoadOption
 .

#### See Also

[SequenceFile.ModuleLoadOption](sequencefile-moduleloadoption.html)

[Step.ModuleLoadOption](step-moduleloadoption.html)

[StepType.ModuleUnloadOption](steptype-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-moduleunloadoption.html language=enus -->
## TOPIC 02844: StepType.ModuleUnloadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-moduleunloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-moduleunloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.ModuleUnloadOption Data Type ModuleUnloadOptions Use the following constants with this data type: UnloadOption_AfterSequenceExecution –(Value: 3) Unloads the code module for a step after the sequence containing the step finishes executing. UnloadOption_AfterStepExecution –(Value: 2)

### StepType.ModuleUnloadOption

#### Syntax

[StepType](steptype.html).ModuleUnloadOption

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

Specifies the option that determines when TestStand unloads the code module for the steps of this type.

#### Remarks

The
 SequenceFile.ModuleUnloadOption
 property takes precedence over this property unless the value of the
 SequenceFile.ModuleUnloadOption
 property is
 UnloadOption_UseStepUnloadOption
 .

#### See Also

[SequenceFile.ModuleUnloadOption](sequencefile-moduleunloadoption.html)

[StepType.ModuleUnloadOption](steptype-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-mutexnameorrefexpr.html language=enus -->
## TOPIC 02845: StepType.MutexNameOrRefExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-mutexnameorrefexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-mutexnameorrefexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.MutexNameOrRefExpr Data Type String Purpose Specifies which lock the step acquires and releases. TestStand ignores this property when the StepType.UseMutex property is False . Remarks Enter a string expression to specify the name of an existing lock. You can also enter an expression

### StepType.MutexNameOrRefExpr

#### Syntax

[StepType](steptype.html).MutexNameOrRefExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies which lock the step acquires and releases. TestStand ignores this property when the
 [StepType.UseMutex](steptype-usemutex.html)
 property is
 False
 .

#### Remarks

Enter a string expression to specify the name of an existing lock. You can also enter an expression that evaluates an ActiveX reference to an existing Lock object. Pass an empty string to specify that TestStand uses a lock unique to the step.

#### See Also

[StepType.BatchSyncOption](steptype-batchsyncoption.html)

[StepType.UseMutex](steptype-usemutex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-name.html language=enus -->
## TOPIC 02846: StepType.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.Name Data Type String Purpose Specifies the name of the step type. Remarks TestStand does not validate step type names you create programmatically for invalid characters, such as spaces, which can result in errors when you use them. Use the TypeUsageList.ValidateNewTypeName method to

### StepType.Name

#### Syntax

[StepType](steptype.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the step type.

#### Remarks

Note

TypeUsageList.ValidateNewTypeName

#### See Also

[StepType.DescriptionExpr](steptype-descriptionexpr.html)

[StepType.GetDefaultName](steptype-getdefaultname.html)

[TypeUsageList.ValidateNewTypeName](typeusagelist-validatenewtypename.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-numsubsteps.html language=enus -->
## TOPIC 02847: StepType.NumSubsteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-numsubsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-numsubsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.NumSubsteps Data Type Long Purpose Returns the number of substeps for this step type. See Also StepType.AddSubstep StepType.GetSubstep StepType.RemoveSubstep Step.CanExecuteSubstep Step.ExecuteSubstep StepType.SwapSubsteps

### StepType.NumSubsteps

#### Syntax

[StepType](steptype.html).NumSubsteps

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of substeps for this step type.

#### See Also

[StepType.AddSubstep](steptype-addsubstep.html)

[StepType.GetSubstep](steptype-getsubstep.html)

[StepType.RemoveSubstep](steptype-removesubstep.html)

[Step.CanExecuteSubstep](step-canexecutesubstep.html)

[Step.ExecuteSubstep](step-executesubstep.html)

[StepType.SwapSubsteps](steptype-swapsubsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-passaction.html language=enus -->
## TOPIC 02848: StepType.PassAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-passaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-passaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.PassAction Data Type String Purpose Specifies the type of post action you want to occur if the step passes. Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues StepType.FailAction StepType.PassActi

### StepType.PassAction

#### Syntax

[StepType](steptype.html).PassAction

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of post action you want to occur if the step passes.

#### Remarks

Assign a
 [PostActionValues](postactionvalues.html)
 string constant to the property to specify the type of post action to perform.

#### See Also

[PostActionValues](postactionvalues.html)

[StepType.FailAction](steptype-failaction.html)

[StepType.PassActionTargetByExpr](steptype-passactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-passactiontargetbyexpr.html language=enus -->
## TOPIC 02849: StepType.PassActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-passactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-passactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.PassActionTargetByExpr Data Type String Purpose Specifies the target for the post action the StepType.PassAction property specifies. Remarks If the StepType.PassAction property is PostAction_GotoStep , the target is the name of the step. If the StepType.PassAction property is PostAct

### StepType.PassActionTargetByExpr

#### Syntax

[StepType](steptype.html).PassActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [StepType.PassAction](steptype-passaction.html)
 property specifies.

#### Remarks

- If the
 StepType.PassAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step.
- If the
 StepType.PassAction 
 property is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[StepType.FailAction](steptype-failaction.html)

[StepType.FailActionTargetByExpr](steptype-failactiontargetbyexpr.html)

[StepType.PassAction](steptype-passaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-postexpression.html language=enus -->
## TOPIC 02850: StepType.PostExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-postexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-postexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.PostExpression Data Type String Purpose Specifies the post-expression for the step. Remarks TestStand evaluates the post-expression after calling the code module and Post-Step substep for the step type. See Also StepType.PreExpression StepType.StatusExpression

### StepType.PostExpression

#### Syntax

[StepType](steptype.html).PostExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the post-expression for the step.

#### Remarks

TestStand evaluates the post-expression after calling the code module and Post-Step substep for the step type.

#### See Also

[StepType.PreExpression](steptype-preexpression.html)

[StepType.StatusExpression](steptype-statusexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-precondition.html language=enus -->
## TOPIC 02851: StepType.Precondition

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-precondition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-precondition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.Precondition Data Type String Purpose Specifies an expression that must evaluate to True or be empty to execute a step of the step type. See Also StepType.EvalPrecondForInteractiveExecution

### StepType.Precondition

#### Syntax

[StepType](steptype.html).Precondition

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression that must evaluate to
 True
 or be empty to execute a step of the step type.

#### See Also

[StepType.EvalPrecondForInteractiveExecution](steptype-evalprecondforinteractiveexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-preexpression.html language=enus -->
## TOPIC 02852: StepType.PreExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-preexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-preexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.PreExpression Data Type String Purpose Specifies the pre-expression for the step. Remarks TestStand evaluates the pre-expression before it calls the Pre-Step substep and code module for the step. See Also StepType.PostExpression StepType.StatusExpression

### StepType.PreExpression

#### Syntax

[StepType](steptype.html).PreExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pre-expression for the step.

#### Remarks

TestStand evaluates the pre-expression before it calls the Pre-Step substep and code module for the step.

#### See Also

[StepType.PostExpression](steptype-postexpression.html)

[StepType.StatusExpression](steptype-statusexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-recordloopiterationresults.html language=enus -->
## TOPIC 02853: StepType.RecordLoopIterationResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-recordloopiterationresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-recordloopiterationresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.RecordLoopIterationResults Data Type Boolean Purpose Specifies whether to add the step results to the sequence results list after each loop iteration. Remarks TestStand also adds the final result it computes for the step loop as a whole if you enable the StepType.ResultRecordingOptio

### StepType.RecordLoopIterationResults

#### Syntax

[StepType](steptype.html).RecordLoopIterationResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to add the step results to the sequence results list after each loop iteration.

#### Remarks

TestStand also adds the final result it computes for the step loop as a whole if you enable the
 [StepType.ResultRecordingOption](steptype-resultrecordingoption.html)
 property for the step.

#### See Also

[StepType.LoopIncExpression](steptype-loopincexpression.html)

[StepType.LoopInitExpression](steptype-loopinitexpression.html)

[StepType.LoopStatusExpression](steptype-loopstatusexpression.html)

[StepType.LoopType](steptype-looptype.html)

[StepType.LoopWhileExpression](steptype-loopwhileexpression.html)

[StepType.ResultRecordingOption](steptype-resultrecordingoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-recordresult.html language=enus -->
## TOPIC 02854: StepType.RecordResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-recordresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-recordresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.RecordResult Data Type Boolean Purpose This property is obsolete. Use the StepType.ResultRecordingOption property instead. Remarks Specifies whether to record the Result properties of the step. If you set this property to True , TestStand records the result of the step unless the Eng

### StepType.RecordResult

#### Syntax

[StepType](steptype.html).RecordResult

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StepType.ResultRecordingOption

#### Remarks

Specifies whether to record the Result properties of the step. If you set this property to
 True
 , TestStand records the result of the step unless the
 [Engine.DisableResults](engine-disableresults.html)
 property is
 True
 or the
 [Sequence.DisableResults](sequence-disableresults.html)
 property is
 True
 .

You can override this setting with the
 [StationOptions.DisableResults](stationoptions-disableresults.html)
 and
 Sequence.DisableResults
 properties.

For steps that loop, use the
 [StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)
 property to specify whether to add step results to the sequence result list after each loop iteration.

#### See Also

[Engine.DisableResults](engine-disableresults.html)

[Sequence.DisableResults](sequence-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[StepType.RecordLoopIterationResults](steptype-recordloopiterationresults.html)

[StepType.ResultRecordingOption](steptype-resultrecordingoption.html)

Parent topic:

Obsolete StepType Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-removesubstep.html language=enus -->
## TOPIC 02855: StepType.RemoveSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-removesubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-removesubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.RemoveSubstep( substepIndex) Purpose Removes the substep specified for the zero-based index passed as an input parameter. Parameters substepIndex As Long [In] Specifies the zero-based index of the substep to remove. See Also StepType.AddSubstep StepType.GetSubstep StepType.NumSubstep

### StepType.RemoveSubstep

#### Syntax

[StepType](steptype.html).RemoveSubstep( substepIndex)

#### Purpose

Removes the substep specified for the zero-based index passed as an input parameter.

#### Parameters

substepIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the substep to remove.

#### See Also

[StepType.AddSubstep](steptype-addsubstep.html)

[StepType.GetSubstep](steptype-getsubstep.html)

[StepType.NumSubsteps](steptype-numsubsteps.html)

[StepType.SwapSubsteps](steptype-swapsubsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-resultrecordingoption.html language=enus -->
## TOPIC 02856: StepType.ResultRecordingOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-resultrecordingoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-resultrecordingoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.ResultRecordingOption Data Type ResultRecordingOptions Use the following constants with this data type: ResultRecordingOption_Disabled –(Value: 0) Specifies that the step does not record results. ResultRecordingOption_Enabled –(Value: 1) Specifies that the step records results unless

### StepType.ResultRecordingOption

#### Syntax

[StepType](steptype.html).ResultRecordingOption

#### Data Type

[ResultRecordingOptions](resultrecordingoptions.html)

Use the following constants with this data type:

- ResultRecordingOption_Disabled 
 –(Value: 0) Specifies that the step does not record results.
- ResultRecordingOption_Enabled 
 –(Value: 1) Specifies that the step records results unless the
 Sequence.DisableResults 
 or
 StationOptions.DisableResults 
 property is
 True 
 .
- ResultRecordingOption_EnabledAndOverrideSequenceSetting 
 –(Value: 2) Specifies that the step records results unless the
 StationOptions.DisableResults 
 property is
 True 
 .

#### Purpose

Specifies whether to record the result properties of the step.

#### Remarks

For steps that loop, use the
 [Step.RecordLoopIterationResults](step-recordloopiterationresults.html)
 property to specify to add step results to the sequence result list after each loop iteration.

#### See Also

[Step.RecordLoopIterationResults](step-recordloopiterationresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-runmode.html language=enus -->
## TOPIC 02857: StepType.RunMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-runmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-runmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.RunMode Data Type String Purpose Specifies the run mode of the step. Remarks This property is the run mode TestStand stores for steps of this type in the sequence file. See Also RunModes

### StepType.RunMode

#### Syntax

[StepType](steptype.html).RunMode

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the run mode of the step.

#### Remarks

This property is the run mode TestStand stores for steps of this type in the sequence file.

#### See Also

[RunModes](runmodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-specifymodule.html language=enus -->
## TOPIC 02858: StepType.SpecifyModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-specifymodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-specifymodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SpecifyModule( specModOptions = SpecMod_NoOptions) Return Value Boolean Returns True if the Specify Module dialog box modifies the step type. Purpose Launches the Specify Module dialog box for the step type, if one exists. Remarks Check the CanSpecifyModule property to verify that yo

### StepType.SpecifyModule

#### Syntax

[StepType](steptype.html).SpecifyModule( specModOptions = SpecMod_NoOptions)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the
 [Specify Module](../tsref/edit-activex-com-call-dialog-box.html)
 dialog box modifies the step type.

#### Purpose

Launches the Specify Module dialog box for the step type, if one exists.

#### Remarks

Check the CanSpecifyModule property to verify that you can call this method.

The current version of TestStand does not support all SpecifyModuleOptions options for all adapters, as the following list indicates:

- LabVIEW Adapter 
 —Supports only
 SpecMod_ReadOnly 
 .
- LabWindows/CVI Adapter 
 —Supports all options.
- C/C++ DLL Adapter 
 —Supports all options.
- ActiveX/COM Adapter 
 —Supports only
 SpecMod_ReadOnly 
 .
- Sequence Adapter 
 —Supports all options.
- HTBasic Adapter 
 —Supports only
 SpecMod_ReadOnly 
 .

#### Parameters

specModOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [SpecifyModuleOptions](specifymoduleoptions.html)
 to modify the behavior of the dialog box.

This parameter has a default value of
 SpecMod_NoOptions
 .

#### See Also

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

[SpecifyModuleOptions](specifymoduleoptions.html)

[StepType.CanSpecifyModule](steptype-canspecifymodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-statusexpression.html language=enus -->
## TOPIC 02859: StepType.StatusExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-statusexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-statusexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.StatusExpression Data Type String Purpose Specifies the status expression for the step. Remarks Use this expression to set the ResultStatus property of the step. TestStand executes this expression after executing all other substeps and expressions for the step. The expression must ev

### StepType.StatusExpression

#### Syntax

[StepType](steptype.html).StatusExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the status expression for the step.

#### Remarks

Use this expression to set the ResultStatus property of the step. TestStand executes this expression after executing all other substeps and expressions for the step. The expression must evaluate to a string.

#### See Also

[StepType.PostExpression](steptype-postexpression.html)

[StepType.PreExpression](steptype-preexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-stepfailcausessequencefail.html language=enus -->
## TOPIC 02860: StepType.StepFailCausesSequenceFail

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-stepfailcausessequencefail.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-stepfailcausessequencefail.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.StepFailCausesSequenceFail Data Type Boolean Purpose Specifies whether failure of the step causes the sequence to fail. Remarks If this property is True and the step fails, TestStand sets the internal status property of the sequence that contains the step to Failure . If the Sequence

### StepType.StepFailCausesSequenceFail

#### Syntax

[StepType](steptype.html).StepFailCausesSequenceFail

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether failure of the step causes the sequence to fail.

#### Remarks

If this property is
 True
 and the step fails, TestStand sets the internal status property of the sequence that contains the step to
 Failure
 . If the
 [Sequence.FailureAction](sequence-failureaction.html)
 property is
 True
 for the sequence, the execution jumps to the Cleanup step group of the sequence.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-swapsubsteps.html language=enus -->
## TOPIC 02861: StepType.SwapSubsteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-swapsubsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-swapsubsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwapSubsteps( Index1, index2) Purpose Swaps the position of the substeps located in the indexes passed as input parameters. Remarks To swap the position of the substeps, both substeps must be of the same type. The following types are available: Pre-, Post-, Edit, and Custom. The orde

### StepType.SwapSubsteps

#### Syntax

[StepType](steptype.html).SwapSubsteps( Index1, index2)

#### Purpose

Swaps the position of the substeps located in the indexes passed as input parameters.

#### Remarks

To swap the position of the substeps, both substeps must be of the same type. The following types are available: Pre-, Post-, Edit, and Custom. The order of the substeps in the list defines the order in which the Pre- and Post-Step substeps execute and the order in which the menu items for the Edit substep appear in the context menu of the Sequence view in the Sequence File window.

#### Parameters

Index1
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index related to one of the substeps to be swapped.

index2
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index related to one of the substeps to be swapped.

#### See Also

[StepType.AddSubstep](steptype-addsubstep.html)

[StepType.GetSubstep](steptype-getsubstep.html)

[StepType.NumSubsteps](steptype-numsubsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecconnectionlifetime.html language=enus -->
## TOPIC 02862: StepType.SwitchExecConnectionLifetime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecconnectionlifetime.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecconnectionlifetime.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecConnectionLifetime Data Type SwitchExecLifetimes Use the following constants with this data type: SwitchExecLifetime_Execution –(Value: 1) Specifies that the route is connected until the execution completes. SwitchExecLifetime_Manual –(Value: 0) Specifies that the route is

### StepType.SwitchExecConnectionLifetime

#### Syntax

[StepType](steptype.html).SwitchExecConnectionLifetime

#### Data Type

[SwitchExecLifetimes](switchexeclifetimes.html)

Use the following constants with this data type:

- SwitchExecLifetime_Execution 
 –(Value: 1) Specifies that the route is connected until the execution completes.
- SwitchExecLifetime_Manual 
 –(Value: 0) Specifies that the route is connected until manually disconnected.
- SwitchExecLifetime_Sequence 
 –(Value: 3) Specifies that the route is connected until the sequence completes executing.
- SwitchExecLifetime_Step 
 –(Value: 4) Specifies that the route is connected until the step completes executing.
- SwitchExecLifetime_Thread 
 –(Value: 2) Specifies that the route is connected until the thread completes.

#### Purpose

Specifies the lifetime TestStand applies to routes when the value of the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property is
 Connect
 or
 ConnectDisconnect
 . You can specify whether you want the route to exist until manually disconnected later or until the step, sequence, thread, or execution completes.

Note

StepType.SwitchExecMulticonnectMode

Multiconnect

Manual

#### See Also

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecMulticonnectMode](steptype-switchexecmulticonnectmode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecenabled.html language=enus -->
## TOPIC 02863: StepType.SwitchExecEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecEnabled Data Type Boolean Purpose Specifies whether to perform a switching operation for the step. The step performs the switching operation the StepType.SwitchExecOperation property specifies for the virtual device the StepType.SwitchExecVirtualDevice property specifies. T

### StepType.SwitchExecEnabled

#### Syntax

[StepType](steptype.html).SwitchExecEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to perform a switching operation for the step. The step performs the switching operation the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property specifies for the virtual device the
 [StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)
 property specifies.

Note

#### See Also

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecmulticonnectmode.html language=enus -->
## TOPIC 02864: StepType.SwitchExecMulticonnectMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecmulticonnectmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecmulticonnectmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecMulticonnectMode Data Type SwitchExecMulticonnectModes Use the following constants with this data type: SwitchExecMulticonnectMode_Default –(Value: -1) Defaults to the multiconnect mode as predefined for each route in the NI Switch Executive. SwitchExecMulticonnectMode_Mult

### StepType.SwitchExecMulticonnectMode

#### Syntax

[StepType](steptype.html).SwitchExecMulticonnectMode

#### Data Type

[SwitchExecMulticonnectModes](switchexecmulticonnectmodes.html)

Use the following constants with this data type:

- SwitchExecMulticonnectMode_Default 
 –(Value: -1) Defaults to the multiconnect mode as predefined for each route in the NI Switch Executive.
- SwitchExecMulticonnectMode_Multiconnect 
 –(Value: 1) A route can connect multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple Connect operations for a specific route, the route is not physically disconnected until an equal number of Disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
- SwitchExecMulticonnectMode_None 
 –(Value: 0) A route can connect only once.

#### Purpose

Specifies the behavior when more than one connection operation occurs on a specific route.

Note

Multiconnect

#### See Also

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecoperation.html language=enus -->
## TOPIC 02865: StepType.SwitchExecOperation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecoperation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecoperation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecOperation Data Type SwitchExecOperations Use the following constants with this data type: SwitchExecOperation_Connect –(Value: 1) Creates the paths for the specified routes in the Step.SwitchExecRoutesToConnect property. SwitchExecOperation_ConnectDisconnect –(Value: 4) Cre

### StepType.SwitchExecOperation

#### Syntax

[StepType](steptype.html).SwitchExecOperation

#### Data Type

[SwitchExecOperations](switchexecoperations.html)

Use the following constants with this data type:

- SwitchExecOperation_Connect 
 –(Value: 1) Creates the paths for the specified routes in the
 Step.SwitchExecRoutesToConnect 
 property.
- SwitchExecOperation_ConnectDisconnect 
 –(Value: 4) Creates the paths for the routes specified in the
 Step.SwitchExecRoutesToConnect 
 property and destroys the paths for the routes specified in the
 Step.SwitchExecRoutesToDisconnect 
 property. Use the
 Step.SwitchExecOperationOrder 
 property to specify whether the Disconnect operation occurs before or after the Connect operation.
- SwitchExecOperation_Disconnect 
 –(Value: 2) Destroys the paths the specified routes define in the
 Step.SwitchExecRoutesToDisconnect 
 property.
- SwitchExecOperation_DisconnectAll 
 –(Value: 3) Disconnects all previously created paths.

#### Purpose

Specifies whether to connect or disconnect the routes the
 StepType.SwitchExecRoutesToConnect
 and
 StepType.SwitchExecRoutesToDisconnect
 properties specify, or disconnect all previously connected routes for a virtual device.

Note

SwitchExecWaitForDebounce

#### See Also

[Step.SwitchExecOperationOrder](step-switchexecoperationorder.html)

[StepType.SwitchExecRoutesToConnect](steptype-switchexecroutestoconnect.html)

[StepType.SwitchExecRoutesToDisconnect](steptype-switchexecroutestodisconnect.html)

[StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)

[StepType.SwitchExecWaitForDebounce](steptype-switchexecwaitfordebounce.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecoperationorder.html language=enus -->
## TOPIC 02866: StepType.SwitchExecOperationOrder

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecoperationorder.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecoperationorder.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecOperationOrder Data Type SwitchExecOperationOrders Use the following constants with this data type: SwitchExecOperationOrder_DisconnectAfterConnect –(Value: 2) Specifies to connect routes before disconnecting any routes. Use this mode of operation when you are switching ele

### StepType.SwitchExecOperationOrder

#### Syntax

[StepType](steptype.html).SwitchExecOperationOrder

#### Data Type

[SwitchExecOperationOrders](switchexecoperationorders.html)

Use the following constants with this data type:

- SwitchExecOperationOrder_DisconnectAfterConnect 
 –(Value: 2) Specifies to connect routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to the source.
- SwitchExecOperationOrder_DisconnectBeforeConnect 
 –(Value: 1) Specifies to disconnect routes before connecting any routes. This is the typical mode of operation.

#### Purpose

Specifies whether the Disconnect operation occurs before or after the Connect operation when the value of the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property is
 ConnectDisconnect
 .

#### See Also

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecroutestoconnect.html language=enus -->
## TOPIC 02867: StepType.SwitchExecRoutesToConnect

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecroutestoconnect.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecroutestoconnect.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecRoutesToConnect Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the routes to connect when the value of the StepType.SwitchExecOperation property is Connect or ConnectDisconnect . The expression must be a valid route specificati

### StepType.SwitchExecRoutesToConnect

#### Syntax

[StepType](steptype.html).SwitchExecRoutesToConnect

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the routes to connect when the value of the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property is
 Connect
 or
 ConnectDisconnect
 .

Note

route specification string

StepType.SwitchExecVirtualDevice

#### See Also

[Route Specification String](/csh?context=ts_tsref_route_spec_string)

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecroutestodisconnect.html language=enus -->
## TOPIC 02868: StepType.SwitchExecRoutesToDisconnect

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecroutestodisconnect.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecroutestodisconnect.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecRoutesToDisconnect Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the routes to disconnect when the value of the StepType.SwitchExecOperation property is Disconnect or ConnectDisconnect . The expression must be a valid route sp

### StepType.SwitchExecRoutesToDisconnect

#### Syntax

[StepType](steptype.html).SwitchExecRoutesToDisconnect

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the routes to disconnect when the value of the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property is
 Disconnect
 or
 ConnectDisconnect
 .

Note

route specification string

StepType.SwitchExecVirtualDevice

#### See Also

[Route Specification String](/csh?context=ts_tsref_route_spec_string)

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecVirtualDevice](steptype-switchexecvirtualdevice.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecvirtualdevice.html language=enus -->
## TOPIC 02869: StepType.SwitchExecVirtualDevice

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecvirtualdevice.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecvirtualdevice.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecVirtualDevice Data Type String Purpose Specifies an expression TestStand evaluates at run time to determine the virtual device name on which to perform the switching operation. Remarks The NI Switch Executive software in Measurement & Automation Explorer defines the virtual

### StepType.SwitchExecVirtualDevice

#### Syntax

[StepType](steptype.html).SwitchExecVirtualDevice

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression TestStand evaluates at run time to determine the virtual device name on which to perform the switching operation.

#### Remarks

Note

#### See Also

[StepType.SwitchExecEnabled](steptype-switchexecenabled.html)

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-switchexecwaitfordebounce.html language=enus -->
## TOPIC 02870: StepType.SwitchExecWaitForDebounce

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-switchexecwaitfordebounce.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-switchexecwaitfordebounce.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.SwitchExecWaitForDebounce Data Type Boolean Purpose Specifies if the operation the StepType.SwitchExecOperation property specifies waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after both the Connect and Disconnect operations are compl

### StepType.SwitchExecWaitForDebounce

#### Syntax

[StepType](steptype.html).SwitchExecWaitForDebounce

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the operation the
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 property specifies waits for all switches to debounce before returning to TestStand.

Note

#### See Also

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-usemutex.html language=enus -->
## TOPIC 02871: StepType.UseMutex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-usemutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-usemutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.UseMutex Data Type Boolean Purpose Specifies that the step acquires the a lock before it executes and releases the lock after it completes. Remarks Use the StepType.MutexNameOrRefExpr property to specify which lock the step uses. See Also StepType.BatchSyncOption StepType.MutexNameOr

### StepType.UseMutex

#### Syntax

[StepType](steptype.html).UseMutex

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the step acquires the a lock before it executes and releases the lock after it completes.

#### Remarks

Use the
 [StepType.MutexNameOrRefExpr](steptype-mutexnameorrefexpr.html)
 property to specify which lock the step uses.

#### See Also

[StepType.BatchSyncOption](steptype-batchsyncoption.html)

[StepType.MutexNameOrRefExpr](steptype-mutexnameorrefexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype-windowactivation.html language=enus -->
## TOPIC 02872: StepType.WindowActivation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype-windowactivation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype-windowactivation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StepType.WindowActivation Data Type WindowActivationOptions Use the following constants with this data type: WinActOption_ActivateWhenStepCompletes –(Value: 2) Activate when the step completes. WinActOption_IfActiveReactivateWhenStepCompletes –(Value: 3) If initially active, reactivate when t

### StepType.WindowActivation

#### Syntax

[StepType](steptype.html).WindowActivation

#### Data Type

[WindowActivationOptions](windowactivationoptions.html)

Use the following constants with this data type:

- WinActOption_ActivateWhenStepCompletes 
 –(Value: 2) Activate when the step completes.
- WinActOption_IfActiveReactivateWhenStepCompletes 
 –(Value: 3) If initially active, reactivate when the step completes.
- WinActOption_None 
 –(Value: 1) No activation.

#### Purpose

Specifies whether the TestStand application activates its window when the step completes.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptype.html language=enus -->
## TOPIC 02873: StepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the StepType class represent step types in TestStand files. Every step is an instance of a step type. You create new step types with the Engine.NewStepType method. Properties AdditionalResultsHints (Read Only) AppliesToBlockStructure BatchSyncOption BlockEndTypes BlockStartTypes CanEncaps

### StepType

Objects of the StepType class represent step types in TestStand files. Every step is an instance of a step type. You create new step types with the
 [Engine.NewStepType](engine-newsteptype.html)
 method.

#### Properties

| AdditionalResultsHints (Read Only) |
| --- |
| AppliesToBlockStructure |
| BatchSyncOption |
| BlockEndTypes |
| BlockStartTypes |
| CanEncapsulate |
| CanSpecifyModule (Read Only) |
| CodeTemplates (Read Only) |
| CustomActionExpression |
| CustomFalseAction |
| CustomFalseActionTargetByExpr |
| CustomTrueAction |
| CustomTrueActionTargetByExpr |
| DefaultNameExpr |
| DescriptionExpr |
| DesignatedAdapter (Read Only) |
| DimmablePropertyKeyNames (Read Only) |
| EvalPrecondForInteractiveExecution |
| FailAction |
| FailActionTargetByExpr |
| IconName |
| IgnoreRTE |
| LoopIncExpression |
| LoopInitExpression |
| LoopStatusExpression |
| LoopType |
| LoopWhileExpression |
| MenuGroupName |
| MenuIcon (Read Only) |
| MenuIconIndex (Read Only) |
| MenuItemNameExpr |
| Module (Read Only) |
| ModuleLoadOption |
| ModuleUnloadOption |
| MutexNameOrRefExpr |
| Name |
| NumSubsteps (Read Only) |
| PassAction |
| PassActionTargetByExpr |
| PostExpression |
| Precondition |
| PreExpression |
| RecordLoopIterationResults |
| ResultRecordingOption |
| RunMode |
| StatusExpression |
| StepFailCausesSequenceFail |
| SwitchExecConnectionLifetime |
| SwitchExecEnabled |
| SwitchExecMulticonnectMode |
| SwitchExecOperation |
| SwitchExecOperationOrder |
| SwitchExecRoutesToConnect |
| SwitchExecRoutesToDisconnect |
| SwitchExecVirtualDevice |
| SwitchExecWaitForDebounce |
| UseMutex |
| WindowActivation |

#### Methods

| AddSubstep |
| --- |
| AsPropertyObject |
| ChangeDesignatedAdapter |
| CreateCombinedStepType |
| DimProperty |
| GetDefaultName |
| GetDimmablePropertyDisplayName |
| GetSubstep |
| IsPropertyDimmed |
| RemoveSubstep |
| SpecifyModule |
| SwapSubsteps |

#### See Also

[Engine.NewStepType](engine-newsteptype.html)

[Step](step.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/steptypes.html language=enus -->
## TOPIC 02874: StepTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/steptypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/steptypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants containing the type names for the built-in step types. Use these constants with the Engine.NewStep method to create a step of a particular step type. This list represents only the commonly used step type names. StepType_Action –(Value: "Action") StepType_Break –(Value: "NI_Flow_Break

### StepTypes

These constants containing the type names for the built-in step types. Use these constants with the
 [Engine.NewStep](engine-newstep.html)
 method to create a step of a particular step type.

Note

- StepType_Action 
 –(Value: "Action")
- StepType_Break 
 –(Value: "NI_Flow_Break")
- StepType_CallExecutable 
 –(Value: "CallExecutable")
- StepType_Case 
 –(Value: "NI_Flow_Case")
- StepType_Continue 
 –(Value: "NI_Flow_Continue")
- StepType_DoWhile 
 –(Value: "NI_Flow_DoWhile")
- StepType_Else 
 –(Value: "NI_Flow_Else")
- StepType_ElseIf 
 –(Value: "NI_Flow_ElseIf")
- StepType_End 
 –(Value: "NI_Flow_End")
- StepType_For 
 –(Value: "NI_Flow_For")
- StepType_ForEach 
 –(Value: "NI_Flow_ForEach")
- StepType_Goto 
 –(Value: "Goto")
- StepType_If 
 –(Value: "NI_Flow_If")
- StepType_Label 
 –(Value: "Label")
- StepType_LimitLoader 
 –(Value: "LimitLoaderStep ") This constant is obsolete. Use
 StepType_PropertyLoaderEx 
 instead.
- StepType_MessagePopup 
 –(Value: "MessagePopup")
- StepType_MultiNumericMeasurement 
 –(Value: "NI_MultipleNumericLimitTest")
- StepType_NumericMeasurement 
 –(Value: "NumericLimitTest")
- StepType_PassFailTest 
 –(Value: "PassFailTest")
- StepType_PropertyLoader 
 –(Value: "NI_VariableAndPropertyLoader") This constant is obsolete. Use
 StepType_PropertyLoaderEx 
 instead.
- StepType_PropertyLoaderEx 
 –(Value: "NI_PropertyLoader")
- StepType_Select 
 –(Value: "NI_Flow_Select")
- StepType_SequenceCall 
 –(Value: "SequenceCall")
- StepType_Statement 
 –(Value: "Statement")
- StepType_StreamLoop 
 –(Value: "NI_Flow_StreamLoop")
- StepType_StringMeasurement 
 –(Value: "StringValueTest")
- StepType_SweepLoop 
 –(Value: "NI_Flow_SweepLoop")
- StepType_Wait 
 –(Value: "NI_Wait")
- StepType_While 
 –(Value: "NI_Flow_While")

#### See Also

[Engine.NewStep](engine-newstep.html)

[StepType](steptype.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/structmemberarraystorageoptions.html language=enus -->
## TOPIC 02875: StructMemberArrayStorageOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/structmemberarraystorageoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/structmemberarraystorageoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommonCAdapter.GetStructMemberArrayStorage and CommonCAdapter.SetStructMemberArrayStorage methods to specify how to store an array inside a structure. StructMemberStorage_ArrayPointer –(Value: 0x101) Specifies to store the array as a pointer to a memory location outside

### StructMemberArrayStorageOptions

Use these constants with the
 [CommonCAdapter.GetStructMemberArrayStorage](commoncadapter-getstructmemberarraystorage.html)
 and
 [CommonCAdapter.SetStructMemberArrayStorage](commoncadapter-setstructmemberarraystorage.html)
 methods to specify how to store an array inside a structure.

- StructMemberStorage_ArrayPointer 
 –(Value: 0x101) Specifies to store the array as a pointer to a memory location outside of the struct.
- StructMemberStorage_InlineArray 
 –(Value 0x100) Specifies to store the array within the structure itself.
- StructMemberStorage_LabVIEWArray 
 –(Value: 0x102) Specifies to store the array in the format that the DLLs created with the LabVIEW Application Builder use.

#### See Also

[CommonCAdapter.GetStructMemberArrayStorage](commoncadapter-getstructmemberarraystorage.html)

[CommonCAdapter.SetStructMemberArrayStorage](commoncadapter-setstructmemberarraystorage.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/structmemberstorageoptions.html language=enus -->
## TOPIC 02876: StructMemberStorageOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/structmemberstorageoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/structmemberstorageoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommonCAdapter.GetStructMemberStorage and CommonCAdapter.SetStructMemberStorage methods to specify how to store a member inside a structure. StructMemberStorage_EmbeddedStruct –(Value: 32) Specifies to store a struct as a member inside the containing struct. StructMember

### StructMemberStorageOptions

Use these constants with the
 [CommonCAdapter.GetStructMemberStorage](commoncadapter-getstructmemberstorage.html)
 and
 [CommonCAdapter.SetStructMemberStorage](commoncadapter-setstructmemberstorage.html)
 methods to specify how to store a member inside a structure.

- StructMemberStorage_EmbeddedStruct 
 –(Value: 32) Specifies to store a struct as a member inside the containing struct.
- StructMemberStorage_InlineString 
 –(Value: 0) Specifies to store a string as an array of characters inside the struct.
- StructMemberStorage_LabVIEWString 
 –(Value: 2) Specifies to store a string in the format used by DLLs created with the LabVIEW Application Builder. The
 CommonCAdapter.GetStructMemberType 
 and
 CommonCAdapter.SetStructMemberType 
 methods do not apply when the
 CommonCAdapter.GetStructMemberStorage 
 method returns this value.
- StructMemberStorage_StringPointer 
 –(Value: 1) Specifies to store a string as a character pointer. The characters themselves are stored at a memory location outside of the containing struct.
- StructMemberStorage_StructPointer 
 –(Value: 33) Specifies to store a pointer inside the containing struct which points to a member struct at a memory location outside of the containing struct.

#### See Also

[CommonCAdapter.GetStructMemberStorage](commoncadapter-getstructmemberstorage.html)

[CommonCAdapter.GetStructMemberType](commoncadapter-getstructmembertype.html)

[CommonCAdapter.SetStructMemberStorage](commoncadapter-setstructmemberstorage.html)

[CommonCAdapter.SetStructMemberType](commoncadapter-setstructmembertype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/structmembertypes.html language=enus -->
## TOPIC 02877: StructMemberTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/structmembertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/structmembertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommonCAdapter.GetStructMemberType and CommonCAdapter.SetStructMemberType methods to get or set the data type of the structure member. StructMemberType_CString –(Value: 0x20) Specifies a string stored as a C-style char pointer. Do not modify the string value in the struc

### StructMemberTypes

Use these constants with the
 [CommonCAdapter.GetStructMemberType](commoncadapter-getstructmembertype.html)
 and
 [CommonCAdapter.SetStructMemberType](commoncadapter-setstructmembertype.html)
 methods to get or set the data type of the structure member.

- StructMemberType_CString 
 –(Value: 0x20) Specifies a string stored as a C-style char pointer. Do not modify the string value in the struct if it has this type.
- StructMemberType_CStringBuffer 
 –(Value: 0x22) Specifies a C-style char string stored as a buffer that can be modified.
- StructMemberType_CVIHandle 
 –(Value: 0x41) Specifies an ActiveX reference stored as a LabWindows/CVI CAObjHandle.
- StructMemberType_Float32 
 –(Value: 0) Specifies a number stored as a 32-bit floating point value.
- StructMemberType_Float64 
 –(Value: 1) Specifies a number stored as a 64-bit floating point value.
- StructMemberType_IDispatch 
 –(Value: 0x40) Specifies an ActiveX reference stored as an IDispatch pointer.
- StructMemberType_Int16 
 –(Value: 4) Specifies a number stored as a 16-bit integer.
- StructMemberType_Int32 
 –(Value: 6) Specifies a number stored as a 32-bit integer.
- StructMemberType_Int64 
 –(Value: 8) Specifies a number stored as a 64-bit integer.
- StructMemberType_Int8 
 –(Value: 2) Specifies a number stored as a 8-bit integer.
- StructMemberType_IUnknown 
 –(Value: 0x42) Specifies a COM reference stored as an IUnknown pointer.
- StructMemberType_UInt16 
 –(Value: 5) Specifies a number stored as a 16-bit unsigned integer.
- StructMemberType_UInt32 
 –(Value: 7) Specifies a number stored as a 32-bit unsigned integer.
- StructMemberType_UInt64 
 –(Value: 9) Specifies a number stored as a 64-bit unsigned integer.
- StructMemberType_UInt8 
 –(Value: 3) Specifies a number stored as a 8-bit unsigned integer.
- StructMemberType_UnicodeString 
 –(Value: 0x21) Specifies a string stored as a C-style wide character pointer, such as a pointer to an array of 16-bit characters. Do not modify the string value in the struct if it has this type.
- StructMemberType_UnicodeStringBuffer 
 –(Value: 0x23) Specifies a C-style wide character string stored as a buffer of 16-bit characters that can be modified.

#### See Also

[CommonCAdapter.GetStructMemberType](commoncadapter-getstructmembertype.html)

[CommonCAdapter.SetStructMemberType](commoncadapter-setstructmembertype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/structpassingoptions.html language=enus -->
## TOPIC 02878: StructPassingOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/structpassingoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/structpassingoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommonCAdapter.DefaultStructPacking property and the CommonCAdapter.GetStructPacking and CommonCAdapter.SetStructPacking methods to specify the packing alignment for structure and union members. StructPassing_AdapterDefault –(Value: 0x0) Specifies to use the default Test

### StructPassingOptions

Use these constants with the
 [CommonCAdapter.DefaultStructPacking](commoncadapter-defaultstructpacking.html)
 property and the
 [CommonCAdapter.GetStructPacking](commoncadapter-getstructpacking.html)
 and
 [CommonCAdapter.SetStructPacking](commoncadapter-setstructpacking.html)
 methods to specify the packing alignment for structure and union members.

- StructPassing_AdapterDefault 
 –(Value: 0x0) Specifies to use the default TestStand setting to store structure and union members. You can change the default TestStand setting by modifying the
 CommonCAdapter.DefaultStructPacking 
 property or by configuring it in the
 C/C++ DLL Adapter Configuration 
 or
 LabWindows/CVI Adapter Configuration 
 dialog boxes. Do not pass
 StructPassing_AdapterDefault 
 to the
 CommonCAdapter.DefaultStructPacking 
 property itself.
- StructPassing_EightByte 
 –(Value: 0x8) Specifies to store structure and union members on an 8-byte boundary.
- StructPassing_FourByte 
 –(Value: 0x4) Specifies to store structure and union members on a 4-byte boundary.
- StructPassing_OneByte 
 –(Value: 0x1) Specifies to store structure and union members on a 1-byte boundary.
- StructPassing_SixteenByte 
 –(Value: 0x16) Specifies to store structure and union members on a 16-byte boundary.
- StructPassing_TwoByte 
 –(Value: 0x2) Specifies to store structure and union members on a 2-byte boundary.

#### See Also

[CommonCAdapter.DefaultStructPacking](commoncadapter-defaultstructpacking.html)

[CommonCAdapter.GetStructPacking](commoncadapter-getstructpacking.html)

[CommonCAdapter.SetStructPacking](commoncadapter-setstructpacking.html)

[C/C++ DLL Adapter Configuration](../tsref/c-c-dll-adapter-configuration-dialog-box.html)

[LabWindows/CVI Adapter Configuration dialog box](../tsref/labwindows-cvi-adapter-configuration-dialog-b.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/switchexeclifetimes.html language=enus -->
## TOPIC 02879: SwitchExecLifetimes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/switchexeclifetimes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/switchexeclifetimes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify a switch connection lifetime. Use the values of this enumeration with the Step.SwitchExecConnectionLifetime and StepType.SwitchExecConnectionLifetime properties. SwitchExecLifetime_Execution –(Value: 1) Specifies that the route is connected until the execu

### SwitchExecLifetimes

This data type contains values that specify a switch connection lifetime. Use the values of this enumeration with the
 [Step.SwitchExecConnectionLifetime](step-switchexecconnectionlifetime.html)
 and
 [StepType.SwitchExecConnectionLifetime](steptype-switchexecconnectionlifetime.html)
 properties.

- SwitchExecLifetime_Execution 
 –(Value: 1) Specifies that the route is connected until the execution completes.
- SwitchExecLifetime_Manual 
 –(Value: 0) Specifies that the route is connected until manually disconnected.
- SwitchExecLifetime_Sequence 
 –(Value: 3) Specifies that the route is connected until the sequence completes executing.
- SwitchExecLifetime_Step 
 –(Value: 4) Specifies that the route is connected until the step completes executing.
- SwitchExecLifetime_Thread 
 –(Value: 2) Specifies that the route is connected until the thread completes.

#### See Also

[Step.SwitchExecConnectionLifetime](step-switchexecconnectionlifetime.html)

[StepType.SwitchExecConnectionLifetime](steptype-switchexecconnectionlifetime.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/switchexecmulticonnectmodes.html language=enus -->
## TOPIC 02880: SwitchExecMulticonnectModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/switchexecmulticonnectmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/switchexecmulticonnectmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify multiconnect behavior. Use the values of this enumeration with the Step.SwitchExecMulticonnectMode and StepType.SwitchExecMulticonnectMode properties. SwitchExecMulticonnectMode_Default –(Value: -1) Defaults to the multiconnect mode as predefined for each

### SwitchExecMulticonnectModes

This data type contains values that specify multiconnect behavior. Use the values of this enumeration with the
 [Step.SwitchExecMulticonnectMode](step-switchexecmulticonnectmode.html)
 and
 [StepType.SwitchExecMulticonnectMode](steptype-switchexecmulticonnectmode.html)
 properties.

- SwitchExecMulticonnectMode_Default 
 –(Value: -1) Defaults to the multiconnect mode as predefined for each route in the NI Switch Executive.
- SwitchExecMulticonnectMode_Multiconnect 
 –(Value: 1) A route can connect multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple Connect operations for a specific route, the route is not physically disconnected until an equal number of Disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
- SwitchExecMulticonnectMode_None 
 –(Value: 0) A route can connect only once.

#### See Also

[Step.SwitchExecMulticonnectMode](step-switchexecmulticonnectmode.html)

[StepType.SwitchExecMulticonnectMode](steptype-switchexecmulticonnectmode.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/switchexecoperationorders.html language=enus -->
## TOPIC 02881: SwitchExecOperationOrders

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/switchexecoperationorders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/switchexecoperationorders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify whether the Disconnect operation occurs before or after the Connect operation. Use the values of this enumeration with the Step.SwitchExecOperationOrder and StepType.SwitchExecOperationOrder properties. SwitchExecOperationOrder_DisconnectAfterConnect –(Val

### SwitchExecOperationOrders

This data type contains values that specify whether the Disconnect operation occurs before or after the Connect operation. Use the values of this enumeration with the
 [Step.SwitchExecOperationOrder](step-switchexecoperationorder.html)
 and
 [StepType.SwitchExecOperationOrder](steptype-switchexecoperationorder.html)
 properties.

- SwitchExecOperationOrder_DisconnectAfterConnect 
 –(Value: 2) Specifies to connect routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to the source.
- SwitchExecOperationOrder_DisconnectBeforeConnect 
 –(Value: 1) Specifies to disconnect routes before connecting any routes. This is the typical mode of operation.

#### See Also

[Step.SwitchExecOperationOrder](step-switchexecoperationorder.html)

[StepType.SwitchExecOperationOrder](steptype-switchexecoperationorder.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/switchexecoperations.html language=enus -->
## TOPIC 02882: SwitchExecOperations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/switchexecoperations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/switchexecoperations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify a switch connection operation. Use the values of this enumeration with the Step.SwitchExecOperation and StepType.SwitchExecOperation properties. SwitchExecOperation_Connect –(Value: 1) Creates the paths for the specified routes in the Step.SwitchExecRoutes

### SwitchExecOperations

This data type contains values that specify a switch connection operation. Use the values of this enumeration with the
 [Step.SwitchExecOperation](step-switchexecoperation.html)
 and
 [StepType.SwitchExecOperation](steptype-switchexecoperation.html)
 properties.

- SwitchExecOperation_Connect 
 –(Value: 1) Creates the paths for the specified routes in the
 Step.SwitchExecRoutesToConnect 
 property.
- SwitchExecOperation_ConnectDisconnect 
 –(Value: 4) Creates the paths for the routes specified in the
 Step.SwitchExecRoutesToConnect 
 property and destroys the paths for the routes specified in the
 Step.SwitchExecRoutesToDisconnect 
 property. Use the
 Step.SwitchExecOperationOrder 
 property to specify whether the Disconnect operation occurs before or after the Connect operation.
- SwitchExecOperation_Disconnect 
 –(Value: 2) Destroys the paths the specified routes define in the
 Step.SwitchExecRoutesToDisconnect 
 property.
- SwitchExecOperation_DisconnectAll 
 –(Value: 3) Disconnects all previously created paths.

#### See Also

[Step.SwitchExecOperation](step-switchexecoperation.html)

[Step.SwitchExecOperationOrder](step-switchexecoperationorder.html)

[Step.SwitchExecRoutesToConnect](step-switchexecroutestoconnect.html)

[Step.SwitchExecRoutesToDisconnect](step-switchexecroutestodisconnect.html)

[StepType.SwitchExecOperation](steptype-switchexecoperation.html)

[StepType.SwitchExecOperationOrder](steptype-switchexecoperationorder.html)

[StepType.SwitchExecRoutesToConnect](steptype-switchexecroutestoconnect.html)

[StepType.SwitchExecRoutesToDisconnect](steptype-switchexecroutestodisconnect.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/teststand-adapter-api-reference.html language=enus -->
## TOPIC 02883: TestStand Adapter API Reference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/teststand-adapter-api-reference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/teststand-adapter-api-reference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object and Description ActiveXAdapter Use objects from the ActiveXAdapter class to configure and obtain ActiveX/COM Adapter-specific information about the module adapter. Call Engine.GetAdapter or Engine.GetAdapterByKeyName to obtain a reference to the adapter object. To access the properties and me

### TestStand Adapter API Reference

| Object and Description |  |
| --- | --- |
| ActiveXAdapter |  |
| Use objects from the ActiveXAdapter class to configure and obtain ActiveX/COM Adapter-specific information about the module adapter. Call Engine.GetAdapter or Engine.GetAdapterByKeyName to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use AsAdapter to obtain an object. |  |
| ActiveXCoClass |  |
| Use an ActiveXCoClass object to obtain information about a coclass defined in a type library. Use the ActiveXServer.CoClasses property to obtain a collection of coclasses the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any coclass information for the server. |  |
| ActiveXCoClasses |  |
| A collection of ActiveXCoClass objects. Use the ActiveXServer.CoClasses property to obtain a collection of ActiveXCoClass objects the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any coclass information for the server. |  |
| ActiveXInterface |  |
| Use an ActiveXInterface object to obtain information about an interface defined in a type library. Use the ActiveXServer.Interfaces property to obtain a collection of interfaces the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any interface information for the server. |  |
| ActiveXInterfaces |  |
| A collection of ActiveXInterface objects. Use the ActiveXServer.Interfaces property to obtain a collection of interfaces the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any interface information for the server. |  |
| ActiveXMember |  |
| Use an ActiveXMember object to obtain information about a method or property defined in a type library. Use the ActiveXInterface.VTableMembers and ActiveXInterface.DispatchMembers properties to obtain a collection of members the type library for an interface of the server defines. |  |
| ActiveXMembers |  |
| A collection of ActiveXMember objects. Use the ActiveXInterface.VTableMembers and ActiveXInterface.DispatchMembers properties to obtain a collection of ActiveXMember objects defined for an interface in the type library of the server. |  |
| ActiveXModule |  |
| Use objects from the ActiveXModule class to specify and obtain ActiveX/COM Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to an ActiveXModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the ActiveXModule.AsModule method to obtain an object. You can use the Module.LoadPrototype method to load the prototype for the module the step specifies. |  |
| ActiveXParameter |  |
| Use objects from the ActiveXParameter class to configure and obtain parameter-specific information for an item in the ActiveXParameters collection class. |  |
| ActiveXParameters |  |
| Use objects from the ActiveXParameters class to configure and obtain parameters for a module that uses the ActiveX/COM Adapter. Use the ActiveXModule.Parameters property to obtain the collection of parameters for a module. |  |
| ActiveXServer |  |
| Use an ActiveXServer object to obtain information about a server and its type library registered on this computer. Use the ActiveXAdapter.Servers property to obtain a collection of ActiveXServer objects. You must call the ActiveXServer.LoadTypeLibrary method before you access any type library related properties. |  |
| ActiveXServers |  |
| A collection of ActiveXServer objects. Use the ActiveXAdapter.Servers property to obtain a collection of ActiveXServer objects. You must call the ActiveXServer.LoadTypeLibrary method before you access any type library related properties. |  |
| CommonCAdapter |  |
| Use objects from the CommonCAdapter class to configure and obtain common information about the LabWindows/CVI and C/C++ DLL Adapters. To access the properties and methods of the Adapter class, use the CommonCAdapter.AsAdapter method to obtain an object. To access the properties and methods of a specific adapter class, query the CommonCAdapter object for the interface of the adapter-specific interface you want. |  |
| CommonCModule |  |
| Use objects from the CommonCModule class to specify and obtain common information for the LabWindows/CVI and C/C++ DLL code modules that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a CommonCModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the CommonCModule.AsModule method to obtain an object. To access the properties and methods of a specific module class, query the CommonCModule object for the interface of the module-specific interface you want to acquire. You can use the Module.LoadPrototype method to load the prototype for the module the step specifies. |  |
| CommonCParameter |  |
| Use objects from the CommonCParameter class to configure and obtain common parameter information for a CVIParameter or DllParameter object. To access the properties and methods of a specific parameter class, query the CommonCParameter object for the interface of the parameter-specific interface you want. |  |
| CVIAdapter |  |
| Use objects from the CVIAdapter class to configure and obtain LabWindows/CVI Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the CVIAdapter.AsAdapter method to obtain an object. |  |
| CVIArgument |  |
| Use objects from the CVIArgument class to set the argument value to pass to a LabWindows/CVI module function using the CVIModule.Execute method. |  |
| CVIArguments |  |
| Use objects from the CVIArguments class to pass specific argument values to a LabWindows/CVI module function using the CVIModule.Execute method. Use the CVIParameters.NewArguments method to create a new arguments collection. |  |
| CVIModule |  |
| Use objects from the CVIModule class to specify and obtain LabWindows/CVI Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a CVIModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the CommonCModule class, use the CVIModule.AsCommonCModule method to obtain an object. You can use the Module.LoadPrototype method to load the prototype for the module the step specifies. |  |
| CVIParameter |  |
| Use objects from the CVIParameters class to configure and obtain LabWindows/CVI parameter-specific information for an item in the CVIParameter collection class. To access the properties and methods of the CommonCParameter class, use the CVIParameter.AsCommonCParameter method to obtain an object. |  |
| CVIParameters |  |
| Use objects from the CVIParameters class to configure and obtain parameters for a module that uses the LabWindows/CVI Adapter. Use the CVIModule.Parameters property to obtain the collection of parameters for a module. |  |
| DllAdapter |  |
| Use objects from the DllAdapter class to configure and obtain C/C++ DLL Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the DllAdapter.AsAdapter method to obtain an object. |  |
| DllArgument |  |
| Use objects from the DllArgument class to set the argument value to pass to a DLL module function using the DllModule.Execute method. |  |
| DllArguments |  |
| Use objects from the DllArguments class to pass specific argument values to a DLL module function using the DllModule.Execute method. Use the DllParameters.NewArguments method to create a new arguments collection. |  |
| DllFunction |  |
| Use objects from the DllFunction class to obtain information about a function exported from a DLL. Use the CommonCAdapter.GetDllFunctions method to obtain a collection of functions from a DLL. |  |
| DllFunctions |  |
| This class is a collection of DllFunction objects. Each item in the collection represents a function exported from a DLL that can be called from TestStand using the LabWindows/CVI or C/C++ DLL adapter. Use the CommonCAdapter.GetDllFunctions method to obtain a collection of functions from a DLL. |  |
| DllModule |  |
| Use objects from the DllModule class to specify and obtain C/C++ DLL Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a DllModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the CommonCModule class, use the DllModule.AsCommonCModule method to obtain an object. You can use the Module.LoadPrototype method to load the prototype for the module the step specifies. |  |
| DllParameter |  |
| Use objects from the DllParameter class to configure and obtain C/C++ DLL parameter-specific information for an item in the DllParameters collection class. To access the properties and methods of the CommonCParameter class, use the DllParameter.AsCommonCParameter method. |  |
| DllParameters |  |
| Use objects from the DllParameters class to configure and obtain parameters for a module that uses the C/C++ DLL Adapter. Use the DllModule.Parameters property to obtain the collection of parameters for a module. |  |
| DotNetAdapter |  |
| Use objects from the DotNetAdapter class to configure and obtain .NET Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the DotNetAdapter.AsAdapter method to obtain an object. |  |
| DotNetArgument |  |
| Use objects from this class to specify the argument value to pass to a DotNetCall object using the DotNetModule.Execute method. |  |
| DotNetArguments |  |
| Use objects from this class to pass specific argument values to a specific DotNetCall object using the DotNetModule.Execute method. Use the DotNetModule.NewModuleArguments method to create a new DotNetModuleArguments collection of DotNetArguments objects. |  |
| DotNetCall |  |
| Use objects from the DotNetCall class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute. Typically, you use this class only when you are writing a sequence editor. You can use the DotNetCall.LoadPrototypeFromSignature method to load the prototype for the call. |  |
| DotNetCalls |  |
| Use objects from the DotNetCalls class to configure and obtain calls for a module the .NET Adapter uses. Use the DotNetModule.Calls property to obtain the collection of calls for a module. |  |
| DotNetModule |  |
| Use objects from the DotNetModule class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a DotNetModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the DotNetModule.AsModule method to obtain an object. |  |
| DotNetModuleArguments |  |
| Use objects from this class to pass specific argument values to a DotNetModule object using the DotNetModule.Execute method. Use the DotNetModule.NewModuleArguments method to create a new DotNetModuleArguments collection. |  |
| DotNetParameter |  |
| Use objects from the DotNetParameters class to configure and obtain parameters for a module that uses the .NET Adapter. Use the DotNetCall.Parameters property to obtain the collection of parameters for a module and the DotNetParameter.Elements property to obtain the collection that represents the members of a structure parameter or the elements of an array of structures parameter. |  |
| DotNetParameters |  |
| Use objects from the DotNetParameters class to configure and obtain parameters for a DotNetCall . Use the DotNetCall.Parameters property to obtain the collection of parameters for a call and the DotNetParameter.Elements method to obtain the collection that represents the members of a structure parameter or the elements of an array of structures parameter. |  |
| HTBasicAdapter |  |
| Use objects from the HTBasicAdapter class to configure and obtain HTBasic Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the HTBasicAdapter.AsAdapter method to obtain an object. |  |
| HTBasicModule |  |
| Use objects from the HTBasicModule class to specify and obtain HTBasic Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to an HTBasicModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the HTBasicModule.AsModule method to obtain an object. |  |
| LabVIEWAdapter |  |
| Use objects from the LabVIEW Adapter class to configure and obtain LabVIEW Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the LabVIEWAdapter.AsAdapter method to obtain an object. |  |
| LabVIEWArgument |  |
| Use objects from the LabVIEWArgument class to set the argument value to pass to a LabVIEW VI using the LabVIEWModule.Execute method. |  |
| LabVIEWArguments |  |
| Use objects from the LabVIEWArguments class to pass specific argument values to a LabVIEW VI using the LabVIEWModule.Execute method. Use the LabVIEWParameters.NewArguments method to create a new arguments collection. |  |
| LabVIEWModule |  |
| Use objects from the LabVIEWModule class to specify and obtain LabVIEW Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a LabVIEWModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the LabVIEWModule.AsModule method to obtain an object. You can use the Module.LoadPrototype method to load the prototype for the module the step specifies. |  |
| LabVIEWNodeProperties |  |
| Use objects from the LabVIEWNodeProperties class to configure and obtain LabVIEWNodeProperties for a module that uses the LabVIEW Adapter. Use the LabVIEWModule.NodeProperties property to obtain the collection of LabVIEWNodeProperties for a module. |  |
| LabVIEWNodeProperty |  |
| Use objects from the LabVIEWNodeProperty class to configure and obtain LabVIEWNodeProperty-specific information for an item in the LabVIEWNodeProperties collection class. |  |
| LabVIEWNXGAdapter |  |
| Use objects from the LabVIEW NXG Adapter class to configure and obtain LabVIEW NXG Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the LabVIEWNXGAdapter.AsAdapter method to obtain an object. |  |
| LabVIEWNXGArgument |  |
| Use objects from the LabVIEWNXGArgument class to set the argument value to pass to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method. |  |
| LabVIEWNXGArguments |  |
| Use objects from the LabVIEWNXGArguments class to pass specific argument values to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method. Use the LabVIEWNXGParameters.NewArguments; method to create a new arguments collection. |  |
| LabVIEWNXGModule |  |
| Use objects from the LabVIEWNXGModule class to specify and obtain LabVIEW NXG Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module; property to obtain a reference to a LabVIEWNXGModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the LabVIEWNXGModule.AsModule; method to obtain an object. You can use the Module.LoadPrototype; method to load the prototype for the module the step specifies. |  |
| LabVIEWNXGNodeProperties |  |
| Use objects from the LabVIEWNXGNodeProperties class to configure and obtain LabVIEWNXGNodeProperties for a module that uses the LabVIEW NXG Adapter. Use the LabVIEWNXGModule.NodeProperties property to obtain the collection of LabVIEWNXGNodeProperties for a module. |  |
| LabVIEWNXGNodeProperty |  |
| Use objects from the LabVIEWNXGNodeProperty class to configure and obtain LabVIEWNXGNodeProperty -specific information for an item in the LabVIEWNXGNodeProperties collection class. |  |
| LabVIEWNXGParameter |  |
| Use objects from the LabVIEWNXGParameter class to configure and obtain LabVIEWNXGParameter -specific information for an item in the LabVIEWNXGParameters collection class. |  |
| LabVIEWNXGParameters |  |
| Use objects from the LabVIEWNXGParameters class to configure and obtain parameters for a module that uses the LabVIEW NXG Adapter. Use the LabVIEWNXGModule.Parameters property to obtain the collection of parameters for a module. |  |
| LabVIEWNXGProject |  |
| Use the objects in the LabVIEWNXGProject class to obtain information about the items present in the LabVIEW NXG project. |  |
| LabVIEWNXGProjectItem |  |
| Use the objects in the LabVIEWNXGProjectItem class to obtain project item details such as path, component name, and so on. |  |
| LabVIEWNXGProjectItems |  |
| Use objects from the LabVIEWNXGProjectItems class to configure and obtain project items for a module that uses the LabVIEW NXG Adapter. |  |
| LabVIEWParameter |  |
| Use objects from the LabVIEWParameter class to configure and obtain LabVIEWParameter-specific information for an item in the LabVIEWParameters collection class. |  |
| LabVIEWParameterElement |  |
| Use objects from the LabVIEWParameterElement class to configure and obtain element-specific information in a cluster or array parameter of a module. Use the LabVIEWParameter.Elements property to obtain the collection of elements for a parameter of a module. |  |
| LabVIEWParameterElements |  |
| Use objects from the LabVIEWParameterElements class to configure and obtain elements for a cluster or array parameter of a module that uses the LabVIEW Adapter. Use the LabVIEWParameter.Elements property to obtain the collection of elements for a parameter of a module and the LabVIEWParameterElement.Elements property to obtain the collection of sub-elements for a parameter element. |  |
| LabVIEWParameters |  |
| Use objects from the LabVIEWParameters class to configure and obtain parameters for a module that uses the LabVIEW Adapter. Use the LabVIEWModule.Parameters property to obtain the collection of parameters for a module. |  |
| PythonAdapter |  |
| Use objects from the PythonAdapter class to configure and obtain Python Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the PythonAdapter.AsAdapter method to obtain an object. |  |
| PythonArgument |  |
| Use objects from the PythonArgument class to set the argument value to pass to a Python module operation (function call, get/set attribute, create class instance) using the PythonModule.Execute method. Use the PythonArguments.Item property to obtain the PythonArgument objects. |  |
| PythonArguments |  |
| Use the object of the PythonArguments class to pass specific argument values to a Python module operation (function call, get/set attribute, create class instance) using the PythonModule.Execute method. Use the PythonModule.Arguments property to obtain the PythonArguments object. Creating a new PythonArguments object using the PythonModule.NewArguments method populates this collection of PythonArgument objects. The number of PythonArgument objects is the same as the number of PythonParameter objects for the PythonModule . |  |
| PythonModule |  |
| Use objects from the PythonModule class to specify and obtain Python Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a PythonModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the PythonModule.AsModule method to obtain an object. |  |
| PythonParameter |  |
| Use objects from the PythonParameter class to configure and obtain parameter-specific information for an item in the PythonParameters collection class. Use the PythonModule.Parameters property to obtain the collection of parameters for a module. |  |
| PythonParameters |  |
| Use objects from the PythonParameters class to configure and obtain parameters for a module that uses the Python Adapter. Use the PythonModule.Parameters property to obtain the collection of parameters for a module. |  |
| SequenceAdapter |  |
| Use objects from the Sequence Adapter class to configure and obtain Sequence Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the SequenceAdapter.AsAdapter method to obtain an object. |  |
| SequenceCallModule |  |
| Use objects from the SequenceCallModule class to specify and obtain Sequence Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a SequenceCallModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire. Typically, you use this class only when you are writing a sequence editor. To access the properties and methods of the Module class, use the AsModule method to obtain an object. You can use the Module.LoadPrototype method to load the prototype for the module that the step specifies. |  |
| SequenceCallParameter |  |
| Use objects from the SequenceCallParameter class to configure and obtain SequenceCallParameter-specific information for an item in the SequenceCallParameters collection class. |  |
| SequenceCallParameters |  |
| Use objects from the SequenceCallParameters class to configure and obtain parameters for a module that uses the Sequence Adapter. Use the SequenceCallModule.Parameters property to obtain the collection of parameters for a module. |  |

Parent topic:

API Classes, Properties, and Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/teststand-api-overview-poster.html language=enus -->
## TOPIC 02884: NI TestStand API Overview

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/teststand-api-overview-poster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/teststand-api-overview-poster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The poster below is available as a PDF at <TestStand>\Doc\Manuals\TestStandAPIReferencePoster.pdf .

### NI TestStand API Overview

The poster below is available as a PDF at
 <TestStand>\Doc\Manuals\TestStandAPIReferencePoster.pdf
 .

[IMAGE alt='image' src='../images/NI_TestStand_API_Overview_1.svg']

[IMAGE alt='image' src='../images/NI_TestStand_API_Overview_2.svg']

[IMAGE alt='image' src='../images/NI_TestStand_API_Overview_3.svg']

[IMAGE alt='image' src='../images/NI_TestStand_API_Overview_4.svg']

[IMAGE alt='image' src='../images/NI_TestStand_API_Overview_5.svg']

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/teststand-api-reference-help.html language=enus -->
## TOPIC 02885: TestStand API

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/teststand-api-reference-help.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/teststand-api-reference-help.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains the following information: Basic information about the TestStand ActiveX Automation server, API concepts, and writing applications with TestStand. Detailed information about the properties, methods, events, constants, and enumerations of the TestStand API. This help file assu

### TestStand API

This help file contains the following information:

- Basic information about the TestStand ActiveX Automation server, API concepts, and writing applications with TestStand.
- Detailed information about the properties, methods, events, constants, and enumerations of the TestStand API.

This help file assumes you have read and are familiar with the concepts presented in the
 [NI TestStand System and Architecture Overview Card](https://www.ni.com/r/gv16fd)
 and the
 [Getting Started with TestStand](/csh?context=ts_8010)
 manual. Refer to the
 [NI TestStand API Reference Poster](teststand-api-overview-poster.html)
 for an illustration of API inheritance.

#### Using TestStand API Objects

In the TestStand API, many objects reference other types of objects. You can obtain an object of one class from an object of another class by calling a method or accessing a property. For example, you can obtain the
 [Engine](engine.html)
 ,
 [Thread](thread.html)
 ,
 [Execution](execution.html)
 , and
 [Report](report.html)
 objects from the
 [SequenceContext](sequencecontext.html)
 object. In another example, a
 [UIMessage](uimessage.html)
 object references an
 Execution
 object, and an
 Execution
 object references a
 [SequenceFile](sequencefile.html)
 object.

#### About This Figure

The following figure includes only existing objects. Color represents items that are duplicated. The figure does not include the following information:

- Explanation of how to create new objects from the
 Engine 
 object
- PropertyObject 
 objects that you can obtain from any object in the figure except an
 Engine 
 object
- Illustration of when you can acquire a reference to a derived class by querying for the derived interface
- References from module type objects to
 Step 
 objects

Click the classes in the following figure for more information about the class and a listing of the properties and methods associated with the class.

[IMAGE alt='image' src='../images/Using_Api_Obj.gif']

#### Additional Information

Note

<TestStand>

TSHelp.chm

To navigate this help file, use the
 Contents
 ,
 Index
 , and
 Search
 tabs to the left of this window.

Copyright © National Instruments Corporation. All rights reserved.

#### See Also

[Engine](engine.html)

[Execution](execution.html)

[PropertyObject](propertyobject.html)

[Report](report.html)

[SequenceContext](sequencecontext.html)

[SequenceFile](sequencefile.html)

[Step](step.html)

[Thread](thread.html)

[TypeUsageList](typeusagelist.html)

[UIMessage](uimessage.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/teststand-api-reference.html language=enus -->
## TOPIC 02886: TestStand API Reference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/teststand-api-reference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/teststand-api-reference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object and Description Adapter Use Adapter objects to configure and obtain information about the module adapters . Typically, you use this class only when you write a user interface application or sequence editor. If you are considering writing a user interface application, National Instruments reco

### TestStand API Reference

| Object and Description |  |
| --- | --- |
| Adapter |  |
| Use Adapter objects to configure and obtain information about the module adapters . Typically, you use this class only when you write a user interface application or sequence editor. Note If you are considering writing a user interface application, National Instruments recommends using the TestStand User Interface (UI) Controls instead of writing the application using the TestStand Engine API. To obtain an Adapter object, call the Engine.GetAdapter method. Pass a zero-based index to specify the Adapter object for which you want to obtain a reference. To find out the number of available adapters, obtain the value of the Engine.NumAdapters property. |  |
| AdditionalResult |  |
| An AdditionalResult specifies additional data to add to the result list when a step executes. An AdditionalResult can be an arbitrary piece of data or the value of a module parameter. An AdditionalResult is a member of the Step.AdditionalResults.ParameterResults collection, the Step.AdditionalResults.CustomResults collection, or the AdditionalResult.Elements collection. |  |
| AdditionalResults |  |
| This class represents a collection of AdditionalResult objects. Use the Step.AdditionalResults.ParameterResults , Step.AdditionalResults.CustomResults , or AdditionalResult.Elements properties to obtain an AdditionalResults collection. |  |
| ArrayDimensions |  |
| Use the ArrayDimensions class to obtain and set array bounds information for a PropertyObject . Use the PropertyObjectType.ArrayDimensions property to obtain an instance of this class. |  |
| CodeTemplate |  |
| Use this interface to obtain information about a code template. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the StepType.CodeTemplates property to obtain a collection of CodeTemplate objects associated with a step type. |  |
| CodeTemplates |  |
| A collection of CodeTemplate objects. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the StepType.CodeTemplates property to obtain a collection of CodeTemplate objects associated with a step type. |  |
| CsvFileInputRecordStream |  |
| CsvFileOutputRecordStream |  |
| EditArgs |  |
| Use objects of the EditArgs class to pass information about the current state of the user interface to methods such as Engine.NewExecution , Sequence.EvalEntryPointNameExpressionEx , Engine.GetEditTimeToolMenuItems , and Engine.GetRunTimeToolMenuItems . Objects of this class contain information about currently selected sequences, steps, sequence files, and executions. This selection information appears in the RunState.InitialSelection property of the sequence context. Create objects of this class using the Engine.NewEditArgs method. Typically, you use this class only when you are writing a user interface or sequence editor. |  |
| EditTimeMenuItem |  |
| Objects of the EditTimeMenuItem class represent menu items in the sequence editor or user interface. A menu item is a command, a call to a sequence, a submenu, or a submenu of calls to sequences in a sequence file. EditTimeMenuItem objects specify the menu item type, which includes paths and arguments for commands, paths for sequence files, and names of sequences. Each object specifies an expression for evaluating item text at run time, and expressions that determine whether the item is enabled or visible at run time. Use the Engine.GetEditTimeToolMenuItems method to obtain a reference to a collection of EditTimeMenuItem objects for the TestStand Tools menu. Use this collection to customize the contents of the Tools menu. Use the Engine.GetRunTimeToolMenuItems method to obtain a reference to a collection of RunTimeMenuItem objects, which represent an evaluated version of the Tools menu. Use this collection to determine what is displayed in the Tools menu at run time. |  |
| EditTimeMenuItems |  |
| The EditTimeMenuItems class specifies a collection of EditTimeMenuItem objects. An EditTimeMenuItem object represents a menu item such as a command, a call to a sequence, a submenu, or a submenu of calls to sequence in a sequence file. Each object in the collection specifies the menu item type and the expressions which determine the item text, hidden state, and enabled state. A submenu item specifies a collection of menu items in the submenu. Use the Engine.GetEditTimeToolMenuItems method to obtain a reference to a collection of this class for the Tools menu. Use this collection to customize the contents of the Tools menu. |  |
| Engine |  |
| Use the Engine class to create and access objects of other classes, control executions, launch built-in dialog boxes, implement a Tools menu, find files and directories, and invoke various utilities. Create the Engine object directly using ActiveX. To access the Engine object from a step, use the TestStand API to obtain the value of the Engine property from the SequenceContext class or pass the SequenceContext property RunState.Engine as an object parameter to the step. The following examples show how to create the initial Engine object: LabWindows/CVI CAObjHandle engineObj = 0; TS_NewEngine(NULL, &engineObj); Visual Basic 'Place the TestStand Engine ActiveX control on the main form. Visual C/C++ #import "C:\\TestStand\\Bin\\teapi.dll" TS::IEnginePtr engine; HRESULT hr = engine.CreateInstance(__uuidof(TS::Engine)) ; |  |
| EngineEnvironment |  |
| EngineInitializationSettings |  |
| Use the EngineInitializationSettings class to configure options that must be set prior to Engine construction. |  |
| EvaluationTypes |  |
| This interface specifies expected types for evaluating an expression. Obtain an EvaluationTypes object by calling the Engine.NewEvaluationTypes method or through a property of a parameter for a module call such as the LabVIEWParameter.ValidEvaluationTypes property. Pass an instance of EvaluationTypes to the Expression.ValidateEvaluationType method to perform type checking on an expression. |  |
| Execution |  |
| An execution is an object TestStand creates to contain all the information it uses to run the sequences and subsequences it calls. Use objects of this class to control and get information about executions. For example, you can use methods to suspend, resume, or terminate execution, and you can use properties to determine whether the execution is an interactive execution or whether the execution is in the process of terminating. |  |
| ExecutionOutputRecordStream |  |
| ExecutionOutputRecordStreams |  |
| Expression |  |
| An Expression object holds an expression string. You can check the validity of the expression string or you can evaluate the expression string to obtain the result of the expression. The Expression object provides the same functionality as the PropertyObject.EvaluateEx , Engine.CheckExpression , and Engine.CheckExprSyntax methods. However, if you are repeatedly evaluating the same expression, it is more efficient to use an Expression object because it only parses the expression string when you first evaluate the expression. Because the Expression object retains the parsed form of the expression, it does not re-parse the expression when you reevaluate the same string. The Expression object also provides the NumTokens property and the Tokenize and GetToken methods, which you can use to identify the operators, identifiers, and constants that comprise an expression. The capability to parse the expression into component tokens is useful for specialized purposes, such as implementing expression syntax coloring. Because TestStand provides an ActiveX Expression control that features syntax coloring, you typically do not need to identify the tokens in an expression. |  |
| ExternalReportViewer |  |
| An ExternalReportViewer represents relationships between a specific report format and the application used to open it. TestStand keeps a list of report viewers. If you do not specify an external viewer for a format, the file opens in the application Microsoft Windows associates with the file extension of the report file. |  |
| ExternalReportViewers |  |
| Collection that contains elements using the ExternalReportViewer type. Represents the list of external report viewers used to open the different report file types TestStand supports. |  |
| FileInformation |  |
| Use FileInformation objects to obtain file information, such as file version, file format version, and file type, on files TestStand recognizes without fully loading the files into memory. When you call methods and properties on a FileInformation object, TestStand can cache the information. For changes made to a file on disk to be reflected in a FileInformation object, you must release the object and use the Engine.GetFileInformation method to obtain a new FileInformation object. |  |
| Images |  |
| This collection class contains objects of the Picture data type. Use the Engine.Images property to acquire the collection object. The collection specifies the images TestStand loads from the <TestStand> \\Components\\Icons and <TestStand Public>\\Components\\Icons directories and images you add using the Engine.AddImage method. Use the Images.FindImage method to find an image using an image name. Use the Images collection as an alternative to using the Engine.LargeImageListEx and Engine.SmallImageListEx properties. |  |
| InputRecordStream |  |
| InputStream |  |
| Objects of the InputStream class represent an abstract stream of data. In a sequence file translator, this stream reads the content of a user file. The InputStream class allows the translators to read, seek, and query the size of a file. You cannot create an InputStream object externally, and you can obtain a reference only in the DLL interface exposed to a sequence file translator. The TestStand Engine creates an InputStream object and passes the object to various callbacks in the DLL interface. |  |
| InteractiveArgs |  |
| When you call the Engine.NewExecution or Thread.DoInteractiveExecution methods to create an interactive execution, use an object of this class to pass information about the current state of the user interface. These methods use the object to determine which steps are currently selected in the user interface. Create objects for this class using the Engine.NewInteractiveArgs method. |  |
| InteractiveContext |  |
| Use objects of this class to obtain additional information about a currently executing interactive execution. Obtain objects of this class using the SequenceContext.InteractiveContext property of the sequence context in which the interactive execution began. |  |
| Location |  |
| The properties of a Location object contain enough information for a user interface to find a specific piece of data the user interface displays. |  |
| Locations |  |
| Locations is a collection of Location objects. Use Locations to instruct the user interface to update the selection. Follow these steps to set the selection in a user interface: Call the Engine.NewLocations method to create a Locations object. Call the Locations.AddFileLocation , Locations.AddExecutionLocation , or Locations.AddTypeLocation method on a Locations object to specify data for the user interface to select. Call the Locations.GotoLocation method on the Locations object to send the Locations object to the user interface. The user interface receives the Locations object through the UIMessage.ActiveXData property of a UIMsg_GotoLocation UIMessage. If the user interface supports the Goto location action, it updates the selection to correspond to the Locations object. |  |
| Module |  |
| Use objects from the module class to specify and obtain information about code modules that steps or step type substeps execute. Typically, you use this class only when you write a sequence editor. To obtain a Module object, use the Step.Module property. To access the properties and methods of an adapter-specific module class, query the Module object for the interface of the adapter-specific module interface you want. |  |
| OutputMessage |  |
| An OutputMessage object specifies the details about an output message. The object lets you specify the message text, timestamp, category, severity, color, icon, and location. When you call the OutputMessage.Post method, TestStand copies the OutputMessage object and adds the copy to the collection TestStand maintains. You can access the collection using the reference the Engine.GetOutputMessages method returns. |  |
| OutputMessages |  |
| This collection class contains elements of the OutputMessage type. You can post an output message to TestStand by calling the Engine.NewOutputMessage method to create a new message object and by calling the OutputMessage.Post method on the object. You can also call the OutputMessage expression function . When the number of items in the collection changes from zero to one, TestStand sends a UIMsg_OutputMessages message to the TestStand application. TestStand adds only messages to the collection and sends a UIMsg_OutputMessages message if you enable the Engine.OutputMessagesEnabled property. An application can retrieve the latest output messages by transferring messages from the collection TestStand maintains to a new collection the application creates, as shown in the following pseudocode: // C# example if (uiMsg.Event == UIMessageCodes.UIMsg_OutputMessages) { OutputMessages outputMessages = uiMsg.ActiveXData as OutputMessages; OutputMessages appOutputMessages = engine.NewOutputMessages(); outputMessages.CopyMessagesToCollection(appOutputMessages); for(i = 0; i < appOutputMessages.Count; i++) { uiControl.Add(appOutputMessages[i].Message); } } // C++ example if (uiMsg->Event == UIMsg_OutputMessages) { TS::OutputMessagesPtr outputMessages = uiMsg->ActiveXData; TS::OutputMessagesPtr appOutputMessages = engine->NewOutputMessages(); outputMessages->CopyMessagesToCollection(appOutputMessages); for(i = 0; i < appOutputMessages->Count; i++) { uiControl.Add(appOutputMessages->Item[i]->Message); } } TestStand always sends output messages to a debugger if you enable the DebugOptions_SendOutputMessagesToDebugger option of the StationOptions.DebugOptions property. |  |
| OutputRecordStream |  |
| PropertyObject |  |
| Use the PropertyObject class to manipulate and access the values of variables and custom step properties. You can also use the PropertyObject to add, copy, or delete subproperties of variables and custom step properties. You can create new objects of this class using the Engine.NewPropertyObject method. You can obtain existing objects of this class as return values from numerous functions. You can obtain the underlying PropertyObject for objects of every class except the Engine class by using the AsPropertyObject method of the respective class. |  |
| PropertyObjectFile |  |
| Use the PropertyObjectFile class to read and write PropertyObjects to disk. All TestStand files, including sequence files, type palette files, workspace files, configuration files, users file, and globals file, are stored as PropertyObjectFiles. Create new PropertyObjectFiles with the Engine.NewPropertyObjectFile method. |  |
| PropertyObjectType |  |
| Use the PropertyObjectType class to obtain type information for a PropertyObject . Use the PropertyObject.Type property or the Engine.NewPropertyObjectType method to obtain an instance of this class. |  |
| Report |  |
| Use objects of the Report class to modify, save, load, retrieve, and view reports. To obtain the Report object for an execution, retrieve the value of the Execution.Report property. Usually, the process model updates the Report object associated with the execution, and the sequence editor or user interface displays it. |  |
| Reports |  |
| This class is a collection of Report objects. |  |
| ReportSection |  |
| Use objects of this class to store, update, and transfer reports. You typically use ReportSection objects to avoid creating copies of a report as the report is transferred between the report generator, process models, Report object, and ReportView control. You can create a new ReportSection object by calling the Report.NewReportSection method. ReportSection objects can contain other ReportSection objects. Typically, a process model creates and updates the ReportSection object and assigns it to the Report object by setting the Report.ReportSection property. |  |
| ReportSections |  |
| This class is a collection of ReportSection objects. The collection contains a list of ReportSection objects that are children of the ReportSection object from which the ReportSections object was obtained. |  |
| ResultLog |  |
| ResultLog objects read TestStand results from a file that a ResultLogger object creates. |  |
| ResultLogger |  |
| ResultLogger objects write TestStand results to a file. Use a ResultLog object to read the results from the file. |  |
| RunTimeMenuItem |  |
| Objects of the RunTimeMenuItem class represent an evaluated version of a EditTimeMenuItem object. The properties of the RunTimeMenuItem object specify the item text, if the menu item is disabled, and if a separator appears before it. You can use the RunTimeMenuItem.InvokeItem method to execute the item, which launches a sequence in a new execution or an executable. Use the Engine.GetRunTimeToolMenuItems method to obtain a reference to a collection of this class for the Tools menu. Use this collection to determine what to display in the Tools menu at run time. |  |
| RunTimeMenuItems |  |
| The RunTimeMenuItems class specifies a collection of RunTimeMenuItem objects, which represent an evaluated version of a EditTimeMenuItem object. The properties of the RunTimeMenuItem object specify the item text and if the menu item is disabled. You can use the RunTimeMenuItem.InvokeItem method to execute the item, which launches an executable or a sequence in a new execution. Use this collection to determine what to display in the Tools menu at run time. Use the Engine.GetRunTimeToolMenuItems method to obtain a reference to a collection of this class for the Tools menu. |  |
| SearchDirectories |  |
| This collection class contains elements using the SearchDirectory type. The collection specifies the directories TestStand searches for finding files. The directories listed first in the collection take precedence over those listed later in the collection. When you run TestStand for the first time, the collection contains a default set of search directory paths . |  |
| SearchDirectory |  |
| A SearchDirectory object specifies a directory in which TestStand searches for finding files. An object of this class specifies a path to an explicit directory or specifies a predefined directory, such as the TestStand directory or the Microsoft Windows directory. An object specifies any file extension restrictions and whether to search subdirectories. |  |
| SearchMatch |  |
| The SearchResults object return objects of the SearchMatch class. SearchResults objects contain details about a match found as a result of a call to the PropertyObject.Search or Engine.SearchFiles methods. |  |
| SearchResults |  |
| Objects in the SearchResult class are both a handle to a search in progress and a container for the results of that search. When you call the PropertyObject.Search or Engine.SearchFiles method, TestStand returns a SearchResults object. The search runs asynchronously, which means you obtain the SearchResults object before the search finishes. To wait for the search to complete, call the SearchResults.IsComplete method. Alternatively, you can access the results as they accumulate asynchronously by using the SearchResults.NumMatches property to obtain the number of matches and then accessing only the SearchMatch objects up to that number. TestStand always appends new SearchMatch objects to the end of the result list. |  |
| SelectedBreakpointItem |  |
| A SelectedBreakpointItem object specifies a breakpoint in a sequence file. Use this object for the selectedItemParam parameter of the Engine.DisplayEditBreakAndWatchDialog method, which returns the last selected item on the Breakpoints tab of the Edit Breakpoints/Watch Expressions dialog box when the user clicks the Goto button. The selected item can be a sequence file, sequence, or step. |  |
| Sequence |  |
| Objects of the Sequence class represent a sequence that can contain steps. Use the Sequence class to examine or modify sequence settings and the list of steps in the sequence. Sequences have three groups of steps. The StepGroups enumeration contains a value for each of the step groups. SequenceTypes constants define several types of sequences. You can obtain a reference to the Sequence objects a sequence file contains by calling the SequenceFile.GetSequence method. You can create new sequences by calling the Engine.NewSequence or SequenceFile.CreateCallbackOverrideSequence methods. Note Built-in properties of sequences are flagged to be shared at run time. Any changes to built-in properties within the run-time copy of the sequence also edit the original Sequence object in the sequence file. |  |
| SequenceContext |  |
| A SequenceContext object contains complete information about an execution at a particular point during the execution. You can use the sequence context to access all the objects, variables, and properties in the execution. From the sequence context, you also can obtain references to all the steps in the current sequence, the sequence contexts for the calling sequences, the Process Model entry point sequence, and the MainSequence in the client sequence file. You can pass the current sequence context or subproperties to code modules you call from steps. |  |
| SequenceFile |  |
| Objects of the SequenceFile class represent a sequence file that can contain sequences. You can obtain a reference to a SequenceFile object by using the Engine.GetSequenceFileEx or Engine.NewSequenceFile methods. Use the reference to examine or modify sequence file settings and to examine or modify the list of sequences in the sequence file. |  |
| StationOptions |  |
| Use the StationOptions class to set preferences for TestStand. The settings affect all sequence editor and user interface sessions. Use the Engine.DisplayOptionsDialog method to launch the Station Options dialog box. |  |
| Step |  |
| Objects of the Step class represent steps in TestStand sequences. A step can perform many tasks, such as initializing an instrument, performing a complex test, or making a decision that affects the flow of execution in a sequence. You can obtain a reference to a step in a sequence by calling the Sequence.GetStep method. Create new steps with the Engine.NewStep method. Note Built-in properties of steps are flagged to be shared at run-time. Any changes to built-in properties within the run-time copy of the step edits the original step object in the sequence file. |  |
| StepAdditionalResults |  |
| Use the Step.AdditionalResults property to obtain an instance of this class, which contains collections for the parameter additional results and custom additional results of a step. |  |
| StepType |  |
| Objects of the StepType class represent step types in TestStand files. Every step is an instance of a step type. You create new step types with the Engine.NewStepType method. |  |
| Thread |  |
| Threads are elements of an Execution. Each thread maintains a call stack that contains a SequenceContext object for each active sequence invocation. You can obtain a thread of an execution by calling the Execution.GetThread method. |  |
| TypeUsageList |  |
| The TypeUsageList contains a list of types a PropertyObjectFile object uses. Use this class to insert or delete types from a file. Note When you edit a PropertyObjectFile object by inserting named data types or step types in to the file, add any new types to the TypeUsageList object for the file so the types immediately appear in the Types view in the sequence editor for the file. Use the TypeUsageList.AddUsedTypes or TypeUsageList.Union method to add new types. |  |
| UIMessage |  |
| TestStand uses UIMessage objects to pass information about the state of the engine and the current executions to the user interface or sequence editor. You can obtain UIMessage objects in a user interface program by providing a callback to the engine. The engine calls the callback when it has a UIMessage object to pass. If you do not provide a callback, you can set the Engine.UIMessagePollingEnabled property to True and call the Engine.GetUIMessage method to poll for UIMessage objects. |  |
| UIStyle |  |
| Use the UIStyle class to configure style settings for dialogs and controls TestStand displays. |  |
| UndoItem |  |
| A user interface receives objects that implement the UndoItem interface through the UIMessage.ActiveXData property of a UIMsg_PushUndoItem UI Message. A user interface uses the UndoItem.EditedFile property to find an appropriate UndoStack to push the undo item onto. You can also use the UndoItem interface to make an edit to a TestStand file undoable if the UndoItemCreator does not provide enough functionality to undo an edit. To do this, create a COM object that implements the UndoItem interface and send an instance of the object to the sequence editor using a UIMsg_PushUndoItem UI Message. Note LabVIEW and LabWindows/CVI do not support implementing custom objects for this interface. |  |
| UndoItem2 |  |
| The UndoItem2 class inherits from the UndoItem class and supports all the UndoItem properties and methods. An object that supports UndoItem might not necessarily support UndoItem2 . You can also use the UndoItem2 interface to make an edit to a TestStand file undoable if the UndoItemCreator does not provide enough functionality to undo an edit. To do this, create a COM object that implements the UndoItem2 interface and send an instance of the object to the sequence editor using a UIMsg_PushUndoItem UI Message. Note LabVIEW and LabWindows/CVI do not support implementing custom objects for this interface. |  |
| UndoItemCreator |  |
| Use UndoItemCreator to make edits to TestStand files undoable. To use UndoItemCreator, first create an UndoItemCreator object using the Engine.NewUndoItemCreator method. Then call the BeginEdit method, make an edit to a TestStand object, and call the EndEdit method. You can call BeginEdit and EndEdit more than once to edit more than one TestStand object. Then call the CreateAndPostUndoItem method to create an undo item for all the edits you made. |  |
| UndoItems |  |
| You can obtain a collection of UndoItem objects from the UndoStack.UndoItems property. |  |
| UndoStack |  |
| An UndoStack manages a stack of undo items and a stack of redo items. Normally, you create an UndoStack for every document in a sequence editor in which you can undo edits to a TestStand file. You receive undo items to push onto an undo stack through the UIMessage.ActiveXData property of a UIMsg_PushUndoItem UI Message. You use the UndoItem.EditedFile property of the undo item to determine onto which document undo stack to push the undo item. Use the Engine.NewUndoStack method to create an UndoStack object. You typically use UndoStack objects with the ApplicationMgr.UndoStack and SequenceFileViewMgr.UndoStack properties. |  |
| UnmappedArgumentValue |  |
| Use objects from the UnmappedArgumentValue class to obtain specific information for an item in the UnmappedArgumentValues collection class. |  |
| UnmappedArgumentValues |  |
| Use objects from the UnmappedArgumentValues class to obtain a list of the current arguments not used as inputs and outputs of the corresponding module. Use the Module.UnmappedArgumentValues and DotNetCall.UnmappedArgumentValues properties to obtain the collection of unmapped argument values for a module. When a module prototype changes, TestStand attempts to map the current module arguments to the new prototype by looking for matching argument names and data types, and by matching argument positions and data types. If TestStand fails to assign an argument to the new prototype, the argument is added to this collection. TestStand does not clear the collection when you load a new prototype. Use the UnmappedArgumentValues.Clear method to clear the collection before calling the Module.LoadPrototype or DotNetCall.LoadPrototypeFromSignature method. |  |
| User |  |
| Objects of the User class represent the data and privileges TestStand associates with a TestStand user or user group. Call the Engine.GetUser or Engine.NewUser method to obtain a User object for a particular user or user group. Obtain the object for the currently logged-in user from the Engine.CurrentUser property. You can obtain an array of users or user groups using the UsersFile.UserList and UsersFile.UserGroupList properties. Use the PropertyObject class methods to add or remove objects from the array to change the TestStand user or user group list. You can use the PropertyObject class to access the subproperties of an object from the User class. Refer to User Data Type Subproperties for the default subproperties TestStand defines. |  |
| UsersFile |  |
| The UsersFile class represents the file that contains a list of TestStand users and user profiles. Use this class to add or delete users and user profiles. You can obtain a reference to the users file TestStand loads at startup with the Engine.UsersFile property. To perform read or write operations for objects from the UsersFile class, obtain a reference to the PropertyObjectFile interface by using the AsPropertyObjectFile methods, then use the PropertyObjectFile.ReadFile and PropertyObjectFile.WriteFile methods. |  |
| Utility |  |
| Use this class to perform utility functions. Use the Engine.Utility property to obtain an instance of this class. |  |
| WatchExpression |  |
| Use objects of the WatchExpression class to monitor the values of properties and variables using expressions. Typically, you use WatchExpression objects to display run-time values in a Watch View pane in a user interface. A WatchExpression object defines an expression TestStand evaluates during sequence execution. You can configure a conditional breakpoint on a watch expression. The breakpoint suspends execution when a value of the watch expression changes, or whenever the coerced value of the watch expression evaluates to True . The TestStand Engine maintains a list of watch expressions and evaluates conditional breakpoints during execution. You can also specify the scope of the watch expression, which specifies whether the expression applies to all executions of the client sequence file or only the current execution, and whether to evaluate the watch expression only when executing within a specific sequence file or sequence. Use the collection object the Engine.GetWatchExpressions method returns to manage a watch expression list. You can create new watch expressions by using the WatchExpressions.Insert method, which adds a new watch expression to the collection and returns the new object. To add a watch expression to the list the engine maintains and monitors, pass True for the insertInEngine parameter. |  |
| WatchExpressions |  |
| Objects of the WatchExpressions class are collections of objects of the WatchExpression class. |  |
| WorkspaceFile |  |
| Objects of the WorkspaceFile class represent workspace files that can contain projects. A workspace file contains a list of project files and source code control provider information. Each project file contains lists of sequence files, code modules, and other files required by a particular test system. To perform read or write operations for objects from the WorkspaceFile class, obtain a reference to the PropertyObjectFile interface by using the WorkspaceFile.AsPropertyObjectFile method, then use the PropertyObjectFile.ReadFile and PropertyObjectFile.WriteFile methods, respectively. |  |
| WorkspaceObject |  |
| Objects of the WorkspaceObject class represent nodes for workspace and project files on the Workspace pane. Workspace objects handle all source code control operations on files. |  |

Parent topic:

API Classes, Properties, and Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/teststandpaths.html language=enus -->
## TOPIC 02887: TestStandPaths

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/teststandpaths.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/teststandpaths.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the values of this enumeration to determine specific TestStand directory paths. TestStandPath_Bin –(Value: 2) Directory where TestStand stores executables and DLLs, typically <TestStand> \Bin . TestStandPath_CommonAppData –(Value: 5) Directory where TestStand stores common application data, such

### TestStandPaths

Use the values of this enumeration to determine specific TestStand directory paths.

- TestStandPath_Bin 
 –(Value: 2) Directory where TestStand stores executables and DLLs, typically
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Bin 
 .
- TestStandPath_CommonAppData 
 –(Value: 5) Directory where TestStand stores common application data, such as configuration information, typically
 C:\ProgramData\National Instruments\TestStand 
 on Windows 8.1/8/7.
- TestStandPath_Config 
 –(Value: 3) Directory where TestStand stores configuration files, typically
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 .
- TestStandPath_GlobalCommonAppData 
 –(Value: 13) Directory where TestStand stores common application data for the global environment (
 <TestStand Application Data> 
 ), such as configuration information, typically C:\ProgramData\National Instruments\TestStand.
- TestStandPath_GlobalConfig 
 –(Value: 11) Directory where TestStand stores configuration files for the global environment, typically
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 .
- TestStandPath_GlobalLocalAppData 
 –(Value: 14) Directory where TestStand stores user-specific application data for the global environment, typically <User Directory>\AppData\Local\National Instruments\TestStand on Windows 10/8.1/7.
- TestStandPath_GlobalPublic 
 –(Value: 12) Directory where TestStand stores publicly editable files for the global environment, typically C:\Users\Public\Documents\National Instruments\TestStand on Windows 10/8.1/7.
- TestStandPath_LocalAppData 
 –(Value: 6) Directory where TestStand stores per-user application data, typically
 <User Directory>\AppData\Local\National Instruments\TestStand 
 on Windows 8.1/8/7.
- TestStandPath_NIComponents 
 –(Value: 8) Directory where TestStand stores components, such as callbacks, icons, language files, step types, and type palettes, typically
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components 
 .
- TestStandPath_Public 
 –(Value: 4) Directory where TestStand stores publicly editable files, typically
 C:\Users\Public\Documents\National Instruments\TestStand 
 on Windows 8.1/8/7.
- TestStandPath_PublicComponents 
 –(Value: 7) Directory where TestStand looks for user-defined components to override National Instruments components, such as callbacks, icons, language files, step types, and type palettes, typically,
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components 
 .
- TestStandPath_Temp 
 –(Value: 9) This value is obsolete. Returns the directory path with a trailing backslash where TestStand stores temporary files. TestStand does not clean up files that you create in this directory but does erase files you create with the
 Engine.CreateTempFile 
 method.
- TestStandPath_Temporary 
 –(Value: 10) Directory where TestStand stores temporary files. TestStand does not clean up files that you create in this directory but does erase files you create with the
 Engine.CreateTempFile 
 method.
- TestStandPath_TestStand 
 –(Value: 1) Directory where TestStand installs the majority of components, typically
 <Program Files>\National Instruments\TestStand <Version> 
 .

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-addtobatch.html language=enus -->
## TOPIC 02888: Thread.AddToBatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-addtobatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-addtobatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.AddToBatch( batchObj, orderNumber) Purpose Adds this thread to a Batch object. Remarks The Batch Synchronization step type uses this method. Parameters batchObj As IUnknown [In] Specifies the batch object to which TestStand adds the thread. orderNumber As Long [In] Specifies the order

### Thread.AddToBatch

#### Syntax

[Thread](thread.html).AddToBatch( batchObj, orderNumber)

#### Purpose

Adds this thread to a Batch object.

#### Remarks

The Batch Synchronization step type uses this method.

#### Parameters

batchObj
 As
 [IUnknown](data-types-for-teststand.html)

[In] Specifies the batch object to which TestStand adds the thread.

orderNumber
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the order number corresponding to the thread within the batch.

#### See Also

[Thread.Batch](thread-batch.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-aspropertyobject.html language=enus -->
## TOPIC 02889: Thread.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the Thread object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### Thread.AsPropertyObject

#### Syntax

[Thread](thread.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the Thread object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-batch.html language=enus -->
## TOPIC 02890: Thread.Batch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-batch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-batch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.Batch Data Type IUnknown Purpose Returns the Batch object to which this thread belongs. Remarks Returns a NULL reference if this thread was not added to a batch. The Batch Synchronization step type uses this method. See Also Thread.AddToBatch Thread.SetBatchRTEOption

### Thread.Batch

#### Syntax

[Thread](thread.html).Batch

#### Data Type

[IUnknown](data-types-for-teststand.html)

#### Purpose

Returns the Batch object to which this thread belongs.

#### Remarks

Returns a
 NULL
 reference if this thread was not added to a batch. The Batch Synchronization step type uses this method.

#### See Also

[Thread.AddToBatch](thread-addtobatch.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-callstacksize.html language=enus -->
## TOPIC 02891: Thread.CallStackSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-callstacksize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-callstacksize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.CallStackSize Data Type Long Purpose Returns the number of call stack entries that currently exist for the thread. Remarks You can obtain a sequence context for each call stack entry by passing a call stack index to the Thread.GetSequenceContext method. See Also SequenceContext.CallSta

### Thread.CallStackSize

#### Syntax

[Thread](thread.html).CallStackSize

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of call stack entries that currently exist for the thread.

#### Remarks

You can obtain a sequence context for each call stack entry by passing a call stack index to the
 [Thread.GetSequenceContext](thread-getsequencecontext.html)
 method.

#### See Also

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[Thread.GetSequenceContext](thread-getsequencecontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-clearcurrentrte.html language=enus -->
## TOPIC 02892: Thread.ClearCurrentRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-clearcurrentrte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-clearcurrentrte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.ClearCurrentRTE Purpose Clears the Result.Error.Occurred property of the current step. Remarks Use this method to cause the execution thread to ignore a run-time error.

### Thread.ClearCurrentRTE

#### Syntax

[Thread](thread.html).ClearCurrentRTE

#### Purpose

Clears the
 Result.Error.Occurred
 property of the current step.

#### Remarks

Use this method to cause the execution thread to ignore a run-time error.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-cleartemporarybreakpoint.html language=enus -->
## TOPIC 02893: Thread.ClearTemporaryBreakpoint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-cleartemporarybreakpoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-cleartemporarybreakpoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.ClearTemporaryBreakpoint Purpose Clears the temporary breakpoint you set by calling the Thread.SetStepInto , Thread.SetStepOut , or Thread.SetStepOver methods. Remarks Call the Execution.ClearTemporaryBreakpoints method to clear temporary breakpoints of all threads in an execution. See

### Thread.ClearTemporaryBreakpoint

#### Syntax

[Thread](thread.html).ClearTemporaryBreakpoint

#### Purpose

Clears the temporary breakpoint you set by calling the
 [Thread.SetStepInto](thread-setstepinto.html)
 ,
 [Thread.SetStepOut](thread-setstepout.html)
 , or
 [Thread.SetStepOver](thread-setstepover.html)
 methods.

#### Remarks

Call the
 [Execution.ClearTemporaryBreakpoints](execution-cleartemporarybreakpoints.html)
 method to clear temporary breakpoints of all threads in an execution.

#### See Also

[Execution.ClearTemporaryBreakpoints](execution-cleartemporarybreakpoints.html)

[Thread.SetStepInto](thread-setstepinto.html)

[Thread.SetStepOut](thread-setstepout.html)

[Thread.SetStepOver](thread-setstepover.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-displayname.html language=enus -->
## TOPIC 02894: Thread.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.DisplayName Data Type String Purpose Returns the name to display for the thread.

### Thread.DisplayName

#### Syntax

[Thread](thread.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name to display for the thread.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-dointeractiveexecution.html language=enus -->
## TOPIC 02895: Thread.DoInteractiveExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-dointeractiveexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-dointeractiveexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.DoInteractiveExecution( InteractiveArgsParam) Purpose Executes specific steps interactively. Remarks You can call this method only if the thread is currently suspended at a breakpoint. You can only run steps in the sequence and step group in which the execution is suspended. Parameters

### Thread.DoInteractiveExecution

#### Syntax

[Thread](thread.html).DoInteractiveExecution( InteractiveArgsParam)

#### Purpose

Executes specific steps interactively.

#### Remarks

You can call this method only if the thread is currently suspended at a breakpoint. You can only run steps in the sequence and step group in which the execution is suspended.

#### Parameters

InteractiveArgsParam
 As
 [InteractiveArgs](interactiveargs.html)

[In] Specifies an
 [InteractiveArgs](interactiveargs.html)
 object that indicates which steps are currently selected steps in the user interface and that contains the looping information necessary for an interactive execution. The selected steps you specify must be in the currently executing step group.

#### See Also

[InteractiveArgs](interactiveargs.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-execution.html language=enus -->
## TOPIC 02896: Thread.Execution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-execution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.Execution Data Type Execution Purpose Returns a reference to the Execution object to which the thread belongs. Remarks Release the Execution reference when you have finished using it. See Also Execution SequenceContext.Execution

### Thread.Execution

#### Syntax

[Thread](thread.html).Execution

#### Data Type

[Execution](execution.html)

#### Purpose

Returns a reference to the Execution object to which the thread belongs.

#### Remarks

Release the Execution reference when you have finished using it.

#### See Also

[Execution](execution.html)

[SequenceContext.Execution](sequencecontext-execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-externallysuspended.html language=enus -->
## TOPIC 02897: Thread.ExternallySuspended

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-externallysuspended.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-externallysuspended.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.ExternallySuspended Data Type Boolean Purpose Because the Allow Break While in Code Modules option on the Execution tab of the Station Options dialog box is enabled by default in TestStand 2014 or later, you do not need to use this property unless you disable the option. Specifies to t

### Thread.ExternallySuspended

#### Syntax

[Thread](thread.html).ExternallySuspended

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Allow Break While in Code Modules

Execution

Station Options

Specifies to treat this thread as suspended when you stop the execution for a breakpoint.

#### Remarks

By default, when a step blocks or takes a long time to complete and the user attempts to suspend (break) execution, execution cannot suspend until the step unblocks and returns. For example, if the user breaks execution when a step launches a dialog box, execution does not suspend until after the user closes the dialog box.

A step uses this property to enable execution to break while it performs a lengthy operation or waits an indeterminate period of time. When a step sets this property, it specifies that TestStand considers the thread to be suspended if the user requests that the execution break. For example, you can add the following code to the step code module:

Boolean previousExternallySuspended = mySequenceContext.GetThread().ExternallySuspended

' set externally suspended to true
 mySequenceContext.GetThread().ExternallySuspended = true

' Insert code to launch a dialog box or perform another operation that might block indefinitely

' restore the previous setting of externally suspended
 mySequenceContext.GetThread().ExternallySuspended = previousExternallySuspended

Note

False

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-flushpostresults.html language=enus -->
## TOPIC 02898: Thread.FlushPostResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-flushpostresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-flushpostresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.FlushPostResults Purpose Instructs the thread to immediately call its PostResults callbacks with accumulated results. This method does nothing if the thread has no accumulated results.

### Thread.FlushPostResults

#### Syntax

[Thread](thread.html).FlushPostResults

#### Purpose

Instructs the thread to immediately call its PostResults callbacks with accumulated results. This method does nothing if the thread has no accumulated results.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-getsequencecontext.html language=enus -->
## TOPIC 02899: Thread.GetSequenceContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-getsequencecontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-getsequencecontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.GetSequenceContext( callStackIndex, frameId) Return Value SequenceContext Purpose Returns a reference to the SequenceContext object that corresponds to the call stack index you specify. Parameters callStackIndex As Long [In] Specifies a zero-based index into the call stack. You obtain

### Thread.GetSequenceContext

#### Syntax

[Thread](thread.html).GetSequenceContext( callStackIndex, frameId)

#### Return Value

[SequenceContext](sequencecontext.html)

#### Purpose

Returns a reference to the SequenceContext object that corresponds to the call stack index you specify.

#### Parameters

callStackIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index into the call stack. You obtain the number of items on the call stack from the
 [Thread.CallStackSize](thread-callstacksize.html)
 property. Call stack index 0 specifies the sequence context for the most recently executing step group.

frameId
 As
 [Long](data-types-for-teststand.html)

[Out] Returns a unique ID for the sequence context that this method returns. Use this ID with subsequent calls to GetSequenceContext to determine whether the execution is in the same sequence. This can help you minimize the number of items that you must update in the execution display in a user interface.

#### See Also

[SequenceContext](sequencecontext.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[Thread.CallStackSize](thread-callstacksize.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-id.html language=enus -->
## TOPIC 02900: Thread.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.Id Data Type Long Purpose Returns a unique ID number for the thread. The ID number is unique with respect to all threads that you initiate before you shut down the TestStand Engine. The ID number is never zero. Remarks Use this ID number to compare two Thread object references to deter

### Thread.Id

#### Syntax

[Thread](thread.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique ID number for the thread. The ID number is unique with respect to all threads that you initiate before you shut down the TestStand Engine.

Note

#### Remarks

Use this ID number to compare two
 [Thread](thread.html)
 object references to determine whether they refer to the same underlying thread.

#### See Also

[Thread](thread.html)

[Thread.DisplayName](thread-displayname.html)

[Thread.UniqueThreadId](thread-uniquethreadid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-postuimessage.html language=enus -->
## TOPIC 02901: Thread.PostUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-postuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-postuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.PostUIMessage( eventCode, numericDataParam, stringDataParam, synchronous) Purpose This method is obsolete. Use the Thread.PostUIMessageEx method instead. Remarks Posts a user interface message to the current user interface or sequence editor. Parameters eventCode As UIMessageCodes [In]

### Thread.PostUIMessage

#### Syntax

[Thread](thread.html).PostUIMessage( eventCode, numericDataParam, stringDataParam, synchronous)

#### Purpose

Note

Thread.PostUIMessageEx

#### Remarks

Posts a user interface message to the current user interface or sequence editor.

#### Parameters

eventCode
 As
 [UIMessageCodes](uimessagecodes.html)

[In] Specifies the type of UIMessage.

numericDataParam
 As
 [Double](data-types-for-teststand.html)

[In] Specifies numeric data to pass with the message. For example, when you post a
 UIMsg_ProgressPercent
 event, this parameter specifies the percent done.

stringDataParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies string data to pass with the message. For example, when you post a
 UIMsg_ProgressText
 event, this parameter specifies the text to display.

synchronous
 As
 [Boolean](data-types-for-teststand.html)

[In] Typically, you pass
 True
 for this parameter to direct the method to wait until the user interface processes the message. If you pass
 False
 , the method returns immediately without waiting for the user interface to handle the message. If you pass
 False
 and post messages faster than the user interface processes messages, the number of messages in the queue the user interface must handle grows unbounded and floods the user interface with messages, which causes the user interface to become unresponsive.

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessage](uimessage.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Obsolete Thread Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-postuimessageex.html language=enus -->
## TOPIC 02902: Thread.PostUIMessageEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-postuimessageex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-postuimessageex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.PostUIMessageEx( eventCode, numericDataParam, stringDataParam, activeXDataParam, synchronous) Purpose Posts a user interface message to the current user interface or sequence editor. Remarks The messages that you can post from a step are UIMsg_ProgressPercent and UIMsg_ProgressText . T

### Thread.PostUIMessageEx

#### Syntax

[Thread](thread.html).PostUIMessageEx( eventCode, numericDataParam, stringDataParam, activeXDataParam, synchronous)

#### Purpose

Posts a user interface message to the current user interface or sequence editor.

#### Remarks

The messages that you can post from a step are
 [UIMsg_ProgressPercent](uimessagecodes.html)
 and
 [UIMsg_ProgressText](uimessagecodes.html)
 . These messages tell the user interface to display a progress indicator or text message for the execution.

#### Parameters

eventCode
 As
 [UIMessageCodes](uimessagecodes.html)

[In] Specifies the type of UIMessage.

numericDataParam
 As
 [Double](data-types-for-teststand.html)

[In] Specifies numeric data to pass with the message. When you post a UIMsg_ProgressPercent event, this parameter specifies the percent done.

stringDataParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies string data to pass with the message. When you post a UIMsg_ProgressText event, this parameter specifies the text to display.

activeXDataParam
 As
 [IUnknown](data-types-for-teststand.html)

[In] Specifies an ActiveX reference to pass with the message.

synchronous
 As
 [Boolean](data-types-for-teststand.html)

[In] Typically, you pass
 True
 for this parameter to direct the method to wait until the user interface processes the message. If you pass
 False
 and post messages faster than the user interface processes messages, the number of messages in the queue the user interface must handle grows unbounded and floods the user interface with messages, which causes the user interface to become unresponsive.

#### See Also

[Engine.PostUIMessage](engine-postuimessage.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-resume.html language=enus -->
## TOPIC 02903: Thread.Resume

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-resume.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-resume.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.Resume Purpose Resumes execution of the thread. Remarks If you create a thread as initially suspended using either a sequence call step or the TestStand API, use this method to begin executing the thread.

### Thread.Resume

#### Syntax

[Thread](thread.html).Resume

#### Purpose

Resumes execution of the thread.

#### Remarks

If you create a thread as initially suspended using either a sequence call step or the TestStand API, use this method to begin executing the thread.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-runtimevariables.html language=enus -->
## TOPIC 02904: Thread.RunTimeVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-runtimevariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-runtimevariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.RunTimeVariables Data Type PropertyObject Purpose Use this PropertyObject to create and access variables you want to exist only for the current run of the thread. Remarks TestStand destroys these variables when the thread completes, terminates, or aborts. See Also Engine.TemporaryGloba

### Thread.RunTimeVariables

#### Syntax

[Thread](thread.html).RunTimeVariables

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Use this PropertyObject to create and access variables you want to exist only for the current run of the thread.

#### Remarks

TestStand destroys these variables when the thread completes, terminates, or aborts.

#### See Also

[Engine.TemporaryGlobals](engine-temporaryglobals.html)

[Execution.RunTimeVariables](execution-runtimevariables.html)

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-setbatchrteoption.html language=enus -->
## TOPIC 02905: Thread.SetBatchRTEOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-setbatchrteoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-setbatchrteoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.SetBatchRTEOption( newValue) Purpose Specifies the behavior of TestStand when a run-time error occurs in any execution with a thread that is part of the same batch as the thread on which you call this method. Remarks Calling this method on a thread that is not part of a batch has no ef

### Thread.SetBatchRTEOption

#### Syntax

[Thread](thread.html).SetBatchRTEOption( newValue)

#### Purpose

Specifies the behavior of TestStand when a run-time error occurs in any execution with a thread that is part of the same batch as the thread on which you call this method.

#### Remarks

Calling this method on a thread that is not part of a batch has no effect.

#### Parameters

newValue
 As
 [RTEOptions](rteoptions.html)

[In] Specifies the behavior of TestStand when a run-time error occurs.

#### See Also

[Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)

[RTEOptions](rteoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-setstepinto.html language=enus -->
## TOPIC 02906: Thread.SetStepInto

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-setstepinto.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-setstepinto.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.SetStepInto Purpose Sets the execution to suspend again at the earliest possible point. Remarks The method does not resume the execution. The Execution.StepInto method, however, performs the equivalent of calling this method on the foreground thread and then resuming the execution. See

### Thread.SetStepInto

#### Syntax

[Thread](thread.html).SetStepInto

#### Purpose

Sets the execution to suspend again at the earliest possible point.

#### Remarks

The method does not resume the execution. The
 [Execution.StepInto](execution-stepinto.html)
 method, however, performs the equivalent of calling this method on the foreground thread and then resuming the execution.

#### See Also

[Execution.StepInto](execution-stepinto.html)

[Thread.ClearTemporaryBreakpoint](thread-cleartemporarybreakpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-setstepout.html language=enus -->
## TOPIC 02907: Thread.SetStepOut

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-setstepout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-setstepout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.SetStepOut Purpose Sets the execution to suspend again after execution of the current sequence completes. Remarks The method does not resume the execution. The Execution.StepOut method, however, performs the equivalent of calling this method on the foreground thread and then resuming t

### Thread.SetStepOut

#### Syntax

[Thread](thread.html).SetStepOut

#### Purpose

Sets the execution to suspend again after execution of the current sequence completes.

#### Remarks

The method does not resume the execution. The
 [Execution.StepOut](execution-stepout.html)
 method, however, performs the equivalent of calling this method on the foreground thread and then resuming the execution.

#### See Also

[Execution.StepOut](execution-stepout.html)

[Thread.ClearTemporaryBreakpoint](thread-cleartemporarybreakpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-setstepover.html language=enus -->
## TOPIC 02908: Thread.SetStepOver

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-setstepover.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-setstepover.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.SetStepOver Purpose Sets the execution to suspend again after execution of the next step completes. Remarks The method does not resume the execution. The Execution.StepOver method, however, performs the equivalent of calling this method on the foreground thread and then resuming the ex

### Thread.SetStepOver

#### Syntax

[Thread](thread.html).SetStepOver

#### Purpose

Sets the execution to suspend again after execution of the next step completes.

#### Remarks

The method does not resume the execution. The
 [Execution.StepOver](execution-stepover.html)
 method, however, performs the equivalent of calling this method on the foreground thread and then resuming the execution.

#### See Also

[Execution.StepOver](execution-stepover.html)

[Thread.ClearTemporaryBreakpoint](thread-cleartemporarybreakpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-terminationoption.html language=enus -->
## TOPIC 02909: Thread.TerminationOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-terminationoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-terminationoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.TerminationOption Data Type ThreadTerminationOptions Use the following constants with this data type: ThreadTerminationOption_Never –(Value: 2) Specifies that a thread does not stop when its execution terminates. The thread must stop before its execution can end. Use this value to prot

### Thread.TerminationOption

#### Syntax

[Thread](thread.html).TerminationOption

#### Data Type

[ThreadTerminationOptions](threadterminationoptions.html)

Use the following constants with this data type:

- ThreadTerminationOption_Never 
 –(Value: 2) Specifies that a thread does not stop when its execution terminates. The thread must stop before its execution can end. Use this value to protect a thread so the thread does not stop and can complete its work even if its execution attempts to terminate.
- ThreadTerminationOption_Normal 
 –(Value: 0) Specifies that a thread stops when its execution terminates.
- ThreadTerminationOption_Prompt 
 –(Value: 1) Specifies that a thread does not stop when its execution terminates unless you set the
 Execution.OverrideNonTerminatableThreads 
 property. If an execution attempts to terminate and the execution is running only threads that specify this option, the execution sends the
 UIMsg_NonTerminatableThreadsArePreventingTermination 
 event. You can use this value to protect a process model worker thread so the thread does not stop if the user terminates the current UUT or batch.

#### Purpose

Specifies the behavior of a thread when its execution attempts to terminate. This property does not inhibit aborting. The default value is
 ThreadTerminationOption_Normal
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-uniquethreadid.html language=enus -->
## TOPIC 02910: Thread.UniqueThreadId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-uniquethreadid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-uniquethreadid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.UniqueThreadId Data Type String Purpose Returns an identification string that is unique among all threads in all instances of the TestStand Engine. Remarks Use this string to uniquely identify a TestStand thread across multiple instances of the TestStand Engine. If you are using only o

### Thread.UniqueThreadId

#### Syntax

[Thread](thread.html).UniqueThreadId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an identification string that is unique among all threads in all instances of the TestStand Engine.

#### Remarks

Use this string to uniquely identify a TestStand thread across multiple instances of the TestStand Engine. If you are using only one instance of the TestStand Engine, you can use the numeric
 [Thread.Id](thread-id.html)
 property of the thread instead.

#### See Also

[Thread.DisplayName](thread-displayname.html)

[Thread.Id](thread-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-waitforend.html language=enus -->
## TOPIC 02911: Thread.WaitForEnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-waitforend.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-waitforend.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.WaitForEnd( millisecondTimeOut, processWindowsMsgs = True, [stepToStoreResultsIn], [callingSequenceContext]) Return Value Boolean Returns True if the thread finished executing. Returns False if the timeout expired. Purpose Waits for the thread to finish executing. Parameters millisecon

### Thread.WaitForEnd

#### Syntax

[Thread](thread.html).WaitForEnd( millisecondTimeOut, processWindowsMsgs = True, [stepToStoreResultsIn], [callingSequenceContext])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the thread finished executing. Returns
 False
 if the timeout expired.

#### Purpose

Waits for the thread to finish executing.

#### Parameters

millisecondTimeOut
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the number of milliseconds to wait or, pass
 -1
 to wait indefinitely.

If you pass a value for the callingSequenceContext parameter, TestStand suspends the timeout while the calling execution is suspended at a breakpoint so that the time spent at a breakpoint does not count towards the elapsed timeout time.

processWindowsMsgs
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting.

This parameter has a default value of
 True
 .

stepToStoreResultsIn
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the step for which the result is set to the sequence result of this thread.

callingSequenceContext
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you call this method from within a sequence, you can pass the current sequence context to specify that the method returns immediately if the user terminates the execution from which you call this method.

#### See Also

[Execution.WaitForEndEx](execution-waitforendex.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread-willstepintomodule.html language=enus -->
## TOPIC 02912: Thread.WillStepIntoModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread-willstepintomodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread-willstepintomodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Thread.WillStepIntoModule Data Type Boolean Purpose Returns True if the execution will step into the code module for the current step. Remarks This property is True only when accessed from a Pre-Step substep and the execution will suspend in the code module for the step that uses the substep.

### Thread.WillStepIntoModule

#### Syntax

[Thread](thread.html).WillStepIntoModule

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the execution will step into the code module for the current step.

#### Remarks

This property is
 True
 only when accessed from a Pre-Step substep and the execution will suspend in the code module for the step that uses the substep. Obtaining this property from other locations, such as an expression or a step code module, always returns
 False
 .

#### See Also

[Thread.SetStepInto](thread-setstepinto.html)

[Using Substeps](/csh?context=ts_tsfundamentals_step_type_prop_substeps)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/thread.html language=enus -->
## TOPIC 02913: Thread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/thread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/thread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Threads are elements of an Execution. Each thread maintains a call stack that contains a SequenceContext object for each active sequence invocation. You can obtain a thread of an execution by calling the Execution.GetThread method. Properties Batch (Read Only) CallStackSize (Read Only) DisplayName (

### Thread

Threads are elements of an Execution. Each thread maintains a call stack that contains a
 [SequenceContext](sequencecontext.html)
 object for each active sequence invocation. You can obtain a thread of an execution by calling the
 [Execution.GetThread](execution-getthread.html)
 method.

#### Properties

| Batch (Read Only) |
| --- |
| CallStackSize (Read Only) |
| DisplayName (Read Only) |
| Execution (Read Only) |
| ExternallySuspended |
| Id (Read Only) |
| RunTimeVariables (Read Only) |
| TerminationOption |
| UniqueThreadId (Read Only) |
| WillStepIntoModule (Read Only) |

#### Methods

| AddToBatch |
| --- |
| AsPropertyObject |
| ClearCurrentRTE |
| ClearTemporaryBreakpoint |
| DoInteractiveExecution |
| FlushPostResults |
| GetSequenceContext |
| PostUIMessageEx |
| Resume |
| SetBatchRTEOption |
| SetStepInto |
| SetStepOut |
| SetStepOver |
| WaitForEnd |

#### See Also

[Execution.GetThread](execution-getthread.html)

[SequenceContext](sequencecontext.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/threadterminationoptions.html language=enus -->
## TOPIC 02914: ThreadTerminationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/threadterminationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/threadterminationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options to determine how a thread responds when its execution terminates. ThreadTerminationOption_Never –(Value: 2) Specifies that a thread does not stop when its execution terminates. The thread must stop before its execution can end. Use this value to protect a thread so the thread does

### ThreadTerminationOptions

Use these options to determine how a thread responds when its execution terminates.

- ThreadTerminationOption_Never 
 –(Value: 2) Specifies that a thread does not stop when its execution terminates. The thread must stop before its execution can end. Use this value to protect a thread so the thread does not stop and can complete its work even if its execution attempts to terminate.
- ThreadTerminationOption_Normal 
 –(Value: 0) Specifies that a thread stops when its execution terminates.
- ThreadTerminationOption_Prompt 
 –(Value: 1) Specifies that a thread does not stop when its execution terminates unless you set the
 Execution.OverrideNonTerminatableThreads 
 property. If an execution attempts to terminate and the execution is running only threads that specify this option, the execution sends the
 UIMsg_NonTerminatableThreadsArePreventingTermination 
 event. You can use this value to protect a process model worker thread so the thread does not stop if the user terminates the current UUT or batch.

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/timelimitactions.html language=enus -->
## TOPIC 02915: TimeLimitActions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/timelimitactions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/timelimitactions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants for the value of the StationOptions.SetTimeLimitAction and StationOptions.GetTimeLimitAction methods. TimeLimitAction_Abort –(Value: 0) Initiates an abort of a running execution. TimeLimitAction_KillThreads –(Value: 1) Ends the thread for a running, terminating, or aborting execu

### TimeLimitActions

Use these constants for the value of the
 [StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)
 and
 [StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)
 methods.

- TimeLimitAction_Abort 
 –(Value: 0) Initiates an abort of a running execution.
- TimeLimitAction_KillThreads 
 –(Value: 1) Ends the thread for a running, terminating, or aborting execution.
- TimeLimitAction_Prompt 
 –(Value: 2) Launches a dialog box with the option to terminate, abort, or kill the execution.
- TimeLimitAction_Terminate 
 –(Value: 3) Initiates a termination of a running execution.

#### See Also

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/timelimitoperations.html language=enus -->
## TOPIC 02916: TimeLimitOperations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/timelimitoperations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/timelimitoperations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants for the value of the StationOptions.SetTimeLimitAction and StationOptions.GetTimeLimitAction methods. TimeLimitOperation_Aborting –(Value: 2) Applies to an execution from an abort request to completion. TimeLimitOperation_Executing –(Value: 0) Applies to an execution from start t

### TimeLimitOperations

Use these constants for the value of the
 [StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)
 and
 [StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)
 methods.

- TimeLimitOperation_Aborting 
 –(Value: 2) Applies to an execution from an abort request to completion.
- TimeLimitOperation_Executing 
 –(Value: 0) Applies to an execution from start to completion.
- TimeLimitOperation_Terminating 
 –(Value: 1) Applies to an execution from a termination request to completion.

#### See Also

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/timelimittypes.html language=enus -->
## TOPIC 02917: TimeLimitTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/timelimittypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/timelimittypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants for the value of the StationOptions.SetTimeLimitAction and StationOptions.GetTimeLimitAction methods. TimeLimitType_Exiting –(Value: 1) Time limits for executions that run while the engine is exiting. TimeLimitType_NormalExecution –(Value: 0) Time limits for normal execution. See

### TimeLimitTypes

Use these constants for the value of the
 [StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)
 and
 [StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)
 methods.

- TimeLimitType_Exiting 
 –(Value: 1) Time limits for executions that run while the engine is exiting.
- TimeLimitType_NormalExecution 
 –(Value: 0) Time limits for normal execution.

#### See Also

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/tokencode.html language=enus -->
## TOPIC 02918: TokenCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/tokencode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/tokencode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the operator, constant, and identifier tokens an expression can contain. The tokenCode parameter of the Expression.GetToken method returns these constants to identify the type of token you specify. TokenCode_Assignment –(Value: 27) TokenCode_Bad –(Value: 4) TokenCode_Binary

### TokenCode

These constants represent the operator, constant, and identifier tokens an expression can contain. The
 tokenCode
 parameter of the
 [Expression.GetToken](expression-gettoken.html)
 method returns these constants to identify the type of token you specify.

- TokenCode_Assignment 
 –(Value: 27)
- TokenCode_Bad 
 –(Value: 4)
- TokenCode_BinaryInteger 
 –(Value: 48)
- TokenCode_BitwiseAnd 
 –(Value: 21)
- TokenCode_BitwiseAndAssignment 
 –(Value: 32)
- TokenCode_BitwiseNot 
 –(Value: 24)
- TokenCode_BitwiseOr 
 –(Value: 22
- TokenCode_BitwiseOrAssignment 
 –(Value: 33)
- TokenCode_Colon 
 –(Value: 45)
- TokenCode_Conditional 
 –(Value: 44)
- TokenCode_Directive 
 –(Value: 63)
- TokenCode_DivAssignment 
 –(Value: 31)
- TokenCode_Divide 
 –(Value: 8)
- TokenCode_DotDot 
 –(Value: 62)
- TokenCode_Equal 
 –(Value: 16)
- TokenCode_ExclusiveOr 
 –(Value: 23)
- TokenCode_ExclusiveOrAssignment 
 –(Value: 34)
- TokenCode_FieldSpecifier 
 –(Value: 40)
- TokenCode_GreaterThan 
 –(Value: 12)
- TokenCode_GreaterThanEqual 
 –(Value: 13)
- TokenCode_HexInteger 
 –(Value: 49)
- TokenCode_Identifier 
 –(Value: 52)
- TokenCode_Integer 
 –(Value: 47)
- TokenCode_Integer64 
 –(Value: 58)
- TokenCode_LeftBrace 
 –(Value: 53)
- TokenCode_LeftBracket 
 –(Value: 41)
- TokenCode_LeftParenthesis 
 –(Value: 38)
- TokenCode_LeftShift 
 –(Value: 26)
- TokenCode_LeftShiftAssignment 
 –(Value: 36)
- TokenCode_LessThan 
 –(Value: 14)
- TokenCode_LessThanEqual 
 –(Value: 15)
- TokenCode_LogicalAnd 
 –(Value: 18)
- TokenCode_LogicalNot 
 –(Value: 20)
- TokenCode_LogicalOr 
 –(Value: 19)
- TokenCode_Minus 
 –(Value: 6)
- TokenCode_MinusAssignment 
 –(Value: 29)
- TokenCode_MinusMinus 
 –(Value: 11)
- TokenCode_ModAssignment 
 –(Value: 37)
- TokenCode_Modulus 
 –(Value: 9)
- TokenCode_MultAssignment 
 –(Value: 30)
- TokenCode_MultiLineComment 
 –(Value: 1)
- TokenCode_Multiply 
 –(Value: 7)
- TokenCode_NotAToken 
 –(Value: 0)
- TokenCode_NotEqual 
 –(Value: 17)
- TokenCode_OctalInteger 
 –(Value: 56)
- TokenCode_Plus 
 –(Value: 5)
- TokenCode_PlusAssignment 
 –(Value: 28)
- TokenCode_PlusPlus 
 –(Value: 10)
- TokenCode_Real 
 –(Value: 46)
- TokenCode_ReferenceFieldSpecifier 
 –(Value: 60)
- TokenCode_RightBrace 
 –(Value: 54)
- TokenCode_RightBracket 
 –(Value: 42)
- TokenCode_RightParenthesis 
 –(Value: 39)
- TokenCode_RightShift 
 –(Value: 25)
- TokenCode_RightShiftAssignment 
 –(Value: 35)
- TokenCode_Separator 
 –(Value: 43)
- TokenCode_SingleLineComment 
 –(Value: 3)
- TokenCode_String 
 –(Value: 50)
- TokenCode_SymbolicConstant 
 –(Value: 55)
- TokenCode_TemporaryVariable 
 –(Value: 57)
- TokenCode_UnescapedString 
 –(Value: 61)
- TokenCode_UnsignedInteger64 
 –(Value: 59)
- TokenCode_UnterminatedMultiLineComment 
 –(Value: 2)
- TokenCode_UnterminatedString 
 –(Value: 51)

#### See Also

[Expression.GetToken](expression-gettoken.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/tokenizeoptions.html language=enus -->
## TOPIC 02919: TokenizeOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/tokenizeoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/tokenizeoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent options you can use with the tokenizeOptions parameter of the Expression.Tokenize method. Use the bitwise-OR operator to specify more than one option. TokenizeOption_NoOptions –(Value: 0x0) No options. TokenizeOption_PreserveComments –(Value: 0x1) Use this option to prevent

### TokenizeOptions

These constants represent options you can use with the
 tokenizeOptions
 parameter of the
 [Expression.Tokenize](expression-tokenize.html)
 method. Use the bitwise-OR operator to specify more than one option.

- TokenizeOption_NoOptions 
 –(Value: 0x0) No options.
- TokenizeOption_PreserveComments 
 –(Value: 0x1) Use this option to prevent the Expression object from removing comment tokens during tokenization.
- TokenizeOption_RecognizeCPPIdentifiers 
 –(Value: 0x4) Use this option to specify that the
 Expression.Tokenize 
 method recognizes C++ scope resolution and template operators when determining if a token is a valid identifier.
 Note 
 This option is only for parsing. You cannot use C++ scope resolution and template operators in identifiers in an expression you evaluate.
- TokenizeOption_RecognizeIncompleteExpression 
 –(Value: 0x3) Use this option to separately tokenize each line of an expression. If you specify this option, string constants and comments that are incomplete at the end of an expression are identified with the codes
 TokenCode_UnterminatedString 
 or
 TokenCode_UnterminatedMultiLineComment 
 instead of the
 TokenCode_Bad 
 code. Also, a dot not followed by a letter or underscore is identified with the code
 TokenCode_FieldSpecifier 
 instead of the
 TokenCode_Bad 
 .
 Note 
 Specifying this option automatically specifies the
 TokenizeOption_PreserveComments
 option.

#### See Also

[Expression.Tokenize](expression-tokenize.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/toolmenuitemattributes.html language=enus -->
## TOPIC 02920: ToolMenuItemAttributes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/toolmenuitemattributes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/toolmenuitemattributes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the bitwise-AND operator to check the itemAttributes parameter of the Engine.GetToolMenuItemInfoEx and Engine.GetToolMenuItemInfoWithIDEx methods. ToolMenuItem_EditsSelectedFile –(Value: 0x4) Indicates that the Tools menu item edits the selected file. ToolMenuItem_Enabled –(

### ToolMenuItemAttributes

Use these constants with the bitwise-AND operator to check the
 itemAttributes
 parameter of the
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 and
 [Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)
 methods.

- ToolMenuItem_EditsSelectedFile 
 –(Value: 0x4) Indicates that the Tools menu item edits the selected file.
- ToolMenuItem_Enabled 
 –(Value: 0x2) Disables the Tools menu item if this flag is set.
- ToolMenuItem_SeparatorBefore 
 –(Value: 0x1) Inserts a separator before the Tools menu item if this flag is set.

#### See Also

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

[Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/toolmenutypes.html language=enus -->
## TOPIC 02921: ToolMenuTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/toolmenutypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/toolmenutypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify a type of menu item. The constants represent the possible values for the EditTimeMenuItem.Type property. ToolMenuType_Command –(Value: 1) Invokes a Microsoft Windows executable or command with optional arguments. ToolMenuType_Sequence –(Value: 2) Initiates

### ToolMenuTypes

This data type contains values that specify a type of menu item. The constants represent the possible values for the
 [EditTimeMenuItem.Type](edittimemenuitem-type.html)
 property.

- ToolMenuType_Command 
 –(Value: 1) Invokes a Microsoft Windows executable or command with optional arguments.
- ToolMenuType_Sequence 
 –(Value: 2) Initiates an execution on a sequence in a sequence file.
- ToolMenuType_SequenceFile 
 –(Value: 4) Creates a submenu that lists all sequences in a sequence file as menu items.
- ToolMenuType_SubMenu 
 –(Value: 3) Contains additional menu items in a submenu.

#### See Also

[EditTimeMenuItem.Type](edittimemenuitem-type.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/tserror.html language=enus -->
## TOPIC 02922: TSError

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/tserror.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/tserror.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These are the error values the TestStand ActiveX API can return. Refer to the error message TestStand returns for a detailed description of why the error occurred. Whenever a method or property in the TestStand API fails, check the TSError code for the application development environment, as follows

### TSError

These are the error values the TestStand ActiveX API can return. Refer to the error message TestStand returns for a detailed description of why the error occurred. Whenever a method or property in the TestStand API fails, check the TSError code for the application development environment, as follows:

LabWindows/CVI

If the HRESULT for an API function is equal to
 DISP_E_EXCEPTION
 , check the value of the sCode member of the ERRORINFO structure. If the HRESULT is not equal to
 DISP_E_EXCEPTION
 , the error is not a TSError. You can use the value of the HRESULT to determine the type of error.

LabVIEW

Check the value of the code number in the "error out" cluster.

Microsoft Visual C/C++ using #import

Use the Error() method of the _com_error class to obtain the error code.

Microsoft Visual Basic .NET

Check the value of ErrorCode from the COMException class in a Try/Catch block to obtain the error code as follows:
 Try
 ...
 Catch exception As COMException
 MessageBox.Show ("Error " + exception.ErrorCode.ToString() + ": " + exception.Message)
 EndIf

C#

Check the value of ErrorCode from the COMException class in a Try/Catch block to obtain the error code as follows:
 try {
 ...
 }
 catch (COMException exception) {
 MessageBox.Show ("Error " + exception.ErrorCode.ToString() + ": " + exception.Message);
 }

The following error codes are listed alphabetically. Press <Ctrl-F> to search for the error code value.

- TS_Err_AccessDenied 
 –(Value: -17205)
- TS_Err_ActiveXAutomationServerException 
 –(Value: -17811)
- TS_Err_AdapterNoConnectToAutoServer 
 –(Value: -18201)
- TS_Err_AdapterServerConnectionLost 
 –(Value: -18202)
- TS_Err_ArrayDimensionExpected 
 –(Value: -17344)
- TS_Err_ArrayDimensionSizeExpected 
 –(Value: -17345)
- TS_Err_ArrayIndexOutOfBounds 
 –(Value: -17324)
- TS_Err_ArrayLocked 
 –(Value: -17310)
- TS_Err_ArrayTypeExpected 
 –(Value: -17343)
- TS_Err_AutomationObjNotValid 
 –(Value: -17810)
- TS_Err_BadExpressionError 
 –(Value: -17322)
- TS_Err_BadFileFormat 
 –(Value: -17100)
- TS_Err_BadNetPath 
 –(Value: -17202)
- TS_Err_BadPropertyOrVariableName 
 –(Value: -17319)
- TS_Err_ConvertedErrorCode 
 –(Value: -17009)
- TS_Err_CurrentSeqFileNotAvailable 
 –(Value: -17330)
- TS_Err_CVIAutoCmdFailed 
 –(Value: -17704)
- TS_Err_CVICantConnectToTecrunServer 
 –(Value: -17711)
- TS_Err_CVIFuncNotFoundInModule 
 –(Value: -17710)
- TS_Err_CVIModuleHasUnresolvedReferences 
 –(Value: -17709)
- TS_Err_CVINonDllModuleNotSupported 
 –(Value: -17713)
- TS_Err_CVINotReg 
 –(Value: -17703)
- TS_Err_CVIOleError 
 –(Value: -17702)
- TS_Err_CVIRegGenericReadError 
 –(Value: -17708)
- TS_Err_CVIRegKeyNotFound 
 –(Value: -17707)
- TS_Err_CVIRegValueNotFound 
 –(Value: -17706)
- TS_Err_CVIRegValueTypeMismatch 
 –(Value: -17705)
- TS_Err_CVIUnableToTerminateUserProgInCVI 
 –(Value: -17712)
- TS_Err_CVIVersionNotSupported 
 –(Value: -17714)
- TS_Err_DDEFail 
 –(Value: -18101)
- TS_Err_DiskFull 
 –(Value: -17207)
- TS_Err_DispMissingParamID 
 –(Value: -17807)
- TS_Err_DispMissingParamName 
 –(Value: -17806)
- TS_Err_DispMissingRequiredArg 
 –(Value: -17809)
- TS_Err_DispObsoleteMember 
 –(Value: -17812)
- TS_Err_DispUnknownInterface 
 –(Value: -17801)
- TS_Err_DispUnknownMemberID 
 –(Value: -17803)
- TS_Err_DispUnknownMemberName 
 –(Value: -17802)
- TS_Err_DispUnknownParamID 
 –(Value: -17805)
- TS_Err_DispUnknownParamName 
 –(Value: -17804)
- TS_Err_DispWrongNumPositionalParams 
 –(Value: -17808)
- TS_Err_DLLNotLoadable 
 –(Value: -17004)
- TS_Err_DNAssemblyMissing 
 –(Value: -18700)
- TS_Err_DoesNotHaveRequiredPrivilege 
 –(Value: -18360)
- TS_Err_DriveNotReady 
 –(Value: -17203)
- TS_Err_DuplicateItemOrValue 
 –(Value: -17305)
- TS_Err_EmptyExpressionError 
 –(Value: -17347)
- TS_Err_EvaluateFunctionEmptyExpressionError 
 –(Value: -17350)
- TS_Err_EvaluationContextNotAvailable 
 –(Value: -17316)
- TS_Err_ExprTypeIncompatibleWithParameter 
 –(Value: -17313)
- TS_Err_ExprValueNotSuperSetOfParameter 
 –(Value: -17314)
- TS_Err_ExternalServerUnavailable 
 –(Value: -17012)
- TS_Err_FailToRegisterClipFormat 
 –(Value: -18251)
- TS_Err_FileAlreadyExists 
 –(Value: -17206)
- TS_Err_FileFormatIsOutOfDate 
 –(Value: -17099)
- TS_Err_FileFormatNewerThanCurrentVersion 
 –(Value: -17098)
- TS_Err_FileNotConvertableToSeqFile 
 –(Value: -17901)
- TS_Err_FileWasNotFound 
 –(Value: -17208)
- TS_Err_FunctionNotFoundInLib 
 –(Value: -17005)
- TS_Err_IllegalOperationOnValue 
 –(Value: -17309)
- TS_Err_IncompatibleParameters 
 –(Value: -17311)
- TS_Err_IndexOutOfRange 
 –(Value: -17301)
- TS_Err_Int32Overflow 
 –(Value: -17010)
- TS_Err_Int64Overflow 
 –(Value: -17013)
- TS_Err_InvalidAdapterName 
 –(Value: -17336)
- TS_Err_InvalidDrive 
 –(Value: -17211)
- TS_Err_InvalidPathname 
 –(Value: -17204)
- TS_Err_InvalidPointer 
 –(Value: -17346)
- TS_Err_InvalidRegularExpression 
 –(Value: -17342)
- TS_Err_IOError 
 –(Value: -17200)
- TS_Err_ItemCannotBeDeleted 
 –(Value: -17331)
- TS_Err_LabVIEWTypeNotSupportedInCVI 
 –(Value: -17341)
- TS_Err_LV_NXG_AutoBuildError 
 –(Value: -18526)
- TS_Err_LV_NXG_AutoServerError 
 –(Value: -18520)
- TS_Err_LV_NXG_MissingRequiredArg 
 –(Value: -18522)
- TS_Err_LV_NXG_ReportedError 
 –(Value: -18521)
- TS_Err_LV_NXG_RTEDllNotLoaded 
 –(Value: -18525)
- TS_Err_LV_NXG_RunTimeEngineError 
 –(Value: -18523)
- TS_Err_LV_NXG_TypeConversionError 
 –(Value: -18524)
- TS_Err_LValueExpected 
 –(Value: -17318)
- TS_Err_LVAutoServerError 
 –(Value: -18001)
- TS_Err_LVMissingRequiredArg 
 –(Value: -18003)
- TS_Err_LVReportedError 
 –(Value: -18002)
- TS_Err_LVRTDllNotLoaded 
 –(Value: -17338)
- TS_Err_LVRunTimeEngineError 
 –(Value: -18004)
- TS_Err_LVTypeConversionError 
 –(Value: -18005)
- TS_Err_MeasStudioInterfaceNotFound 
 –(Value: -18390)
- TS_Err_MemoryChecking 
 –(Value: -17214)
- TS_Err_MethodOrPropertyNotAvailable 
 –(Value: -18400)
- TS_Err_MismatchedArrayBounds 
 –(Value: -17326)
- TS_Err_MismatchedItems 
 –(Value: -17348)
- TS_Err_MissingType 
 –(Value: -17328)
- TS_Err_ModuleLoadFailure 
 –(Value: -17600)
- TS_Err_ModuleNotSpecified 
 –(Value: -17601)
- TS_Err_NameAlreadyInUse 
 –(Value: -17327)
- TS_Err_NoError 
 –(Value: 0)
- TS_Err_NoFileAssoc 
 –(Value: -18151)
- TS_Err_NoItemsInList 
 –(Value: -17302)
- TS_Err_NotSupported 
 –(Value: -17503)
- TS_Err_ObjectCannotBeAdded 
 –(Value: -17335)
- TS_Err_ObjectLocked 
 –(Value: -17349)
- TS_Err_ObjectTypeIncompatibleWithParameter 
 –(Value: -17332)
- TS_Err_OperationCanceled 
 –(Value: -17604)
- TS_Err_OperationFailed 
 –(Value: -17500)
- TS_Err_OperationInProgress 
 –(Value: -17401)
- TS_Err_OperationOnlyValidWhenSuspended 
 –(Value: -17323)
- TS_Err_OperationTimedOut 
 –(Value: -17402)
- TS_Err_OS_Exception 
 –(Value: -17502)
- TS_Err_OutOfMemory 
 –(Value: -17000)
- TS_Err_PathNotFound 
 –(Value: -17212)
- TS_Err_ProgramError 
 –(Value: -17001)
- TS_Err_ReadObjectNotFound 
 –(Value: -17339)
- TS_Err_RegistryAccessError 
 –(Value: -17002)
- TS_Err_RegistryItemNotFound 
 –(Value: -17003)
- TS_Err_RemoteHostNotSpecified 
 –(Value: -17853)
- TS_Err_RemoteSequenceError 
 –(Value: -17850)
- TS_Err_RemoteSequenceErrorUnableToConnect 
 –(Value: -17851)
- TS_Err_RemoteSequenceRemoteExecutionDenied 
 –(Value: -17852)
- TS_Err_RStringNotFound 
 –(Value: -18051)
- TS_Err_SequenceAborted 
 –(Value: -17602)
- TS_Err_SequenceTerminated 
 –(Value: -17603)
- TS_Err_SharingViolation 
 –(Value: -17209)
- TS_Err_SingleDimensionalNumericArrayExpected 
 –(Value: -17317)
- TS_Err_SourceCodeControlError 
 –(Value: -18370)
- TS_Err_StackOverflow 
 –(Value: -17008)
- TS_Err_StepTypeNotFound 
 –(Value: -17337)
- TS_Err_ThreadCreationFailed 
 –(Value: -17400)
- TS_Err_TooManyItems 
 –(Value: -17303)
- TS_Err_TwoDimensionalNumericArrayExpected 
 –(Value: -17340)
- TS_Err_TypeCannotBeDeleted 
 –(Value: -17333)
- TS_Err_TypeConflict 
 –(Value: -17329)
- TS_Err_TypeLibraryReadError 
 –(Value: -18351)
- TS_Err_TypeMismatchError 
 –(Value: -17321)
- TS_Err_TypePaletteFileLoadErrors 
 –(Value: 17902)
- TS_Err_TypeWithDependingInstancesCannotBeDeleted 
 –(Value: -17334)
- TS_Err_UInt32Overflow 
 –(Value: -17011)
- TS_Err_UInt64Overflow 
 –(Value: -17014)
- TS_Err_UnableToAllocateSystemResource 
 –(Value: -17006)
- TS_Err_UnableToCloseFile 
 –(Value: -17213)
- TS_Err_UnableToInitializeOLESystemDLLs 
 –(Value: -17007)
- TS_Err_UnableToLaunchCVI 
 –(Value: -17701)
- TS_Err_UnableToOpenDirectory 
 –(Value: -17215)
- TS_Err_UnableToOpenFile 
 –(Value: -17201)
- TS_Err_UnableToPassByReference 
 –(Value: -17312)
- TS_Err_UnexpectedChangeCount 
 –(Value: -17351)
- TS_Err_UnexpectedEndOfFile 
 –(Value: -17216)
- TS_Err_UnexpectedSystemError 
 –(Value: -17501)
- TS_Err_UnexpectedType 
 –(Value: -17308)
- TS_Err_UnknownFunctionOrSequenceName 
 –(Value: -17320)
- TS_Err_UnknownType 
 –(Value: -17307)
- TS_Err_UnknownVariableOrProperty 
 –(Value: -17306)
- TS_Err_UnRecognizedValue 
 –(Value: -17304)
- TS_Err_ValueIsInvalidOrOutOfRange 
 –(Value: -17300)
- TS_Err_VisualStudioAutomationError 
 –(Value: -18500)
- TS_Err_WatchExpressionError 
 –(Value: -18380)
- TS_Err_WriteProtected 
 –(Value: -17210)
- TS_Err_WrongNumberOfArrayIndices 
 –(Value: -17325)
- TS_Err_WrongNumberOfParameters 
 –(Value: -17315)
- TS_Err_XMLError 
 –(Value: -18600)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typecategories.html language=enus -->
## TOPIC 02923: TypeCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typecategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typecategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following constants represent the categories to which a type can belong: TypeCategory_BuiltinDataTypes –(Value: 3) Specifies a built-in data type. TypeCategory_CustomDataTypes –(Value: 2) Specifies a custom data type. TypeCategory_None –(Value: 0) Specifies no data type. TypeCategory_StepTypes –

### TypeCategories

The following constants represent the categories to which a type can belong:

- TypeCategory_BuiltinDataTypes 
 –(Value: 3) Specifies a built-in data type.
- TypeCategory_CustomDataTypes 
 –(Value: 2) Specifies a custom data type.
- TypeCategory_None 
 –(Value: 0) Specifies no data type.
- TypeCategory_StepTypes 
 –(Value: 1) Specifies a step type.

#### See Also

[PropertyObject.TypeCategory](propertyobject-typecategory.html)

[TypeUsageList](typeusagelist.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeconflicthandlertypes.html language=enus -->
## TOPIC 02924: TypeConflictHandlerTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeconflicthandlertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeconflicthandlertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify how TestStand responds when encountering two conflicting definitions for the same type. Type conflicts generally occur when TestStand reads a type from a sequence file that has a different structure than the type already loaded. ConflictHandler_Error –(Value: 1) Specifies tha

### TypeConflictHandlerTypes

These constants specify how TestStand responds when encountering two conflicting definitions for the same type.
 [Type conflicts](/csh?context=ts_tsfundamentals_types)
 generally occur when TestStand reads a type from a sequence file that has a different structure than the type already loaded.

- ConflictHandler_Error 
 –(Value: 1) Specifies that the method returns an error if type conflicts exist.
- ConflictHandler_Prompt 
 –(Value: 3) Specifies that the method prompts the user with a dialog box to resolve each type conflict.
- ConflictHandler_UseGlobalType 
 –(Value: 4) Specifies that the method converts the conflicting type to the currently loaded (global) type if a type conflict exists.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.UnserializeObjects](engine-unserializeobjects.html)

[PropertyObject.ReadEx](propertyobject-readex.html)

[PropertyObject.UnserializeEx](propertyobject-unserializeex.html)

[PropertyObjectFile.HandleTypeConflicts](propertyobjectfile-handletypeconflicts.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeequaloptions.html language=enus -->
## TOPIC 02925: TypeEqualOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeequaloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeequaloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the PropertyObjectType.IsEqualTo method. TypeEqualOption_DoNotCompareDimensions –(Value: 0x1) Specifies that the PropertyObjectType.IsEqualTo method does not compare the array dimensions that the PropertyObjectType.ArrayDimensions property specifies. TypeEqualOption_DoNotCom

### TypeEqualOptions

Use these constants with the
 [PropertyObjectType.IsEqualTo](propertyobjecttype-isequalto.html)
 method.

- TypeEqualOption_DoNotCompareDimensions 
 –(Value: 0x1) Specifies that the
 PropertyObjectType.IsEqualTo 
 method does not compare the array dimensions that the
 PropertyObjectType.ArrayDimensions 
 property specifies.
- TypeEqualOption_DoNotCompareIsObject 
 –(Value: 0x2) Specifies that the
 PropertyObjectType.IsEqualTo 
 method does not compare the
 PropertyObjectType.IsObject 
 property.
- TypeEqualOption_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[PropertyObjectType.ArrayDimensions](propertyobjecttype-arraydimensions.html)

[PropertyObjectType.IsEqualTo](propertyobjecttype-isequalto.html)

[PropertyObjectType.IsObject](propertyobjecttype-isobject.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-addusedtypes.html language=enus -->
## TOPIC 02926: TypeUsageList.AddUsedTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-addusedtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-addusedtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.AddUsedTypes( propObject) Return Value Boolean Returns True if any types were added to the type usage list. Purpose Adds all the types the specified object uses to the type usage list. Parameters propObject As PropertyObject [In] Specifies the object from which to add types to t

### TypeUsageList.AddUsedTypes

#### Syntax

[TypeUsageList](typeusagelist.html).AddUsedTypes( propObject)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if any types were added to the type usage list.

#### Purpose

Adds all the types the specified object uses to the type usage list.

#### Parameters

propObject
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the object from which to add types to the type usage list.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-changecount.html language=enus -->
## TOPIC 02927: TypeUsageList.ChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-changecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-changecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.ChangeCount Data Type Long Purpose Returns the number of modifications made to the type usage list.

### TypeUsageList.ChangeCount

#### Syntax

[TypeUsageList](typeusagelist.html).ChangeCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of modifications made to the type usage list.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-createandinsertnewtypefromexist.html language=enus -->
## TOPIC 02928: TypeUsageList.CreateAndInsertNewTypeFromExisting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-createandinsertnewtypefromexist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-createandinsertnewtypefromexist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.CreateAndInsertNewTypeFromExisting( existingType, index, typeCategoryParam, reservedParam = 0) Return Value PropertyObject Returns the newly created type, which is already inserted into and attached to the type usage list. Purpose Creates a new type with a unique name based on t

### TypeUsageList.CreateAndInsertNewTypeFromExisting

#### Syntax

[TypeUsageList](typeusagelist.html).CreateAndInsertNewTypeFromExisting( existingType, index, typeCategoryParam, reservedParam = 0)

#### Return Value

[PropertyObject](propertyobject.html)

Returns the newly created type, which is already inserted into and attached to the type usage list.

#### Purpose

Creates a new type with a unique name based on the type you specify in the
 existingType
 parameter and inserts and attaches the new type to the type usage list. This method also clears some type-specific settings in the newly created type, such as the flags
 PropFlags_NotDeletable
 ,
 PropFlags_NotEditable
 , and
 PropFlags_NameNotEditable
 ; the type flags
 PropTypeFlags_NIInstalledType
 and
 PropTypeFlags_PreventEditingType
 ; the
 TypeMinimumTestStandVersion
 ; and the password protection settings. Using this method is equivalent to copying and pasting a type in the
 [Types](../tsref/types-window.html)
 window in the TestStand Sequence Editor to create a new type based on an existing type.

#### Parameters

existingType
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the existing root type definition on which to base the newly created type.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index in the type usage list at which to insert the new type.

typeCategoryParam
 As
 [TypeCategories](typecategories.html)

[In] Specifies the type category in which to insert the new type.

reservedParam
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use. Pass
 0
 for this parameter.

This parameter has a default value of
 0
 .

#### See Also

[PropertyFlags](propertyflags.html)

[PropertyObject.TypeMinimumTestStandVersion](propertyobject-typeminimumteststandversion.html)

[PropertyObject.GetTypeDefinitionProtection](propertyobject-gettypedefinitionprotection.html)

[PropertyObjTypeFlags](propertyobjtypeflags.html)

[TypeCategories](typecategories.html)

[TypeUsageList.InsertType](typeusagelist-inserttype.html)

[TypeUsageList.SetIsTypeAttachedToFile](typeusagelist-setistypeattachedtofile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-getistypeattachedtofile.html language=enus -->
## TOPIC 02929: TypeUsageList.GetIsTypeAttachedToFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-getistypeattachedtofile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-getistypeattachedtofile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.GetIsTypeAttachedToFile( index) Return Value Boolean Returns True if the type is attached to the file. Purpose Returns a value that indicates whether the type the index parameter specifies is attached to the file that contains the type usage list. Remarks Types that are attached

### TypeUsageList.GetIsTypeAttachedToFile

#### Syntax

[TypeUsageList](typeusagelist.html).GetIsTypeAttachedToFile( index)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the type is attached to the file.

#### Purpose

Returns a value that indicates whether the type the
 index
 parameter specifies is attached to the file that contains the type usage list.

#### Remarks

Types that are attached to a file are saved with the file to which the list belongs, even if no instances of the type exist in the file.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the type in the type usage list.

#### See Also

[TypeUsageList.SetIsTypeAttachedToFile](typeusagelist-setistypeattachedtofile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-gettypedefinition.html language=enus -->
## TOPIC 02930: TypeUsageList.GetTypeDefinition

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-gettypedefinition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-gettypedefinition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.GetTypeDefinition( index) Return Value PropertyObject Purpose Returns the type the index parameter specifies. Parameters index As Long [In] Specifies the zero-based index of the type in the type usage list. See Also PropertyObject

### TypeUsageList.GetTypeDefinition

#### Syntax

[TypeUsageList](typeusagelist.html).GetTypeDefinition( index)

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the type the
 index
 parameter specifies.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the type in the type usage list.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-gettypeindex.html language=enus -->
## TOPIC 02931: TypeUsageList.GetTypeIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-gettypeindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-gettypeindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.GetTypeIndex( typeNameParam) Return Value Long The index of the type with the specified name. Returns -1 if no type in the list has the specified name. Purpose Returns the index of the type the typeNameParam parameter specifies. Parameters typeNameParam As String [In] Specifies

### TypeUsageList.GetTypeIndex

#### Syntax

[TypeUsageList](typeusagelist.html).GetTypeIndex( typeNameParam)

#### Return Value

[Long](data-types-for-teststand.html)

The index of the type with the specified name. Returns
 -1
 if no type in the list has the specified name.

#### Purpose

Returns the index of the type the
 typeNameParam
 parameter specifies.

#### Parameters

typeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the type name to locate in the list.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-inserttype.html language=enus -->
## TOPIC 02932: TypeUsageList.InsertType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-inserttype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-inserttype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.InsertType( typeToInsert, index, typeCategoryParam) Purpose Inserts a type into the type usage list and associates it with a type category. Parameters typeToInsert As PropertyObject [In] Specifies the new type definition to insert. index As Long [In] Specifies the zero-based ind

### TypeUsageList.InsertType

#### Syntax

[TypeUsageList](typeusagelist.html).InsertType( typeToInsert, index, typeCategoryParam)

#### Purpose

Inserts a type into the type usage list and associates it with a type category.

#### Parameters

typeToInsert
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the new type definition to insert.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index at which to insert the type into the type usage list.

typeCategoryParam
 As
 [TypeCategories](typecategories.html)

[In] Specifies the type category to associate with the type.

#### See Also

[PropertyObject](propertyobject.html)

[TypeCategories](typecategories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-movetype.html language=enus -->
## TOPIC 02933: TypeUsageList.MoveType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-movetype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-movetype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.MoveType( index, newIndex) Purpose Moves the type the index parameter specifies to a new index in the type usage list. Parameters index As Long [In] Specifies the zero-based index of the type to move. newIndex As Long [In] Specifies the new zero-based index of the type.

### TypeUsageList.MoveType

#### Syntax

[TypeUsageList](typeusagelist.html).MoveType( index, newIndex)

#### Purpose

Moves the type the
 index
 parameter specifies to a new index in the type usage list.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the type to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the new zero-based index of the type.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-numtypes.html language=enus -->
## TOPIC 02934: TypeUsageList.NumTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-numtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-numtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.NumTypes Data Type Long Purpose Returns the number of types in the type usage list.

### TypeUsageList.NumTypes

#### Syntax

[TypeUsageList](typeusagelist.html).NumTypes

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of types in the type usage list.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-removetype.html language=enus -->
## TOPIC 02935: TypeUsageList.RemoveType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-removetype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-removetype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.RemoveType( index) Return Value PropertyObject The removed type. Purpose Removes the type the index parameter specifies from the type usage list. Parameters index As Long [In] Specifies the zero-based index of the type to remove. See Also PropertyObject

### TypeUsageList.RemoveType

#### Syntax

[TypeUsageList](typeusagelist.html).RemoveType( index)

#### Return Value

[PropertyObject](propertyobject.html)

The removed type.

#### Purpose

Removes the type the
 index
 parameter specifies from the type usage list.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the type to remove.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-setistypeattachedtofile.html language=enus -->
## TOPIC 02936: TypeUsageList.SetIsTypeAttachedToFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-setistypeattachedtofile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-setistypeattachedtofile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.SetIsTypeAttachedToFile( index, store) Purpose Specifies if the type the index parameter specifies is attached to the file that contains the type usage list. Remarks Types attached to a file are saved with the file to which the list belongs, even if no instances of the type exis

### TypeUsageList.SetIsTypeAttachedToFile

#### Syntax

[TypeUsageList](typeusagelist.html).SetIsTypeAttachedToFile( index, store)

#### Purpose

Specifies if the type the
 index
 parameter specifies is attached to the file that contains the type usage list.

#### Remarks

Types attached to a file are saved with the file to which the list belongs, even if no instances of the type exist in the file.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the type in the type usage list.

store
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to attach the type to the file.

#### See Also

[TypeUsageList.GetIsTypeAttachedToFile](typeusagelist-getistypeattachedtofile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-union.html language=enus -->
## TOPIC 02937: TypeUsageList.Union

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-union.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-union.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.Union( unionTypeUsageList) Return Value Boolean Returns True if any types were added. Otherwise, returns False . Purpose Adds all the types from one type usage list to another. Remarks Does not add types that already exist in both type usage lists. Parameters unionTypeUsageList

### TypeUsageList.Union

#### Syntax

[TypeUsageList](typeusagelist.html).Union( unionTypeUsageList)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if any types were added. Otherwise, returns
 False
 .

#### Purpose

Adds all the types from one type usage list to another.

#### Remarks

Does not add types that already exist in both type usage lists.

#### Parameters

unionTypeUsageList
 As
 [TypeUsageList](typeusagelist.html)

[In] Specifies the type usage list that contains the types to add.

#### See Also

[Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)

[TypeUsageList](typeusagelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist-validatenewtypename.html language=enus -->
## TOPIC 02938: TypeUsageList.ValidateNewTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist-validatenewtypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist-validatenewtypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax TypeUsageList.ValidateNewTypeName( newName, allowDuplicates, isValid) Return Value String Returns a description of why the name is not valid. Purpose Determines if the specified name is valid for a new type definition. Remarks Call this method before adding a new type definition to a type usa

### TypeUsageList.ValidateNewTypeName

#### Syntax

[TypeUsageList](typeusagelist.html).ValidateNewTypeName( newName, allowDuplicates, isValid)

#### Return Value

[String](data-types-for-teststand.html)

Returns a description of why the name is not valid.

#### Purpose

Determines if the specified name is valid for a new type definition.

#### Remarks

Call this method before adding a new type definition to a type usage list to determine whether the name of the new type definition is valid.

#### Parameters

newName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the new name to validate.

allowDuplicates
 As
 [Boolean](data-types-for-teststand.html)

[In] In addition to validating the name, also check if the name is already in use. If this parameter is
 False
 , the method reports that the new name is invalid if it is already in use.

isValid
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the new name is valid.

#### See Also

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[PropertyObject.ValidateNewName](propertyobject-validatenewname.html)

[PropertyObject.ValidateNewSubPropertyName](propertyobject-validatenewsubpropertyname.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeusagelist.html language=enus -->
## TOPIC 02939: TypeUsageList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeusagelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeusagelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TypeUsageList contains a list of types a PropertyObjectFile object uses. Use this class to insert or delete types from a file. When you edit a PropertyObjectFile object by inserting named data types or step types in to the file, add any new types to the TypeUsageList object for the file so the t

### TypeUsageList

The TypeUsageList contains a list of types a PropertyObjectFile object uses. Use this class to insert or delete types from a file.

Note

TypeUsageList.AddUsedTypes

TypeUsageList.Union

#### Properties

| ChangeCount (Read Only) |
| --- |
| NumTypes (Read Only) |

#### Methods

| AddUsedTypes |
| --- |
| CreateAndInsertNewTypeFromExisting |
| GetIsTypeAttachedToFile |
| GetTypeDefinition |
| GetTypeIndex |
| InsertType |
| MoveType |
| RemoveType |
| SetIsTypeAttachedToFile |
| Union |
| ValidateNewTypeName |

#### See Also

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[TypeUsageList.AddUsedTypes](typeusagelist-addusedtypes.html)

[TypeUsageList.Union](typeusagelist-union.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/typeversionautoincrement.html language=enus -->
## TOPIC 02940: TypeVersionAutoIncrement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/typeversionautoincrement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/typeversionautoincrement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the StationOptions.TypeVersionAutoIncrementOpt property or with the versionIncOption parameter of PropertyObjectFile.CheckForModifiedTypes method. TypeVersionInc_Build –(Value: 4) Auto-increment build version number. TypeVersionInc_Major –(Value: 1) Auto-increment ma

### TypeVersionAutoIncrement

Use the following constants with the
 [StationOptions.TypeVersionAutoIncrementOpt](stationoptions-typeversionautoincrementopt.html)
 property or with the
 versionIncOption
 parameter of
 [PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)
 method.

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

#### See Also

[PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)

[StationOptions.TypeVersionAutoIncrementOpt](stationoptions-typeversionautoincrementopt.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-acknowledge.html language=enus -->
## TOPIC 02941: UIMessage.Acknowledge

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-acknowledge.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-acknowledge.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.Acknowledge Purpose If you are not using the TestStand manager controls in a custom user interface, call this method on each UIMessage you receive after you finish using the message. The TestStand manager controls automatically call this method. If the user interface message is sync

### UIMessage.Acknowledge

#### Syntax

[UIMessage](uimessage.html).Acknowledge

#### Purpose

If you are not using the TestStand manager controls in a custom user interface, call this method on each UIMessage you receive after you finish using the message. The TestStand manager controls automatically call this method. If the user interface message is synchronous, this method unblocks the thread that posts the message. This method also indicates to the engine that you are ready to receive further messages.

#### See Also

[UIMessage.IsSynchronous](uimessage-issynchronous.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-activexdata.html language=enus -->
## TOPIC 02942: UIMessage.ActiveXData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-activexdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-activexdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.ActiveXData Data Type IUnknown Purpose Returns the ActiveX reference passed to the activeXDataParam parameter of the Thread.PostUIMessageEx method that posted the user interface message. See Also Thread.PostUIMessageEx

### UIMessage.ActiveXData

#### Syntax

[UIMessage](uimessage.html).ActiveXData

#### Data Type

[IUnknown](data-types-for-teststand.html)

#### Purpose

Returns the ActiveX reference passed to the
 activeXDataParam
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 method that posted the user interface message.

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-aspropertyobject.html language=enus -->
## TOPIC 02943: UIMessage.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the UIMessage object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### UIMessage.AsPropertyObject

#### Syntax

[UIMessage](uimessage.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the UIMessage object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-event.html language=enus -->
## TOPIC 02944: UIMessage.Event

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-event.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-event.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.Event Data Type UIMessageCodes Purpose Returns the event code that describes the type of UIMessage. The eventCode parameter of the Thread.PostUIMessageEx method that posted the user interface message specifies the value this method returns. See Also Thread.PostUIMessageEx UIMessage.

### UIMessage.Event

#### Syntax

[UIMessage](uimessage.html).Event

#### Data Type

[UIMessageCodes](uimessagecodes.html)

#### Purpose

Returns the event code that describes the type of UIMessage. The
 eventCode
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 method that posted the user interface message specifies the value this method returns.

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessage.Execution](uimessage-execution.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-execution.html language=enus -->
## TOPIC 02945: UIMessage.Execution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-execution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.Execution Data Type Execution Purpose Returns a reference to the execution to which the event applies. Remarks Release the execution reference when you are done using it. If the event is not associated with an execution, this property returns a NULL reference. See Also Execution

### UIMessage.Execution

#### Syntax

[UIMessage](uimessage.html).Execution

#### Data Type

[Execution](execution.html)

#### Purpose

Returns a reference to the execution to which the event applies.

#### Remarks

Release the execution reference when you are done using it. If the event is not associated with an execution, this property returns a
 NULL
 reference.

#### See Also

[Execution](execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-issynchronous.html language=enus -->
## TOPIC 02946: UIMessage.IsSynchronous

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-issynchronous.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-issynchronous.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.IsSynchronous Data Type Boolean Purpose Returns True if the thread that posted the event is blocked and is waiting for you to acknowledge the UIMessage. Remarks Threads can post UIMessages synchronously or asynchronously. If a thread posts a user interface message synchronously, the

### UIMessage.IsSynchronous

#### Syntax

[UIMessage](uimessage.html).IsSynchronous

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the thread that posted the event is blocked and is waiting for you to acknowledge the UIMessage.

#### Remarks

Threads can post UIMessages synchronously or asynchronously. If a thread posts a user interface message synchronously, the thread blocks until the message is acknowledged or the last reference to the user interface message is released. If a thread posts a user interface message asynchronously, the thread returns
 False
 .

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessage.Acknowledge](uimessage-acknowledge.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-numericdata.html language=enus -->
## TOPIC 02947: UIMessage.NumericData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-numericdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-numericdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.NumericData Data Type Double Purpose Returns the numeric value passed to the numericDataParam parameter of the Thread.PostUIMessageEx method that posted the UIMessage. Remarks An example of a user interface message event that uses numericDataParam is the UIMsg_ProgressPercent event.

### UIMessage.NumericData

#### Syntax

[UIMessage](uimessage.html).NumericData

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the numeric value passed to the
 numericDataParam
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 method that posted the UIMessage.

#### Remarks

An example of a user interface message event that uses numericDataParam is the
 UIMsg_ProgressPercent
 event. If you define custom user interface message events, you can pass numeric data to the
 Thread.PostUIMessageEx
 method.

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-stringdata.html language=enus -->
## TOPIC 02948: UIMessage.StringData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-stringdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-stringdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.StringData Data Type String Purpose Returns the string value passed to the stringDataParam parameter of the Thread.PostUIMessageEx method that posted the UIMessage. Remarks An example of a user interface message event that uses stringDataParam is the UIMsg_ProgressText event. If you

### UIMessage.StringData

#### Syntax

[UIMessage](uimessage.html).StringData

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the string value passed to the
 stringDataParam
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 method that posted the UIMessage.

#### Remarks

An example of a user interface message event that uses stringDataParam is the
 UIMsg_ProgressText
 event. If you define custom user interface message events, you can pass string data to the
 Thread.PostUIMessageEx
 method.

#### See Also

[Thread.PostUIMessageEx](thread-postuimessageex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage-thread.html language=enus -->
## TOPIC 02949: UIMessage.Thread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage-thread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage-thread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIMessage.Thread Data Type Thread Purpose Returns a reference to the thread to which the event applies. Remarks Release the thread reference when you are done using it. If the event is not associated with a thread, this property returns a NULL reference. See Also Thread

### UIMessage.Thread

#### Syntax

[UIMessage](uimessage.html).Thread

#### Data Type

[Thread](thread.html)

#### Purpose

Returns a reference to the thread to which the event applies.

#### Remarks

Release the thread reference when you are done using it. If the event is not associated with a thread, this property returns a
 NULL
 reference.

#### See Also

[Thread](thread.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessage.html language=enus -->
## TOPIC 02950: UIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand uses UIMessage objects to pass information about the state of the engine and the current executions to the user interface or sequence editor. You can obtain UIMessage objects in a user interface program by providing a callback to the engine. The engine calls the callback when it has a UIMe

### UIMessage

TestStand uses UIMessage objects to pass information about the state of the engine and the current executions to the user interface or sequence editor. You can obtain UIMessage objects in a user interface program by providing a callback to the engine. The engine calls the callback when it has a UIMessage object to pass. If you do not provide a callback, you can set the
 [Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)
 property to
 True
 and call the
 [Engine.GetUIMessage](engine-getuimessage.html)
 method to poll for UIMessage objects.

#### Properties

| ActiveXData (Read Only) |
| --- |
| Event (Read Only) |
| Execution (Read Only) |
| IsSynchronous (Read Only) |
| NumericData (Read Only) |
| StringData (Read Only) |
| Thread (Read Only) |

#### Methods

| Acknowledge |
| --- |
| AsPropertyObject |

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[User Interface (UI) Messages](/csh?context=ts_tsapiref_app_user_interface_ui_messages)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uimessagecodes.html language=enus -->
## TOPIC 02951: UIMessageCodes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uimessagecodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uimessagecodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants for the eventCode parameter of the Thread.PostUIMessageEx and Engine.PostUIMessage methods. These methods allow you to pass data with the message using the numericDataParam , stringDataParam , and activeXDataParam parameters. A user interface can respond to ModelState messages by

### UIMessageCodes

Use these constants for the
 eventCode
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 and
 [Engine.PostUIMessage](engine-postuimessage.html)
 methods. These methods allow you to pass data with the message using the
 numericDataParam
 ,
 stringDataParam
 , and
 activeXDataParam
 parameters.

Note

- UIMsg_AbortingExecution 
 –(Value: 6) TestStand posts this message just before aborting an execution. TestStand does not actually abort execution until the user interface releases the UIMessage.
- UIMsg_BreakOnBreakpoint 
 –(Value: 2) TestStand posts this message to the user interface to notify it that the execution has suspended. The user interface must update the display accordingly.
- UIMsg_BreakOnRunTimeError 
 –(Value: 3) TestStand posts this message to the user interface to notify it that a run-time error has been encountered in the execution. The user interface must update the display accordingly.
 Note 
 The engine posts this event only when you select
 Show Dialog
 from the On Run-Time Error ring control on the
 [Execution tab](../tsref/execution-tab-station-options-dialog-box.html)
 of the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box. A user interface typically calls the
 [Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)
 method.
- UIMsg_BreakOnUserRequest 
 –(Value: 1) TestStand posts this message to the user interface to notify it that the execution suspended in response to a user request. The user interface must update the display accordingly.
- UIMsg_CascadeWindows 
 –(Value: 24) Post this message to the user interface to instruct it to cascade the windows the
 activeXDataParam 
 parameter specifies. Use an array of ActiveX reference objects that reference a PropertyObjectFile or an Execution for the
 activeXDataParam 
 parameter. The user interface cascades the windows that correspond to the objects in the array. To cascade all windows, pass a
 NULL 
 reference for the
 activeXDataParam 
 parameter or use the
 Nothing 
 keyword if you are using the ActiveX/COM Adapter.
- UIMsg_ClientFileChanged 
 –(Value: 28) An Execution object posts this message when a client changes the value of the
 Execution.ClientFile 
 property. The
 UIMessage.Execution 
 property references the Execution that sends the message.
- UIMsg_CloseWindows 
 –(Value: 26) Post this message to the user interface to instruct it to close a window or windows that display a PropertyObjectFile or an execution. Specify the window by passing a PropertyObjectFile or Execution reference for the
 activeXDataParam 
 parameter, or specify several windows by passing an ActiveX reference array of such objects for the
 activeXDataParam 
 parameter. Pass a
 NULL 
 reference, or use the
 Nothing 
 keyword if you are using the ActiveX/COM Adapter, to close all currently open document windows in the user interface.
- UIMsg_DisplayReport 
 –(Value: 29) Post this message when you want the user interface to display the current contents of the execution report.
- UIMsg_EndExecution 
 –(Value: 8) TestStand posts this message after an execution completes. The user interface must update the display accordingly.
- UIMsg_EndFileExecution 
 –(Value: 19) TestStand posts this message when the execution finishes using a sequence file. TestStand specifies the file in the
 UIMessage.ActiveXData 
 property.
- UIMsg_EndInteractiveExecution 
 –(Value: 14) TestStand posts this message whenever an interactive execution ends.
- UIMsg_GotoLocation 
 –(Value: 38) The
 Locations.GotoLocation 
 method posts this message to the user interface to instruct the user interface to select the Locations passed in as the
 activeXDataParam 
 parameter.
- UIMsg_KillingExecutionThreads 
 –(Value: 7) TestStand posts this message just before killing the threads in an execution. TestStand does not actually kill the threads until the user interface releases the UIMessage.
- UIMsg_LocalizationSettingChanged 
 –(Value: 21) TestStand posts this message to notify the user interface that the decimal point localization setting has changed in the system setting for the operating system or in the
 StationOptions.UseLocalizedDecimalPoint 
 setting. When a user interface receives this message, it should refresh any values it displays that these changes might affect.
- UIMsg_ModelState_BeginTesting 
 –(Value: 33) TestStand process models post this message to the user interface prior to calling
 MainSequence 
 in the client sequence file. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_EnabledStateSet 
 –(Value: 36) TestStand Batch process models post this message to the user interface after setting the enabled state of a test-socket execution. The value of the
 stringDataParam 
 parameter is
 True 
 if the socket is enabled and
 False 
 if the socket is disabled. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_Identified 
 –(Value: 32) TestStand process models post this message to the user interface after identifying the serial number for a unit under test (UUT) or batch of UUTs. The
 stringDataParam 
 parameter specifies the UUT serial number unless the execution is a batch controller. If the execution is a batch controller, the
 stringDataParam 
 parameter specifies the batch serial number. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_Initializing 
 –(Value: 30) TestStand process models post this message to the user interface before performing initialization prior to testing. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_PostProcessing 
 –(Value: 43) TestStand process models post this message to the user interface before generating the report and logging the data for a client sequence file. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_PostProcessingComplete 
 –(Value: 35) TestStand process models post this message to the user interface after generating the report and logging the data for a client sequence file. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_TestingComplete 
 –(Value: 34) TestStand process models post this message to the user interface after the
 MainSequence 
 in the client sequence file returns control to the model. If the execution is not a batch controller or a parallel controller, the
 stringDataParam 
 parameter specifies the UUT result status. If the execution is a batch controller or a parallel controller, the value of the stringDataParam parameter specifies the overall status of the controlling execution, which by default can be
 Passed, Failed, Error, Terminated 
 , or
 Aborted 
 . The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_ModelState_Waiting 
 –(Value: 31) TestStand process models post this message to the user interface before waiting for an action to occur, such as the user entering a serial number in response to a prompt. The
 numericDataParam 
 parameter specifies the test-socket index. The
 activeXDataParam 
 parameter contains a reference to the sequence context for the process model sequence file that posts the message.
- UIMsg_NonTerminatableThreadsArePreventingTermination 
 –(Value: 42) An execution posts this message when it attempts to terminate and every thread in the execution uses a value of
 ThreadTerminationOptions_Prompt 
 for the
 Thread.TerminationOption 
 property. A user interface typically handles this event by prompting users to terminate all threads. If the user chooses to terminate all threads, the user interface calls the
 Execution.OverrideNonTerminatableThreads 
 property to signal the threads that use a value of
 ThreadTerminationOptions_Prompt 
 for the
 Thread.TerminationOption 
 property to stop running.
- UIMsg_OpenWindows 
 –(Value: 22) Post this message to the user interface to instruct it to open a file in a window. If the file or execution is already open, the application brings the file to the front. A file can be specified by a pathname in the
 stringDataParam 
 parameter or by a PropertyObjectFile object in the
 activeXDataParam 
 parameter. An execution can be specified by an Execution object in the
 activeXDataParam 
 parameter. A list of files and/or executions can be specified by an array of references to PropertyObjectFile and Execution objects in the
 activeXDataParam 
 parameter. For sequence files, the
 stringDataParam 
 parameter can also contain a '|' separator followed by the name of a sequence to display. If you specify the sequence file in the
 activeXDataParam 
 parameter, you can specify just the sequence name in the
 stringDataParam 
 parameter. This constant does not support opening workspace files.
- UIMsg_OutputMessages 
 –(Value: 40) TestStand posts this message at periodic intervals when it holds references to output messages that calls to the
 OutputMessage.Post 
 method queue. TestStand transfers the queued messages to an
 OutputMessages 
 collection attached to the
 UIMessage.ActiveXData 
 property for this event. Ensure that an application that processes output messages copies the output message references from the collection in
 UIMessage.ActiveXData 
 to a private OutputMessages collection by passing the private collection to the
 OutputMessages.CopyMessagesToCollection 
 method. An application calls the
 Engine.NewOutputMessages 
 method to create a private OutputMessage collection. TestStand generates this event only if the
 Engine.OutputMessagesEnabled 
 property is
 True 
 . Because there can be more than one handler for this event, ensure that the application does not modify the OutputMessages collection the
 UIMessage.ActiveXData 
 property holds.
- UIMsg_ProgressPercent 
 –(Value: 11) TestStand step modules post this message to the user interface to notify it to update the progress indicator associated with an execution. The
 activeXDataParam 
 parameter specifies an execution. The
 numericDataParam 
 parameter specifies a value from 0 to 100 that indicates the percentage of progress the current execution reports. This value indicates the progress of operations for which the execution chooses to report the amount of progress. The value does not necessarily reflect the progress of the execution as a whole.
- UIMsg_ProgressText 
 –(Value: 12) TestStand step modules post this message to the user interface to notify it to update the progress message associated with an execution. The
 activeXDataParam 
 parameter specifies an execution. The
 stringDataParam 
 parameter specifies a progress message.
- UIMsg_PushUndoItem 
 –(Value: 39) Post this message to the sequence editor to instruct the sequence editor to push an undo item onto an UndoStack. An undo item is a COM object that implements the
 UndoItem 
 interface. You pass the undo item as the
 activeXDataParam 
 parameter. The sequence editor uses the
 UndoItem.EditedFile 
 property to determine which UndoStack to push the undo item onto. Send this message synchronously to determine which UndoStack the sequence editor placed the undo item onto immediately after the call to the
 PostUIMessage 
 method returns by checking the
 UndoItem.UndoStack 
 property.
- UIMsg_RefreshWindows 
 –(Value: 27) Post this message to the user interface to instruct it to refresh the data it displays for the corresponding PropertyObjectFile or SequenceContext you pass for the
 activeXDataParam 
 parameter. Pass a single reference or an ActiveX array of references using the
 activeXDataParam 
 parameter to specify which window or windows to refresh. Pass a SequenceContext object to refresh the values for the steps which the user interface displays for that execution. Pass
 NULL 
 for the
 activeXDataParam 
 parameter to refresh the displays for all the files and executions. The
 Overriding SequenceFilePostStepFailure Callback 
 and the
 Overriding SequenceFilePostStepRuntimeError Callback 
 examples located in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Examples\Modifying Process Models\Overriding Engine Callbacks 
 directory demonstrate how to use this UIMessage.
- UIMsg_ReportChanged 
 –(Value: 25) The TestStand Engine posts this message to the user interface whenever you update the report of an execution. This allows the user interface to refresh the Report view if it is showing.
- UIMsg_ReportCollectionChanged 
 –(Value: 44) The TestStand Engine posts this message when the content or an active report changes for the
 Reports 
 collection of an execution. If the active report changes, the
 activeXDataParam 
 parameter contains a reference to the previously active report.
- UIMsg_ReportLocationChanged 
 –(Value: 37) The TestStand Engine posts this message to the user interface whenever you change the location of the report.
- UIMsg_ResumeFromBreak 
 –(Value: 17) TestStand posts this message when an execution resumes after being suspended at a breakpoint. The execution resumes when the user interface message is released.
- UIMsg_RuntimeError 
 –(Value: 45) TestStand posts this message to the user interface to notify the user interface that the execution has encountered a run-time error. The user interface can alter the error, for example, by adding contextual information to the error message.
- UIMsg_ShutDownCancelled 
 –(Value: 20) TestStand posts this message to notify the user interface that the user cancelled a pending shutdown.
- UIMsg_ShutDownComplete 
 –(Value: 9) TestStand posts this message when a
 shutdown 
 completes. If this is not the final shutdown, the user interface can continue to load and execute sequences.
- UIMsg_StartExecution 
 –(Value: 10) TestStand posts this message when an execution begins. This message serves to notify the user interface to update the display accordingly.
- UIMsg_StartFileExecution 
 –(Value: 18) TestStand posts this message when it begins using a sequence file. TestStand specifies the file in the
 UIMessage.ActiveXData 
 property.
- UIMsg_StartInteractiveExecution 
 –(Value: 13) TestStand posts this message whenever an interactive execution begins.
- UIMsg_TerminatingExecution 
 –(Value: 5) TestStand posts this message just before terminating an execution. The execution does not actually terminate until the user interface releases the UIMessage.
- UIMsg_TerminatingInteractiveExecution 
 –(Value: 15) TestStand posts this message just before terminating an interactive execution. The interactive execution does not actually terminate until the user interface message is released.
- UIMsg_TerminationCancelled 
 –(Value: 16) TestStand posts this message to notify the user interface to update the display when a pending termination is cancelled.
- UIMsg_TileWindows 
 –(Value: 23) Post this message to the user interface to instruct it to tile the windows the
 activeXDataParam 
 parameter specifies. Use an array of ActiveX reference objects that reference a PropertyObjectFile or an Execution for the
 activeXDataParam 
 parameter. The user interface tiles the windows that correspond to the objects in the array. To tile all windows, pass a
 NULL 
 reference for the
 activeXDataParam 
 parameter or use the
 Nothing 
 keyword if you are using the ActiveX/COM Adapter.
- UIMsg_Trace 
 –(Value: 4) TestStand posts this message to the user interface to notify it that the execution has reached a trace point. The user interface must update the display accordingly.
- UIMsg_TypePaletteFileListChanged 
 –(Value: 41) TestStand posts this message to the user interface to notify it that the type palette file list has changed. The user interface must update its display accordingly. This event occurs after calling the
 Engine.UnloadTypePaletteFiles 
 ,
 Engine.LoadTypePaletteFilesEx 
 , and
 Engine.SetTypePaletteFileList 
 methods.
- UIMsg_UserMessageBase 
 –(Value: 10000) Codes for all user-defined messages must be greater than or equal to the value of this constant. Define and use event codes greater than
 UIMsg_UserMessageBase 
 only when you can ensure that the event code does not conflict with event codes for messages that other custom TestStand components, such as add-on products, define. National Instruments recommends using the
 Engine.RegisterUIMessage 
 method to obtain an event code for a message to guarantee that the code is unique for the lifetime of the engine. Components that generate and process the message call this method, which returns the previously assigned message code if the message is already assigned.

#### See Also

[Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)

[Engine.GetOutputMessages](engine-getoutputmessages.html)

[Engine.NewOutputMessages](engine-newoutputmessages.html)

[Engine.OutputMessagesEnabled](engine-outputmessagesenabled.html)

[Engine.PostUIMessage](engine-postuimessage.html)

[Engine.Shutdown](engine-shutdown.html)

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[Execution.ClientFile](execution-clientfile.html)

[Locations.GotoLocation](locations-gotolocation.html)

[OutputMessage.Post](outputmessage-post.html)

[OutputMessages](outputmessages.html)

[OutputMessages.CopyMessagesToCollection](outputmessages-copymessagestocollection.html)

[OutputMessages.TransferMessagesToCollection](outputmessages-transfermessagestocollection.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessage](uimessage.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

[UIMessage.Event](uimessage-event.html)

[UIMessage.Execution](uimessage-execution.html)

[UndoItem](undoitem.html)

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.UndoStack](undoitem-undostack.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-backgroundcolor.html language=enus -->
## TOPIC 02952: UIStyle.BackgroundColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-backgroundcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-backgroundcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.BackgroundColor Data Type Long Purpose Returns the background color.

### UIStyle.BackgroundColor

#### Syntax

[UIStyle](uistyle.html).BackgroundColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the background color.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-fontname.html language=enus -->
## TOPIC 02953: UIStyle.FontName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-fontname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-fontname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.FontName Data Type String Purpose Returns the name of the font.

### UIStyle.FontName

#### Syntax

[UIStyle](uistyle.html).FontName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the font.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-fontsize.html language=enus -->
## TOPIC 02954: UIStyle.FontSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-fontsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-fontsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.FontSize Data Type Double Purpose Returns the size of the font.

### UIStyle.FontSize

#### Syntax

[UIStyle](uistyle.html).FontSize

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the size of the font.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-foregroundcolor.html language=enus -->
## TOPIC 02955: UIStyle.ForegroundColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-foregroundcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-foregroundcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.ForegroundColor Data Type Long Purpose Returns the foreground color.

### UIStyle.ForegroundColor

#### Syntax

[UIStyle](uistyle.html).ForegroundColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the foreground color.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-getcolor.html language=enus -->
## TOPIC 02956: UIStyle.GetColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-getcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-getcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.GetColor( color) Return Value Long Purpose Returns the color for the UIStyleColor the parameter specifies. Parameters color As UIStyleColors [In] Specifies the style color to return.

### UIStyle.GetColor

#### Syntax

[UIStyle](uistyle.html).GetColor( color)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the color for the
 UIStyleColor
 the parameter specifies.

#### Parameters

color
 As
 [UIStyleColors](uistylecolors.html)

[In] Specifies the style color to return.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-getfonttypename.html language=enus -->
## TOPIC 02957: UIStyle.GetFontTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-getfonttypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-getfonttypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.GetFontTypeName( fontType) Return Value String Purpose Returns the font name for the fontType parameter. Parameters fontType As UIStyleFontTypes [In] Specifies the font type to return.

### UIStyle.GetFontTypeName

#### Syntax

[UIStyle](uistyle.html).GetFontTypeName( fontType)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the font name for the
 fontType
 parameter.

#### Parameters

fontType
 As
 [UIStyleFontTypes](uistylefonttypes.html)

[In] Specifies the font type to return.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-getfonttypesize.html language=enus -->
## TOPIC 02958: UIStyle.GetFontTypeSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-getfonttypesize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-getfonttypesize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.GetFontTypeSize( fontType) Return Value Double Purpose Returns the font size for the fontType parameter. Parameters fontType As UIStyleFontTypes [In] Specifies the font type to return.

### UIStyle.GetFontTypeSize

#### Syntax

[UIStyle](uistyle.html).GetFontTypeSize( fontType)

#### Return Value

[Double](data-types-for-teststand.html)

#### Purpose

Returns the font size for the
 fontType
 parameter.

#### Parameters

fontType
 As
 [UIStyleFontTypes](uistylefonttypes.html)

[In] Specifies the font type to return.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-gridlinecolor.html language=enus -->
## TOPIC 02959: UIStyle.GridLineColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-gridlinecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-gridlinecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.GridLineColor Data Type Long Purpose Returns the color of the grid lines in tables.

### UIStyle.GridLineColor

#### Syntax

[UIStyle](uistyle.html).GridLineColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the color of the grid lines in tables.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-headerforegroundcolor.html language=enus -->
## TOPIC 02960: UIStyle.HeaderForegroundColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-headerforegroundcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-headerforegroundcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.HeaderForegroundColor Data Type Long Purpose Returns the text color for table headers.

### UIStyle.HeaderForegroundColor

#### Syntax

[UIStyle](uistyle.html).HeaderForegroundColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the text color for table headers.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-sectionheaderfontname.html language=enus -->
## TOPIC 02961: UIStyle.SectionHeaderFontName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-sectionheaderfontname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-sectionheaderfontname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.SectionHeaderFontName Data Type String Purpose Returns the name of the section header font.

### UIStyle.SectionHeaderFontName

#### Syntax

[UIStyle](uistyle.html).SectionHeaderFontName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the section header font.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-sectionheaderfontsize.html language=enus -->
## TOPIC 02962: UIStyle.SectionHeaderFontSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-sectionheaderfontsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-sectionheaderfontsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.SectionHeaderFontSize Data Type Double Purpose Returns the size of the section header font.

### UIStyle.SectionHeaderFontSize

#### Syntax

[UIStyle](uistyle.html).SectionHeaderFontSize

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the size of the section header font.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-selectedbackgroundcolor.html language=enus -->
## TOPIC 02963: UIStyle.SelectedBackgroundColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-selectedbackgroundcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-selectedbackgroundcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.SelectedBackgroundColor Data Type Long Purpose Returns the background color for an item you select in the TestStand Sequence Editor or a TestStand User Interface.

### UIStyle.SelectedBackgroundColor

#### Syntax

[UIStyle](uistyle.html).SelectedBackgroundColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the background color for an item you select in the TestStand Sequence Editor or a TestStand User Interface.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle-selectedforegroundcolor.html language=enus -->
## TOPIC 02964: UIStyle.SelectedForegroundColor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle-selectedforegroundcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle-selectedforegroundcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UIStyle.SelectedForegroundColor Data Type Long Purpose Returns the foreground color for an item you select in the TestStand Sequence Editor or a TestStand User Interface.

### UIStyle.SelectedForegroundColor

#### Syntax

[UIStyle](uistyle.html).SelectedForegroundColor

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the foreground color for an item you select in the TestStand Sequence Editor or a TestStand User Interface.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistyle.html language=enus -->
## TOPIC 02965: UIStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the UIStyle class to configure style settings for dialogs and controls TestStand displays. Properties BackgroundColor (Read Only) FontName (Read Only) FontSize (Read Only) ForegroundColor (Read Only) GridLineColor (Read Only) HeaderForegroundColor (Read Only) SectionHeaderFontName (Read Only) Se

### UIStyle

Use the UIStyle class to configure style settings for dialogs and controls TestStand displays.

#### Properties

| BackgroundColor (Read Only) |
| --- |
| FontName (Read Only) |
| FontSize (Read Only) |
| ForegroundColor (Read Only) |
| GridLineColor (Read Only) |
| HeaderForegroundColor (Read Only) |
| SectionHeaderFontName (Read Only) |
| SectionHeaderFontSize (Read Only) |
| SelectedBackgroundColor (Read Only) |
| SelectedForegroundColor (Read Only) |

#### Methods

| GetColor |
| --- |
| GetFontTypeName |
| GetFontTypeSize |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistylecolors.html language=enus -->
## TOPIC 02966: UIStyleColors

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistylecolors.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistylecolors.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with UIStyle.GetColor to specify which color to get. UIStyleColor_Background –(Value: 0) Get the background color. UIStyleColor_Background2 –(Value: 1) Get the second background color. Provides an alternative color that a control can use. Some controls use BackroundColor2 to fill

### UIStyleColors

Use these constants with
 UIStyle.GetColor
 to specify which color to get.

- UIStyleColor_Background 
 –(Value: 0) Get the background color.
- UIStyleColor_Background2 
 –(Value: 1) Get the second background color. Provides an alternative color that a control can use. Some controls use
 BackroundColor2 
 to fill empty space.
- UIStyleColor_Foreground 
 –(Value: 2) Get foreground color.
- UIStyleColor_GridLine 
 –(Value: 3) Get grid line color.
- UIStyleColor_HeaderForeground 
 –(Value: 4) Get header foreground color.
- UIStyleColor_MatchedDelimiterBackground 
 –(Value: 7) Get background color to highlight matching delimiters.
- UIStyleColor_SelectedBackground 
 –(Value: 5) Get selected background color.
- UIStyleColor_SelectedForeground 
 –(Value: 6) Get selected foreground color.

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/uistylefonttypes.html language=enus -->
## TOPIC 02967: UIStyleFontTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/uistylefonttypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/uistylefonttypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the font type. UIStyleFontType_Monospaced –(Value: 1) Specifies the monospaced GUI font. UIStyleFontType_Proportional –(Value: 0) Specifies the general proportional GUI font. UIStyleFontType_SectionHeader –(Value: 2) Specifies the section header. UIStyleFontType_Subtit

### UIStyleFontTypes

Use these constants to specify the font type.

- UIStyleFontType_Monospaced 
 –(Value: 1) Specifies the monospaced GUI font.
- UIStyleFontType_Proportional 
 –(Value: 0) Specifies the general proportional GUI font.
- UIStyleFontType_SectionHeader 
 –(Value: 2) Specifies the section header.
- UIStyleFontType_Subtitle2 
 –(Value: 3) Specifies the subtitle2.

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-canredo.html language=enus -->
## TOPIC 02968: UndoItem.CanRedo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-canredo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-canredo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.CanRedo Data Type Boolean Purpose If this property is False , do not call the UndoItem.Redo method. See Also UndoItem.CanUndo UndoItem.Redo

### UndoItem.CanRedo

#### Syntax

[UndoItem](undoitem.html).CanRedo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 False
 , do not call the
 [UndoItem.Redo](undoitem-redo.html)
 method.

#### See Also

[UndoItem.CanUndo](undoitem-canundo.html)

[UndoItem.Redo](undoitem-redo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-canundo.html language=enus -->
## TOPIC 02969: UndoItem.CanUndo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-canundo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-canundo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.CanUndo Data Type Boolean Purpose If this property is False , do not call the UndoItem.Undo method. See Also UndoItem.CanRedo UndoItem.Undo

### UndoItem.CanUndo

#### Syntax

[UndoItem](undoitem.html).CanUndo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 False
 , do not call the
 [UndoItem.Undo](undoitem-undo.html)
 method.

#### See Also

[UndoItem.CanRedo](undoitem-canredo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-editedfile.html language=enus -->
## TOPIC 02970: UndoItem.EditedFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-editedfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-editedfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.EditedFile Data Type PropertyObjectFile Purpose Returns the file the UndoItem.Undo and UndoItem.Redo methods modify. Use this property to associate an undo item with an UndoStack object. See Also PropertyObjectFile UndoItem.Redo UndoItem.Undo UndoStack

### UndoItem.EditedFile

#### Syntax

[UndoItem](undoitem.html).EditedFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the file the
 [UndoItem.Undo](undoitem-undo.html)
 and
 [UndoItem.Redo](undoitem-redo.html)
 methods modify. Use this property to associate an undo item with an
 [UndoStack](undostack.html)
 object.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

[UndoStack](undostack.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-editedobjects.html language=enus -->
## TOPIC 02971: UndoItem.EditedObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-editedobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-editedobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.EditedObjects Data Type Object Array Purpose Returns the objects the UndoItem.Undo and UndoItem.Redo methods modify. Remarks Calling this property returns all objects that UndoItem2.TopObjects[i].GetPropertyObject(UndoItem2.LookupStrings[i]) references. If one of the objects does not

### UndoItem.EditedObjects

#### Syntax

[UndoItem](undoitem.html).EditedObjects

#### Data Type

[Object Array](data-types-for-teststand.html)

#### Purpose

Returns the objects the
 [UndoItem.Undo](undoitem-undo.html)
 and
 [UndoItem.Redo](undoitem-redo.html)
 methods modify.

#### Remarks

Calling this property returns all objects that
 UndoItem2.TopObjects[i].GetPropertyObject(UndoItem2.LookupStrings[i])
 references. If one of the objects does not exist, this property fails and returns an error explaining that the property the
 lookupstring
 parameter specifies does not exist.

#### See Also

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-posteditchangecount.html language=enus -->
## TOPIC 02972: UndoItem.PostEditChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-posteditchangecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-posteditchangecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.PostEditChangeCount Data Type Long Purpose Returns the change count of the UndoItem.EditedFile property after the user made the edit this undo item reverts. Remarks The UndoItem.Undo method returns a TS_Err_UnexpectedChangeCount error if EditedFile.ChangeCount does not equal the valu

### UndoItem.PostEditChangeCount

#### Syntax

[UndoItem](undoitem.html).PostEditChangeCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the change count of the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property after the user made the edit this undo item reverts.

#### Remarks

The
 [UndoItem.Undo](undoitem-undo.html)
 method returns a
 TS_Err_UnexpectedChangeCount
 error if
 EditedFile.ChangeCount
 does not equal the value of this property. The
 [UndoItem.Redo](undoitem-redo.html)
 method restores
 EditedFile.ChangeCount
 to the value of this property after redoing the edit.

#### See Also

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.PreEditChangeCount](undoitem-preeditchangecount.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-posteditlocations.html language=enus -->
## TOPIC 02973: UndoItem.PostEditLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-posteditlocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-posteditlocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.PostEditLocations Data Type Locations Purpose If the UndoItem.RefreshEnabled property is True , the UndoItem.Redo method calls the Locations.GotoLocation method on this property after making all edits, and the UndoItem.Undo method calls the Locations.GotoLocation method on this prope

### UndoItem.PostEditLocations

#### Syntax

[UndoItem](undoitem.html).PostEditLocations

#### Data Type

[Locations](locations.html)

#### Purpose

If the
 [UndoItem.RefreshEnabled](undoitem-refreshenabled.html)
 property is
 True
 , the
 [UndoItem.Redo](undoitem-redo.html)
 method calls the
 [Locations.GotoLocation](locations-gotolocation.html)
 method on this property after making all edits, and the
 [UndoItem.Undo](undoitem-undo.html)
 method calls the
 Locations.GotoLocation
 method on this property before making any edits.

#### See Also

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[UndoItem.PreEditLocations](undoitem-preeditlocations.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.RefreshEnabled](undoitem-refreshenabled.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-preeditchangecount.html language=enus -->
## TOPIC 02974: UndoItem.PreEditChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-preeditchangecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-preeditchangecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.PreEditChangeCount Data Type Long Purpose Returns the change count of the UndoItem.EditedFile property before the user made the edit this undo item reverts. Remarks The UndoItem.Redo method returns a TS_Err_UnexpectedChangeCount error if EditedFile.ChangeCount does not equal the valu

### UndoItem.PreEditChangeCount

#### Syntax

[UndoItem](undoitem.html).PreEditChangeCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the change count of the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property before the user made the edit this undo item reverts.

#### Remarks

The
 [UndoItem.Redo](undoitem-redo.html)
 method returns a
 TS_Err_UnexpectedChangeCount
 error if
 EditedFile.ChangeCount
 does not equal the value of this property. The
 [UndoItem.Undo](undoitem-undo.html)
 method restores
 EditedFile.ChangeCount
 to the value of this property after undoing the edit.

#### See Also

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.PostEditChangeCount](undoitem-posteditchangecount.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-preeditlocations.html language=enus -->
## TOPIC 02975: UndoItem.PreEditLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-preeditlocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-preeditlocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.PreEditLocations Data Type Locations Purpose If the UndoItem.RefreshEnabled property is True , the UndoItem.Redo method calls the Locations.GotoLocation method on this property before making any edits, and the UndoItem.Undo method calls the Locations.GotoLocation method on this prope

### UndoItem.PreEditLocations

#### Syntax

[UndoItem](undoitem.html).PreEditLocations

#### Data Type

[Locations](locations.html)

#### Purpose

If the
 [UndoItem.RefreshEnabled](undoitem-refreshenabled.html)
 property is
 True
 , the
 [UndoItem.Redo](undoitem-redo.html)
 method calls the
 [Locations.GotoLocation](locations-gotolocation.html)
 method on this property before making any edits, and the
 [UndoItem.Undo](undoitem-undo.html)
 method calls the
 Locations.GotoLocation
 method on this property after making all edits.

#### See Also

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[UndoItem.PostEditLocations](undoitem-posteditlocations.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.RefreshEnabled](undoitem-refreshenabled.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-redo.html language=enus -->
## TOPIC 02976: UndoItem.Redo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-redo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-redo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.Redo Purpose Redoes an edit to the UndoItem.EditedFile property that the UndoItem.Undo method reverted. Remarks This method returns a TS_Err_UnexpectedChangeCount error if the change count of the UndoItem.EditedFile property is not equal to the value it was before the user made the e

### UndoItem.Redo

#### Syntax

[UndoItem](undoitem.html).Redo

#### Purpose

Redoes an edit to the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property that the
 [UndoItem.Undo](undoitem-undo.html)
 method reverted.

#### Remarks

This method returns a
 TS_Err_UnexpectedChangeCount
 error if the change count of the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property is not equal to the value it was before the user made the edit that this undo item reverts.

Calling this method also restores the change count of the
 UndoItem.EditedFile
 property to the value it was after the user made the edit that this undo item reverts, sends a
 UIMsg_RefreshWindows
 user interface message to the sequence editor if the
 [UndoItem.RefreshEnabled](undoitem-refreshenabled.html)
 property is
 True
 , and sends a
 UIMsg_GotoLocation
 user interface message to the sequence editor to go to the location of the edit if the
 UndoItem.RefreshEnabled
 property is
 True
 .

#### See Also

[PropertyObjectFile.ChangeCount](propertyobjectfile-changecount.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItem.CanRedo](undoitem-canredo.html)

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.RefreshEnabled](undoitem-refreshenabled.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-redodescription.html language=enus -->
## TOPIC 02977: UndoItem.RedoDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-redodescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-redodescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.RedoDescription Data Type String Purpose Returns the edit that the UndoItem.Redo method performs. Remarks This text normally appears in a menu item and is usually the same as the UndoItem.UndoDescription property text. See Also UndoItem.Redo UndoItem.UndoDescription

### UndoItem.RedoDescription

#### Syntax

[UndoItem](undoitem.html).RedoDescription

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the edit that the
 [UndoItem.Redo](undoitem-redo.html)
 method performs.

#### Remarks

This text normally appears in a menu item and is usually the same as the
 [UndoItem.UndoDescription](undoitem-undodescription.html)
 property text.

#### See Also

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.UndoDescription](undoitem-undodescription.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-redoeditkind.html language=enus -->
## TOPIC 02978: UndoItem.RedoEditKind

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-redoeditkind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-redoeditkind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.RedoEditKind Data Type EditKinds Purpose Returns the kind of edit the UndoItem.Redo method performs. See Also EditKinds UndoItem.Redo UndoItem.UndoEditKind

### UndoItem.RedoEditKind

#### Syntax

[UndoItem](undoitem.html).RedoEditKind

#### Data Type

[EditKinds](editkinds.html)

#### Purpose

Returns the kind of edit the
 [UndoItem.Redo](undoitem-redo.html)
 method performs.

#### See Also

[EditKinds](editkinds.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.UndoEditKind](undoitem-undoeditkind.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-refreshenabled.html language=enus -->
## TOPIC 02979: UndoItem.RefreshEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-refreshenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-refreshenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.RefreshEnabled Data Type Boolean Purpose If this property is True , the UndoItem.Undo and UndoItem.Redo methods send a UIMsg_RefreshWindows user interface message to refresh the UndoItem.EditedFile property and a UIMsg_GotoLocation user interface message to go to the location of the

### UndoItem.RefreshEnabled

#### Syntax

[UndoItem](undoitem.html).RefreshEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 True
 , the
 [UndoItem.Undo](undoitem-undo.html)
 and
 [UndoItem.Redo](undoitem-redo.html)
 methods send a
 UIMsg_RefreshWindows
 user interface message to refresh the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property and a
 UIMsg_GotoLocation
 user interface message to go to the location of the edit.

#### See Also

[UIMessageCodes](uimessagecodes.html)

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-undo.html language=enus -->
## TOPIC 02980: UndoItem.Undo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-undo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-undo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.Undo Purpose Reverts an edit to the UndoItem.EditedFile . Remarks This method returns a TS_Err_UnexpectedChangeCount error if the change count of UndoItem.EditedFile is not equal to the value it was after the user made the edit this undo item reverts. Calling this method also restore

### UndoItem.Undo

#### Syntax

[UndoItem](undoitem.html).Undo

#### Purpose

Reverts an edit to the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 .

#### Remarks

This method returns a
 TS_Err_UnexpectedChangeCount
 error if the change count of
 UndoItem.EditedFile
 is not equal to the value it was after the user made the edit this undo item reverts.

Calling this method also restores the change count of the EditedFile to the value it was before the user made the edit this undo item reverts, sends a
 UIMsg_RefreshWindows
 user interface message to the sequence editor if
 [UndoItem.RefreshEnabled](undoitem-refreshenabled.html)
 is
 True
 , and sends a
 UIMsg_GotoLocation
 user interface message to the sequence editor to go to the location of the edit if RefreshEnabled is
 True
 .

#### See Also

[PropertyObjectFile.ChangeCount](propertyobjectfile-changecount.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItem.CanUndo](undoitem-canundo.html)

[UndoItem.EditedFile](undoitem-editedfile.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.RefreshEnabled](undoitem-refreshenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-undodescription.html language=enus -->
## TOPIC 02981: UndoItem.UndoDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-undodescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-undodescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.UndoDescription Data Type String Purpose Returns the edit the UndoItem.Undo method reverts. Remarks This text normally appears in a menu item and is usually the same as the UndoItem.RedoDescription property text. See Also UndoItem.RedoDescription UndoItem.Undo

### UndoItem.UndoDescription

#### Syntax

[UndoItem](undoitem.html).UndoDescription

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the edit the
 [UndoItem.Undo](undoitem-undo.html)
 method reverts.

#### Remarks

This text normally appears in a menu item and is usually the same as the
 [UndoItem.RedoDescription](undoitem-redodescription.html)
 property text.

#### See Also

[UndoItem.RedoDescription](undoitem-redodescription.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-undoeditkind.html language=enus -->
## TOPIC 02982: UndoItem.UndoEditKind

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-undoeditkind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-undoeditkind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.UndoEditKind Data Type EditKinds Purpose Returns the kind of edit the UndoItem.Undo method performs. See Also EditKinds UndoItem.RedoEditKind UndoItem.Undo

### UndoItem.UndoEditKind

#### Syntax

[UndoItem](undoitem.html).UndoEditKind

#### Data Type

[EditKinds](editkinds.html)

#### Purpose

Returns the kind of edit the
 [UndoItem.Undo](undoitem-undo.html)
 method performs.

#### See Also

[EditKinds](editkinds.html)

[UndoItem.RedoEditKind](undoitem-redoeditkind.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem-undostack.html language=enus -->
## TOPIC 02983: UndoItem.UndoStack

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem-undostack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem-undostack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem.UndoStack Data Type UndoStack Purpose Returns the UndoStack object that this undo item is on. Remarks The UndoStack object sets this property when you call UndoStack.Push . See Also UndoStack UndoStack.Push

### UndoItem.UndoStack

#### Syntax

[UndoItem](undoitem.html).UndoStack

#### Data Type

[UndoStack](undostack.html)

#### Purpose

Returns the UndoStack object that this undo item is on.

#### Remarks

The UndoStack object sets this property when you call
 [UndoStack.Push](undostack-push.html)
 .

#### See Also

[UndoStack](undostack.html)

[UndoStack.Push](undostack-push.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem.html language=enus -->
## TOPIC 02984: UndoItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A user interface receives objects that implement the UndoItem interface through the UIMessage.ActiveXData property of a UIMsg_PushUndoItem UI Message. A user interface uses the UndoItem.EditedFile property to find an appropriate UndoStack to push the undo item onto. You can also use the UndoItem int

### UndoItem

A user interface receives objects that implement the UndoItem interface through the
 [UIMessage.ActiveXData](uimessage-activexdata.html)
 property of a
 UIMsg_PushUndoItem
 UI Message. A user interface uses the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property to find an appropriate UndoStack to push the undo item onto.

You can also use the UndoItem interface to make an edit to a TestStand file undoable if the
 [UndoItemCreator](undoitemcreator.html)
 does not provide enough functionality to undo an edit. To do this, create a COM object that implements the UndoItem interface and send an instance of the object to the sequence editor using a
 UIMsg_PushUndoItem
 UI Message.

Note

#### Properties

| CanRedo (Read Only) |
| --- |
| CanUndo (Read Only) |
| EditedFile (Read Only) |
| EditedObjects (Read Only) |
| PostEditChangeCount (Read Only) |
| PostEditLocations (Read Only) |
| PreEditChangeCount (Read Only) |
| PreEditLocations (Read Only) |
| RedoDescription (Read Only) |
| RedoEditKind (Read Only) |
| RefreshEnabled |
| UndoDescription (Read Only) |
| UndoEditKind (Read Only) |
| UndoStack |

#### Methods

| Redo |
| --- |
| Undo |

#### See Also

[EditedFile](undoitem-editedfile.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItemCreator](undoitemcreator.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem2-lookupstrings.html language=enus -->
## TOPIC 02985: UndoItem2.LookupStrings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem2-lookupstrings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem2-lookupstrings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem2.LookupStrings Data Type String Array Purpose Returns the lookup strings that, when combined with the corresponding items in the UndoItem2.TopObjects property, specify the objects the UndoItem.Undo and UndoItem.Redo methods modify. Remarks Calling the UndoItem.EditedObjects property

### UndoItem2.LookupStrings

#### Syntax

[UndoItem2](undoitem2.html).LookupStrings

#### Data Type

[String Array](data-types-for-teststand.html)

#### Purpose

Returns the lookup strings that, when combined with the corresponding items in the
 [UndoItem2.TopObjects](undoitem2-topobjects.html)
 property, specify the objects the
 [UndoItem.Undo](undoitem-undo.html)
 and
 [UndoItem.Redo](undoitem-redo.html)
 methods modify.

#### Remarks

Calling the
 [UndoItem.EditedObjects](undoitem-editedobjects.html)
 property returns all objects that
 UndoItem2.TopObjects[i].GetPropertyObject(UndoItem2.LookupStrings[i])
 references. If one of the objects does not exist, the
 UndoItem.EditedObjects
 property fails and returns an error that explains that the property the
 lookupstring
 parameter specifies does not exist.

#### See Also

[UndoItem.EditedObjects](undoitem-editedobjects.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

[UndoItem2.TopObjects](undoitem2-topobjects.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem2-topobjects.html language=enus -->
## TOPIC 02986: UndoItem2.TopObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem2-topobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem2-topobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItem2.TopObjects Data Type Object Array Purpose Returns the objects that, when combined with the corresponding items in the UndoItem2.LookupStrings property, specify the objects the UndoItem.Undo and UndoItem.Redo methods modify. Remarks Calling the UndoItem.EditedObjects property returns

### UndoItem2.TopObjects

#### Syntax

[UndoItem2](undoitem2.html).TopObjects

#### Data Type

[Object Array](data-types-for-teststand.html)

#### Purpose

Returns the objects that, when combined with the corresponding items in the
 [UndoItem2.LookupStrings](undoitem2-lookupstrings.html)
 property, specify the objects the
 [UndoItem.Undo](undoitem-undo.html)
 and
 [UndoItem.Redo](undoitem-redo.html)
 methods modify.

#### Remarks

Calling the
 [UndoItem.EditedObjects](undoitem-editedobjects.html)
 property returns all objects that
 UndoItem2.TopObjects[i].GetPropertyObject(UndoItem2.LookupStrings[i])
 references. If one of the objects does not exist, the
 UndoItem.EditedObjects
 property fails and returns an error that explains that the property the
 lookupstring
 parameter specifies does not exist.

#### See Also

[UndoItem.EditedObjects](undoitem-editedobjects.html)

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

[UndoItem2.LookupStrings](undoitem2-lookupstrings.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitem2.html language=enus -->
## TOPIC 02987: UndoItem2

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitem2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitem2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The UndoItem2 class inherits from the UndoItem class and supports all the UndoItem properties and methods. An object that supports UndoItem might not necessarily support UndoItem2 . You can also use the UndoItem2 interface to make an edit to a TestStand file undoable if the UndoItemCreator does not

### UndoItem2

The
 UndoItem2
 class inherits from the
 [UndoItem](undoitem.html)
 class and supports all the
 UndoItem
 properties and methods. An object that supports
 UndoItem
 might not necessarily support
 UndoItem2
 .

You can also use the
 UndoItem2
 interface to make an edit to a TestStand file undoable if the
 [UndoItemCreator](undoitemcreator.html)
 does not provide enough functionality to undo an edit. To do this, create a COM object that implements the
 UndoItem2
 interface and send an instance of the object to the sequence editor using a
 UIMsg_PushUndoItem
 UI Message.

Note

#### Properties

| LookupStrings (Read Only) |
| --- |
| TopObjects (Read Only) |

#### See Also

[UndoItem.EditedFile](undoitem-editedfile.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItemCreator](undoitemcreator.html)

[UndoItem](undoitem.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-beginbatchedit.html language=enus -->
## TOPIC 02988: UndoItemCreator.BeginBatchEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-beginbatchedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-beginbatchedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.BeginBatchEdit( objs) Purpose Call this method before you modify a batch of TestStand objects. Remarks Instead of calling this method and the UndoItemCreator.EndBatchEdit method, you could call the UndoItemCreator.BeginEditEx and UndoItemCreator.EndEdit methods once for every

### UndoItemCreator.BeginBatchEdit

#### Syntax

[UndoItemCreator](undoitemcreator.html).BeginBatchEdit( objs)

#### Purpose

Call this method before you modify a batch of TestStand objects.

#### Remarks

Instead of calling this method and the
 [UndoItemCreator.EndBatchEdit](undoitemcreator-endbatchedit.html)
 method, you could call the
 [UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)
 and
 [UndoItemCreator.EndEdit](undoitemcreator-endedit.html)
 methods once for every object you pass to this method. However, it is somewhat more efficient to insert, delete, and move steps using the
 UndoItemCreator.BeginBatchEdit
 and
 UndoItemCreator.EndBatchEdit
 methods.

#### Parameters

objs
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies the objects you are about to modify. The objects you pass depend on which EditKinds you passed to the
 [Engine.NewUndoItemCreator](engine-newundoitemcreator.html)
 method. Because you pass the same object to this method as you would pass to the
 UndoItemCreator.BeginEdit
 method, see the
 UndoItemCreator.BeginEdit
 method for more information about which objects to pass to this method.

#### See Also

[Engine.NewUndoItemCreator](engine-newundoitemcreator.html)

[UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)

[UndoItemCreator.EndBatchEdit](undoitemcreator-endbatchedit.html)

[UndoItemCreator.EndEdit](undoitemcreator-endedit.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-beginedit.html language=enus -->
## TOPIC 02989: UndoItemCreator.BeginEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-beginedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-beginedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.BeginEdit( obj) Purpose This method is obsolete. Use the UndoItemCreator.BeginEditEx method instead. Remarks Call this method before you modify a TestStand object. Parameters obj As PropertyObject [In] Specifies the object you are about to edit. The object you pass depends on

### UndoItemCreator.BeginEdit

#### Syntax

[UndoItemCreator](undoitemcreator.html).BeginEdit( obj)

#### Purpose

Note

UndoItemCreator.BeginEditEx

#### Remarks

Call this method before you modify a TestStand object.

#### Parameters

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the object you are about to edit. The object you pass depends on which
 [EditKinds](editkinds.html)
 you passed to the
 [Engine.NewUndoItemCreator](engine-newundoitemcreator.html)
 method. For each of the following EditKinds, pass the specified object.

- EditKind_ChangeNumericFormat 
 –Pass the property object with the numeric format you are changing to this method.
- EditKind_ChangeObject 
 –Pass the object you are modifying to this method. For this EditKind, an UndoItemCreator creates an undo item that restores all subproperties of the property object you pass in.
- EditKind_ChangeRunMode 
 –Pass the step you are changing the run mode of to this method. Call
 Step.SetRunModeEx 
 to change the run mode of a step.
- EditKind_ChangeSequenceFileProperties 
 –Pass the sequence file you are modifying through the Sequence File Properties Dialog Box to this method.
- EditKind_ChangeSequenceProperties 
 –Pass the sequence you are modifying through the Sequence Properties Dialog Box to this method.
- EditKind_ChangeStep 
 –Pass the step with the properties you are changing to this method. For example, you could pass a step you are modifying through the Step Properties Dialog Box to this method.
- EditKind_ChangeValue 
 –Pass the property object with the value you are changing to this method. Call a
 PropertyObject.SetVal 
 method to change the value of a property object.
- EditKind_DeleteProperty 
 –Pass the property object you are deleting to this method. Call the
 PropertyObject.DeleteSubProperty 
 method to delete a property object.
- EditKind_DeleteSequence 
 –Pass the sequence you are deleting to this method. Call the
 SequenceFile.DeleteSequence 
 or
 SequenceFile.RemoveSequence 
 method to delete a sequence.
- EditKind_DeleteStep 
 –Pass the step you are deleting to this method. Call the
 Sequence.DeleteStep 
 method to delete a step.
- EditKind_InsertProperty 
 –Pass the property object you are inserting to this method. Call the
 PropertyObject.InsertSubProperty 
 method to insert a property object.
- EditKind_InsertSequence 
 –Pass the sequence you are inserting to this method. Call the
 SequenceFile.InsertSequenceEx 
 method to insert a sequence.
- EditKind_InsertStep 
 –Pass the step you are inserting to this method. Call the
 Sequence.InsertStep 
 method to insert a step.
- EditKind_InsertType 
 –Pass the type you are inserting to this method. Call the
 TypeUsageList.InsertType 
 method to insert a type.
- EditKind_ModifyComment 
 –Pass the property object with the comment you are changing to this method.
- EditKind_ModifyFlags 
 –Pass the property object with the flags you are changing to this method.
- EditKind_MoveProperty 
 –Pass the property object you are moving to this method. Call the
 PropertyObject.DeleteSubProperty 
 method and then the
 PropertyObject.InsertSubProperty 
 method to move a property object.
- EditKind_MoveSequence 
 –Pass the sequence you are moving to this method. Call the
 SequenceFile.DeleteSequence 
 or
 SequenceFile.RemoveSequence 
 method and then the
 SequenceFile.InsertSequenceEx 
 method to move a sequence.
- EditKind_MoveStep 
 –Pass the step you are moving to this method. Call the
 Sequence.DeleteStep 
 method and then the
 Sequence.InsertStep 
 method to move a step.
- EditKind_Rename 
 –Pass the property object you are renaming to this method.
- EditKind_ReplaceProperty 
 –Pass the property object you are replacing to this method. Call the
 PropertyObject.SetPropertyObject 
 method to replace a property object.

#### See Also

[EditKinds](editkinds.html)

[Engine.NewUndoItemCreator](engine-newundoitemcreator.html)

[PropertyObject](propertyobject.html)

[PropertyObject.DeleteSubProperty](propertyobject-deletesubproperty.html)

[PropertyObject.InsertSubProperty](propertyobject-insertsubproperty.html)

[PropertyObject.SetPropertyObject](propertyobject-setpropertyobject.html)

[Sequence File Properties dialog box](../tsref/sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](../tsref/sequence-properties-dialog-box.html)

[Sequence.DeleteStep](sequence-deletestep.html)

[Sequence.InsertStep](sequence-insertstep.html)

[SequenceFile.DeleteSequence](sequencefile-deletesequence.html)

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

[TypeUsageList.InsertType](typeusagelist-inserttype.html)

[UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)

[UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)

[UndoItemCreator.EndEdit](undoitemcreator-endedit.html)

Parent topic:

Obsolete UndoItemCreator Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-begineditex.html language=enus -->
## TOPIC 02990: UndoItemCreator.BeginEditEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-begineditex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-begineditex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.BeginEditEx( obj, lookupString) Purpose Call this method before you modify a TestStand object. Remarks The object you specify with the obj and lookupString parameters depends on which EditKinds enumeration value you passed to the Engine.NewUndoItemCreator method. For each of t

### UndoItemCreator.BeginEditEx

#### Syntax

[UndoItemCreator](undoitemcreator.html).BeginEditEx( obj, lookupString)

#### Purpose

Call this method before you modify a TestStand object.

#### Remarks

The object you specify with the
 obj
 and
 lookupString
 parameters depends on which
 [EditKinds](editkinds.html)
 enumeration value you passed to the
 [Engine.NewUndoItemCreator](engine-newundoitemcreator.html)
 method. For each of the following EditKinds enumeration values, pass the specified object.

- EditKind_ChangeNumericFormat 
 –Pass the property object with the numeric format you are changing to this method.
- EditKind_ChangeObject 
 –Pass the object you are modifying to this method. For this EditKind, an UndoItemCreator creates an undo item that restores all subproperties of the property object you pass in.
- EditKind_ChangeRunMode 
 –Pass the step you are changing the run mode of to this method. Call
 Step.SetRunModeEx 
 to change the run mode of a step.
- EditKind_ChangeSequenceFileProperties 
 –Pass the sequence file you are modifying through the Sequence File Properties Dialog Box to this method.
- EditKind_ChangeSequenceProperties 
 –Pass the sequence you are modifying through the Sequence Properties Dialog Box to this method.
- EditKind_ChangeStep 
 –Pass the step with the properties you are changing to this method. For example, you could pass a step you are modifying through the Step Properties Dialog Box to this method.
- EditKind_ChangeValue 
 –Pass the property object with the value you are changing to this method. Call a
 PropertyObject.SetVal 
 method to change the value of a property object.
- EditKind_DeleteProperty 
 –Pass the property object you are deleting to this method. Call the
 PropertyObject.DeleteSubProperty 
 method to delete a property object.
- EditKind_DeleteSequence 
 –Pass the sequence you are deleting to this method. Call the
 SequenceFile.DeleteSequence 
 or
 SequenceFile.RemoveSequence 
 method to delete a sequence.
- EditKind_DeleteStep 
 –Pass the step you are deleting to this method. Call the
 Sequence.DeleteStep 
 method to delete a step.
- EditKind_InsertProperty 
 –Pass the property object you are inserting to this method. Call the
 PropertyObject.InsertSubProperty 
 method to insert a property object.
- EditKind_InsertSequence 
 –Pass the sequence you are inserting to this method. Call the
 SequenceFile.InsertSequenceEx 
 method to insert a sequence.
- EditKind_InsertStep 
 –Pass the step you are inserting to this method. Call the
 Sequence.InsertStep 
 method to insert a step.
- EditKind_InsertType 
 –Pass the type you are inserting to this method. Call the
 TypeUsageList.InsertType 
 method to insert a type.
- EditKind_ModifyComment 
 –Pass the property object with the comment you are changing to this method.
- EditKind_ModifyFlags 
 –Pass the property object with the flags you are changing to this method.
- EditKind_MoveProperty 
 –Pass the property object you are moving to this method. Call the
 PropertyObject.DeleteSubProperty 
 method and then the
 PropertyObject.InsertSubProperty 
 method to move a property object.
- EditKind_MoveSequence 
 –Pass the sequence you are moving to this method. Call the
 SequenceFile.DeleteSequence 
 or
 SequenceFile.RemoveSequence 
 method and then the
 SequenceFile.InsertSequenceEx 
 method to move a sequence.
- EditKind_MoveStep 
 –Pass the step you are moving to this method. Call the
 Sequence.DeleteStep 
 method and then the
 Sequence.InsertStep 
 method to move a step.
- EditKind_Rename 
 –Pass the property object you are renaming to this method.
- EditKind_ReplaceProperty 
 –Pass the property object you are replacing to this method. Call the
 PropertyObject.SetPropertyObject 
 method to replace a property object.

#### Parameters

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an object that contains the location the
 lookupString
 parameter specifies. If you are modifying an element of an array object, pass the array object or an object that contains the array object.

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Pass an empty string to denote the obj parameter, or pass the
 [name of a subproperty](/csh?context=ts_tsapiref_api_lookupstring)
 within
 obj
 for the object you are modifying or the array index if
 obj
 is an array object. Array index strings are a list of numbers, enclosed in brackets, that index each dimension of the array. For example,
 [0][1]
 is an array index for a two-dimensional array.

#### See Also

[EditKinds](editkinds.html)

[Engine.NewUndoItemCreator](engine-newundoitemcreator.html)

[PropertyObject](propertyobject.html)

[PropertyObject.DeleteSubProperty](propertyobject-deletesubproperty.html)

[PropertyObject.InsertSubProperty](propertyobject-insertsubproperty.html)

[PropertyObject.SetPropertyObject](propertyobject-setpropertyobject.html)

[Sequence File Properties dialog box](../tsref/sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](../tsref/sequence-properties-dialog-box.html)

[Sequence.DeleteStep](sequence-deletestep.html)

[Sequence.InsertStep](sequence-insertstep.html)

[SequenceFile.DeleteSequence](sequencefile-deletesequence.html)

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

[TypeUsageList.InsertType](typeusagelist-inserttype.html)

[UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)

[UndoItemCreator.EndEdit](undoitemcreator-endedit.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-createandpostundoitem.html language=enus -->
## TOPIC 02991: UndoItemCreator.CreateAndPostUndoItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-createandpostundoitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-createandpostundoitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.CreateAndPostUndoItem( options = 0, locationsApplicationSite = ApplicationSite_DefaultSite, [locationsUserData]) Return Value UndoItem Purpose Call this method to create an undo item that can undo and redo edits. This method sends the undo item to the sequence editor using a s

### UndoItemCreator.CreateAndPostUndoItem

#### Syntax

[UndoItemCreator](undoitemcreator.html).CreateAndPostUndoItem( options = 0, locationsApplicationSite = ApplicationSite_DefaultSite, [locationsUserData])

#### Return Value

[UndoItem](undoitem.html)

#### Purpose

Call this method to create an undo item that can undo and redo edits. This method sends the undo item to the sequence editor using a synchronous
 UIMsg_PushUndoItem
 user interface message and then returns the created undo item.

#### Remarks

Do not call this method if the
 [UndoItemCreator.HaveEditsBeenMade](undoitemcreator-haveeditsbeenmade.html)
 property is
 False
 . You also need to increment the change count of the edited file before calling this method.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of
 [CreateUndoItemOptions](createundoitemoptions.html)
 .

This parameter has a default value of
 0
 .

locationsApplicationSite
 As
 [ApplicationSites](applicationsites.html)

[In] Specifies the value of the
 [Locations.ApplicationSite](locations-applicationsite.html)
 properties of the undo item this method creates.

This parameter has a default value of
 ApplicationSite_DefaultSite
 .

locationsUserData
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the value of the
 [Locations.UserData](locations-userdata.html)
 properties of the undo item this method creates.

#### See Also

[ApplicationSites](applicationsites.html)

[CreateUndoItemOptions](createundoitemoptions.html)

[Locations.ApplicationSite](locations-applicationsite.html)

[Locations.UserData](locations-userdata.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObjectFile.IncChangeCount](propertyobjectfile-incchangecount.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItem](undoitem.html)

[UndoItemCreator.HaveEditsBeenMade](undoitemcreator-haveeditsbeenmade.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-endbatchedit.html language=enus -->
## TOPIC 02992: UndoItemCreator.EndBatchEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-endbatchedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-endbatchedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.EndBatchEdit Purpose Call this method after you modify a batch of TestStand objects. See Also UndoItemCreator.BeginBatchEdit UndoItemCreator.EndEdit

### UndoItemCreator.EndBatchEdit

#### Syntax

[UndoItemCreator](undoitemcreator.html).EndBatchEdit

#### Purpose

Call this method after you modify a batch of TestStand objects.

#### See Also

[UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)

[UndoItemCreator.EndEdit](undoitemcreator-endedit.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-endedit.html language=enus -->
## TOPIC 02993: UndoItemCreator.EndEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-endedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-endedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.EndEdit Purpose Call this method after you modify a TestStand object. See Also UndoItemCreator.BeginEditEx

### UndoItemCreator.EndEdit

#### Syntax

[UndoItemCreator](undoitemcreator.html).EndEdit

#### Purpose

Call this method after you modify a TestStand object.

#### See Also

[UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator-haveeditsbeenmade.html language=enus -->
## TOPIC 02994: UndoItemCreator.HaveEditsBeenMade

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator-haveeditsbeenmade.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator-haveeditsbeenmade.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItemCreator.HaveEditsBeenMade Data Type Boolean Purpose This property is True if you modify a TestStand object between calls to the UndoItemCreator.BeginEdit method and UndoItemCreator.EndEdit method or between calls to the UndoItemCreator.BeginBatchEdit method and UndoItemCreator.EndBatc

### UndoItemCreator.HaveEditsBeenMade

#### Syntax

[UndoItemCreator](undoitemcreator.html).HaveEditsBeenMade

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

This property is
 True
 if you modify a TestStand object between calls to the
 [UndoItemCreator.BeginEdit](undoitemcreator-beginedit.html)
 method and
 [UndoItemCreator.EndEdit](undoitemcreator-endedit.html)
 method or between calls to the
 [UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)
 method and
 [UndoItemCreator.EndBatchEdit](undoitemcreator-endbatchedit.html)
 method. If this property is
 False
 , do not increment the change count of the edited file or call the
 [UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)
 method.

#### See Also

[UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)

[UndoItemCreator.BeginEdit](undoitemcreator-beginedit.html)

[UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)

[UndoItemCreator.EndBatchEdit](undoitemcreator-endbatchedit.html)

[UndoItemCreator.EndEdit](undoitemcreator-endedit.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitemcreator.html language=enus -->
## TOPIC 02995: UndoItemCreator

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitemcreator.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitemcreator.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use UndoItemCreator to make edits to TestStand files undoable. To use UndoItemCreator, first create an UndoItemCreator object using the Engine.NewUndoItemCreator method. Then call the BeginEdit method, make an edit to a TestStand object, and call the EndEdit method. You can call BeginEdit and EndEdi

### UndoItemCreator

Use UndoItemCreator to make edits to TestStand files undoable. To use UndoItemCreator, first create an UndoItemCreator object using the
 [Engine.NewUndoItemCreator](engine-newundoitemcreator.html)
 method. Then call the
 [BeginEdit](undoitemcreator-beginedit.html)
 method, make an edit to a TestStand object, and call the
 [EndEdit](undoitemcreator-endedit.html)
 method. You can call BeginEdit and EndEdit more than once to edit more than one TestStand object. Then call the
 [CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)
 method to create an undo item for all the edits you made.

#### Property

| HaveEditsBeenMade (Read Only) |
| --- |

#### Methods

| BeginBatchEdit |
| --- |
| BeginEditEx |
| CreateAndPostUndoItem |
| EndBatchEdit |
| EndEdit |

#### See Also

[BeginEdit](undoitemcreator-beginedit.html)

[CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)

[EndEdit](undoitemcreator-endedit.html)

[Engine.NewUndoItemCreator](engine-newundoitemcreator.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitems-count.html language=enus -->
## TOPIC 02996: UndoItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItems.Count Data Type Long Purpose Returns the number of items in the collection.

### UndoItems.Count

#### Syntax

[UndoItems](undoitems.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitems-item.html language=enus -->
## TOPIC 02997: UndoItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItems.Item( index) Data Type UndoItem Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Long [In] Specifies the zero-based index of the item to retrieve. See Also UndoItem UndoItems.TopItem

### UndoItems.Item

#### Syntax

[UndoItems](undoitems.html).Item( index)

#### Data Type

[UndoItem](undoitem.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[UndoItem](undoitem.html)

[UndoItems.TopItem](undoitems-topitem.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitems-remove.html language=enus -->
## TOPIC 02998: UndoItems.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitems-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitems-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItems.Remove( index) Return Value UndoItem Purpose Removes the specified item from this collection, if it exists. Parameters index As Long [In] Specifies the zero-based index of the item to remove. See Also UndoItem

### UndoItems.Remove

#### Syntax

[UndoItems](undoitems.html).Remove( index)

#### Return Value

[UndoItem](undoitem.html)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[UndoItem](undoitem.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitems-topitem.html language=enus -->
## TOPIC 02999: UndoItems.TopItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitems-topitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitems-topitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoItems.TopItem Data Type UndoItem Purpose Returns the item at the highest index in the collection. This property is NULL if the collection is empty. See Also UndoItem UndoItems.Item

### UndoItems.TopItem

#### Syntax

[UndoItems](undoitems.html).TopItem

#### Data Type

[UndoItem](undoitem.html)

#### Purpose

Returns the item at the highest index in the collection. This property is
 NULL
 if the collection is empty.

#### See Also

[UndoItem](undoitem.html)

[UndoItems.Item](undoitems-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undoitems.html language=enus -->
## TOPIC 03000: UndoItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undoitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undoitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can obtain a collection of UndoItem objects from the UndoStack.UndoItems property. Properties Count (Read Only) Item (Read Only) TopItem (Read Only) Method Remove See Also UndoItem UndoStack.UndoItems

### UndoItems

You can obtain a collection of
 [UndoItem](undoitem.html)
 objects from the
 [UndoStack.UndoItems](undostack-undoitems.html)
 property.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |
| TopItem (Read Only) |

#### Method

| Remove |
| --- |

#### See Also

[UndoItem](undoitem.html)

[UndoStack.UndoItems](undostack-undoitems.html)

Parent topic:

TestStand API Reference
