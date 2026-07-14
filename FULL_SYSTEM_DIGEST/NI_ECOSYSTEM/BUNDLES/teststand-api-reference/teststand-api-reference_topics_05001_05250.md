# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=5001 end=5250 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-replaceexecutiononclose.html language=enus -->
## TOPIC 05001: ExecutionViewMgr.ReplaceExecutionOnClose

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-replaceexecutiononclose.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-replaceexecutiononclose.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ReplaceExecutionOnClose Data Type Boolean Purpose When this property is True , closing the selected execution replaces the closed execution with another execution not displayed in any other ExecutionView Manager control. Otherwise, the selected execution becomes NULL . See Al

### ExecutionViewMgr.ReplaceExecutionOnClose

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ReplaceExecutionOnClose

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , closing the selected execution replaces the closed execution with another execution not displayed in any other ExecutionView Manager control. Otherwise, the selected execution becomes
 NULL
 .

#### See Also

[ApplicationMgr.CloseExecution](applicationmgr-closeexecution.html)

[ExecutionViewMgr.Execution](executionviewmgr-execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-restartexecution.html language=enus -->
## TOPIC 05002: ExecutionViewMgr.RestartExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-restartexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-restartexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.RestartExecution Purpose Restarts the stopped execution. See Also CommandKind_Restart CommandKind_TerminateRestart ExecutionViewMgr.AbortExecution ExecutionViewMgr.RunState ExecutionViewMgr.TerminateExecution

### ExecutionViewMgr.RestartExecution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).RestartExecution

#### Purpose

Restarts the stopped execution.

#### See Also

[CommandKind_Restart](commandkinds.html)

[CommandKind_TerminateRestart](commandkinds.html)

[ExecutionViewMgr.AbortExecution](executionviewmgr-abortexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

[ExecutionViewMgr.TerminateExecution](executionviewmgr-terminateexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-resumeexecution.html language=enus -->
## TOPIC 05003: ExecutionViewMgr.ResumeExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-resumeexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-resumeexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ResumeExecution Purpose Resumes the paused execution. See Also CommandKind_BreakResume CommandKind_Resume ExecutionViewMgr.Break ExecutionViewMgr.RunState

### ExecutionViewMgr.ResumeExecution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ResumeExecution

#### Purpose

Resumes the paused execution.

#### See Also

[CommandKind_BreakResume](commandkinds.html)

[CommandKind_Resume](commandkinds.html)

[ExecutionViewMgr.Break](executionviewmgr-break.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-runselectedsteps.html language=enus -->
## TOPIC 05004: ExecutionViewMgr.RunSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-runselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-runselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.RunSelectedSteps( [interArgs]) Purpose Interactively executes the selected steps within the current execution. Remarks You can call this method only when the execution is paused and the execution is not in interactive mode. Parameters interArgs As Variant [In] [ Optional ] Sp

### ExecutionViewMgr.RunSelectedSteps

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).RunSelectedSteps( [interArgs])

#### Purpose

Interactively executes the selected steps within the current execution.

#### Remarks

Note

#### Parameters

interArgs
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies an
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 object. When you do not pass
 InteractiveArgs
 objects, the ExecutionView Manager control creates the appropriate
 InteractiveArgs
 objects.

#### See Also

[CommandKind_RunSelectedSteps](commandkinds.html)

[ExecutionViewMgr.BuildInteractiveArgs](executionviewmgr-buildinteractiveargs.html)

[ExecutionViewMgr.LoopOnSelectedSteps](executionviewmgr-looponselectedsteps.html)

[InteractiveArgs](../tsapiref/interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-runstate.html language=enus -->
## TOPIC 05005: ExecutionViewMgr.RunState

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-runstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-runstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.RunState Data Type ExecutionRunStates Use the following constants with this data type: ExecRunState_Paused –(Value: 2) The execution is suspended. ExecRunState_Running –(Value: 1) The execution is running. ExecRunState_Stopped –(Value: 3) The execution has finished executing.

### ExecutionViewMgr.RunState

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).RunState

#### Data Type

[ExecutionRunStates](../tsapiref/executionrunstates.html)

Use the following constants with this data type:

- ExecRunState_Paused 
 –(Value: 2) The execution is suspended.
- ExecRunState_Running 
 –(Value: 1) The execution is running.
- ExecRunState_Stopped 
 –(Value: 3) The execution has finished executing.

#### Purpose

Returns the run state of the execution.

#### Remarks

The ExecutionView Manager control generates the
 [ExecutionViewMgr.RunStateChanged](executionviewmgr-runstatechanged.html)
 event when this property changes. The value this property obtains does not necessarily correspond to the value the
 
 [Execution.GetStates](../tsapiref/execution-getstates.html)
 method obtains. The
 Execution.GetStates
 method returns the instantaneous state of the execution, while the
 ExecutionViewMgr.RunState
 property returns the current state the ExecutionView Manager control displays.

Note

ExecutionViewMgr.RunState

ExecutionViewMgr.TerminationState

Execution.GetStates

ExecutionViewMgr.RunState

ExecutionViewMgr.TerminationState

ExecutionViewMgr.RunState

ExecutionViewMgr.TerminationState

#### See Also

[ApplicationMgr.GetRunState](applicationmgr-getrunstate.html)

[Execution.GetStates](../tsapiref/execution-getstates.html)

[ExecutionViewMgr.RunStateChanged](executionviewmgr-runstatechanged.html)

[ExecutionViewMgr.TerminationState](executionviewmgr-terminationstate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-runstatechanged.html language=enus -->
## TOPIC 05006: ExecutionViewMgr.RunStateChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-runstatechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-runstatechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_RunStateChanged( newRunState) Applies To ExecutionViewMgr Purpose Occurs when the run state of the execution changes or when the execution changes and the new execution has a different run state. Parameters newRunState As ExecutionRunStates [In] Specifies the new run state of the

### ExecutionViewMgr.RunStateChanged

#### Syntax

ControlName_RunStateChanged( newRunState)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the run state of the execution changes or when the execution changes and the new execution has a different run state.

#### Parameters

newRunState
 As
 
 [ExecutionRunStates](../tsapiref/executionrunstates.html)

[In] Specifies the new run state of the execution.

#### See Also

[ExecutionViewMgr.EndExecution](executionviewmgr-endexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-selectedpropertyobjects.html language=enus -->
## TOPIC 05007: ExecutionViewMgr.SelectedPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-selectedpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-selectedpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.SelectedPropertyObjects Data Type SelectedPropertyObjects Purpose Returns a collection of selected property objects. Remarks Use this collection to obtain the selected property objects or change the selected property objects for the selected execution. TestStand User Interfac

### ExecutionViewMgr.SelectedPropertyObjects

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).SelectedPropertyObjects

#### Data Type

[SelectedPropertyObjects](selectedpropertyobjects.html)

#### Purpose

Returns a collection of selected property objects.

#### Remarks

Use this collection to obtain the selected property objects or change the selected property objects for the selected execution. TestStand User Interface Controls connected to an
 [ExecutionView Manager](executionviewmgr.html)
 control, such as the
 [VariablesView](variablesview.html)
 control, automatically set this property when you select variables and properties. The ExecutionView Manager control also generates a
 [ExecutionViewMgr.PropertyObjectSelectionChanged](executionviewmgr-propertyobjectselectionchang.html)
 event when this property changes.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.PropertyObjectSelectionChanged](executionviewmgr-propertyobjectselectionchang.html)

[SelectedPropertyObjects](selectedpropertyobjects.html)

[VariablesView](variablesview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-selectedsteps.html language=enus -->
## TOPIC 05008: ExecutionViewMgr.SelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-selectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-selectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.SelectedSteps Data Type SelectedSteps Purpose Returns the collection of selected steps. Remarks Use this collection to obtain the selected steps or to change the selected steps. TestStand User Interface Controls connected to an ExecutionView Manager control, such as the Seque

### ExecutionViewMgr.SelectedSteps

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).SelectedSteps

#### Data Type

[SelectedSteps](selectedsteps.html)

#### Purpose

Returns the collection of selected steps.

#### Remarks

Use this collection to obtain the selected steps or to change the selected steps. TestStand User Interface Controls connected to an
 [ExecutionView Manager](executionviewmgr.html)
 control, such as the
 [SequenceView](sequenceview.html)
 control, automatically set this property when you select steps. The ExecutionView Manager control also generates the
 [ExecutionViewMgr.SelectionChanged](executionviewmgr-selectionchanged.html)
 event when this property changes.

Note

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.SelectionChanged](executionviewmgr-selectionchanged.html)

[SelectedSteps](selectedsteps.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-selectionchanged.html language=enus -->
## TOPIC 05009: ExecutionViewMgr.SelectionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-selectionchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-selectionchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SelectionChanged Applies To ExecutionViewMgr Purpose Occurs when the set of selected steps changes. See Also ExecutionViewMgr.SelectedSteps

### ExecutionViewMgr.SelectionChanged

#### Syntax

ControlName_SelectionChanged

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the set of selected steps changes.

#### See Also

[ExecutionViewMgr.SelectedSteps](executionviewmgr-selectedsteps.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-sequencecontext.html language=enus -->
## TOPIC 05010: ExecutionViewMgr.SequenceContext

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-sequencecontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-sequencecontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.SequenceContext Data Type SequenceContext Purpose Specifies the current SequenceContext of the ExecutionView Manager control. Remarks The ExecutionView Manager control automatically sets this property when pausing an execution. You can read and write to this property only whe

### ExecutionViewMgr.SequenceContext

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).SequenceContext

#### Data Type

[SequenceContext](../tsapiref/sequencecontext.html)

#### Purpose

Specifies the current SequenceContext of the
 [ExecutionView Manager](executionviewmgr.html)
 control.

#### Remarks

The ExecutionView Manager control automatically sets this property when pausing an execution.

Note

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[SequenceContext](../tsapiref/sequencecontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-stepgroupmode.html language=enus -->
## TOPIC 05011: ExecutionViewMgr.StepGroupMode

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-stepgroupmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-stepgroupmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.StepGroupMode Data Type StepGroupModes Use the following constants with this data type: StepGroupMode_AllGroups –(Value: 2) Displays the Setup, Main, and Cleanup step groups. StepGroupMode_OneGroup –(Value: 1) Displays only one step group. Purpose Specifies whether the Sequen

### ExecutionViewMgr.StepGroupMode

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).StepGroupMode

#### Data Type

[StepGroupModes](stepgroupmodes.html)

Use the following constants with this data type:

- StepGroupMode_AllGroups 
 –(Value: 2) Displays the Setup, Main, and Cleanup step groups.
- StepGroupMode_OneGroup 
 –(Value: 1) Displays only one step group.

#### Purpose

Specifies whether the
 [SequenceView](sequenceview.html)
 controls that connect to the
 [ExecutionView Manager](executionviewmgr.html)
 control display steps in all the step groups or only steps in the current step group.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-terminateexecution.html language=enus -->
## TOPIC 05012: ExecutionViewMgr.TerminateExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-terminateexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-terminateexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.TerminateExecution Purpose Terminates the current execution if it is running. Remarks The ExecutionView Manager control generates the ExecutionViewMgr.TerminationStateChanged event after calling this method and the ExecutionViewMgr.EndExecution event when the execution has en

### ExecutionViewMgr.TerminateExecution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).TerminateExecution

#### Purpose

Terminates the current execution if it is running.

#### Remarks

The ExecutionView Manager control generates the
 [ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)
 event after calling this method and the
 [ExecutionViewMgr.EndExecution](executionviewmgr-endexecution.html)
 event when the execution has ended.

#### See Also

[CommandKind_Terminate](commandkinds.html)

[CommandKind_TerminateRestart](commandkinds.html)

[ExecutionViewMgr.EndExecution](executionviewmgr-endexecution.html)

[ExecutionViewMgr.RestartExecution](executionviewmgr-restartexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

[ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-terminationstate.html language=enus -->
## TOPIC 05013: ExecutionViewMgr.TerminationState

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-terminationstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-terminationstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.TerminationState Data Type ExecutionTerminationStates Use the following constants with this data type: ExecTermState_Aborting –(Value: 4) TestStand is aborting the running execution. ExecTermState_KillingThreads –(Value: 5) TestStand is ending the threads in the execution. Ex

### ExecutionViewMgr.TerminationState

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).TerminationState

#### Data Type

[ExecutionTerminationStates](../tsapiref/executionterminationstates.html)

Use the following constants with this data type:

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

#### Purpose

Returns the termination state of the execution.

#### Remarks

The ExecutionView Manager control generates the
 [ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)
 event when this property changes. The value obtained from this property does not necessarily correspond to the value obtained from the
 
 [Execution.GetStates](../tsapiref/execution-getstates.html)
 method. The
 Execution.GetStates
 method returns the instantaneous state of the execution, while the
 [ExecutionViewMgr.RunState](executionviewmgr-runstate.html)
 property returns the current state the ExecutionView Manager control displays.

Note

ExecutionViewMgr.RunState

ExecutionViewMgr.TerminationState

Execution.GetStates

#### See Also

[ApplicationMgr.GetTerminationState](applicationmgr-getterminationstate.html)

[Execution.GetStates](../tsapiref/execution-getstates.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

[ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-terminationstatechanged.html language=enus -->
## TOPIC 05014: ExecutionViewMgr.TerminationStateChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-terminationstatechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-terminationstatechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_TerminationStateChanged( newTermState) Applies To ExecutionViewMgr Purpose Occurs when the termination state for the execution changes or when the execution changes and the new execution has a different termination state. Parameters newTermState As ExecutionTerminationStates [In]

### ExecutionViewMgr.TerminationStateChanged

#### Syntax

ControlName_TerminationStateChanged( newTermState)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the termination state for the execution changes or when the execution changes and the new execution has a different termination state.

#### Parameters

newTermState
 As
 
 [ExecutionTerminationStates](../tsapiref/executionterminationstates.html)

[In] Specifies the new termination state of the execution.

#### See Also

[ExecutionViewMgr.TerminationState](executionviewmgr-terminationstate.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-thread.html language=enus -->
## TOPIC 05015: ExecutionViewMgr.Thread

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-thread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-thread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.Thread Data Type Thread Purpose Specifies the foreground thread of the selected execution. Remarks You can read or write to this property only when the selected execution is paused. When you write to this property, the thread must belong to the selected execution. Although yo

### ExecutionViewMgr.Thread

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).Thread

#### Data Type

[Thread](../tsapiref/thread.html)

#### Purpose

Specifies the foreground thread of the selected execution.

#### Remarks

Note

Note

#### See Also

[Thread](../tsapiref/thread.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-threadchanged.html language=enus -->
## TOPIC 05016: ExecutionViewMgr.ThreadChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-threadchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-threadchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ThreadChanged( thrd) Applies To ExecutionViewMgr Purpose Occurs when the ExecutionViewMgr.Thread property changes programmatically or when a control connected to a ThreadListConnection changes the property. Parameters thrd As Thread [In] Specifies the current foreground thread of

### ExecutionViewMgr.ThreadChanged

#### Syntax

ControlName_ThreadChanged( thrd)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the
 [ExecutionViewMgr.Thread](executionviewmgr-thread.html)
 property changes programmatically or when a control connected to a
 [ThreadListConnection](threadlistconnection.html)
 changes the property.

#### Parameters

thrd
 As
 
 [Thread](../tsapiref/thread.html)

[In] Specifies the current foreground thread of the execution in the ExecutionView Manager control.

#### See Also

[ExecutionViewMgr.Thread](executionviewmgr-thread.html)

[ThreadListConnection](threadlistconnection.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-trace.html language=enus -->
## TOPIC 05017: ExecutionViewMgr.Trace

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-trace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-trace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Trace( exec, thrd, ctxt) Applies To ExecutionViewMgr Purpose Occurs when the execution sends a UIMsg_Trace message. Parameters exec As Execution [In] Specifies the current execution. thrd As Thread [In] Specifies the current thread. ctxt As SequenceContext [In] Specifies the curre

### ExecutionViewMgr.Trace

#### Syntax

ControlName_Trace( exec, thrd, ctxt)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the execution sends a
 UIMsg_Trace
 message.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the current execution.

thrd
 As
 
 [Thread](../tsapiref/thread.html)

[In] Specifies the current thread.

ctxt
 As
 
 [SequenceContext](../tsapiref/sequencecontext.html)

[In] Specifies the current context.

#### See Also

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-userdata.html language=enus -->
## TOPIC 05018: ExecutionViewMgr.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.UserData Data Type Variant Purpose Stores data associated with this control. Remarks Stored data is cleared during the shutdown process.

### ExecutionViewMgr.UserData

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).UserData

#### Data Type

[Variant](data-types-for-teststand-user-interface.html)

#### Purpose

Stores data associated with this control.

#### Remarks

Stored data is cleared during the shutdown process.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-usermessage.html language=enus -->
## TOPIC 05019: ExecutionViewMgr.UserMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-usermessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-usermessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_UserMessage( uiMsg) Applies To ExecutionViewMgr Purpose Occurs when the execution sends a user message. Remarks User messages are messages with codes that are greater than or equal to UIMsg_UserMessageBase . The ExecutionView Manager control automatically acknowledges the user mes

### ExecutionViewMgr.UserMessage

#### Syntax

ControlName_UserMessage( uiMsg)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the execution sends a user message.

#### Remarks

User messages are messages with codes that are greater than or equal to
 UIMsg_UserMessageBase
 .

The ExecutionView Manager control automatically acknowledges the user message when this event completes. Therefore, you do not have to directly call the
 
 [UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)
 method from within this event.

#### Parameters

uiMsg
 As
 
 [UIMessage](../tsapiref/uimessage.html)

[In] Specifies the user-defined UIMessage object.

#### See Also

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr.html language=enus -->
## TOPIC 05020: ExecutionViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An ExecutionView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected TestStand execution: Designates an execution as the selected execution. Tracks which thread, stack frame, sequence, step group, and steps

### ExecutionViewMgr

An ExecutionView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected TestStand execution:

- Designates an execution as the selected execution.
- Tracks which thread, stack frame, sequence, step group, and steps are selected in the selected execution.
- Displays aspects of the selected execution in the visible TestStand UI Controls to which the control connects.
- Enables visible TestStand UI Controls to which the control connects to change the selected thread, stack frame, sequence, step group, and steps.
- Generates events to notify the application of the progress and state of the selected execution.
- Provides debugging commands.
- Updates the
 ReportView 
 control to show the current report for the selected execution.

An application must have one ExecutionView Manager control for each location, such as a window, form, or panel, in which you display an execution or let the user select a current execution.

#### Properties

| ApplicationMgr (Read Only) |
| --- |
| ConfigurationEntryPoints (Read Only) |
| Connections (Read Only) |
| Execution |
| ExecutionEntryPoints (Read Only) |
| ReplaceExecutionOnClose |
| RunState (Read Only) |
| SelectedPropertyObjects (Read Only) |
| SelectedSteps (Read Only) |
| SequenceContext |
| StepGroupMode |
| TerminationState (Read Only) |
| Thread |
| UserData |

#### Methods

| AbortExecution |
| --- |
| BreakExecution |
| BuildEditArgs |
| BuildInteractiveArgs |
| ConnectCallStack |
| ConnectCaption |
| ConnectCommand |
| ConnectExecutionList |
| ConnectExecutionView |
| ConnectImage |
| ConnectNumeric |
| ConnectReportView |
| ConnectThreadList |
| ConnectVariables |
| GetCaptionText |
| GetCommand |
| GetImageName |
| GetNumericValue |
| LoopOnSelectedSteps |
| NewEditContext |
| Refresh |
| RefreshStep |
| RefreshStepEx |
| RestartExecution |
| ResumeExecution |
| RunSelectedSteps |
| TerminateExecution |

#### Events

| Break |
| --- |
| ContextChanged |
| DisplayReport |
| EndExecution |
| ExecutionChanged |
| PropertyObjectSelectionChanged |
| RefreshWindow |
| RunStateChanged |
| SelectionChanged |
| TerminationStateChanged |
| ThreadChanged |
| Trace |
| UserMessage |

#### See Also

[ReportView](reportview.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-callstack.html language=enus -->
## TOPIC 05021: ExecutionViewMgrConnections.CallStack

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-callstack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-callstack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.CallStack Data Type CallStackConnections Purpose Collection of CallStackConnection objects. See Also CallStackConnection CallStackConnections ExecutionViewMgr.ConnectCallStack

### ExecutionViewMgrConnections.CallStack

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).CallStack

#### Data Type

[CallStackConnections](callstackconnections.html)

#### Purpose

Collection of
 [CallStackConnection](callstackconnection.html)
 objects.

#### See Also

[CallStackConnection](callstackconnection.html)

[CallStackConnections](callstackconnections.html)

[ExecutionViewMgr.ConnectCallStack](executionviewmgr-connectcallstack.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-caption.html language=enus -->
## TOPIC 05022: ExecutionViewMgrConnections.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.Caption Data Type CaptionConnections Purpose Collection of CaptionConnection objects. See Also CaptionConnection CaptionConnections ExecutionViewMgr.ConnectCaption

### ExecutionViewMgrConnections.Caption

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).Caption

#### Data Type

[CaptionConnections](captionconnections.html)

#### Purpose

Collection of
 [CaptionConnection](captionconnection.html)
 objects.

#### See Also

[CaptionConnection](captionconnection.html)

[CaptionConnections](captionconnections.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-command.html language=enus -->
## TOPIC 05023: ExecutionViewMgrConnections.Command

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-command.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-command.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.Command Data Type CommandConnections Purpose Collection of CommandConnection objects. See Also CommandConnection CommandConnections ExecutionViewMgr.ConnectCommand

### ExecutionViewMgrConnections.Command

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).Command

#### Data Type

[CommandConnections](commandconnections.html)

#### Purpose

Collection of
 [CommandConnection](commandconnection.html)
 objects.

#### See Also

[CommandConnection](commandconnection.html)

[CommandConnections](commandconnections.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-executionlist.html language=enus -->
## TOPIC 05024: ExecutionViewMgrConnections.ExecutionList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-executionlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-executionlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.ExecutionList Data Type ExecutionListConnections Purpose Collection of ExecutionListConnection objects. See Also ExecutionListConnection ExecutionListConnections ExecutionViewMgr.ConnectExecutionList

### ExecutionViewMgrConnections.ExecutionList

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).ExecutionList

#### Data Type

[ExecutionListConnections](executionlistconnections.html)

#### Purpose

Collection of
 [ExecutionListConnection](executionlistconnection.html)
 objects.

#### See Also

[ExecutionListConnection](executionlistconnection.html)

[ExecutionListConnections](executionlistconnections.html)

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-executionview.html language=enus -->
## TOPIC 05025: ExecutionViewMgrConnections.ExecutionView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-executionview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-executionview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.ExecutionView Data Type ExecutionViewConnections Purpose Collection of ExecutionViewConnection objects. See Also ExecutionViewConnection ExecutionViewConnections ExecutionViewMgr.ConnectExecutionView

### ExecutionViewMgrConnections.ExecutionView

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).ExecutionView

#### Data Type

[ExecutionViewConnections](executionviewconnections.html)

#### Purpose

Collection of
 [ExecutionViewConnection](executionviewconnection.html)
 objects.

#### See Also

[ExecutionViewConnection](executionviewconnection.html)

[ExecutionViewConnections](executionviewconnections.html)

[ExecutionViewMgr.ConnectExecutionView](executionviewmgr-connectexecutionview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-image.html language=enus -->
## TOPIC 05026: ExecutionViewMgrConnections.Image

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-image.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-image.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.Image Data Type ImageConnections Purpose Collection of ImageConnection objects. See Also ExecutionViewMgr.ConnectImage ImageConnection ImageConnections

### ExecutionViewMgrConnections.Image

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).Image

#### Data Type

[ImageConnections](imageconnections.html)

#### Purpose

Collection of
 [ImageConnection](imageconnection.html)
 objects.

#### See Also

[ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)

[ImageConnection](imageconnection.html)

[ImageConnections](imageconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-numeric.html language=enus -->
## TOPIC 05027: ExecutionViewMgrConnections.Numeric

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-numeric.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-numeric.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.Numeric Data Type NumericConnections Purpose Collection of NumericConnection objects. See Also ExecutionViewMgr.ConnectNumeric NumericConnection NumericConnections

### ExecutionViewMgrConnections.Numeric

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).Numeric

#### Data Type

[NumericConnections](numericconnections.html)

#### Purpose

Collection of
 [NumericConnection](numericconnection.html)
 objects.

#### See Also

[ExecutionViewMgr.ConnectNumeric](executionviewmgr-connectnumeric.html)

[NumericConnection](numericconnection.html)

[NumericConnections](numericconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-reportview.html language=enus -->
## TOPIC 05028: ExecutionViewMgrConnections.ReportView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-reportview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-reportview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.ReportView Data Type ReportViewConnections Purpose Collection of ReportViewConnection objects. See Also ExecutionViewMgr.ConnectReportView ReportViewConnection ReportViewConnections

### ExecutionViewMgrConnections.ReportView

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).ReportView

#### Data Type

[ReportViewConnections](reportviewconnections.html)

#### Purpose

Collection of
 [ReportViewConnection](reportviewconnection.html)
 objects.

#### See Also

[ExecutionViewMgr.ConnectReportView](executionviewmgr-connectreportview.html)

[ReportViewConnection](reportviewconnection.html)

[ReportViewConnections](reportviewconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-threadlist.html language=enus -->
## TOPIC 05029: ExecutionViewMgrConnections.ThreadList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-threadlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-threadlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.ThreadList Data Type ThreadListConnections Purpose Collection of ThreadListConnection objects. See Also ExecutionViewMgr.ConnectThreadList ThreadListConnection ThreadListConnections

### ExecutionViewMgrConnections.ThreadList

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).ThreadList

#### Data Type

[ThreadListConnections](threadlistconnections.html)

#### Purpose

Collection of
 [ThreadListConnection](threadlistconnection.html)
 objects.

#### See Also

[ExecutionViewMgr.ConnectThreadList](executionviewmgr-connectthreadlist.html)

[ThreadListConnection](threadlistconnection.html)

[ThreadListConnections](threadlistconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections-variables.html language=enus -->
## TOPIC 05030: ExecutionViewMgrConnections.Variables

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections-variables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgrConnections.Variables Data Type VariablesConnections Purpose Collection of VariablesConnection objects. See Also ExecutionViewMgr.ConnectVariables VariablesConnection VariablesConnections

### ExecutionViewMgrConnections.Variables

#### Syntax

[ExecutionViewMgrConnections](executionviewmgrconnections.html).Variables

#### Data Type

[VariablesConnections](variablesconnections.html)

#### Purpose

Collection of
 [VariablesConnection](variablesconnection.html)
 objects.

#### See Also

[ExecutionViewMgr.ConnectVariables](executionviewmgr-connectvariables.html)

[VariablesConnection](variablesconnection.html)

[VariablesConnections](variablesconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgrconnections.html language=enus -->
## TOPIC 05031: ExecutionViewMgrConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgrconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgrconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the connections for an ExecutionView Manager control. Properties CallStack (Read Only) Caption (Read Only) Command (Read Only) ExecutionList (Read Only) ExecutionView (Read Only) Image (Read Only) Numeric (Read Only) ReportView (Read Only) ThreadList (Read Only) Variables (Read Only) See Al

### ExecutionViewMgrConnections

Contains the connections for an
 [ExecutionView Manager](executionviewmgr.html)
 control.

#### Properties

| CallStack (Read Only) |
| --- |
| Caption (Read Only) |
| Command (Read Only) |
| ExecutionList (Read Only) |
| ExecutionView (Read Only) |
| Image (Read Only) |
| Numeric (Read Only) |
| ReportView (Read Only) |
| ThreadList (Read Only) |
| Variables (Read Only) |

#### See Also

[ApplicationMgrConnections](applicationmgrconnections.html)

[ExecutionView Manager](executionviewmgr.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewoptions.html language=enus -->
## TOPIC 05032: ExecutionViewOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the opts parameter of the ExecutionViewMgr.ConnectExecutionView method. ExecutionViewConnection_IgnoreColors –(Value: 1) The control connected to the ExecutionView Manager control does not change colors based on the execution state when this option is used. ExecutionViewConn

### ExecutionViewOptions

Use these constants with the
 opts
 parameter of the
 [ExecutionViewMgr.ConnectExecutionView](executionviewmgr-connectexecutionview.html)
 method.

- ExecutionViewConnection_IgnoreColors 
 –(Value: 1) The control connected to the ExecutionView Manager control does not change colors based on the execution state when this option is used.
- ExecutionViewConnection_NoOptions 
 –(Value: 0) No options.

#### See Also

[ExecutionViewMgr.ConnectExecutionView](executionviewmgr-connectexecutionview.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-advanced-property-page.html language=enus -->
## TOPIC 05033: ExpressionEdit Advanced Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-advanced-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-advanced-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Property Page The Advanced property page contains the following controls: Expression Browser Dialog Options —Configures the title and options parameter TestStand passes to the ExpressionEdit.DisplayBrowseExprDialog method when you call this method directly or indirectly through the Browse m

### ExpressionEdit Advanced Property Page

#### Advanced Property Page

The Advanced property page contains the following controls:

- Expression Browser Dialog Options 
 —Configures the title and options parameter TestStand passes to the
 ExpressionEdit.DisplayBrowseExprDialog 
 method when you call this method directly or indirectly through the Browse menu item in the context menu of the
 ExpressionEdit 
 control.
  - Title 
 —The title of the
 Expression Browser 
 dialog box. Pass an empty string to use the default title for the dialog box.
  - For Viewing Types 
 —The Expression Browser dialog box shows properties TestStand hides in an instance of a type.
  - Show Context Menus 
 —The list box of the Expression Browser dialog box contains a context menu for users to insert, rename, and delete items. Disable this option when you do not want users to edit the
 ExpressionEdit.Context 
 property using the Expression Browser dialog box.
  - Modal to active window 
 —The Expression Browser dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from the
 
 Engine.AppMainHwnd 
 property.
  - Modal to main application window 
 —The Expression Browser dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to enable this option.
- Max Length 
 —The maximum number of characters you can type in the
 ExpressionEdit 
 control. When you specify
 0 
 , the maximum number of characters is 64,000. You may specify a number greater than 64,000.
- Auto Localize 
 —When you enable this option, Text is a delocalized expression. When you disable this option, Text is a localized expression.
 Note 
 This option is obsolete. Use the
 [ExpressionEdit.DisplayText](expressionedit-displaytext.html)
 property instead.
- Word Wrap 
 —Allows lines too long to display on one line to wrap to the next line.
  - False 
 —Word wrap is disabled.
  - True 
 —Word wrap is enabled.
  - Use Preference 
 —The Word Wrap option in the
 Expression Editing Options 
 dialog box determines the setting. You can launch the Expression Editing Options dialog box by selecting
 Options 
 from the context menu of the
 ExpressionEdit 
 control.
- Want Return 
 —The
 ExpressionEdit 
 control processes the <Enter> key. When the
 ExpressionEdit 
 control does not process the <Enter> key, the <Enter> key goes to the default button.
  - False 
 —The <Enter> key goes to the default button.
  - True 
 —The
 ExpressionEdit 
 control processes the <Enter> key.
  - Use Preference 
 —The Want Return option in the Expression Editing Options dialog box determines the setting. You can launch the Expression Editing Options dialog box by selecting
 Options 
 from the context menu of the
 ExpressionEdit 
 control.

#### See Also

[Engine.AppMainHwnd](../tsapiref/engine-appmainhwnd.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.Context](expressionedit-context.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

[ExpressionEdit.DisplayText](expressionedit-displaytext.html)

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-allowempty.html language=enus -->
## TOPIC 05034: ExpressionEdit.AllowEmpty

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-allowempty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-allowempty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.AllowEmpty Data Type Boolean Purpose TestStand returns an error for an empty expression only when this property is False . Remarks The ExpressionEdit control displays the text "<The expression cannot be empty>" when this property is False , the control contains an empty express

### ExpressionEdit.AllowEmpty

#### Syntax

[ExpressionEdit](expressionedit.html).AllowEmpty

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

TestStand returns an error for an empty expression only when this property is
 False
 .

#### Remarks

The ExpressionEdit control displays the text
 "<The expression cannot be empty>"
 when this property is
 False
 , the control contains an empty expression, the control is not active, and error checking is enabled.

#### See Also

[EvaluationTypes](../tsapiref/evaluationtypes.html)

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-applydefaultstyle.html language=enus -->
## TOPIC 05035: ExpressionEdit.ApplyDefaultStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-applydefaultstyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-applydefaultstyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ApplyDefaultStyle Data Type Boolean Purpose Specifies whether the control uses the default style for the ExpressionEdit buttons, and sets ExpressionEdit.FontSource property to FontSource_UseUIStyleFont . Remarks TestStand 2020 introduced new default icons for the ExpressionEdit

### ExpressionEdit.ApplyDefaultStyle

#### Syntax

[ExpressionEdit](expressionedit.html).ApplyDefaultStyle

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control uses the default style for the ExpressionEdit buttons, and sets
 ExpressionEdit.FontSource
 property to
 FontSource_UseUIStyleFont
 .

#### Remarks

TestStand 2020 introduced new default icons for the ExpressionEdit buttons.

#### See Also

[ExpressionEdit.FontSource](expressionedit-fontsource.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-autocompletionhwnd.html language=enus -->
## TOPIC 05036: ExpressionEdit.AutoCompletionHwnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-autocompletionhwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-autocompletionhwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.AutoCompletionHwnd Data Type Long Purpose Returns the Window handle of the autocompletion listbox. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior. See Also Expr

### ExpressionEdit.AutoCompletionHwnd

#### Syntax

[ExpressionEdit](expressionedit.html).AutoCompletionHwnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the autocompletion listbox.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

#### See Also

[ExpressionEdit.FunctionTipHwnd](expressionedit-functiontiphwnd.html)

[ExpressionEdit.hWnd](expressionedit-hwnd.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-autolocalize.html language=enus -->
## TOPIC 05037: ExpressionEdit.AutoLocalize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-autolocalize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-autolocalize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.AutoLocalize Data Type Boolean Purpose This property is obsolete. Use ExpressionEdit.DisplayText instead. Remarks When this property is True , the ExpressionEdit.Text property is a delocalized expression. When this property is False , the ExpressionEdit.Text property is a local

### ExpressionEdit.AutoLocalize

#### Syntax

[ExpressionEdit](expressionedit.html).AutoLocalize

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Note

ExpressionEdit.DisplayText

#### Remarks

When this property is
 True
 , the
 [ExpressionEdit.Text](expressionedit-text.html)
 property is a delocalized expression. When this property is
 False
 , the
 ExpressionEdit.Text
 property is a localized expression. The default value of the property is
 True
 .

#### See Also

[ExpressionEdit.DisplayText](expressionedit-displaytext.html)

[ExpressionEdit.Text](expressionedit-text.html)

Parent topic:

Obsolete ExpressionEdit Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-automaticallyprefixvariables.html language=enus -->
## TOPIC 05038: ExpressionEdit.AutomaticallyPrefixVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-automaticallyprefixvariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-automaticallyprefixvariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.AutomaticallyPrefixVariables Data Type BooleanOrPreference Use the following constants with this data type: BooleanOrPreference_False –(Value: 0) Specifies a value of False . BooleanOrPreference_True –(Value: 1) Specifies a value of True . BooleanOrPreference_UsePreference –(Va

### ExpressionEdit.AutomaticallyPrefixVariables

#### Syntax

[ExpressionEdit](expressionedit.html).AutomaticallyPrefixVariables

#### Data Type

[BooleanOrPreference](booleanorpreference.html)

Use the following constants with this data type:

- BooleanOrPreference_False 
 –(Value: 0) Specifies a value of
 False 
 .
- BooleanOrPreference_True 
 –(Value: 1) Specifies a value of
 True 
 .
- BooleanOrPreference_UsePreference 
 –(Value: 3) Use the corresponding preference option in the
 Expression Editing Options 
 dialog box.

#### Purpose

Specifies whether the ExpressionEdit control automatically replaces variable names the user types with the full pathname of the variable.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-backcolor.html language=enus -->
## TOPIC 05039: ExpressionEdit.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.BackColor Data Type Color Purpose Specifies the background color of the ExpressionEdit control.

### ExpressionEdit.BackColor

#### Syntax

[ExpressionEdit](expressionedit.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the ExpressionEdit control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-borderdragged.html language=enus -->
## TOPIC 05040: ExpressionEdit.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To ExpressionEdit Purpose Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable bo

### ExpressionEdit.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable borders to track the mouse cursor. However, you can choose to modify the location or size to which you set the control. For example, you can limit the width of the control so the left edge cannot be dragged off the visible portion of the window.

In addition to changing the size and position of the control, you might also update the sizes and positions of the other controls on the window to account for the change.

#### Remarks

If you are using LabVIEW, you must add the Horizontal and Vertical components of the origin of the LabVIEW front panel to the
 newX
 and
 newY
 event parameter values before you can use the
 newX
 and
 newY
 event parameters to set the ActiveX Container (AxCont) Left and Top properties for the control. To obtain the origin of a LabVIEW front panel, place an ActiveX property node on the block diagram of the VI, right-click the node, and select
 Link to»Pane
 from the context menu. Right-click the node again and select
 Select Property»Origin
 .

#### Parameters

bordersChanged
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies which borders the user dragged. Refer to the
 [WhichBorders](whichborders.html)
 constants for more information about draggable borders.

newX
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new x-coordinate for the control.

newY
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new y-coordinate for the control.

newWidth
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new width for the control.

newHeight
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new height for the control.

finalResize
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the event is the final event for the drag operation the user performs.

#### See Also

[Borders](borders.html)

[WhichBorders](whichborders.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-borders-property-page.html language=enus -->
## TOPIC 05041: ExpressionEdit Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### ExpressionEdit Borders Property Page

#### Borders Property Page

The property page contains the following controls:

- Control Frame 
 —This section contains the following options:
  - Visible 
 —The control displays a thin rectangular frame that surrounds the control.
  - Frame Location 
 —The location of the frame the control displays. The Frame Location ring control contains the following options:
    - Inside Borders 
 —The frame appears within the draggable borders of the control.
    - Outside Borders 
 —The frame appears around the draggable borders of the control.
  - Frame Style 
 —The appearance of the frame the control displays. The Frame Style ring control contains the following options:
    - Flat 
 —The frame appears flat.
    - Fixed Single 
 —The frame is a black line, one pixel thick.
    - Control Edge 
 —The frame has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings.
    - Raised 
 —The frame has a raised three-dimensional appearance.
    - Inset 
 —The frame has a sunken three-dimensional appearance.
- Drag Borders 
 —This section contains the following options:
  - Top Border 
 —A border at the top edge of the control.
  - Left Border 
 —A border at the left edge of the control.
  - Bottom Border 
 —A border at the bottom edge of the control.
  - Right Border 
 —A border at the right edge of the control.
  - Enable Border Drag Events 
 —The control displays a resizing cursor over the draggable borders and that the control generates
 BorderDragged 
 events when the user drags a draggable border with the mouse.
  - Edge Style 
 —The appearance of the border edge the control displays. The Edge Style contains the following options:
    - Flat 
 —The edge appears flat.
    - Fixed Single 
 —The edge is a black line, one pixel thick.
    - Control Edge 
 —The edge has the appearance of a control edge. The appearance can vary depending on the Windows appearance settings.
    - Raised 
 —The edge has a raised, three-dimensional appearance.
    - Inset 
 —The edge has a sunken, three-dimensional appearance.
  - Width 
 —The width, in pixels, of the draggable borders the control displays.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-borders.html language=enus -->
## TOPIC 05042: ExpressionEdit.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders ExpressionEdit.BorderDragged

### ExpressionEdit.Borders

#### Syntax

[ExpressionEdit](expressionedit.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[ExpressionEdit.BorderDragged](expressionedit-borderdragged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-browseexprdialogclosed.html language=enus -->
## TOPIC 05043: ExpressionEdit.BrowseExprDialogClosed

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-browseexprdialogclosed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-browseexprdialogclosed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BrowseExprDialogClosed( userHitOK, contextModified) Applies To ExpressionEdit Purpose Occurs when you close an Expression Browser dialog box displayed using the Browse menu item in the ExpressionEdit control context menu or the ExpressionEdit.DisplayBrowseExprDialog method. Parame

### ExpressionEdit.BrowseExprDialogClosed

#### Syntax

ControlName_BrowseExprDialogClosed( userHitOK, contextModified)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when you close an
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box displayed using the Browse menu item in the ExpressionEdit control context menu or the
 [ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)
 method.

#### Parameters

userHitOK
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] This parameter is
 True
 when you click OK in the Expression Browser dialog box and
 False
 when you click Cancel.

contextModified
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] This parameter is
 True
 when a variable or property in the context is created, deleted, or renamed through the context menu in the Expression Browser dialog box while the Expression Browser dialog box is displayed. This parameter is
 False
 when the user modifies only the value of a variable or property.

#### See Also

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.BrowseExprDialogOpened](expressionedit-browseexprdialogopened.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-browseexprdialogopened.html language=enus -->
## TOPIC 05044: ExpressionEdit.BrowseExprDialogOpened

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-browseexprdialogopened.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-browseexprdialogopened.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BrowseExprDialogOpened( dlgTitle, dlgOptions, selectionStart, selectionEnd, initialVariableName, cancel) Applies To ExpressionEdit Purpose Occurs just before the ExpressionEdit control displays the Expression Browser dialog box. Use this event to override the default parameter val

### ExpressionEdit.BrowseExprDialogOpened

#### Syntax

ControlName_BrowseExprDialogOpened( dlgTitle, dlgOptions, selectionStart, selectionEnd, initialVariableName, cancel)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs just before the ExpressionEdit control displays the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box. Use this event to override the default parameter values the ExpressionEdit control passes to the Expression Browser dialog box or to cancel displaying the Expression Browser dialog box to the user.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the title of the Expression Browser dialog box. Assign a value to this parameter to override the default title.

dlgOptions
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the BrowseExprDialogOptions the ExpressionEdit control passes to the Expression Browser dialog box. Assign a value to this parameter to override the default options.

selectionStart
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the zero-based character index where selection begins. Assign a value to this parameter to override the default start of selection.

selectionEnd
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the zero-based character index where selection ends. Assign a value to this parameter to override the default end of selection.

initialVariableName
 As
 [String](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the name of the initial variable or property to show as selected in the tree view portion of the Expression Browser dialog box. Assign a value to this parameter to override the default initially selected variable. Assign an empty string to this parameter to select the first item.

cancel
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[Out] Assign
 True
 to this parameter to prevent the ExpressionEdit control from displaying the Expression Browser dialog box to the user.

#### See Also

[BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)

[Engine.DisplayBrowseExprDialogEx](../tsapiref/engine-displaybrowseexprdialogex.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEditButton](expressioneditbutton.html)

[ExpressionEdit.BrowseExprDialogClosed](expressionedit-browseexprdialogclosed.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-browseexprdialogoptions.html language=enus -->
## TOPIC 05045: ExpressionEdit.BrowseExprDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-browseexprdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-browseexprdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.BrowseExprDialogOptions Data Type Long Purpose Specifies the options in the Expression Browser dialog box when you call the ExpressionEdit.DisplayBrowseExprDialog method or when you select Browse from the context menu of the ExpressionEdit control. Use any combination of the Br

### ExpressionEdit.BrowseExprDialogOptions

#### Syntax

[ExpressionEdit](expressionedit.html).BrowseExprDialogOptions

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the options in the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box when you call the
 [ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)
 method or when you select Browse from the context menu of the ExpressionEdit control. Use any combination of the
 
 [BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)
 constants with this property.

#### Remarks

The constant
 BrowseExpr_UsesCRLF
 is ignored.

#### See Also

[BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.BrowseExprDialogTitle](expressionedit-browseexprdialogtitle.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-browseexprdialogtitle.html language=enus -->
## TOPIC 05046: ExpressionEdit.BrowseExprDialogTitle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-browseexprdialogtitle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-browseexprdialogtitle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.BrowseExprDialogTitle Data Type String Purpose Specifies the title for the Expression Browser dialog box when you call the ExpressionEdit.DisplayBrowseExprDialog method or when you select Browse in the context menu of the ExpressionEdit control. Set this property to an empty st

### ExpressionEdit.BrowseExprDialogTitle

#### Syntax

[ExpressionEdit](expressionedit.html).BrowseExprDialogTitle

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the title for the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box when you call the
 [ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)
 method or when you select Browse in the context menu of the ExpressionEdit control. Set this property to an empty string to use the default title for the dialog box.

#### See Also

[BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-buttonclick.html language=enus -->
## TOPIC 05047: ExpressionEdit.ButtonClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-buttonclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-buttonclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ButtonClick( btn) Applies To ExpressionEdit Purpose Responds to clicking on a custom button. Remarks This event does not occur when you click on a non-custom button. Parameters btn As ExpressionEditButton [In] Specifies the button the user clicked.

### ExpressionEdit.ButtonClick

#### Syntax

ControlName_ButtonClick( btn)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Responds to clicking on a custom button.

#### Remarks

This event does not occur when you click on a non-custom button.

#### Parameters

btn
 As
 [ExpressionEditButton](expressioneditbutton.html)

[In] Specifies the button the user clicked.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-buttons-property-page.html language=enus -->
## TOPIC 05048: ExpressionEdit Buttons Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-buttons-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-buttons-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Buttons Property Page The Buttons property page contains the following controls: Buttons —List of buttons in the ExpressionEdit control. Insert —Inserts a new button after the currently selected button. Remove —Deletes the currently selected button. Move Up —Moves the currently selected button up on

### ExpressionEdit Buttons Property Page

#### Buttons Property Page

The Buttons property page contains the following controls:

- Buttons 
 —List of buttons in the
 ExpressionEdit 
 control.
- Insert 
 —Inserts a new button after the currently selected button.
- Remove 
 —Deletes the currently selected button.
- Move Up 
 —Moves the currently selected button up one position.
- Move Down 
 —Moves the currently selected button down one position.
- Kind 
 —Use these options to make the currently selected button one of the following kinds:
  - Expression Browser 
 —This kind of button displays the
 Expression Browser 
 dialog box. The Icon, Enabled, Visible, and Tooltip options are set automatically for this kind of button.
  - Check Expression 
 —This kind of button displays the error message in a dialog box when the expression has an error. The Icon, Enabled, Visible, and Tooltip options are set automatically for this kind of button.
  - Custom 
 —Enable this option to define the behavior and appearance of the button. Use the
 ExpressionEdit.ButtonClick 
 event to respond to button clicks.
    - Kind 
 —Specify an ID for the custom button. Use any value starting with 1000.
- Use Icon 
 —Enable this option to make the currently selected button display a picture.
  - Browse 
 —Displays a dialog box, in which you can select a picture for the currently selected button.
- Style 
 —Use these options to specify the style of the buttons:
  - System 
 —The button looks like a standard button for the operating system.
  - Standard 
 —The button is three-dimensional.
  - Flat 
 —The button is flat.
  - Tool Bar Button 
 —This style is the same as
 System 
 except when the application supports Microsoft Windows XP themes, the button has no border when you hover over the button.
- Background Color 
 —The text background color.
- Tool Tip 
 —Specify a tooltip for the currently selected button.
- Shortcut 
 —Specify a keyboard shortcut for clicking the currently selected button when the
 ExpressionEdit 
 control is active.
- Appears In Context Menu 
 —Enable this option to create a menu item in the context menu of the
 ExpressionEdit 
 control for the currently selected button. Clicking the context menu item is equivalent to clicking the button.
  - Menu Item Caption 
 —Specify the caption of the menu item that corresponds to the currently selected button.
- Enabled 
 —Enable this option to make the currently selected button initially enabled. A disabled button does not respond to button clicks.
- Visible 
 —Enable this option to make the currently selected button initially visible.

#### See Also

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.ButtonClick](expressionedit-buttonclick.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-buttons.html language=enus -->
## TOPIC 05049: ExpressionEdit.Buttons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-buttons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-buttons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Buttons Data Type ExpressionEditButtons Purpose Returns a collection of the buttons for the ExpressionEdit control. See Also ExpressionEditButtons

### ExpressionEdit.Buttons

#### Syntax

[ExpressionEdit](expressionedit.html).Buttons

#### Data Type

[ExpressionEditButtons](expressioneditbuttons.html)

#### Purpose

Returns a collection of the buttons for the ExpressionEdit control.

#### See Also

[ExpressionEditButtons](expressioneditbuttons.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-change.html language=enus -->
## TOPIC 05050: ExpressionEdit.Change

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-change.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-change.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Change Applies To ExpressionEdit Purpose Occurs when the text in the control changes. See Also ExpressionEdit.KeyPress

### ExpressionEdit.Change

#### Syntax

ControlName_Change

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the text in the control changes.

#### See Also

[ExpressionEdit.KeyPress](expressionedit-keypress.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-checkexpression.html language=enus -->
## TOPIC 05051: ExpressionEdit.CheckExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-checkexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-checkexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CheckExpression( errorCode, errorDescription, errorStartPosition, errorEndPosition) Applies To ExpressionEdit Purpose Occurs when the control checks the expression for errors. Remarks The initial values of the event parameters indicate whether the control detected an error in the

### ExpressionEdit.CheckExpression

#### Syntax

ControlName_CheckExpression( errorCode, errorDescription, errorStartPosition, errorEndPosition)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the control checks the expression for errors.

#### Remarks

The initial values of the event parameters indicate whether the control detected an error in the expression. Use the event to evaluate, modify, or ignore the error or to perform and report additional expression checking on the expression.

#### Parameters

errorCode
 As
 
 [TSError](../tsapiref/tserror.html)

[In/Out] Specifies the error code for an error that exists in the expression.

errorDescription
 As
 [String](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the error description for an error that exists in the expression.

errorStartPosition
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the starting index of the error when an error exists in the expression.

errorEndPosition
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies one character past the ending index of the error when an error exists in the expression.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-checkexpression2.html language=enus -->
## TOPIC 05052: ExpressionEdit.CheckExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-checkexpression2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-checkexpression2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.CheckExpression( errorDescription, errorStartPosition, errorEndPosition) Return Value TSError An error code. Purpose Returns the result of the error checking the ExpressionEdit.ErrorCheck , ExpressionEdit.SetValidEvaluationTypes , and ExpressionEdit.GetValidEvaluationTypes meth

### ExpressionEdit.CheckExpression

#### Syntax

[ExpressionEdit](expressionedit.html).CheckExpression( errorDescription, errorStartPosition, errorEndPosition)

#### Return Value

[TSError](../tsapiref/tserror.html)

An error code.

#### Purpose

Returns the result of the error checking the
 [ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)
 ,
 [ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)
 , and
 [ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)
 methods specify.

#### Remarks

When you call this method, the ExpressionEdit control might modify the text to automatically prefix variables that do not have a full path specified.

Calling this method does not display an error.

To display an error, call the
 [ExpressionEdit.DisplayError](expressionedit-displayerror.html)
 method.

#### Parameters

errorDescription
 As
 [String](data-types-for-teststand-user-interface.html)

[Out] When an error exists, this parameter returns an error message that describes the error.

errorStartPosition
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] When an error exists, this parameter returns the starting character index of the error in the expression.

errorEndPosition
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] When an error exists, this parameter returns the index of one character past the ending character index of the error in the expression.

#### See Also

[EvaluationTypes.AllowedArrayRepresentations](../tsapiref/evaluationtypes-allowedarrayrepresentations.html)

[EvaluationTypes.AllowedRepresentations](../tsapiref/evaluationtypes-allowedrepresentations.html)

[ExpressionEdit.AllowEmpty](expressionedit-allowempty.html)

[ExpressionEdit.Context](expressionedit-context.html)

[ExpressionEdit.DisplayError](expressionedit-displayerror.html)

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-click.html language=enus -->
## TOPIC 05053: ExpressionEdit.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To ExpressionEdit Purpose Occurs when you press and release the mouse on the control.

### ExpressionEdit.Click

#### Syntax

ControlName_Click

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when you press and release the mouse on the control.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-combo-box-items-property-page.html language=enus -->
## TOPIC 05054: ExpressionEdit Combo Box Items Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-combo-box-items-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-combo-box-items-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Combo Box Items Property Page The Combo Box Items property page contains the following controls: Control is a Combo Box —Enable this option to make the ExpressionEdit control an Expression Combo Box control. Show Display Name in ExpressionEdit when ExpressionEdit is Inactive —When you enable this op

### ExpressionEdit Combo Box Items Property Page

#### Combo Box Items Property Page

The Combo Box Items property page contains the following controls:

- Control is a Combo Box 
 —Enable this option to make the
 ExpressionEdit 
 control an Expression Combo Box control.
- Show Display Name in ExpressionEdit when ExpressionEdit is Inactive 
 —When you enable this option and the text in the
 ExpressionEdit 
 control corresponds to the value of an item in the drop-down list and the item has a display name, the
 ExpressionEdit 
 control shows the display name of the item instead of the text when the
 ExpressionEdit 
 control is inactive.
- Drop Down List Items 
 —The items that appear in the drop-down list when you click the
 Combo Box 
 button of the
 ExpressionEdit 
 control.
- Insert 
 —Inserts a new item in the drop-down list after the currently selected item.
- Remove 
 —Removes the currently selected item from the drop-down list.
- Move Up 
 —Moves the currently selected item up one position.
- Move Down 
 —Moves the currently selected item down one position.
- Copy 
 —Copies the currently selected item.
- Paste 
 —Inserts the last item the
 ExpressionEdit 
 control copied after the currently selected item.
- Value 
 —An expression that replaces the existing text in the
 ExpressionEdit 
 control when this item is chosen in the drop-down list. The value is visible in the drop-down list when the Display Name option is empty.
- Display Name 
 —When the Display Name is not empty, it is visible in the drop-down list instead of the value. When you select this item in the drop-down list, the value, not the display name, replaces the existing text. The display name is useful for displaying a simple name for a complex expression in the drop-down list.
- Use Icon 
 —Enable this option to make the currently selected item display a picture.
  - Browse 
 —Displays a dialog box, in which you can select a picture for the currently selected item.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-comboboxitems.html language=enus -->
## TOPIC 05055: ExpressionEdit.ComboBoxItems

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-comboboxitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-comboboxitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ComboBoxItems Data Type ExpressionEditComboBoxItems Purpose Returns a collection of the items in the drop-down list when the ExpressionEdit control is a combo box. See Also ExpressionEdit.Style ExpressionEditComboBoxItems

### ExpressionEdit.ComboBoxItems

#### Syntax

[ExpressionEdit](expressionedit.html).ComboBoxItems

#### Data Type

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html)

#### Purpose

Returns a collection of the items in the drop-down list when the ExpressionEdit control is a combo box.

#### See Also

[ExpressionEdit.Style](expressionedit-style.html)

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-connectionactivity.html language=enus -->
## TOPIC 05056: ExpressionEdit.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To ExpressionEdit Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### ExpressionEdit.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-context.html language=enus -->
## TOPIC 05057: ExpressionEdit.Context

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-context.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-context.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Context Data Type PropertyObject Purpose Specifies the set of available variables and properties for autocompletion, error checking, evaluation, and the Expression Browser dialog box. Set this property to a PropertyObject in which the expression you are editing can be evaluated

### ExpressionEdit.Context

#### Syntax

[ExpressionEdit](expressionedit.html).Context

#### Data Type

[PropertyObject](../tsapiref/propertyobject.html)

#### Purpose

Specifies the set of available variables and properties for autocompletion, error checking, evaluation, and the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box. Set this property to a PropertyObject in which the expression you are editing can be evaluated.

#### Remarks

The ExpressionEdit control might create an
 
 [Engine](../tsapiref/engine.html)
 object when you set the Context to a PropertyObject that is not a SequenceContext. Refer to the
 [ExpressionEdit.Engine](expressionedit-engine.html)
 property for more information about creating a reference to an Engine object.

#### See Also

[Engine](../tsapiref/engine.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.CheckExpression](expressionedit-checkexpression2.html)

[ExpressionEdit.DisplayError](expressionedit-displayerror.html)

[ExpressionEdit.Engine](expressionedit-engine.html)

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-contextchanged.html language=enus -->
## TOPIC 05058: ExpressionEdit.ContextChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-contextchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-contextchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ContextChanged( reason) Applies To ExpressionEdit Purpose Occurs when the ExpressionEdit.Context property changes. Parameters reason As ContextChangedReasons [In] Specifies how the ExpressionEdit.Context property changed. See Also ExpressionEdit.Context

### ExpressionEdit.ContextChanged

#### Syntax

ControlName_ContextChanged( reason)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the
 [ExpressionEdit.Context](expressionedit-context.html)
 property changes.

#### Parameters

reason
 As
 [ContextChangedReasons](contextchangedreasons.html)

[In] Specifies how the
 ExpressionEdit.Context
 property changed.

#### See Also

[ExpressionEdit.Context](expressionedit-context.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-contextmenuitemclick.html language=enus -->
## TOPIC 05059: ExpressionEdit.ContextMenuItemClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-contextmenuitemclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-contextmenuitemclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ContextMenuItemClick( menuItemId) Applies To ExpressionEdit Purpose Occurs when the user selects a menu item from the ExpressionEdit control context menu. Parameters menuItemId As Long [In] Specifies the menu item ID of the menu item the user selects. See Also ExpressionEdit.Creat

### ExpressionEdit.ContextMenuItemClick

#### Syntax

ControlName_ContextMenuItemClick( menuItemId)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user selects a menu item from the ExpressionEdit control context menu.

#### Parameters

menuItemId
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the menu item ID of the menu item the user selects.

#### See Also

[ExpressionEdit.CreateContextMenu](expressionedit-createcontextmenu.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-createcontextmenu.html language=enus -->
## TOPIC 05060: ExpressionEdit.CreateContextMenu

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-createcontextmenu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-createcontextmenu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CreateContextMenu( menuHandle, x, y) Applies To ExpressionEdit Purpose Occurs just before the ExpressionEdit control displays its context menu. Use this event to add or remove items from the context menu of the ExpressionEdit control. Remarks The ExpressionEdit control creates a n

### ExpressionEdit.CreateContextMenu

#### Syntax

ControlName_CreateContextMenu( menuHandle, x, y)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs just before the ExpressionEdit control displays its context menu. Use this event to add or remove items from the context menu of the ExpressionEdit control.

#### Remarks

The ExpressionEdit control creates a new context menu every time it displays its context menu to the user.

#### Parameters

menuHandle
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the Microsoft Windows menu handle (HMENU) of the context menu. Use menu functions in the Windows Software Development Kit to modify this menu. Use the
 [ExpressionEdit.ContextMenuItemClick](expressionedit-contextmenuitemclick.html)
 event to respond to the user clicking menu items you add.

When the context menu closes, the control disposes of the menu items. Thus, you do not need to dispose of menu items you insert.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies where the left edge of the context menu is visible, relative to the control.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies where the top edge of the context menu is visible, relative to the control.

#### See Also

[ExpressionEdit.ContextMenuItemClick](expressionedit-contextmenuitemclick.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-dblclick.html language=enus -->
## TOPIC 05061: ExpressionEdit.DblClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-dblclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-dblclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DblClick Applies To ExpressionEdit Purpose Occurs when you double-click the control.

### ExpressionEdit.DblClick

#### Syntax

ControlName_DblClick

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when you double-click the control.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-displaybrowseexprdialog.html language=enus -->
## TOPIC 05062: ExpressionEdit.DisplayBrowseExprDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-displaybrowseexprdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-displaybrowseexprdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.DisplayBrowseExprDialog Return Value Boolean Returns True when you click OK in the Expression Browser dialog box. Returns False when you click Cancel . Purpose Launches the Expression Browser dialog box. Use the ExpressionEdit.BrowseExprDialogTitle property to customize the tit

### ExpressionEdit.DisplayBrowseExprDialog

#### Syntax

[ExpressionEdit](expressionedit.html).DisplayBrowseExprDialog

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when you click
 OK
 in the Expression Browser dialog box. Returns
 False
 when you click
 Cancel
 .

#### Purpose

Launches the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box. Use the
 [ExpressionEdit.BrowseExprDialogTitle](expressionedit-browseexprdialogtitle.html)
 property to customize the title for the dialog box, and use the
 
 [BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)
 constants to specify additional options.

#### See Also

[BrowseExprDialogOptions](../tsapiref/browseexprdialogoptions.html)

[Engine.DisplayBrowseExprDialogEx](../tsapiref/engine-displaybrowseexprdialogex.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.BrowseExprDialogClosed](expressionedit-browseexprdialogclosed.html)

[ExpressionEdit.BrowseExprDialogOpened](expressionedit-browseexprdialogopened.html)

[ExpressionEdit.BrowseExprDialogTitle](expressionedit-browseexprdialogtitle.html)

[ExpressionEdit.Context](expressionedit-context.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-displayerror.html language=enus -->
## TOPIC 05063: ExpressionEdit.DisplayError

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-displayerror.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-displayerror.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.DisplayError( options = 0) Purpose Performs error checking the ExpressionEdit.ErrorCheck and ExpressionEdit.AllowEmpty properties and the ExpressionEdit.SetValidEvaluationTypes and ExpressionEdit.GetValidEvaluationTypes methods specify. The ExpressionEdit control displays any e

### ExpressionEdit.DisplayError

#### Syntax

[ExpressionEdit](expressionedit.html).DisplayError( options = 0)

#### Purpose

Performs error checking the
 [ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)
 and
 [ExpressionEdit.AllowEmpty](expressionedit-allowempty.html)
 properties and the
 [ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)
 and
 [ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)
 methods specify. The ExpressionEdit control displays any errors in a different font and displays the error message in a tooltip.

#### Remarks

Use this method to force the ExpressionEdit control to check for errors as it does when you select Check for Errors from the ExpressionEdit control context menu.

When you call this method, the ExpressionEdit control might modify the text to automatically prefix variables that do not have a full path specified.

#### Parameters

options
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies a bitwise-OR combination of the
 [DisplayErrorOptions](displayerroroptions.html)
 constants.

This parameter has a default value of
 0
 .

#### See Also

[EvaluationTypes.AllowedArrayRepresentations](../tsapiref/evaluationtypes-allowedarrayrepresentations.html)

[EvaluationTypes.AllowedRepresentations](../tsapiref/evaluationtypes-allowedrepresentations.html)

[ExpressionEdit.AllowEmpty](expressionedit-allowempty.html)

[ExpressionEdit.CheckExpression](expressionedit-checkexpression2.html)

[ExpressionEdit.Context](expressionedit-context.html)

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

[DisplayErrorOptions](displayerroroptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-displayformattedvalue.html language=enus -->
## TOPIC 05064: ExpressionEdit.DisplayFormattedValue

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-displayformattedvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-displayformattedvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.DisplayFormattedValue Data Type Boolean Purpose When this property is True , the ExpressionEdit control displays the formatted value of a numeric constant you type in a tooltip and replaces the text you type with the formatted value when the ExpressionEdit control loses focus.

### ExpressionEdit.DisplayFormattedValue

#### Syntax

[ExpressionEdit](expressionedit.html).DisplayFormattedValue

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the ExpressionEdit control displays the formatted value of a numeric constant you type in a tooltip and replaces the text you type with the formatted value when the ExpressionEdit control loses focus.

#### See Also

[ExpressionEdit.NumericFormat](expressionedit-numericformat.html)

[PropertyObject.GetFormattedValue](../tsapiref/propertyobject-getformattedvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-displaytext.html language=enus -->
## TOPIC 05065: ExpressionEdit.DisplayText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-displaytext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-displaytext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.DisplayText Data Type String Purpose Specifies a localized expression for the text in the ExpressionEdit control. The value of the ExpressionEdit.Text property updates when you set this property. Remarks This property specifies the actual text in the ExpressionEdit control. Use

### ExpressionEdit.DisplayText

#### Syntax

[ExpressionEdit](expressionedit.html).DisplayText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a localized expression for the text in the ExpressionEdit control. The value of the
 [ExpressionEdit.Text](expressionedit-text.html)
 property updates when you set this property.

#### Remarks

This property specifies the actual text in the ExpressionEdit control. Use this property when you use the ExpressionEdit control with expression strings that are already localized for display. Refer to the
 
 [Engine.LocalizeExpression](../tsapiref/engine-localizeexpression.html)
 and
 
 [Engine.DelocalizeExpression](../tsapiref/engine-delocalizeexpression.html)
 methods for more information about localized and delocalized expressions.

#### See Also

[Engine.DelocalizeExpression](../tsapiref/engine-delocalizeexpression.html)

[Engine.LocalizeExpression](../tsapiref/engine-localizeexpression.html)

[ExpressionEdit.MaxLength](expressionedit-maxlength.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

[ExpressionEdit.Text](expressionedit-text.html)

[ExpressionEdit.TextLength](expressionedit-textlength.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-dropdown.html language=enus -->
## TOPIC 05066: ExpressionEdit.DropDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-dropdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-dropdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DropDown Applies To ExpressionEdit Purpose Occurs when the list portion of the control is about to drop down. Remarks This event is useful if you want to wait until the list is visible to populate the list with items. See Also ExpressionEditComboBoxItems

### ExpressionEdit.DropDown

#### Syntax

ControlName_DropDown

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the list portion of the control is about to drop down.

#### Remarks

This event is useful if you want to wait until the list is visible to populate the list with items.

#### See Also

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-dropdownlisthwnd.html language=enus -->
## TOPIC 05067: ExpressionEdit.DropDownListHwnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-dropdownlisthwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-dropdownlisthwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.DropDownListHwnd Data Type Long Purpose Returns the Window handle of the drop-down list visible when the ExpressionEdit control is a combo box. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this propert

### ExpressionEdit.DropDownListHwnd

#### Syntax

[ExpressionEdit](expressionedit.html).DropDownListHwnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the drop-down list visible when the ExpressionEdit control is a combo box.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

#### See Also

[ExpressionEdit.Style](expressionedit-style.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-enabled.html language=enus -->
## TOPIC 05068: ExpressionEdit.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Enabled Data Type Boolean Purpose The control responds to user input only when this property is True . See Also ExpressionEdit.ReadOnly

### ExpressionEdit.Enabled

#### Syntax

[ExpressionEdit](expressionedit.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user input only when this property is
 True
 .

#### See Also

[ExpressionEdit.ReadOnly](expressionedit-readonly.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-engine.html language=enus -->
## TOPIC 05069: ExpressionEdit.Engine

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-engine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Engine Data Type Engine Purpose Specifies a reference to the Engine object. The ExpressionEdit control uses the Engine object for the following purposes: Displaying the Expression Browser dialog box. Displaying the Expression Editing Options dialog box, which you can access thr

### ExpressionEdit.Engine

#### Syntax

[ExpressionEdit](expressionedit.html).Engine

#### Data Type

[Engine](../tsapiref/engine.html)

#### Purpose

Specifies a reference to the
 
 [Engine](../tsapiref/engine.html)
 object. The ExpressionEdit control uses the
 Engine
 object for the following purposes:

- Displaying the
 Expression Browser 
 dialog box.
- Displaying the
 Expression Editing Options 
 dialog box, which you can access through the Options item in the context menu of the ExpressionEdit control.
- Reading options configured in the Expression Editing Options dialog box.

#### Remarks

You do not need to set this property because the ExpressionEdit control automatically obtains a reference to an
 Engine
 object when a reference is needed. However, because the ExpressionEdit control creates an
 Engine
 object when it cannot obtain one from the
 [ExpressionEdit.Context](expressionedit-context.html)
 property, it is useful to set this property when the
 ExpressionEdit.Context
 property has not been set to a PropertyObject that is also a SequenceContext and when an
 Engine
 object has already been created in a different process than the ExpressionEdit control. The TestStand Engine is considered needed when the
 ExpressionEdit.Context
 property is set or when this property is read, even when the property is read internally to launch an engine dialog box.

#### See Also

[Engine](../tsapiref/engine.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.Context](expressionedit-context.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-error-checking-property-page.html language=enus -->
## TOPIC 05070: ExpressionEdit Error Checking Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-error-checking-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-error-checking-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Error Checking Property Page The Error Checking property page contains the following controls: Error Check —Enables error checking in the ExpressionEdit control. The ExpressionEdit control displays the error in a different color and font style and displays an error message in a tooltip. None —Disabl

### ExpressionEdit Error Checking Property Page

#### Error Checking Property Page

The Error Checking property page contains the following controls:

- Error Check 
 —Enables error checking in the
 ExpressionEdit 
 control. The
 ExpressionEdit 
 control displays the error in a different color and font style and displays an error message in a tooltip.
  - None 
 —Disables error checking.
  - Syntax 
 —Checks only for syntax errors.
  - Syntax and Evaluation 
 —Checks for syntax and evaluation errors. TestStand returns an evaluation error when the text in the
 ExpressionEdit 
 control does not evaluate to the type the
 ExpressionEdit.GetValidEvaluationTypes 
 and
 ExpressionEdit.SetValidEvaluationTypes 
 methods specify.
- Allow Empty Expression 
 —When this option is disabled, an empty expression is considered an error. When this option is enabled, an empty expression is never considered an error, even when the value of the Error Check option is Syntax and Evaluation and the expression is required to evaluate to a particular type.
- Required Types 
 —The types the expression can evaluate to. The following types are available:
  - Any 
 —The expression can evaluate to any type, but you must be able to evaluate the expression.
  - Boolean 
 —The expression can evaluate to a Boolean.
  - Number 
 —The expression can evaluate to a number.
  - String 
 —The expression can evaluate to a string.
  - Reference 
 —The expression can evaluate to an object reference.
  - Container 
 —The expression can evaluate to a container.
  - Named Type (separate names by new lines) 
 —The expression can evaluate to any specified named type.
  - Boolean Array 
 —The expression can evaluate to an array of Boolean values.
  - Number Array 
 —The expression can evaluate to an array of numbers.
  - String Array 
 —The expression can evaluate to an array of strings.
  - Reference Array 
 —The expression can evaluate to an array of object references.
  - Container Array 
 —The expression can evaluate to an array of containers.
  - Named Type Arrays (separate names by new lines) 
 —The expression can evaluate to an array of any specified named type.

#### See Also

[EvaluationTypes.AllowedArrayRepresentations](../tsapiref/evaluationtypes-allowedarrayrepresentations.html)

[EvaluationTypes.AllowedRepresentations](../tsapiref/evaluationtypes-allowedrepresentations.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-errorcheck.html language=enus -->
## TOPIC 05071: ExpressionEdit.ErrorCheck

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-errorcheck.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-errorcheck.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ErrorCheck Data Type ErrorCheck Use the following constants with this data type: ErrorCheck_None –(Value: 0) No error checking. ErrorCheck_Syntax –(Value: 1) Checks only for syntax errors. ErrorCheck_SyntaxAndEvaluation –(Value: 2) Checks for syntax and evaluation errors. Purpo

### ExpressionEdit.ErrorCheck

#### Syntax

[ExpressionEdit](expressionedit.html).ErrorCheck

#### Data Type

[ErrorCheck](errorcheck.html)

Use the following constants with this data type:

- ErrorCheck_None 
 –(Value: 0) No error checking.
- ErrorCheck_Syntax 
 –(Value: 1) Checks only for syntax errors.
- ErrorCheck_SyntaxAndEvaluation 
 –(Value: 2) Checks for syntax and evaluation errors.

#### Purpose

Specifies whether the control performs error checking on the expression. When the value of this property is a value other than
 ErrorCheck_None
 , the expression is checked for errors when the ExpressionEdit control loses focus, when you select Check for Errors from the context menu, or when the
 [ExpressionEdit.DisplayError](expressionedit-displayerror.html)
 method is called.

#### Remarks

When an error is found, the error is displayed in a different font color or style. The error message is displayed in a tooltip.

#### See Also

[EvaluationTypes.AllowedArrayRepresentations](../tsapiref/evaluationtypes-allowedarrayrepresentations.html)

[EvaluationTypes.AllowedRepresentations](../tsapiref/evaluationtypes-allowedrepresentations.html)

[ExpressionEdit.CheckExpression](expressionedit-checkexpression2.html)

[ExpressionEdit.DisplayError](expressionedit-displayerror.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-evaluate.html language=enus -->
## TOPIC 05072: ExpressionEdit.Evaluate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-evaluate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-evaluate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Evaluate( evaluationOptions) Return Value PropertyObject The result of the evaluation. Purpose Evaluates the current expression using the context the ExpressionEdit.Context property specifies. Parameters evaluationOptions As Long [In] Pass Eval_NoOptions to specify the default

### ExpressionEdit.Evaluate

#### Syntax

[ExpressionEdit](expressionedit.html).Evaluate( evaluationOptions)

#### Return Value

[PropertyObject](../tsapiref/propertyobject.html)

The result of the evaluation.

#### Purpose

Evaluates the current expression using the context the
 [ExpressionEdit.Context](expressionedit-context.html)
 property specifies.

#### Parameters

evaluationOptions
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Pass
 Eval_NoOptions
 to specify the default behavior, or pass one or more
 
 [EvaluationOptions](../tsapiref/evaluationoptions.html)
 constants. The
 EvalOption_AllowEmptyExpression
 constant is ignored. Use the
 [ExpressionEdit.AllowEmpty](expressionedit-allowempty.html)
 property to determine whether to treat an empty expression as an error. Use the bitwise-OR operator to specify multiple options.

#### See Also

[ExpressionEdit.AllowEmpty](expressionedit-allowempty.html)

[ExpressionEdit.Context](expressionedit-context.html)

[EvaluationOptions](../tsapiref/evaluationoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-font.html language=enus -->
## TOPIC 05073: ExpressionEdit.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Font Data Type Font Purpose Specifies the current font for the ExpressionEdit control when the value of the ExpressionEdit.FontSource property is FontSource_UseFontProperty . Remarks Only the font name and size are used. All other properties of this parameter are ignored becaus

### ExpressionEdit.Font

#### Syntax

[ExpressionEdit](expressionedit.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the current font for the ExpressionEdit control when the value of the
 [ExpressionEdit.FontSource](expressionedit-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### Remarks

Only the font name and size are used. All other properties of this parameter are ignored because those properties are set on a per-text element basis in the
 [Expression Editing Options](../tsref/expression-editing-options-dialog-box.html)
 dialog box, which you can access through the Options item from the context menu of the ExpressionEdit control.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.FontSource](expressionedit-fontsource.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-fontsource.html language=enus -->
## TOPIC 05074: ExpressionEdit.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIF

### ExpressionEdit.FontSource

#### Syntax

[ExpressionEdit](expressionedit.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the current font for the ExpressionEdit control. The default value for this property is
 FontSource_UseGUIFont
 . When the value of this property is
 FontSource_UseFontProperty
 , the
 [ExpressionEdit.Font](expressionedit-font.html)
 property specifies the current font.

#### Remarks

Only the font name and size are used. All other properties of this parameter are ignored because the other properties are set on a per-text element basis in the
 [Expression Editing Options](../tsref/expression-editing-options-dialog-box.html)
 dialog box, which you can access through the Options item from the context menu of the ExpressionEdit control.

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 ExpressionEdit.Font
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.Font](expressionedit-font.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-functiontiphwnd.html language=enus -->
## TOPIC 05075: ExpressionEdit.FunctionTipHwnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-functiontiphwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-functiontiphwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.FunctionTipHwnd Data Type Long Purpose Returns the Window handle of the function tip. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior. See Also ExpressionEdit.Au

### ExpressionEdit.FunctionTipHwnd

#### Syntax

[ExpressionEdit](expressionedit.html).FunctionTipHwnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the function tip.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

#### See Also

[ExpressionEdit.AutoCompletionHwnd](expressionedit-autocompletionhwnd.html)

[ExpressionEdit.hWnd](expressionedit-hwnd.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-general-property-page.html language=enus -->
## TOPIC 05076: ExpressionEdit General Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-general-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-general-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Property Page The General property page contains the following controls: Text —The default text contained in an ExpressionEdit control. Text Type —Use this property to make an ExpressionEdit control function like an ordinary edit box or text box. This is useful when you want an edit box you

### ExpressionEdit General Property Page

#### General Property Page

The General property page contains the following controls:

- Text 
 —The default text contained in an
 ExpressionEdit 
 control.
  - Text Type 
 —Use this property to make an
 ExpressionEdit 
 control function like an ordinary edit box or text box. This is useful when you want an edit box you can use to edit an expression or plain text.
    - Plain Text 
 —The text is not an expression. This value makes an
 ExpressionEdit 
 control function like an edit box or text box. The
 ExpressionEdit 
 control does not use syntax highlighting, perform error checking, perform autocompletion, or show function tips. The context menu of the
 ExpressionEdit 
 control contains items only for text editing.
    - Expression 
 —The text is an expression.
    - Expression with C++ Identifiers 
 —The text is an expression that might contain C++ scope resolution and template operators.
- Font 
 —This section contains the following options:
  - Font to Use 
 —The font for the
 ExpressionEdit 
 control. Set this option to Custom Font to choose any available font. Because font styles and color are set on a per-text element basis in the
 Expression Editing Options 
 dialog box, only the font name and size are used, even when using a Custom Font. Refer to the
 FontSources 
 enumeration for more information about this option.
  - Custom Font 
 —Displays the custom font specified for the
 ExpressionEdit 
 control. Click the
 Change 
 button to launch the Font dialog box. This option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring control. If you change the system language or apply a font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.
  - Change 
 —Launches the Font dialog box, in which you can specify a custom font.
- Appearance 
 —This section contains the following options:
  - Mouse Pointer 
 —The cursor that displays when the mouse is over the
 ExpressionEdit 
 control.
  - Background Color 
 —The color of the background.
  - Multiline 
 —The
 ExpressionEdit 
 control can contain more than one line of text.
  - Enabled 
 —TestStand enables the
 ExpressionEdit 
 control. A disabled control cannot be active.
  - Read Only 
 —You cannot edit the
 ExpressionEdit 
 control, but it can be active.
  - Hide Selection 
 —The selection is not visible when the
 ExpressionEdit 
 control is not active.
  - Horizontal Scrollbar 
 —The
 ExpressionEdit 
 control contains a horizontal scrollbar.
  - Vertical Scrollbar 
 —The
 ExpressionEdit 
 control contains a vertical scrollbar.
  - Syntax and Error Highlighting 
 —The
 ExpressionEdit 
 control displays text elements such as comments, strings, identifiers, and errors in a different color and font style.
 Note 
 Do not use this property when you use an
 ExpressionEdit
 control to display text that is not an expression. Set the Text Type option to
 Plain Text
 to display plain text.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[FontSources](fontsources.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-getadditionalevaluationconstan.html language=enus -->
## TOPIC 05077: ExpressionEdit.GetAdditionalEvaluationConstants

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-getadditionalevaluationconstan.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-getadditionalevaluationconstan.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.GetAdditionalEvaluationConstants Return Value Object Array Purpose Returns a copy of the additional constants you passed to the ExpressionEdit.SetAdditionalEvaluationConstants method. See Also ExpressionEdit.SetAdditionalEvaluationConstants

### ExpressionEdit.GetAdditionalEvaluationConstants

#### Syntax

[ExpressionEdit](expressionedit.html).GetAdditionalEvaluationConstants

#### Return Value

[Object Array](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a copy of the additional constants you passed to the
 [ExpressionEdit.SetAdditionalEvaluationConstants](expressionedit-setadditionalevaluationconstan.html)
 method.

#### See Also

[ExpressionEdit.SetAdditionalEvaluationConstants](expressionedit-setadditionalevaluationconstan.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-getvalidevaluationtypes.html language=enus -->
## TOPIC 05078: ExpressionEdit.GetValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-getvalidevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-getvalidevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.GetValidEvaluationTypes Return Value EvaluationTypes Purpose Obtains the valid evaluation types. See Also EvaluationTypes ExpressionEdit.SetValidEvaluationTypes

### ExpressionEdit.GetValidEvaluationTypes

#### Syntax

[ExpressionEdit](expressionedit.html).GetValidEvaluationTypes

#### Return Value

[EvaluationTypes](../tsapiref/evaluationtypes.html)

#### Purpose

Obtains the valid evaluation types.

#### See Also

[EvaluationTypes](../tsapiref/evaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-hideselection.html language=enus -->
## TOPIC 05079: ExpressionEdit.HideSelection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-hideselection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-hideselection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.HideSelection Data Type Boolean Purpose When this property is True , text selection is hidden when the ExpressionEdit control loses focus. When this property is False , text selection is never hidden.

### ExpressionEdit.HideSelection

#### Syntax

[ExpressionEdit](expressionedit.html).HideSelection

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , text selection is hidden when the ExpressionEdit control loses focus. When this property is
 False
 , text selection is never hidden.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-hwnd.html language=enus -->
## TOPIC 05080: ExpressionEdit.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.hWnd Data Type Long Purpose Returns the Window handle of the ExpressionEdit control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior. See Also ExpressionEdit.Aut

### ExpressionEdit.hWnd

#### Syntax

[ExpressionEdit](expressionedit.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the ExpressionEdit control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

#### See Also

[ExpressionEdit.AutoCompletionHwnd](expressionedit-autocompletionhwnd.html)

[ExpressionEdit.FunctionTipHwnd](expressionedit-functiontiphwnd.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-insertcomboboxitem.html language=enus -->
## TOPIC 05081: ExpressionEdit.InsertComboBoxItem

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-insertcomboboxitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-insertcomboboxitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_InsertComboBoxItem( item, insertStart, insertEnd) Applies To ExpressionEdit Purpose Occurs when the user selects an item in the drop-down list. This event is useful when you do not want the selected item to replace the existing text. Remarks You cannot use this event to change wha

### ExpressionEdit.InsertComboBoxItem

#### Syntax

ControlName_InsertComboBoxItem( item, insertStart, insertEnd)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user selects an item in the drop-down list. This event is useful when you do not want the selected item to replace the existing text.

#### Remarks

You cannot use this event to change what text to insert into the ExpressionEdit control.

#### Parameters

item
 As
 [ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

[In] Specifies the item to insert into the ExpressionEdit control.

insertStart
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the zero-based index of the character where the selected item is inserted.

This parameter is initialized to zero. You can change the value of this parameter to change where the selected item is inserted.

insertEnd
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the zero-based index of the last character the selected item replaces.

This parameter is initialized to the index of the last character in the ExpressionEdit control. You can change the value of this parameter to change what text the selected item replaces.

#### See Also

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-keydown.html language=enus -->
## TOPIC 05082: ExpressionEdit.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To ExpressionEdit Purpose Occurs when the user presses any key while the control has the input focus. This event occurs before the ExpressionEdit.KeyPress event. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the

### ExpressionEdit.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user presses any key while the control has the input focus. This event occurs before the
 [ExpressionEdit.KeyPress](expressionedit-keypress.html)
 event.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[ExpressionEdit.KeyPress](expressionedit-keypress.html)

[ExpressionEdit.KeyUp](expressionedit-keyup.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-keypress.html language=enus -->
## TOPIC 05083: ExpressionEdit.KeyPress

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-keypress.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-keypress.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyPress( keyAscii) Applies To ExpressionEdit Purpose Occurs when the user presses a key while a control is active. This event occurs after the ExpressionEdit.KeyDown event. Parameters keyAscii As Integer [In/Out] Specifies the ASCII value of the pressed key. See Also ExpressionEd

### ExpressionEdit.KeyPress

#### Syntax

ControlName_KeyPress( keyAscii)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user presses a key while a control is active. This event occurs after the
 [ExpressionEdit.KeyDown](expressionedit-keydown.html)
 event.

#### Parameters

keyAscii
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the ASCII value of the pressed key.

#### See Also

[ExpressionEdit.KeyDown](expressionedit-keydown.html)

[ExpressionEdit.KeyUp](expressionedit-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-keyup.html language=enus -->
## TOPIC 05084: ExpressionEdit.KeyUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-keyup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-keyup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyUp( keyCode, shift) Applies To ExpressionEdit Purpose Occurs when the user releases any key while the control has the input focus. Parameters keyCode As Integer [In] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of th

### ExpressionEdit.KeyUp

#### Syntax

ControlName_KeyUp( keyCode, shift)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user releases any key while the control has the input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[ExpressionEdit.KeyDown](expressionedit-keydown.html)

[ExpressionEdit.KeyPress](expressionedit-keypress.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-localize.html language=enus -->
## TOPIC 05085: ExpressionEdit.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Localize( sectionName) Purpose Localizes the ToolTipText and ContextMenuItemCaption properties for each ExpressionEditButton and the DisplayName property of each ExpressionEditComboBoxItem. Remarks First, update a .ini file located in the TestStand Language directory with the r

### ExpressionEdit.Localize

#### Syntax

[ExpressionEdit](expressionedit.html).Localize( sectionName)

#### Purpose

Localizes the
 [ToolTipText](expressioneditbutton-tooltiptext.html)
 and
 [ContextMenuItemCaption](expressioneditbutton-contextmenuitemcaption.html)
 properties for each ExpressionEditButton and the
 [DisplayName](expressioneditcomboboxitem-displayname.html)
 property of each ExpressionEditComboBoxItem.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required string. Second, use the string tag in the
 .ini
 file as the
 ToolTipText
 and
 ContextMenuItemCaption
 properties of each button and the
 DisplayName
 property of each combo box item.

When you call this method, the control replaces the
 ToolTipText
 and
 ContextMenuItemCaption
 properties of each button and the
 DisplayName
 property of each combo box item with the string from the
 .ini
 file. If the
 ToolTipText
 ,
 ContextMenuItemCaption
 , or
 DisplayName
 property is not a tag in the
 .ini
 file, the property does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ExpressionEditButton.ContextMenuItemCaption](expressioneditbutton-contextmenuitemcaption.html)

[ExpressionEditButton.ToolTipText](expressioneditbutton-tooltiptext.html)

[ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-maxlength.html language=enus -->
## TOPIC 05086: ExpressionEdit.MaxLength

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-maxlength.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-maxlength.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.MaxLength Data Type Long Purpose Specifies the maximum number of characters the ExpressionEdit control can contain. When the value of this property is 0 , the maximum number of characters is 64,000. You can specify a number greater than 64,000. See Also ExpressionEdit.Text Expr

### ExpressionEdit.MaxLength

#### Syntax

[ExpressionEdit](expressionedit.html).MaxLength

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the maximum number of characters the ExpressionEdit control can contain. When the value of this property is
 0
 , the maximum number of characters is 64,000. You can specify a number greater than 64,000.

#### See Also

[ExpressionEdit.Text](expressionedit-text.html)

[ExpressionEdit.TextLength](expressionedit-textlength.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-mousedown.html language=enus -->
## TOPIC 05087: ExpressionEdit.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To ExpressionEdit Purpose Occurs when the user clicks the mouse on the control. This event occurs before the ExpressionEdit.MouseUp event. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any on

### ExpressionEdit.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user clicks the mouse on the control. This event occurs before the
 [ExpressionEdit.MouseUp](expressionedit-mouseup.html)
 event.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[ExpressionEdit.Click](expressionedit-click.html)

[ExpressionEdit.MouseMove](expressionedit-mousemove.html)

[ExpressionEdit.MouseUp](expressionedit-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-mouseicon.html language=enus -->
## TOPIC 05088: ExpressionEdit.MouseIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-mouseicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-mouseicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.MouseIcon Data Type Picture Purpose Displays the specified picture as the cursor for the ExpressionEdit control. Remarks The value of the ExpressionEdit.MousePointer property must be MousePointer_Custom for you to use the ExpressionEdit.MouseIcon property. When you set this pro

### ExpressionEdit.MouseIcon

#### Syntax

[ExpressionEdit](expressionedit.html).MouseIcon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Displays the specified picture as the cursor for the ExpressionEdit control.

#### Remarks

The value of the
 [ExpressionEdit.MousePointer](expressionedit-mousepointer.html)
 property must be
 MousePointer_Custom
 for you to use the
 ExpressionEdit.MouseIcon
 property. When you set this property to
 NULL
 , the value of the
 ExpressionEdit.MousePointer
 property changes to
 MousePointer_Default
 .

#### See Also

[ExpressionEdit.MousePointer](expressionedit-mousepointer.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-mousemove.html language=enus -->
## TOPIC 05089: ExpressionEdit.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To ExpressionEdit Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies

### ExpressionEdit.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[ExpressionEdit.Click](expressionedit-click.html)

[ExpressionEdit.MouseDown](expressionedit-mousedown.html)

[ExpressionEdit.MouseUp](expressionedit-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-mousepointer.html language=enus -->
## TOPIC 05090: ExpressionEdit.MousePointer

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-mousepointer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-mousepointer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.MousePointer Data Type MousePointerStyles Use the following constants with this data type: MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(Value: 2) MousePointer_Custom –(Value: 99) MousePo

### ExpressionEdit.MousePointer

#### Syntax

[ExpressionEdit](expressionedit.html).MousePointer

#### Data Type

[MousePointerStyles](mousepointerstyles.html)

Use the following constants with this data type:

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### Purpose

Specifies the appearance of the mouse cursor when the cursor is over the control.

#### Remarks

When the parameter is
 MousePointer_Custom
 , the mouse cursor is the picture the
 [ExpressionEdit.MouseIcon](expressionedit-mouseicon.html)
 property specifies.

#### See Also

[ExpressionEdit.MouseIcon](expressionedit-mouseicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-mouseup.html language=enus -->
## TOPIC 05091: ExpressionEdit.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To ExpressionEdit Purpose Occurs when the user releases the mouse on the control. This event occurs before the ExpressionEdit.Click event. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one

### ExpressionEdit.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the user releases the mouse on the control. This event occurs before the
 [ExpressionEdit.Click](expressionedit-click.html)
 event.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[ExpressionEdit.Click](expressionedit-click.html)

[ExpressionEdit.MouseDown](expressionedit-mousedown.html)

[ExpressionEdit.MouseMove](expressionedit-mousemove.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-multiline.html language=enus -->
## TOPIC 05092: ExpressionEdit.Multiline

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-multiline.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-multiline.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Multiline Data Type Boolean Purpose Specifies whether the ExpressionEdit control is a multi-line or single-line control. See Also ExpressionEdit.WantReturn ExpressionEdit.WordWrap

### ExpressionEdit.Multiline

#### Syntax

[ExpressionEdit](expressionedit.html).Multiline

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the ExpressionEdit control is a multi-line or single-line control.

#### See Also

[ExpressionEdit.WantReturn](expressionedit-wantreturn.html)

[ExpressionEdit.WordWrap](expressionedit-wordwrap.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-numericformat.html language=enus -->
## TOPIC 05093: ExpressionEdit.NumericFormat

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-numericformat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-numericformat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.NumericFormat Data Type String Purpose Specifies the format string that the ExpressionEdit control uses to calculate the formatted value of the text when the ExpressionEdit.DisplayFormattedValue property is True . Assign any string to this property that you would pass as the fo

### ExpressionEdit.NumericFormat

#### Syntax

[ExpressionEdit](expressionedit.html).NumericFormat

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the format string that the ExpressionEdit control uses to calculate the formatted value of the text when the
 [ExpressionEdit.DisplayFormattedValue](expressionedit-displayformattedvalue.html)
 property is
 True
 . Assign any string to this property that you would pass as the
 formatString
 parameter in the
 
 [PropertyObject.GetFormattedValue](../tsapiref/propertyobject-getformattedvalue.html)
 method.

#### See Also

[ExpressionEdit.DisplayFormattedValue](expressionedit-displayformattedvalue.html)

[PropertyObject.GetFormattedValue](../tsapiref/propertyobject-getformattedvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-readonly.html language=enus -->
## TOPIC 05094: ExpressionEdit.ReadOnly

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-readonly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-readonly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ReadOnly Data Type Boolean Purpose Specifies that the control can be edited.

### ExpressionEdit.ReadOnly

#### Syntax

[ExpressionEdit](expressionedit.html).ReadOnly

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies that the control can be edited.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-requirednamedtypearrays.html language=enus -->
## TOPIC 05095: ExpressionEdit.RequiredNamedTypeArrays

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-requirednamedtypearrays.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-requirednamedtypearrays.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.RequiredNamedTypeArrays Data Type Strings Purpose This property is obsolete. Use the ExpressionEdit.GetValidEvaluationTypes and ExpressionEdit.SetValidEvaluationTypes methods instead. Remarks Returns a collection of strings that specify the named type arrays allowed when the va

### ExpressionEdit.RequiredNamedTypeArrays

#### Syntax

[ExpressionEdit](expressionedit.html).RequiredNamedTypeArrays

#### Data Type

[Strings](strings.html)

#### Purpose

Note

ExpressionEdit.GetValidEvaluationTypes

ExpressionEdit.SetValidEvaluationTypes

#### Remarks

Returns a collection of strings that specify the named type arrays allowed when the value of the
 [ExpressionEdit.RequiredTypes](expressionedit-requiredtypes.html)
 property is
 ValidExpressionType_NamedTypeArray
 . The ExpressionEdit control highlights the expression as an evaluation error when the expression fails to evaluate to a named type array listed in the collection.

#### See Also

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.RequiredNamedTypes](expressionedit-requirednamedtypes.html)

[ExpressionEdit.RequiredTypes](expressionedit-requiredtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

[Strings](strings.html)

[ValidExpressionTypes](validexpressiontypes.html)

Parent topic:

Obsolete ExpressionEdit Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-requirednamedtypes.html language=enus -->
## TOPIC 05096: ExpressionEdit.RequiredNamedTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-requirednamedtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-requirednamedtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.RequiredNamedTypes Data Type Strings Purpose This property is obsolete. Use the ExpressionEdit.GetValidEvaluationTypes and ExpressionEdit.SetValidEvaluationTypes methods instead. Remarks Returns a collection of strings that specify the named types that are allowed when the valu

### ExpressionEdit.RequiredNamedTypes

#### Syntax

[ExpressionEdit](expressionedit.html).RequiredNamedTypes

#### Data Type

[Strings](strings.html)

#### Purpose

Note

ExpressionEdit.GetValidEvaluationTypes

ExpressionEdit.SetValidEvaluationTypes

#### Remarks

Returns a collection of strings that specify the named types that are allowed when the value of the
 [ExpressionEdit.RequiredTypes](expressionedit-requiredtypes.html)
 property is
 ValidExpressionType_NamedType
 . The ExpressionEdit control highlights the expression as an evaluation error when the expression fails to evaluate to a named type listed in the collection.

#### See Also

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.RequiredNamedTypeArrays](expressionedit-requirednamedtypearrays.html)

[ExpressionEdit.RequiredTypes](expressionedit-requiredtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

[Strings](strings.html)

[ValidExpressionTypes](validexpressiontypes.html)

Parent topic:

Obsolete ExpressionEdit Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-requiredtypes.html language=enus -->
## TOPIC 05097: ExpressionEdit.RequiredTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-requiredtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-requiredtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.RequiredTypes Data Type Long Purpose This property is obsolete. Use the ExpressionEdit.GetValidEvaluationTypes and ExpressionEdit.SetValidEvaluationTypes methods instead. Remarks Specifies any combination of the ValidExpressionTypes constants. Use the bitwise-OR operator to spe

### ExpressionEdit.RequiredTypes

#### Syntax

[ExpressionEdit](expressionedit.html).RequiredTypes

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Note

ExpressionEdit.GetValidEvaluationTypes

ExpressionEdit.SetValidEvaluationTypes

#### Remarks

Specifies any combination of the
 [ValidExpressionTypes](validexpressiontypes.html)
 constants. Use the bitwise-OR operator to specify more than one valid type.

Specifies the allowed evaluation result types when the value of the
 [ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)
 property is
 ErrorCheck_SyntaxAndEvaluation
 .

If the value of this property is
 ValidExpressionType_NamedType
 or
 ValidExpressionType_NamedTypeArray
 , the named types or named type arrays must be specified using the
 [RequiredNamedTypes](expressionedit-requirednamedtypes.html)
 property and the
 [RequiredNamedTypeArrays](expressionedit-requirednamedtypearrays.html)
 property, respectively.

#### See Also

[ExpressionEdit.CheckExpression](expressionedit-checkexpression2.html)

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.RequiredNamedTypeArrays](expressionedit-requirednamedtypearrays.html)

[ExpressionEdit.RequiredNamedTypes](expressionedit-requirednamedtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](expressionedit-setvalidevaluationtypes.html)

[ValidExpressionTypes](validexpressiontypes.html)

Parent topic:

Obsolete ExpressionEdit Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-scalewithdpi.html language=enus -->
## TOPIC 05098: ExpressionEdit.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls a

### ExpressionEdit.ScaleWithDPI

#### Syntax

[ExpressionEdit](expressionedit.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-scrollbars.html language=enus -->
## TOPIC 05099: ExpressionEdit.ScrollBars

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-scrollbars.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-scrollbars.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ScrollBars Data Type ScrollBars Use the following constants with this data type: ScrollBar_Both –(Value: 1) Shows the horizontal and vertical scrollbars. ScrollBar_Horizontal –(Value: 2) Shows only the horizontal scrollbar. ScrollBar_None –(Value: 0) Does not show the horizonta

### ExpressionEdit.ScrollBars

#### Syntax

[ExpressionEdit](expressionedit.html).ScrollBars

#### Data Type

[ScrollBars](scrollbars.html)

Use the following constants with this data type:

- ScrollBar_Both 
 –(Value: 1) Shows the horizontal and vertical scrollbars.
- ScrollBar_Horizontal 
 –(Value: 2) Shows only the horizontal scrollbar.
- ScrollBar_None 
 –(Value: 0) Does not show the horizontal or vertical scrollbars.
- ScrollBar_Vertical 
 –(Value: 3) Shows only the vertical scrollbar.

#### Purpose

Specifies which scrollbars are visible in the ExpressionEdit control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-selchange.html language=enus -->
## TOPIC 05100: ExpressionEdit.SelChange

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-selchange.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-selchange.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SelChange Applies To ExpressionEdit Purpose Occurs when the current selection changes. See Also ExpressionEdit.SelLength ExpressionEdit.SelStart ExpressionEdit.SelText

### ExpressionEdit.SelChange

#### Syntax

ControlName_SelChange

#### Applies To

[ExpressionEdit](expressionedit.html)

#### Purpose

Occurs when the current selection changes.

#### See Also

[ExpressionEdit.SelLength](expressionedit-sellength.html)

[ExpressionEdit.SelStart](expressionedit-selstart.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-selectall.html language=enus -->
## TOPIC 05101: ExpressionEdit.SelectAll

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-selectall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-selectall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SelectAll Purpose Selects all the text in the ExpressionEdit control. See Also ExpressionEdit.SelLength ExpressionEdit.SelStart ExpressionEdit.SelText

### ExpressionEdit.SelectAll

#### Syntax

[ExpressionEdit](expressionedit.html).SelectAll

#### Purpose

Selects all the text in the ExpressionEdit control.

#### See Also

[ExpressionEdit.SelLength](expressionedit-sellength.html)

[ExpressionEdit.SelStart](expressionedit-selstart.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-sellength.html language=enus -->
## TOPIC 05102: ExpressionEdit.SelLength

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-sellength.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-sellength.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SelLength Data Type Long Purpose Specifies the number of characters in the current selection. See Also ExpressionEdit.SelStart ExpressionEdit.SelText

### ExpressionEdit.SelLength

#### Syntax

[ExpressionEdit](expressionedit.html).SelLength

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the number of characters in the current selection.

#### See Also

[ExpressionEdit.SelStart](expressionedit-selstart.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-selstart.html language=enus -->
## TOPIC 05103: ExpressionEdit.SelStart

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-selstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-selstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SelStart Data Type Long Purpose Specifies the zero-based index of the starting character for the current selection. See Also ExpressionEdit.SelLength ExpressionEdit.SelText

### ExpressionEdit.SelStart

#### Syntax

[ExpressionEdit](expressionedit.html).SelStart

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the zero-based index of the starting character for the current selection.

#### See Also

[ExpressionEdit.SelLength](expressionedit-sellength.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-seltext.html language=enus -->
## TOPIC 05104: ExpressionEdit.SelText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-seltext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-seltext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SelText Data Type String Purpose Use this property to obtain or replace the currently selected text. Remarks This property is a portion of the displayed text which is a localized expression. See Also ExpressionEdit.DisplayText ExpressionEdit.SelLength ExpressionEdit.SelStart Ex

### ExpressionEdit.SelText

#### Syntax

[ExpressionEdit](expressionedit.html).SelText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Use this property to obtain or replace the currently selected text.

#### Remarks

This property is a portion of the displayed text which is a localized expression.

#### See Also

[ExpressionEdit.DisplayText](expressionedit-displaytext.html)

[ExpressionEdit.SelLength](expressionedit-sellength.html)

[ExpressionEdit.SelStart](expressionedit-selstart.html)

[ExpressionEdit.Text](expressionedit-text.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-setadditionalevaluationconstan.html language=enus -->
## TOPIC 05105: ExpressionEdit.SetAdditionalEvaluationConstants

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-setadditionalevaluationconstan.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-setadditionalevaluationconstan.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SetAdditionalEvaluationConstants( val) Purpose Use this method to specify additional constants that the expression can contain that are not part of the Context . The ExpressionEdit control does not consider an identifier that has the same name as one of these constants as an er

### ExpressionEdit.SetAdditionalEvaluationConstants

#### Syntax

[ExpressionEdit](expressionedit.html).SetAdditionalEvaluationConstants( val)

#### Purpose

Use this method to specify additional constants that the expression can contain that are not part of the
 [Context](expressionedit-context.html)
 . The ExpressionEdit control does not consider an identifier that has the same name as one of these constants as an error.

#### Remarks

This method is useful when the expression can contain a constant from an enumeration, such as a parameter value of a module call when the type of that parameter is an enumeration.

#### Parameters

val
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies variables that are valid in the expression but are not part of the context. For example, include a numeric or string
 
 [PropertyObject](../tsapiref/propertyobject.html)
 where the name and value of the object are the name and value of the enumeration or constant. The control ignores subproperties of the object.

#### See Also

[ExpressionEdit.Context](expressionedit-context.html)

[ExpressionEdit.GetAdditionalEvaluationConstants](expressionedit-getadditionalevaluationconstan.html)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-setvalidevaluationtypes.html language=enus -->
## TOPIC 05106: ExpressionEdit.SetValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-setvalidevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-setvalidevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SetValidEvaluationTypes( val) Purpose Sets the valid evaluation types. Parameters val As EvaluationTypes [In] Specifies the expected types for evaluating an expression. See Also EvaluationTypes ExpressionEdit.GetValidEvaluationTypes

### ExpressionEdit.SetValidEvaluationTypes

#### Syntax

[ExpressionEdit](expressionedit.html).SetValidEvaluationTypes( val)

#### Purpose

Sets the valid evaluation types.

#### Parameters

val
 As
 
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[In] Specifies the expected types for evaluating an expression.

#### See Also

[EvaluationTypes](../tsapiref/evaluationtypes.html)

[ExpressionEdit.GetValidEvaluationTypes](expressionedit-getvalidevaluationtypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-showdisplaynamewheninactive.html language=enus -->
## TOPIC 05107: ExpressionEdit.ShowDisplayNameWhenInactive

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-showdisplaynamewheninactive.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-showdisplaynamewheninactive.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.ShowDisplayNameWhenInactive Data Type Boolean Purpose When this property is True and the text in the ExpressionEdit control corresponds to the value of an item in the drop-down list and the item has a DisplayName , the ExpressionEdit control shows the DisplayName of the item in

### ExpressionEdit.ShowDisplayNameWhenInactive

#### Syntax

[ExpressionEdit](expressionedit.html).ShowDisplayNameWhenInactive

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 and the text in the ExpressionEdit control corresponds to the value of an item in the drop-down list and the item has a
 [DisplayName](expressioneditcomboboxitem-displayname.html)
 , the ExpressionEdit control shows the DisplayName of the item instead of the text when the ExpressionEdit control is inactive.

#### Remarks

The ExpressionEdit control uses this property only when the style is
 ExpressionEditStyle_DropDownCombo
 .

#### See Also

[ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)

[ExpressionEditStyles](expressioneditstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-style.html language=enus -->
## TOPIC 05108: ExpressionEdit.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Style Data Type ExpressionEditStyles Use the following constants with this data type: ExpressionEditStyle_DropDownCombo –(Value: 1) Specifies that the ExpressionEdit control is a combo box control. ExpressionEditStyle_Edit –(Value: 0) Specifies that the ExpressionEdit control i

### ExpressionEdit.Style

#### Syntax

[ExpressionEdit](expressionedit.html).Style

#### Data Type

[ExpressionEditStyles](expressioneditstyles.html)

Use the following constants with this data type:

- ExpressionEditStyle_DropDownCombo 
 –(Value: 1) Specifies that the ExpressionEdit control is a combo box control.
- ExpressionEditStyle_Edit 
 –(Value: 0) Specifies that the ExpressionEdit control is an edit control.

#### Purpose

Specifies the appearance of the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-syntaxhighlightingenabled.html language=enus -->
## TOPIC 05109: ExpressionEdit.SyntaxHighlightingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-syntaxhighlightingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-syntaxhighlightingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.SyntaxHighlightingEnabled Data Type Boolean Purpose Specifies whether the ExpressionEdit control displays different text elements, such as numbers, strings, and comments, in different colors and styles. Remarks Do not use this property to display text that is not an expression

### ExpressionEdit.SyntaxHighlightingEnabled

#### Syntax

[ExpressionEdit](expressionedit.html).SyntaxHighlightingEnabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the ExpressionEdit control displays different text elements, such as numbers, strings, and comments, in different colors and styles.

#### Remarks

Do not use this property to display text that is not an expression in an ExpressionEdit control. Instead, set the
 [ExpressionEdit.TextType](expressionedit-texttype.html)
 property to
 TextType_PlainText
 .

#### See Also

[ExpressionEdit.TextType](expressionedit-texttype.html)

[TextTypes](texttypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-text.html language=enus -->
## TOPIC 05110: ExpressionEdit.Text

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-text.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-text.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.Text Data Type String Purpose Specifies a delocalized expression for the text in the ExpressionEdit control. The value of the ExpressionEdit.DisplayText property updates when you set this property. Remarks When the ExpressionEdit.TextType property is TextType_PlainText , this p

### ExpressionEdit.Text

#### Syntax

[ExpressionEdit](expressionedit.html).Text

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a delocalized expression for the text in the ExpressionEdit control. The value of the
 [ExpressionEdit.DisplayText](expressionedit-displaytext.html)
 property updates when you set this property.

#### Remarks

When the
 [ExpressionEdit.TextType](expressionedit-texttype.html)
 property is
 TextType_PlainText
 , this property specifies the actual text in the ExpressionEdit control rather than a delocalized version of the text. Refer to the
 
 [Engine.LocalizeExpression](../tsapiref/engine-localizeexpression.html)
 and
 
 [Engine.DelocalizeExpression](../tsapiref/engine-delocalizeexpression.html)
 methods for more information about localized and delocalized expressions.

#### See Also

[Engine.DelocalizeExpression](../tsapiref/engine-delocalizeexpression.html)

[Engine.LocalizeExpression](../tsapiref/engine-localizeexpression.html)

[ExpressionEdit.DisplayText](expressionedit-displaytext.html)

[ExpressionEdit.MaxLength](expressionedit-maxlength.html)

[ExpressionEdit.SelText](expressionedit-seltext.html)

[ExpressionEdit.TextLength](expressionedit-textlength.html)

[ExpressionEdit.TextType](expressionedit-texttype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-textlength.html language=enus -->
## TOPIC 05111: ExpressionEdit.TextLength

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-textlength.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-textlength.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.TextLength Data Type Long Purpose Returns the number of characters in the ExpressionEdit control text. See Also ExpressionEdit.MaxLength ExpressionEdit.SelLength ExpressionEdit.SelStart ExpressionEdit.Text

### ExpressionEdit.TextLength

#### Syntax

[ExpressionEdit](expressionedit.html).TextLength

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of characters in the ExpressionEdit control text.

#### See Also

[ExpressionEdit.MaxLength](expressionedit-maxlength.html)

[ExpressionEdit.SelLength](expressionedit-sellength.html)

[ExpressionEdit.SelStart](expressionedit-selstart.html)

[ExpressionEdit.Text](expressionedit-text.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-texttype.html language=enus -->
## TOPIC 05112: ExpressionEdit.TextType

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-texttype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-texttype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.TextType Data Type TextTypes Use the following constants with this data type: TextType_Expression –(Value: 1) Indicates the text in an ExpressionEdit control is an expression. TextType_ExpressionWithCppIdentifiers –(Value: 2) Indicates the text in an ExpressionEdit control is a

### ExpressionEdit.TextType

#### Syntax

[ExpressionEdit](expressionedit.html).TextType

#### Data Type

[TextTypes](texttypes.html)

Use the following constants with this data type:

- TextType_Expression 
 –(Value: 1) Indicates the text in an
 ExpressionEdit 
 control is an expression.
- TextType_ExpressionWithCppIdentifiers 
 –(Value: 2) Indicates the text in an ExpressionEdit control is an expression that might contain C++ scope resolution and template operators.
- TextType_PlainText 
 –(Value: 0) Indicates the text in an ExpressionEdit control is not an expression. The value of the
 ExpressionEdit.Text 
 property is equivalent to the value of the
 ExpressionEdit.DisplayText 
 property. This value makes an ExpressionEdit control behave like an edit or text box control. The ExpressionEdit control does not use syntax highlighting, perform error checking, perform autocompletion, or display function tips. The ExpressionEdit control context menu contains only menu items for text editing.

#### Purpose

Use this property to make an ExpressionEdit control behave like an ordinary edit or text box control. This is useful when you want to use an edit control for editing expressions and plain text.

#### See Also

[ExpressionEdit.DisplayText](expressionedit-displaytext.html)

[ExpressionEdit.Text](expressionedit-text.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-wantreturn.html language=enus -->
## TOPIC 05113: ExpressionEdit.WantReturn

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-wantreturn.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-wantreturn.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.WantReturn Data Type BooleanOrPreference Use the following constants with this data type: BooleanOrPreference_False –(Value: 0) Specifies a value of False . BooleanOrPreference_True –(Value: 1) Specifies a value of True . BooleanOrPreference_UsePreference –(Value: 3) Use the co

### ExpressionEdit.WantReturn

#### Syntax

[ExpressionEdit](expressionedit.html).WantReturn

#### Data Type

[BooleanOrPreference](booleanorpreference.html)

Use the following constants with this data type:

- BooleanOrPreference_False 
 –(Value: 0) Specifies a value of
 False 
 .
- BooleanOrPreference_True 
 –(Value: 1) Specifies a value of
 True 
 .
- BooleanOrPreference_UsePreference 
 –(Value: 3) Use the corresponding preference option in the
 Expression Editing Options 
 dialog box.

#### Purpose

Specifies whether the ExpressionEdit control processes the <Enter> key. When the ExpressionEdit control is not processing the <Enter> key, the <Enter> key goes to the default button.

- When the value of this property is
 BooleanOrPreference_False 
 , the <Enter> key goes to the default button.
- When the value of this property is
 BooleanOrPreference_True 
 , the control applies the <Enter> key to the expression.
- When the value of this property is
 BooleanOrPreference_UsePreference 
 , the Want Return option in the Expression Editing Options dialog box determines the setting.

#### Remarks

If the
 [ExpressionEdit.Multiline](expressionedit-multiline.html)
 property is
 False
 , this property is ignored and the <Enter> key is never processed.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.Multiline](expressionedit-multiline.html)

[ExpressionEdit.WordWrap](expressionedit-wordwrap.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit-wordwrap.html language=enus -->
## TOPIC 05114: ExpressionEdit.WordWrap

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit-wordwrap.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit-wordwrap.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEdit.WordWrap Data Type BooleanOrPreference Use the following constants with this data type: BooleanOrPreference_False –(Value: 0) Specifies a value of False . BooleanOrPreference_True –(Value: 1) Specifies a value of True . BooleanOrPreference_UsePreference –(Value: 3) Use the corr

### ExpressionEdit.WordWrap

#### Syntax

[ExpressionEdit](expressionedit.html).WordWrap

#### Data Type

[BooleanOrPreference](booleanorpreference.html)

Use the following constants with this data type:

- BooleanOrPreference_False 
 –(Value: 0) Specifies a value of
 False 
 .
- BooleanOrPreference_True 
 –(Value: 1) Specifies a value of
 True 
 .
- BooleanOrPreference_UsePreference 
 –(Value: 3) Use the corresponding preference option in the
 Expression Editing Options 
 dialog box.

#### Purpose

Specifies that lines too long to display on one line wrap to the next line.

- When the value of this property is
 BooleanOrPreference_False 
 , word wrap is off.
- When the value of this property is
 BooleanOrPreference_True 
 , word wrap is on.
- When the value of this property is
 BooleanOrPreference_UsePreference 
 , the Word Wrap option in the Expression Editing Options dialog box determines whether word wrap is on.

#### Remarks

When the
 [ExpressionEdit.Multiline](expressionedit-multiline.html)
 property is
 False
 , this property is ignored.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.Multiline](expressionedit-multiline.html)

[ExpressionEdit.WantReturn](expressionedit-wantreturn.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressionedit.html language=enus -->
## TOPIC 05115: ExpressionEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressionedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressionedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an ExpressionEdit control so users can edit a TestStand expression with syntax coloring, popup help, and statement completion. Although you typically do not need to edit expressions in a user interface application, you can connect a manager control to a read-only ExpressionEdit control to displa

### ExpressionEdit

Use an ExpressionEdit control so users can edit a TestStand expression with syntax coloring, popup help, and statement completion. Although you typically do not need to edit expressions in a user interface application, you can connect a manager control to a read-only ExpressionEdit control to display text information about the application state, such as the pathname of the sequence file selection or the name of the current user.

You can also use ExpressionEdit controls in dialog boxes for step types and in tools in which you prompt users to enter a TestStand expression.

#### Properties

| AllowEmpty |
| --- |
| ApplyDefaultStyle |
| AutoCompletionHwnd (Read Only) |
| AutomaticallyPrefixVariables |
| BackColor |
| Borders (Read Only) |
| BrowseExprDialogOptions |
| BrowseExprDialogTitle |
| Buttons (Read Only) |
| ComboBoxItems (Read Only) |
| Context |
| DisplayFormattedValue |
| DisplayText |
| DropDownListHwnd (Read Only) |
| Enabled |
| Engine |
| ErrorCheck |
| Font |
| FontSource |
| FunctionTipHwnd (Read Only) |
| HideSelection |
| hWnd (Read Only) |
| MaxLength |
| MouseIcon |
| MousePointer |
| Multiline |
| NumericFormat |
| ReadOnly |
| ScaleWithDPI |
| ScrollBars |
| SelLength |
| SelStart |
| SelText |
| ShowDisplayNameWhenInactive |
| Style |
| SyntaxHighlightingEnabled |
| Text |
| TextLength (Read Only) |
| TextType |
| WantReturn |
| WordWrap |

#### Methods

| CheckExpression |
| --- |
| DisplayBrowseExprDialog |
| DisplayError |
| Evaluate |
| GetAdditionalEvaluationConstants |
| GetValidEvaluationTypes |
| Localize |
| SelectAll |
| SetAdditionalEvaluationConstants |
| SetValidEvaluationTypes |

#### Events

| BorderDragged |
| --- |
| BrowseExprDialogClosed |
| BrowseExprDialogOpened |
| ButtonClick |
| Change |
| CheckExpression |
| Click |
| ConnectionActivity |
| ContextChanged |
| ContextMenuItemClick |
| CreateContextMenu |
| DblClick |
| DropDown |
| InsertComboBoxItem |
| KeyDown |
| KeyPress |
| KeyUp |
| MouseDown |
| MouseMove |
| MouseUp |
| SelChange |

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-backcolor.html language=enus -->
## TOPIC 05116: ExpressionEditButton.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.BackColor Data Type Color Purpose Specifies the background color for the ExpressionEdit button.

### ExpressionEditButton.BackColor

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color for the ExpressionEdit button.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-contextmenuitemcaption.html language=enus -->
## TOPIC 05117: ExpressionEditButton.ContextMenuItemCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-contextmenuitemcaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-contextmenuitemcaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.ContextMenuItemCaption Data Type String Purpose Set this property to a non-empty string to create a menu item in the ExpressionEdit control context menu for the ExpressionEdit button. Selecting the context menu item is equivalent to clicking the ExpressionEdit button. Rem

### ExpressionEditButton.ContextMenuItemCaption

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).ContextMenuItemCaption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Set this property to a non-empty string to create a menu item in the ExpressionEdit control context menu for the ExpressionEdit button. Selecting the context menu item is equivalent to clicking the ExpressionEdit button.

#### Remarks

Note

ContextMenuItemCaption

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-doclick.html language=enus -->
## TOPIC 05118: ExpressionEditButton.DoClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-doclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-doclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.DoClick Purpose Call this method to simulate a button click. Remarks You can call this method to simulate a button click when the button is disabled or invisible.

### ExpressionEditButton.DoClick

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).DoClick

#### Purpose

Call this method to simulate a button click.

#### Remarks

You can call this method to simulate a button click when the button is disabled or invisible.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-enabled.html language=enus -->
## TOPIC 05119: ExpressionEditButton.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.Enabled Data Type Boolean Purpose The control responds to user-generated events only when this property is True . Remarks The ExpressionEdit button is disabled when this property is False or the ExpressionEdit.Enabled property is False . See Also ExpressionEdit.Enabled Ex

### ExpressionEditButton.Enabled

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user-generated events only when this property is
 True
 .

#### Remarks

The ExpressionEdit button is disabled when this property is
 False
 or the
 [ExpressionEdit.Enabled](expressionedit-enabled.html)
 property is
 False
 .

#### See Also

[ExpressionEdit.Enabled](expressionedit-enabled.html)

[ExpressionEditButton.Visible](expressioneditbutton-visible.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-hwnd.html language=enus -->
## TOPIC 05120: ExpressionEditButton.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.hWnd Data Type Long Purpose Returns the Window handle of the ExpressionEdit button. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### ExpressionEditButton.hWnd

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the ExpressionEdit button.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-icon.html language=enus -->
## TOPIC 05121: ExpressionEditButton.Icon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-icon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-icon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.Icon Data Type Picture Purpose Specifies the picture the ExpressionEdit button displays. Remarks To programmatically add an icon to a custom button, store the icon in the <TestStand Public> \Components\Icons directory and use the following pseudocode to set the image to u

### ExpressionEditButton.Icon

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).Icon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the picture the ExpressionEdit button displays.

#### Remarks

To programmatically add an icon to a custom button, store the icon in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 directory and use the following pseudocode to set the image to use:

ExpressionEditButton.Icon = (stdole.IPictureDisp)Engine.Images.FindImage("MyIcon.ico", 16, 16)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-kind.html language=enus -->
## TOPIC 05122: ExpressionEditButton.Kind

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-kind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-kind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.Kind Data Type Long Purpose Specifies the type of ExpressionEdit button. Use the ExpressionEditButtonKinds constants with this property. See Also ExpressionEditButtonKinds

### ExpressionEditButton.Kind

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).Kind

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the type of ExpressionEdit button. Use the
 [ExpressionEditButtonKinds](expressioneditbuttonkinds.html)
 constants with this property.

#### See Also

[ExpressionEditButtonKinds](expressioneditbuttonkinds.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-shortcutkey.html language=enus -->
## TOPIC 05123: ExpressionEditButton.ShortcutKey

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-shortcutkey.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-shortcutkey.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.ShortcutKey Data Type ShortcutKeys Purpose Specifies a keyboard shortcut for clicking the ExpressionEdit button when the ExpressionEdit control is active. See Also ExpressionEditButton.ShortcutModifier ExpressionEditButtons ShortcutKeys

### ExpressionEditButton.ShortcutKey

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).ShortcutKey

#### Data Type

[ShortcutKeys](shortcutkeys.html)

#### Purpose

Specifies a keyboard shortcut for clicking the ExpressionEdit button when the ExpressionEdit control is active.

#### See Also

[ExpressionEditButton.ShortcutModifier](expressioneditbutton-shortcutmodifier.html)

[ExpressionEditButtons](expressioneditbuttons.html)

[ShortcutKeys](shortcutkeys.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-shortcutmodifier.html language=enus -->
## TOPIC 05124: ExpressionEditButton.ShortcutModifier

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-shortcutmodifier.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-shortcutmodifier.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.ShortcutModifier Data Type Long Purpose Specifies modifiers for a keyboard shortcut for clicking the ExpressionEdit button. Use any combination of the ShortcutModifiers constants. See Also ExpressionEditButton.ShortcutKey ExpressionEditButtons ShortcutModifiers

### ExpressionEditButton.ShortcutModifier

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).ShortcutModifier

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies modifiers for a keyboard shortcut for clicking the ExpressionEdit button. Use any combination of the
 [ShortcutModifiers](shortcutmodifiers.html)
 constants.

#### See Also

[ExpressionEditButton.ShortcutKey](expressioneditbutton-shortcutkey.html)

[ExpressionEditButtons](expressioneditbuttons.html)

[ShortcutModifiers](shortcutmodifiers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-style.html language=enus -->
## TOPIC 05125: ExpressionEditButton.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.Style Data Type ExpressionEditButtonStyles Use the following constants with this data type: ExpressionEditButtonStyle_Flat –(Value: 3) The button is flat. ExpressionEditButtonStyle_Standard –(Value: 2) The button is three-dimensional. ExpressionEditButtonStyle_System –(Va

### ExpressionEditButton.Style

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).Style

#### Data Type

[ExpressionEditButtonStyles](expressioneditbuttonstyles.html)

Use the following constants with this data type:

- ExpressionEditButtonStyle_Flat 
 –(Value: 3) The button is flat.
- ExpressionEditButtonStyle_Standard 
 –(Value: 2) The button is three-dimensional.
- ExpressionEditButtonStyle_System 
 –(Value: 1) The button looks like a standard button for the operating system of the user.
- ExpressionEditButtonStyle_ToolBarButton 
 –(Value: 4) This style is the same as
 ExpressionEditButtonStyle_System 
 except when the application supports Microsoft Windows XP themes, the button has no border when you hover over the button.

#### Purpose

Specifies the appearance of the button.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-tooltiptext.html language=enus -->
## TOPIC 05126: ExpressionEditButton.ToolTipText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-tooltiptext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-tooltiptext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.ToolTipText Data Type String Purpose Specifies the tooltip for the ExpressionEdit button.

### ExpressionEditButton.ToolTipText

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).ToolTipText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the tooltip for the ExpressionEdit button.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton-visible.html language=enus -->
## TOPIC 05127: ExpressionEditButton.Visible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton-visible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton-visible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButton.Visible Data Type Boolean Purpose Specifies whether the button is visible. See Also ExpressionEditButton.Enabled

### ExpressionEditButton.Visible

#### Syntax

[ExpressionEditButton](expressioneditbutton.html).Visible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the button is visible.

#### See Also

[ExpressionEditButton.Enabled](expressioneditbutton-enabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbutton.html language=enus -->
## TOPIC 05128: ExpressionEditButton

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbutton.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbutton.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An ExpressionEditButton can be a non-custom button, such as an Expression Browser button, which the ExpressionEdit control manages automatically. An ExpressionEditButton can also be a custom button. You can manage the custom button using the properties of an ExpressionEditButton. Properties BackColo

### ExpressionEditButton

An ExpressionEditButton can be a non-custom button, such as an Expression Browser button, which the
 [ExpressionEdit](expressionedit.html)
 control manages automatically. An ExpressionEditButton can also be a custom button. You can manage the custom button using the properties of an ExpressionEditButton.

#### Properties

| BackColor |
| --- |
| ContextMenuItemCaption |
| Enabled |
| hWnd (Read Only) |
| Icon |
| Kind |
| ShortcutKey |
| ShortcutModifier |
| Style |
| ToolTipText |
| Visible |

#### Method

| DoClick |
| --- |

#### See Also

[ExpressionEdit](expressionedit.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttonkinds.html language=enus -->
## TOPIC 05129: ExpressionEditButtonKinds

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttonkinds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttonkinds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEditButtons.Insert method and the ExpressionEditButton.Kind property. ExpressionEditButtonKind_BrowseExpression –(Value: 1) This kind of button calls the ExpressionEdit.DisplayBrowseExprDialog method. The ExpressionEditButton.Enabled , ExpressionEditButton.Icon

### ExpressionEditButtonKinds

Use these constants with the
 [ExpressionEditButtons.Insert](expressioneditbuttons-insert.html)
 method and the
 [ExpressionEditButton.Kind](expressioneditbutton-kind.html)
 property.

- ExpressionEditButtonKind_BrowseExpression 
 –(Value: 1) This kind of button calls the
 ExpressionEdit.DisplayBrowseExprDialog 
 method. The
 ExpressionEditButton.Enabled 
 ,
 ExpressionEditButton.Icon 
 ,
 ExpressionEditButton.ToolTipText 
 , and
 ExpressionEditButton.Visible 
 properties are managed automatically for this kind of button.
- ExpressionEditButtonKind_CheckExpression 
 –(Value: 2) This kind of button calls the
 ExpressionEdit.CheckExpression 
 method and displays the result in a dialog box. The
 ExpressionEditButton.Enabled 
 ,
 ExpressionEditButton.Icon 
 ,
 ExpressionEditButton.ToolTipText 
 , and
 ExpressionEditButton.Visible 
 properties are managed automatically for this kind of button.
- ExpressionEditButtonKind_CustomBase 
 –(Value: 1000) Use constants starting at
 ExpressionEditButtonKind_CustomBase 
 to define custom buttons. You define the behavior and appearance of custom buttons yourself. Use the
 ExpressionEdit.ButtonClick 
 event to respond to button clicks.

#### See Also

[ExpressionEdit.ButtonClick](expressionedit-buttonclick.html)

[ExpressionEdit.CheckExpression](expressionedit-checkexpression2.html)

[ExpressionEdit.DisplayBrowseExprDialog](expressionedit-displaybrowseexprdialog.html)

[ExpressionEditButtons.Insert](expressioneditbuttons-insert.html)

[ExpressionEditButton.Kind](expressioneditbutton-kind.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons-clear.html language=enus -->
## TOPIC 05130: ExpressionEditButtons.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButtons.Clear Purpose Removes all items from the collection. See Also ExpressionEditButtons.Remove

### ExpressionEditButtons.Clear

#### Syntax

[ExpressionEditButtons](expressioneditbuttons.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ExpressionEditButtons.Remove](expressioneditbuttons-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons-count.html language=enus -->
## TOPIC 05131: ExpressionEditButtons.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButtons.Count Data Type Long Purpose Returns the number of items in the collection. See Also ExpressionEditButtons.GetItem

### ExpressionEditButtons.Count

#### Syntax

[ExpressionEditButtons](expressioneditbuttons.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[ExpressionEditButtons.GetItem](expressioneditbuttons-getitem.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons-getitem.html language=enus -->
## TOPIC 05132: ExpressionEditButtons.GetItem

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons-getitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons-getitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButtons.GetItem( indexOrKind, specify) Return Value ExpressionEditButton Purpose Returns the ExpressionEdit button at the specified index or of the specified kind. Parameters indexOrKind As Long [In] When you pass SpecifyButton_ByIndex as the specify parameter, indexOrKind is th

### ExpressionEditButtons.GetItem

#### Syntax

[ExpressionEditButtons](expressioneditbuttons.html).GetItem( indexOrKind, specify)

#### Return Value

[ExpressionEditButton](expressioneditbutton.html)

#### Purpose

Returns the ExpressionEdit button at the specified index or of the specified kind.

#### Parameters

indexOrKind
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] When you pass
 SpecifyButton_ByIndex
 as the specify parameter,
 indexOrKind
 is the zero-based index of the button to return. When you pass
 SpecifyButton_ByKind
 , the first button in the collection with a kind of
 indexOrKind
 is returned or
 NULL
 is returned when no button with a kind of
 indexOrKind
 exists.

specify
 As
 [SpecifyExpressionEditButton](specifyexpressioneditbutton.html)

[In] Specifies whether
 indexOrKind
 is a button index or a button kind.

#### See Also

[ExpressionEditButtonKinds](expressioneditbuttonkinds.html)

[ExpressionEditButtons.Count](expressioneditbuttons-count.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons-insert.html language=enus -->
## TOPIC 05133: ExpressionEditButtons.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButtons.Insert( itemIndexParam, kind) Return Value ExpressionEditButton The button added to the collection. Purpose Adds a new item to the collection. Parameters itemIndexParam As Long [In] Specifies the zero-based index where the new button is inserted. Pass -1 to insert the Ex

### ExpressionEditButtons.Insert

#### Syntax

[ExpressionEditButtons](expressioneditbuttons.html).Insert( itemIndexParam, kind)

#### Return Value

[ExpressionEditButton](expressioneditbutton.html)

The button added to the collection.

#### Purpose

Adds a new item to the collection.

#### Parameters

itemIndexParam
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index where the new button is inserted. Pass
 -1
 to insert the ExpressionEdit button at the end of the collection.

kind
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Use the
 [ExpressionEditButtonKinds](expressioneditbuttonkinds.html)
 constants to specify what kind of ExpressionEdit button is created.

#### See Also

[ExpressionEditButtonKinds](expressioneditbuttonkinds.html)

[ExpressionEditButtons.Remove](expressioneditbuttons-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons-remove.html language=enus -->
## TOPIC 05134: ExpressionEditButtons.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditButtons.Remove( indexOrKind, specify) Purpose Removes the specified item from this collection, if it exists. Parameters indexOrKind As Long [In] When you pass SpecifyButton_ByIndex as the specify parameter, indexOrKind is the zero-based index of the button to remove from the col

### ExpressionEditButtons.Remove

#### Syntax

[ExpressionEditButtons](expressioneditbuttons.html).Remove( indexOrKind, specify)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

indexOrKind
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] When you pass
 SpecifyButton_ByIndex
 as the specify parameter,
 indexOrKind
 is the zero-based index of the button to remove from the collection. When you pass
 SpecifyButton_ByKind
 , all buttons with a kind of
 indexOrKind
 are removed from the collection.

specify
 As
 [SpecifyExpressionEditButton](specifyexpressioneditbutton.html)

[In] Specifies whether
 indexOrKind
 is a button index or a button kind.

#### See Also

[ExpressionEditButtonKinds](expressioneditbuttonkinds.html)

[ExpressionEditButtons.Clear](expressioneditbuttons-clear.html)

[ExpressionEditButtons.Insert](expressioneditbuttons-insert.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttons.html language=enus -->
## TOPIC 05135: ExpressionEditButtons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ExpressionEditButton objects. Use the ExpressionEdit.Buttons property to retrieve the ExpressionEditButtons object for an ExpressionEdit control. Property Count (Read Only) Methods Clear GetItem Insert Remove See Also ExpressionEdit ExpressionEdit.Buttons ExpressionEditButton

### ExpressionEditButtons

A collection of
 [ExpressionEditButton](expressioneditbutton.html)
 objects. Use the
 [ExpressionEdit.Buttons](expressionedit-buttons.html)
 property to retrieve the ExpressionEditButtons object for an
 [ExpressionEdit](expressionedit.html)
 control.

#### Property

| Count (Read Only) |
| --- |

#### Methods

| Clear |
| --- |
| GetItem |
| Insert |
| Remove |

#### See Also

[ExpressionEdit](expressionedit.html)

[ExpressionEdit.Buttons](expressionedit-buttons.html)

[ExpressionEditButton](expressioneditbutton.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditbuttonstyles.html language=enus -->
## TOPIC 05136: ExpressionEditButtonStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditbuttonstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditbuttonstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEditButton.Style property. ExpressionEditButtonStyle_Flat –(Value: 3) The button is flat. ExpressionEditButtonStyle_Standard –(Value: 2) The button is three-dimensional. ExpressionEditButtonStyle_System –(Value: 1) The button looks like a standard button for th

### ExpressionEditButtonStyles

Use these constants with the
 [ExpressionEditButton.Style](expressioneditbutton-style.html)
 property.

- ExpressionEditButtonStyle_Flat 
 –(Value: 3) The button is flat.
- ExpressionEditButtonStyle_Standard 
 –(Value: 2) The button is three-dimensional.
- ExpressionEditButtonStyle_System 
 –(Value: 1) The button looks like a standard button for the operating system of the user.
- ExpressionEditButtonStyle_ToolBarButton 
 –(Value: 4) This style is the same as
 ExpressionEditButtonStyle_System 
 except when the application supports Microsoft Windows XP themes, the button has no border when you hover over the button.

#### See Also

[ExpressionEditButton.Style](expressioneditbutton-style.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitem-displayname.html language=enus -->
## TOPIC 05137: ExpressionEditComboBoxItem.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitem-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitem-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItem.DisplayName Data Type String Purpose When this property is not empty, the display name is shown in the drop-down list instead of the ExpressionEditComboBoxItem.Value property. When you choose this item in the drop-down list, the ExpressionEditComboBoxItem.Value prop

### ExpressionEditComboBoxItem.DisplayName

#### Syntax

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html).DisplayName

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is not empty, the display name is shown in the drop-down list instead of the
 [ExpressionEditComboBoxItem.Value](expressioneditcomboboxitem-value.html)
 property. When you choose this item in the drop-down list, the
 ExpressionEditComboBoxItem.Value
 property, not the display name, replaces the existing text. This property is useful for displaying a simple name for a complex expression in the drop-down list.

#### See Also

[ExpressionEditComboBoxItem.Value](expressioneditcomboboxitem-value.html)

[ExpressionEdit.ShowDisplayNameWhenInactive](expressionedit-showdisplaynamewheninactive.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitem-icon.html language=enus -->
## TOPIC 05138: ExpressionEditComboBoxItem.Icon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitem-icon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitem-icon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItem.Icon Data Type Picture Purpose Specifies the picture that appears in the drop-down list for this item.

### ExpressionEditComboBoxItem.Icon

#### Syntax

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html).Icon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the picture that appears in the drop-down list for this item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitem-value.html language=enus -->
## TOPIC 05139: ExpressionEditComboBoxItem.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitem-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitem-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItem.Value Data Type String Purpose Specifies an expression that replaces the text in the ExpressionEdit control when the user selects this item in the drop-down list. The value appears in the drop-down list when the ExpressionEditComboBoxItem.DisplayName property is emp

### ExpressionEditComboBoxItem.Value

#### Syntax

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html).Value

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an expression that replaces the text in the ExpressionEdit control when the user selects this item in the drop-down list. The value appears in the drop-down list when the
 [ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)
 property is empty.

#### See Also

[ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitem.html language=enus -->
## TOPIC 05140: ExpressionEditComboBoxItem

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An ExpressionEditComboBoxItem is an item that appears in the drop-down list when the ExpressionEdit control is a combo box. Properties DisplayName Icon Value See Also ExpressionEdit

### ExpressionEditComboBoxItem

An ExpressionEditComboBoxItem is an item that appears in the drop-down list when the
 [ExpressionEdit](expressionedit.html)
 control is a combo box.

#### Properties

| DisplayName |
| --- |
| Icon |
| Value |

#### See Also

[ExpressionEdit](expressionedit.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems-clear.html language=enus -->
## TOPIC 05141: ExpressionEditComboBoxItems.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItems.Clear Purpose Removes all items from the drop-down list. See Also ExpressionEditComboBoxItems.Insert ExpressionEditComboBoxItems.Remove

### ExpressionEditComboBoxItems.Clear

#### Syntax

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html).Clear

#### Purpose

Removes all items from the drop-down list.

#### See Also

[ExpressionEditComboBoxItems.Insert](expressioneditcomboboxitems-insert.html)

[ExpressionEditComboBoxItems.Remove](expressioneditcomboboxitems-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems-count.html language=enus -->
## TOPIC 05142: ExpressionEditComboBoxItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItems.Count Data Type Long Purpose Returns the number of items in the collection. See Also ExpressionEditComboBoxItems.Item

### ExpressionEditComboBoxItems.Count

#### Syntax

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[ExpressionEditComboBoxItems.Item](expressioneditcomboboxitems-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems-insert.html language=enus -->
## TOPIC 05143: ExpressionEditComboBoxItems.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItems.Insert( itemIndexParam, val, displayName = "", icon = NULL) Return Value ExpressionEditComboBoxItem The item added to the drop-down list. Purpose Adds a new ExpressionEditComboBoxItem in the drop-down list. Parameters itemIndexParam As Long [In] Specifies the zero-

### ExpressionEditComboBoxItems.Insert

#### Syntax

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html).Insert( itemIndexParam, val, displayName = "", icon = NULL)

#### Return Value

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

The item added to the drop-down list.

#### Purpose

Adds a new
 [ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)
 in the drop-down list.

#### Parameters

itemIndexParam
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index where the new item is inserted. Pass
 -1
 to insert the item at the end of the drop-down list.

val
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [ExpressionEditComboBoxItem.Value](expressioneditcomboboxitem-value.html)
 property of the new item. This value appears in the drop-down list when the
 displayName
 parameter is empty.

displayName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)
 property of the new item. When this value is not empty, the display name is shown in the drop-down list for the item instead of the
 val
 parameter. Display names are useful for displaying a simple name for a complex expression in the drop-down list.

This parameter has a default value of
 ""
 .

icon
 As
 [Picture](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [ExpressionEditComboBoxItem.Icon](expressioneditcomboboxitem-icon.html)
 property of the new item. This method makes a copy of the picture you pass. You can use the
 ExpressionEditComboBoxItem.Icon
 property to either use a picture directly or make a copy of a picture.

This parameter has a default value of
 NULL
 .

#### See Also

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

[ExpressionEditComboBoxItem.DisplayName](expressioneditcomboboxitem-displayname.html)

[ExpressionEditComboBoxItem.Icon](expressioneditcomboboxitem-icon.html)

[ExpressionEditComboBoxItem.Value](expressioneditcomboboxitem-value.html)

[ExpressionEditComboBoxItems.Remove](expressioneditcomboboxitems-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems-item.html language=enus -->
## TOPIC 05144: ExpressionEditComboBoxItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItems.Item( itemIndexParam) Data Type ExpressionEditComboBoxItem Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndexParam As Long [In] Specifies the zero-based index of the item to return. See Also ExpressionEditComboBoxI

### ExpressionEditComboBoxItems.Item

#### Syntax

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html).Item( itemIndexParam)

#### Data Type

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndexParam
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to return.

#### See Also

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

[ExpressionEditComboBoxItems.Count](expressioneditcomboboxitems-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems-remove.html language=enus -->
## TOPIC 05145: ExpressionEditComboBoxItems.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExpressionEditComboBoxItems.Remove( itemIndexParam) Purpose Removes an item from the drop-down list. Parameters itemIndexParam As Long [In] Specifies the zero-based index of the item to remove from the drop-down list. See Also ExpressionEditComboBoxItems.Clear ExpressionEditComboBoxItems.Inse

### ExpressionEditComboBoxItems.Remove

#### Syntax

[ExpressionEditComboBoxItems](expressioneditcomboboxitems.html).Remove( itemIndexParam)

#### Purpose

Removes an item from the drop-down list.

#### Parameters

itemIndexParam
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to remove from the drop-down list.

#### See Also

[ExpressionEditComboBoxItems.Clear](expressioneditcomboboxitems-clear.html)

[ExpressionEditComboBoxItems.Insert](expressioneditcomboboxitems-insert.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditcomboboxitems.html language=enus -->
## TOPIC 05146: ExpressionEditComboBoxItems

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditcomboboxitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditcomboboxitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ExpressionEditComboBoxItem objects. Use the ExpressionEdit.ComboBoxItems property to retrieve the ExpressionEditComboBoxItems for an ExpressionEdit control. Properties Count (Read Only) Item (Read Only) Methods Clear Insert Remove See Also ExpressionEdit ExpressionEdit.ComboBoxItems

### ExpressionEditComboBoxItems

A collection of
 [ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)
 objects. Use the
 [ExpressionEdit.ComboBoxItems](expressionedit-comboboxitems.html)
 property to retrieve the ExpressionEditComboBoxItems for an
 [ExpressionEdit](expressionedit.html)
 control.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| Remove |

#### See Also

[ExpressionEdit](expressionedit.html)

[ExpressionEdit.ComboBoxItems](expressionedit-comboboxitems.html)

[ExpressionEditComboBoxItem](expressioneditcomboboxitem.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/expressioneditstyles.html language=enus -->
## TOPIC 05147: ExpressionEditStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/expressioneditstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/expressioneditstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEdit.Style property to specify the appearance of the control and how the control operates. ExpressionEditStyle_DropDownCombo –(Value: 1) Specifies that the ExpressionEdit control is a combo box control. ExpressionEditStyle_Edit –(Value: 0) Specifies that the Ex

### ExpressionEditStyles

Use these constants with the
 [ExpressionEdit.Style](expressionedit-style.html)
 property to specify the appearance of the control and how the control operates.

- ExpressionEditStyle_DropDownCombo 
 –(Value: 1) Specifies that the ExpressionEdit control is a combo box control.
- ExpressionEditStyle_Edit 
 –(Value: 0) Specifies that the ExpressionEdit control is an edit control.

#### See Also

[ExpressionEdit.Style](expressionedit-style.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/fontsources.html language=enus -->
## TOPIC 05148: FontSources

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/fontsources.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/fontsources.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with controls that have a FontSource property. FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(Value: 1) The default system fo

### FontSources

Use these constants with controls that have a
 FontSource
 property.

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnection-source.html language=enus -->
## TOPIC 05149: ImageConnection.Source

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnection-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnection-source.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnection.Source Data Type ImageSources Use the following constants with this data type: ImageSource_BatchState –(Value: 6) Displays an image that indicates the execution state of the batch that contains the current execution. This image source applies only to the ExecutionView Manager

### ImageConnection.Source

#### Syntax

[ImageConnection](imageconnection.html).Source

#### Data Type

[ImageSources](imagesources.html)

Use the following constants with this data type:

- ImageSource_BatchState 
 –(Value: 6) Displays an image that indicates the execution state of the batch that contains the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_BatchStatus 
 –(Value: 5) Displays an image that indicates the batch result status for the batch that contains the current execution. This image source applies only to the
 ExecutionView Manager 
 control.
- ImageSource_CurrentCallStackEntry 
 –(Value: 23) Displays a call stack icon for the selected stack frame in the current execution thread. When no current thread exists, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentExecution 
 –(Value: 21) Displays an execution icon when a current execution exists. Otherwise, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentProcessModelFile 
 –(Value: 24) Displays a sequence file icon when a process model exists for the currently executing or currently selected file. Otherwise, the image source displays an empty image. This image source applies to the
 ExecutionView Manager 
 and
 SequenceFileView Manager 
 controls.
- ImageSource_CurrentSequence 
 –(Value: 12) Displays a sequence icon when a currently executing or currently selected sequence exists. Otherwise, the image source displays an empty image. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentSequenceFile 
 –(Value: 11) Displays a sequence file icon when a currently executing or currently selected file exists. Otherwise, the image source displays an empty image. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentStep 
 –(Value: 14) Displays the icon for the current step in the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentStepGroup 
 –(Value: 13) Displays an image that indicates the currently executing or currently selected step group. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentThread 
 –(Value: 22) Displays a thread icon when a current thread for the current execution exists. When no current thread exists, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_ModelState 
 –(Value: 7) Displays an image that indicates the state of the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_NotASource 
 –(Value: 0) Guaranteed to never be a valid image source specifier.
- ImageSource_UUTStatus 
 –(Value: 3) Displays an image that indicates the result status of the unit under test for the current execution. This image source applies only to the ExecutionView Manager control.

#### Purpose

Specifies the type of ImageConnection to obtain an image from.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnection.html language=enus -->
## TOPIC 05150: ImageConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection to an image source. Property Source See Also ImageConnections

### ImageConnection

Represents a connection to an image source.

#### Property

| Source |
| --- |

#### See Also

[ImageConnections](imageconnections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-add.html language=enus -->
## TOPIC 05151: ImageConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.Add( uiObj) Return Value ImageConnection New ImageConnection. Purpose Creates and adds a new ImageConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ExecutionViewMgr.ConnectImage ImageConnections.Remove

### ImageConnections.Add

#### Syntax

[ImageConnections](imageconnections.html).Add( uiObj)

#### Return Value

[ImageConnection](imageconnection.html)

New ImageConnection.

#### Purpose

Creates and adds a new ImageConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)

[ImageConnections.Remove](imageconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-clear.html language=enus -->
## TOPIC 05152: ImageConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.Clear Purpose Removes all items from the collection. See Also ImageConnections.Remove

### ImageConnections.Clear

#### Syntax

[ImageConnections](imageconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ImageConnections.Remove](imageconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-count.html language=enus -->
## TOPIC 05153: ImageConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### ImageConnections.Count

#### Syntax

[ImageConnections](imageconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-fromcontrol.html language=enus -->
## TOPIC 05154: ImageConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.FromControl( uiObj) Return Value ImageConnection ImageConnection connected to the uiObj parameter. When no ImageConnection exists for this control, this method returns NULL . Purpose Returns the ImageConnection connected to the uiObj parameter. Parameters uiObj As Object [In]

### ImageConnections.FromControl

#### Syntax

[ImageConnections](imageconnections.html).FromControl( uiObj)

#### Return Value

[ImageConnection](imageconnection.html)

ImageConnection connected to the
 uiObj
 parameter. When no ImageConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the ImageConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-item.html language=enus -->
## TOPIC 05155: ImageConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.Item( itemIndex) Data Type ImageConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also ImageConnection ImageConnec

### ImageConnections.Item

#### Syntax

[ImageConnections](imageconnections.html).Item( itemIndex)

#### Data Type

[ImageConnection](imageconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[ImageConnection](imageconnection.html)

[ImageConnections.Count](imageconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections-remove.html language=enus -->
## TOPIC 05156: ImageConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ImageConnections.Remove( uiObj) Return Value Boolean Returns True when the ImageConnection is removed. Returns False when the ImageConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user interface objec

### ImageConnections.Remove

#### Syntax

[ImageConnections](imageconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the ImageConnection is removed. Returns
 False
 when the ImageConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[ImageConnections.Add](imageconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imageconnections.html language=enus -->
## TOPIC 05157: ImageConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imageconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imageconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ImageConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also ExecutionViewMgr.ConnectImage ImageConnection

### ImageConnections

A collection of
 [ImageConnection](imageconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)

[ImageConnection](imageconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/imagesources.html language=enus -->
## TOPIC 05158: ImageSources

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/imagesources.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/imagesources.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify types of image sources. Each image source provides an icon that indicates an aspect of the current application state. You can use these constants to connect an image to a StatusBar pane or button using the ExecutionViewMgr.ConnectImage or SequenceFileViewMgr.ConnectImage meth

### ImageSources

These constants specify types of image sources. Each image source provides an icon that indicates an aspect of the current application state. You can use these constants to connect an image to a StatusBar pane or button using the
 [ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)
 or
 [SequenceFileViewMgr.ConnectImage](sequencefileviewmgr-connectimage.html)
 methods.

To obtain an image name without connecting it to a control, call the
 [ApplicationMgr.GetImageName](applicationmgr-getimagename.html)
 ,
 [ExecutionViewMgr.GetImageName](executionviewmgr-getimagename.html)
 , or
 [SequenceFileViewMgr.GetImageName](sequencefileviewmgr-getimagename.html)
 method. An image name is an icon name you can use to retrieve an icon from the TestStand Engine.

An image source applies to all manager controls unless the help for the enumeration element specifies particular manager controls to which it applies.

- ImageSource_BatchState 
 –(Value: 6) Displays an image that indicates the execution state of the batch that contains the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_BatchStatus 
 –(Value: 5) Displays an image that indicates the batch result status for the batch that contains the current execution. This image source applies only to the
 ExecutionView Manager 
 control.
- ImageSource_CurrentCallStackEntry 
 –(Value: 23) Displays a call stack icon for the selected stack frame in the current execution thread. When no current thread exists, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentExecution 
 –(Value: 21) Displays an execution icon when a current execution exists. Otherwise, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentProcessModelFile 
 –(Value: 24) Displays a sequence file icon when a process model exists for the currently executing or currently selected file. Otherwise, the image source displays an empty image. This image source applies to the
 ExecutionView Manager 
 and
 SequenceFileView Manager 
 controls.
- ImageSource_CurrentSequence 
 –(Value: 12) Displays a sequence icon when a currently executing or currently selected sequence exists. Otherwise, the image source displays an empty image. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentSequenceFile 
 –(Value: 11) Displays a sequence file icon when a currently executing or currently selected file exists. Otherwise, the image source displays an empty image. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentStep 
 –(Value: 14) Displays the icon for the current step in the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_CurrentStepGroup 
 –(Value: 13) Displays an image that indicates the currently executing or currently selected step group. This image source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- ImageSource_CurrentThread 
 –(Value: 22) Displays a thread icon when a current thread for the current execution exists. When no current thread exists, the image source displays an empty image. This image source applies only to the ExecutionView Manager control.
- ImageSource_ModelState 
 –(Value: 7) Displays an image that indicates the state of the current execution. This image source applies only to the ExecutionView Manager control.
- ImageSource_NotASource 
 –(Value: 0) Guaranteed to never be a valid image source specifier.
- ImageSource_UUTStatus 
 –(Value: 3) Displays an image that indicates the result status of the unit under test for the current execution. This image source applies only to the ExecutionView Manager control.

#### See Also

[ApplicationMgr.GetImageName](applicationmgr-getimagename.html)

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)

[ExecutionViewMgr.GetImageName](executionviewmgr-getimagename.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectImage](sequencefileviewmgr-connectimage.html)

[SequenceFileViewMgr.GetImageName](sequencefileviewmgr-getimagename.html)

Parent topic:

Support UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-allowediting.html language=enus -->
## TOPIC 05159: InsertionPalette.AllowEditing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-allowediting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-allowediting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.AllowEditing Data Type Boolean Purpose Specifies whether you can modify the templates list and step types list panels of the control.

### InsertionPalette.AllowEditing

#### Syntax

[InsertionPalette](insertionpalette.html).AllowEditing

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether you can modify the templates list and step types list panels of the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-borderdragged.html language=enus -->
## TOPIC 05160: InsertionPalette.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To InsertionPalette Purpose Occurs when you drag a draggable border of a control. This event provides the location and size to which you must set the control for the draggable borders to track the

### InsertionPalette.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[InsertionPalette](insertionpalette.html)

#### Purpose

Occurs when you drag a draggable border of a control. This event provides the location and size to which you must set the control for the draggable borders to track the mouse cursor. However, you can choose to modify the location or size to which you set the control. For example, you can limit the width of the control so the left edge of the control cannot be dragged off of the visible portion of the window.

In addition to changing the size and position of the control, you can also update the sizes and positions of the other controls on the window to account for the change.

#### Remarks

If you are using LabVIEW, you must add the Horizontal and Vertical components of the origin of the LabVIEW front panel to the
 newX
 and
 newY
 event parameter values before you can use the
 newX
 and
 newY
 event parameters to set the ActiveX Container (AxCont) Left and Top properties for the control. To obtain the origin of a LabVIEW front panel, place an ActiveX property node on the block diagram of the VI, right-click the node, and select
 Link to»Pane
 from the context menu. Right-click the node again and select
 Select Property»Origin
 .

#### Parameters

bordersChanged
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies which borders you dragged. Refer to the
 [WhichBorders](whichborders.html)
 constants for more information about draggable borders.

newX
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new x-coordinate for the control.

newY
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new y-coordinate for the control.

newWidth
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new width for the control.

newHeight
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new height for the control.

finalResize
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the event is the final event for the drag operation the user performs.

#### See Also

[InsertionPalette.Borders](insertionpalette-borders.html)

[WhichBorders](whichborders.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-borders-property-page.html language=enus -->
## TOPIC 05161: InsertionPalette Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### InsertionPalette Borders Property Page

#### Borders Property Page

The property page contains the following controls:

- Control Frame 
 —This section contains the following options:
  - Visible 
 —The control displays a thin rectangular frame that surrounds the control.
  - Frame Location 
 —The location of the frame the control displays. The Frame Location ring control contains the following options:
    - Inside Borders 
 —The frame appears within the draggable borders of the control.
    - Outside Borders 
 —The frame appears around the draggable borders of the control.
  - Frame Style 
 —The appearance of the frame the control displays. The Frame Style ring control contains the following options:
    - Flat 
 —The frame appears flat.
    - Fixed Single 
 —The frame is a black line, one pixel thick.
    - Control Edge 
 —The frame has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings.
    - Raised 
 —The frame has a raised three-dimensional appearance.
    - Inset 
 —The frame has a sunken three-dimensional appearance.
- Drag Borders 
 —This section contains the following options:
  - Top Border 
 —A border at the top edge of the control.
  - Left Border 
 —A border at the left edge of the control.
  - Bottom Border 
 —A border at the bottom edge of the control.
  - Right Border 
 —A border at the right edge of the control.
  - Enable Border Drag Events 
 —The control displays a resizing cursor over the draggable borders and that the control generates
 BorderDragged 
 events when the user drags a draggable border with the mouse.
  - Edge Style 
 —The appearance of the border edge the control displays. The Edge Style contains the following options:
    - Flat 
 —The edge appears flat.
    - Fixed Single 
 —The edge is a black line, one pixel thick.
    - Control Edge 
 —The edge has the appearance of a control edge. The appearance can vary depending on the Windows appearance settings.
    - Raised 
 —The edge has a raised, three-dimensional appearance.
    - Inset 
 —The edge has a sunken, three-dimensional appearance.
  - Width 
 —The width, in pixels, of the draggable borders the control displays.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-borders.html language=enus -->
## TOPIC 05162: InsertionPalette.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders InsertionPalette.BorderDragged InsertionPalette.Borders

### InsertionPalette.Borders

#### Syntax

[InsertionPalette](insertionpalette.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[InsertionPalette.BorderDragged](insertionpalette-borderdragged.html)

[InsertionPalette.Borders](insertionpalette-borders.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-connectionactivity.html language=enus -->
## TOPIC 05163: InsertionPalette.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To InsertionPalette Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### InsertionPalette.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[InsertionPalette](insertionpalette.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-enabled.html language=enus -->
## TOPIC 05164: InsertionPalette.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.Enabled Data Type Boolean Purpose The control responds to user-generated events only when this property is True . Remarks When you connect this control to a manager control, the manager control automatically sets this property.

### InsertionPalette.Enabled

#### Syntax

[InsertionPalette](insertionpalette.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user-generated events only when this property is
 True
 .

#### Remarks

When you connect this control to a manager control, the manager control automatically sets this property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-hwnd.html language=enus -->
## TOPIC 05165: InsertionPalette.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.hWnd Data Type Long Purpose Returns a Window handle for the control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### InsertionPalette.hWnd

#### Syntax

[InsertionPalette](insertionpalette.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-keydown.html language=enus -->
## TOPIC 05166: InsertionPalette.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To InsertionPalette Purpose Occurs when the user presses any key while the control has the input focus. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] A combination of the K

### InsertionPalette.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[InsertionPalette](insertionpalette.html)

#### Purpose

Occurs when the user presses any key while the control has the input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] A combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[KeyCodes](keycodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-pages.html language=enus -->
## TOPIC 05167: InsertionPalette.Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-pages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-pages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.Pages Data Type InsertionPalettePages Purpose Returns a collection of the InsertionPalette pages. See Also InsertionPalette InsertionPalettePages

### InsertionPalette.Pages

#### Syntax

[InsertionPalette](insertionpalette.html).Pages

#### Data Type

[InsertionPalettePages](insertionpalettepages.html)

#### Purpose

Returns a collection of the
 [InsertionPalette](insertionpalette.html)
 pages.

#### See Also

[InsertionPalette](insertionpalette.html)

[InsertionPalettePages](insertionpalettepages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-palettelayout.html language=enus -->
## TOPIC 05168: InsertionPalette.PaletteLayout

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-palettelayout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-palettelayout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.PaletteLayout Data Type String Purpose Specifies a serialized string you use to persist the layout of the control. Use the serialized string to later restore the layout of the control. Remarks The layout information is composed of the state of the nodes in the Step Types list

### InsertionPalette.PaletteLayout

#### Syntax

[InsertionPalette](insertionpalette.html).PaletteLayout

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a serialized string you use to persist the layout of the control. Use the serialized string to later restore the layout of the control.

#### Remarks

The layout information is composed of the state of the nodes in the Step Types list and the Templates list on the Insertion Palette pane, including information about the selected nodes and whether the nodes are expanded or collapsed.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette-scalewithdpi.html language=enus -->
## TOPIC 05169: InsertionPalette.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalette.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls

### InsertionPalette.ScaleWithDPI

#### Syntax

[InsertionPalette](insertionpalette.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

National Instruments recommends the following settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalette.html language=enus -->
## TOPIC 05170: InsertionPalette

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalette.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalette.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a SequenceFileView Manager control to an InsertionPalette control so users can insert steps and template items into a sequence file by dragging or double-clicking. Select Customize from the context menu of the Step Types list to launch the Step Type Menu Editor dialog box, in which you can c

### InsertionPalette

Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control to an InsertionPalette control so users can insert steps and template items into a sequence file by dragging or double-clicking.

Select
 Customize
 from the context menu of the Step Types list to launch the
 [Step Type Menu Editor](../tsref/step-type-menu-editor-dialog-box.html)
 dialog box, in which you can customize the structure of the menu.

You can add sequences, steps, or variables to the Templates list by dragging sequences, steps, or variables to the InsertionPalette control from a
 [ListBox](listbox.html)
 ,
 [ListBar](listbar.html)
 ,
 [SequenceView](sequenceview.html)
 , or
 [VariablesView](variablesview.html)
 control. You can rename, copy, paste, delete, import, and export the items in the Templates list using the context menu, and you can rearrange the items using drag and drop.

You can use one of the following operations to insert a step from the Step Types list or a sequence, step, or variable from the Templates list to a user interface control that displays a list of the corresponding object type:

- Double-click an item in the InsertionPalette control. TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Select an item in the InsertionPalette control and press <Enter>. TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Right-click an item in the InsertionPalette control and select
 Insert 
 from the context menu. TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Drag an item from the InsertionPalette control and drop the item in the corresponding user interface control that contains a list of the type of items.

#### Properties

| AllowEditing |
| --- |
| Borders (Read Only) |
| Enabled |
| hWnd (Read Only) |
| Pages (Read Only) |
| PaletteLayout |
| ScaleWithDPI |

#### Events

| BorderDragged |
| --- |
| ConnectionActivity |
| KeyDown |

#### See Also

[ListBar](listbar.html)

[ListBox](listbox.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceView](sequenceview.html)

[Step Type Menu Editor dialog box](../tsref/step-type-menu-editor-dialog-box.html)

[VariablesView](variablesview.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnection-steptypespage.html language=enus -->
## TOPIC 05171: InsertionPaletteConnection.StepTypesPage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnection-steptypespage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnection-steptypespage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnection.StepTypesPage Data Type Long Purpose Specifies the index of the Step Types page in the InsertionPalettePages collection. See Also InsertionPaletteConnection.TemplatesPage InsertionPalettePage InsertionPalettePages

### InsertionPaletteConnection.StepTypesPage

#### Syntax

[InsertionPaletteConnection](insertionpaletteconnection.html).StepTypesPage

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the index of the Step Types page in the
 [InsertionPalettePages](insertionpalettepages.html)
 collection.

#### See Also

[InsertionPaletteConnection.TemplatesPage](insertionpaletteconnection-templatespage.html)

[InsertionPalettePage](insertionpalettepage.html)

[InsertionPalettePages](insertionpalettepages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnection-templatespage.html language=enus -->
## TOPIC 05172: InsertionPaletteConnection.TemplatesPage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnection-templatespage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnection-templatespage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnection.TemplatesPage Data Type Long Purpose Specifies the index of the Templates page in the InsertionPalettePages collection. See Also InsertionPaletteConnection.StepTypesPage InsertionPalettePage InsertionPalettePages

### InsertionPaletteConnection.TemplatesPage

#### Syntax

[InsertionPaletteConnection](insertionpaletteconnection.html).TemplatesPage

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the index of the Templates page in the
 [InsertionPalettePages](insertionpalettepages.html)
 collection.

#### See Also

[InsertionPaletteConnection.StepTypesPage](insertionpaletteconnection-steptypespage.html)

[InsertionPalettePage](insertionpalettepage.html)

[InsertionPalettePages](insertionpalettepages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnection-uicontrol.html language=enus -->
## TOPIC 05173: InsertionPaletteConnection.UIControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnection-uicontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnection-uicontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnection.UIControl Data Type Object Purpose Returns the user interface control the connection connects to a SequenceFileView Manager control. See Also SequenceFileViewMgr

### InsertionPaletteConnection.UIControl

#### Syntax

[InsertionPaletteConnection](insertionpaletteconnection.html).UIControl

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the user interface control the connection connects to a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control.

#### See Also

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnection.html language=enus -->
## TOPIC 05174: InsertionPaletteConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from a SequenceFileView Manager control to an InsertionPalette control. The InsertionPalette control displays a list of step types and a list of user defined template steps, sequences, and variables. Use the connected control to insert a step, sequence, or variable into a seq

### InsertionPaletteConnection

Represents a connection from a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control to an
 [InsertionPalette](insertionpalette.html)
 control. The InsertionPalette control displays a list of step types and a list of user defined template steps, sequences, and variables. Use the connected control to insert a step, sequence, or variable into a sequence file.

#### Properties

| StepTypesPage |
| --- |
| TemplatesPage |
| UIControl (Read Only) |

#### See Also

[InsertionPalette](insertionpalette.html)

[SequenceFileView Manager](sequencefileviewmgr.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-add.html language=enus -->
## TOPIC 05175: InsertionPaletteConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.Add( uiObj) Return Value InsertionPaletteConnection New InsertionPaletteConnection object. Purpose Creates and adds a new InsertionPaletteConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also Executio

### InsertionPaletteConnections.Add

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).Add( uiObj)

#### Return Value

[InsertionPaletteConnection](insertionpaletteconnection.html)

New InsertionPaletteConnection object.

#### Purpose

Creates and adds a new InsertionPaletteConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionViewMgr.ConnectVariables](executionviewmgr-connectvariables.html)

[InsertionPaletteConnections.Remove](insertionpaletteconnections-remove.html)

[SequenceFileViewMgr.ConnectVariables](sequencefileviewmgr-connectvariables.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-clear.html language=enus -->
## TOPIC 05176: InsertionPaletteConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.Clear Purpose Removes all items from the collection. See Also InsertionPaletteConnections.Remove

### InsertionPaletteConnections.Clear

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[InsertionPaletteConnections.Remove](insertionpaletteconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-count.html language=enus -->
## TOPIC 05177: InsertionPaletteConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### InsertionPaletteConnections.Count

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-fromcontrol.html language=enus -->
## TOPIC 05178: InsertionPaletteConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.FromControl( uiObj) Return Value InsertionPaletteConnection InsertionPaletteConnection connected to this user interface object. When no InsertionPaletteConnection exists for this control, this method returns NULL . Purpose Returns the InsertionPaletteConnection con

### InsertionPaletteConnections.FromControl

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).FromControl( uiObj)

#### Return Value

[InsertionPaletteConnection](insertionpaletteconnection.html)

InsertionPaletteConnection connected to this user interface object. When no InsertionPaletteConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the InsertionPaletteConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-item.html language=enus -->
## TOPIC 05179: InsertionPaletteConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.Item( itemIndex) Data Type InsertionPaletteConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the zero-based index of the item to retrieve. See

### InsertionPaletteConnections.Item

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).Item( itemIndex)

#### Data Type

[InsertionPaletteConnection](insertionpaletteconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[InsertionPaletteConnection](insertionpaletteconnection.html)

[InsertionPaletteConnections.Count](insertionpaletteconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections-remove.html language=enus -->
## TOPIC 05180: InsertionPaletteConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPaletteConnections.Remove( uiObj) Return Value Boolean Returns True when the InsertionPaletteConnection is removed. Returns False when the InsertionPaletteConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] S

### InsertionPaletteConnections.Remove

#### Syntax

[InsertionPaletteConnections](insertionpaletteconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the InsertionPaletteConnection is removed. Returns
 False
 when the InsertionPaletteConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[InsertionPaletteConnections.Add](insertionpaletteconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpaletteconnections.html language=enus -->
## TOPIC 05181: InsertionPaletteConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpaletteconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpaletteconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of InsertionPaletteConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also InsertionPaletteConnection SequenceFileViewMgr.ConnectInsertionPalette

### InsertionPaletteConnections

A collection of
 [InsertionPaletteConnection](insertionpaletteconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[InsertionPaletteConnection](insertionpaletteconnection.html)

[SequenceFileViewMgr.ConnectInsertionPalette](sequencefileviewmgr-connectinsertionpalette.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage-expanded.html language=enus -->
## TOPIC 05182: InsertionPalettePage.Expanded

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage-expanded.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage-expanded.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePage.Expanded Data Type Boolean Purpose Specifies whether the content of the page is expanded to show the list. See Also InsertionPalettePage.Visible

### InsertionPalettePage.Expanded

#### Syntax

[InsertionPalettePage](insertionpalettepage.html).Expanded

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the content of the page is expanded to show the list.

#### See Also

[InsertionPalettePage.Visible](insertionpalettepage-visible.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage-index.html language=enus -->
## TOPIC 05183: InsertionPalettePage.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePage.Index Data Type Long Purpose Returns the zero-based index of the page on the InsertionPalette . See Also InsertionPalette

### InsertionPalettePage.Index

#### Syntax

[InsertionPalettePage](insertionpalettepage.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the zero-based index of the page on the
 [InsertionPalette](insertionpalette.html)
 .

#### See Also

[InsertionPalette](insertionpalette.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage-showsubpages.html language=enus -->
## TOPIC 05184: InsertionPalettePage.ShowSubPages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage-showsubpages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage-showsubpages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePage.ShowSubPages Data Type Boolean Purpose Specifies whether the content of the sub pages of the InsertionPalette page needs to be displayed. See Also InsertionPalettePage.Expanded InsertionPalettePage.SplitterRatio InsertionPalettePage.Visible

### InsertionPalettePage.ShowSubPages

#### Syntax

[InsertionPalettePage](insertionpalettepage.html).ShowSubPages

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the content of the sub pages of the InsertionPalette page needs to be displayed.

#### See Also

[InsertionPalettePage.Expanded](insertionpalettepage-expanded.html)

[InsertionPalettePage.SplitterRatio](insertionpalettepage-splitterratio.html)

[InsertionPalettePage.Visible](insertionpalettepage-visible.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage-splitterratio.html language=enus -->
## TOPIC 05185: InsertionPalettePage.SplitterRatio

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage-splitterratio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage-splitterratio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePage.SplitterRatio Data Type Float Purpose Specifies the percentage of the InsertionPalette the page uses. Changes to this property affect this property for other pages. This property is valid only when pages exist after the current page. In all other cases, this property is i

### InsertionPalettePage.SplitterRatio

#### Syntax

[InsertionPalettePage](insertionpalettepage.html).SplitterRatio

#### Data Type

[Float](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the percentage of the
 [InsertionPalette](insertionpalette.html)
 the page uses. Changes to this property affect this property for other pages.

Note

#### See Also

[InsertionPalette](insertionpalette.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage-visible.html language=enus -->
## TOPIC 05186: InsertionPalettePage.Visible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage-visible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage-visible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePage.Visible Data Type Boolean Purpose Specifies whether the page is visible. See Also InsertionPalettePage.Expanded

### InsertionPalettePage.Visible

#### Syntax

[InsertionPalettePage](insertionpalettepage.html).Visible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the page is visible.

#### See Also

[InsertionPalettePage.Expanded](insertionpalettepage-expanded.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepage.html language=enus -->
## TOPIC 05187: InsertionPalettePage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an InsertionPalettePage object to control whether a page is expanded or visible on an InsertionPalette control. Properties Expanded Index (Read Only) ShowSubPages SplitterRatio Visible See Also InsertionPalette

### InsertionPalettePage

Use an InsertionPalettePage object to control whether a page is expanded or visible on an
 [InsertionPalette](insertionpalette.html)
 control.

#### Properties

| Expanded |
| --- |
| Index (Read Only) |
| ShowSubPages |
| SplitterRatio |
| Visible |

#### See Also

[InsertionPalette](insertionpalette.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepages-count.html language=enus -->
## TOPIC 05188: InsertionPalettePages.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepages-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepages-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePages.Count Data Type Long Purpose Returns the number of items in the collection. See Also InsertionPalettePage

### InsertionPalettePages.Count

#### Syntax

[InsertionPalettePages](insertionpalettepages.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[InsertionPalettePage](insertionpalettepage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepages-item.html language=enus -->
## TOPIC 05189: InsertionPalettePages.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepages-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepages-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertionPalettePages.Item( itemIdx) Data Type InsertionPalettePage Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIdx As Long [In] Specifies the zero-based index of the item. See Also InsertionPalettePage

### InsertionPalettePages.Item

#### Syntax

[InsertionPalettePages](insertionpalettepages.html).Item( itemIdx)

#### Data Type

[InsertionPalettePage](insertionpalettepage.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item.

#### See Also

[InsertionPalettePage](insertionpalettepage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/insertionpalettepages.html language=enus -->
## TOPIC 05190: InsertionPalettePages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/insertionpalettepages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/insertionpalettepages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of InsertionPalettePage objects. Use the InsertionPalette.Pages property to retrieve the InsertionPalettePages object for an InsertionPalette . Use the InsertionPalettePage.Visible property to control whether the page is visible. Properties Count (Read Only) Item (Read Only) See Also In

### InsertionPalettePages

A collection of
 [InsertionPalettePage](insertionpalettepage.html)
 objects.

Use the
 [InsertionPalette.Pages](insertionpalette-pages.html)
 property to retrieve the InsertionPalettePages object for an
 [InsertionPalette](insertionpalette.html)
 . Use the
 [InsertionPalettePage.Visible](insertionpalettepage-visible.html)
 property to control whether the page is visible.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[InsertionPalette](insertionpalette.html)

[InsertionPalette.Pages](insertionpalette-pages.html)

[InsertionPalettePage](insertionpalettepage.html)

[InsertionPalettePage.Visible](insertionpalettepage-visible.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/keycodes.html language=enus -->
## TOPIC 05191: KeyCodes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/keycodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/keycodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify the virtual key codes for the KeyDown and KeyUp events. KeyCode_VK_0 –(Value: 0x30) The 0 key. KeyCode_VK_1 –(Value: 0x31) The 1 key. KeyCode_VK_2 –(Value: 0x32) The 2 key. KeyCode_VK_3 –(Value: 0x33) The 3 key. KeyCode_VK_4 –(Value: 0x34) The 4 key. KeyCode_VK_5 –(Value: 0x3

### KeyCodes

These constants specify the virtual key codes for the
 KeyDown
 and
 KeyUp
 events.

- KeyCode_VK_0 
 –(Value: 0x30) The 0 key.
- KeyCode_VK_1 
 –(Value: 0x31) The 1 key.
- KeyCode_VK_2 
 –(Value: 0x32) The 2 key.
- KeyCode_VK_3 
 –(Value: 0x33) The 3 key.
- KeyCode_VK_4 
 –(Value: 0x34) The 4 key.
- KeyCode_VK_5 
 –(Value: 0x35) The 5 key.
- KeyCode_VK_6 
 –(Value: 0x36) The 6 key.
- KeyCode_VK_7 
 –(Value: 0x37) The 7 key.
- KeyCode_VK_8 
 –(Value: 0x38) The 8 key.
- KeyCode_VK_9 
 –(Value: 0x39) The 9 key.
- KeyCode_VK_A 
 –(Value: 0x41) The A key.
- KeyCode_VK_ACCEPT 
 –(Value: 0x1E) The Input Method Editor (IME) Accept key.
- KeyCode_VK_ADD 
 –(Value: 0x6B) The Add key.
- KeyCode_VK_APPS 
 –(Value: 0x5D) The Applications key.
- KeyCode_VK_B 
 –(Value: 0x42) The B key.
- KeyCode_VK_BACK 
 –(Value: 0x08) The Backspace key.
- KeyCode_VK_C 
 –(Value: 0x43) The C key.
- KeyCode_VK_CANCEL 
 –(Value: 0x03) The Cancel key.
- KeyCode_VK_CAPITAL 
 –(Value: 0x14) The Caps Lock key.
- KeyCode_VK_CLEAR 
 –(Value: 0x0C) The Clear key.
- KeyCode_VK_CONTROL 
 –(Value: 0x11) The Ctrl key.
- KeyCode_VK_CONVERT 
 –(Value: 0x1C) The IME Convert key.
- KeyCode_VK_D 
 –(Value: 0x44) The D key.
- KeyCode_VK_DECIMAL 
 –(Value: 0x6E) The Decimal key.
- KeyCode_VK_DELETE 
 –(Value: 0x2E) The Delete key.
- KeyCode_VK_DIVIDE 
 –(Value: 0x6F) The Divide key.
- KeyCode_VK_DOWN 
 –(Value: 0x28) The Down Arrow key.
- KeyCode_VK_E 
 –(Value: 0x45) The E key.
- KeyCode_VK_END 
 –(Value: 0x23) The End key.
- KeyCode_VK_ESCAPE 
 –(Value: 0x1B) The Escape key.
- KeyCode_VK_EXECUTE 
 –(Value: 0x2B) The Execute key.
- KeyCode_VK_F 
 –(Value: 0x46) The F key.
- KeyCode_VK_F1 
 –(Value: 0x70) The F1 key.
- KeyCode_VK_F10 
 –(Value: 0x79) The F10 key.
- KeyCode_VK_F11 
 –(Value: 0x7A) The F11 key.
- KeyCode_VK_F12 
 –(Value: 0x7B) The F12 key.
- KeyCode_VK_F13 
 –(Value: 0x7C) The F13 key.
- KeyCode_VK_F14 
 –(Value: 0x7D) The F14 key.
- KeyCode_VK_F15 
 –(Value: 0x7E) The F15 key.
- KeyCode_VK_F16 
 –(Value: 0x7F) The F16 key.
- KeyCode_VK_F17 
 –(Value: 0x80) The F17 key.
- KeyCode_VK_F18 
 –(Value: 0x81) The F18 key.
- KeyCode_VK_F19 
 –(Value: 0x82) The F19 key.
- KeyCode_VK_F2 
 –(Value: 0x71) The F2 key.
- KeyCode_VK_F20 
 –(Value: 0x83) The F20 key.
- KeyCode_VK_F21 
 –(Value: 0x84) The F21 key.
- KeyCode_VK_F22 
 –(Value: 0x85) The F22 key.
- KeyCode_VK_F23 
 –(Value: 0x86) The F23 key.
- KeyCode_VK_F24 
 –(Value: 0x87) The F24 key.
- KeyCode_VK_F3 
 –(Value: 0x72) The F3 key.
- KeyCode_VK_F4 
 –(Value: 0x73) The F4 key.
- KeyCode_VK_F5 
 –(Value: 0x74) The F5 key.
- KeyCode_VK_F6 
 –(Value: 0x75) The F6 key.
- KeyCode_VK_F7 
 –(Value: 0x76) The F7 key.
- KeyCode_VK_F8 
 –(Value: 0x77) The F8 key.
- KeyCode_VK_F9 
 –(Value: 0x78) The F9 key.
- KeyCode_VK_FINAL 
 –(Value: 0x18) The Final key.
- KeyCode_VK_G 
 –(Value: 0x47) The G key.
- KeyCode_VK_H 
 –(Value: 0x48) The H key.
- KeyCode_VK_HANGEUL 
 –(Value: 0x15) The Hangeul key.
- KeyCode_VK_HANGUL 
 –(Value: 0x15) The Hangul key.
- KeyCode_VK_HANJA 
 –(Value: 0x19) The Hanja key.
- KeyCode_VK_HELP 
 –(Value: 0x2F) The Help key.
- KeyCode_VK_HOME 
 –(Value: 0x24) The Home key.
- KeyCode_VK_I 
 –(Value: 0x49) The I key.
- KeyCode_VK_INSERT 
 –(Value: 0x2D) The Insert key.
- KeyCode_VK_J 
 –(Value: 0x4A) The J key.
- KeyCode_VK_JUNJA 
 –(Value: 0x17) The Junja key.
- KeyCode_VK_K 
 –(Value: 0x4B) The K key.
- KeyCode_VK_KANA 
 –(Value: 0x15) The Kana key.
- KeyCode_VK_KANJI 
 –(Value: 0x19) The Kanji key.
- KeyCode_VK_L 
 –(Value: 0x4C) The L key.
- KeyCode_VK_LEFT 
 –(Value: 0x25) The Left Arrow key.
- KeyCode_VK_LWIN 
 –(Value: 0x5B) The Left Microsoft Windows key.
- KeyCode_VK_M 
 –(Value: 0x4D) The M key.
- KeyCode_VK_MENU 
 –(Value: 0x12) The Alt key.
- KeyCode_VK_MODECHANGE 
 –(Value: 0x1F) The IME Mode Change Request key.
- KeyCode_VK_MULTIPLY 
 –(Value: 0x6A) The Multiply key.
- KeyCode_VK_N 
 –(Value: 0x4E) The N key.
- KeyCode_VK_NEXT 
 –(Value: 0x22) The Page Down key.
- KeyCode_VK_NONCONVERT 
 –(Value: 0x1D) The IME Nonconvert key.
- KeyCode_VK_NUMLOCK 
 –(Value: 0x90) The Num Lock key.
- KeyCode_VK_NUMPAD0 
 –(Value: 0x60) The numeric keypad 0 key.
- KeyCode_VK_NUMPAD1 
 –(Value: 0x61) The numeric keypad 1 key.
- KeyCode_VK_NUMPAD2 
 –(Value: 0x62) The numeric keypad 2 key.
- KeyCode_VK_NUMPAD3 
 –(Value: 0x63) The numeric keypad 3 key.
- KeyCode_VK_NUMPAD4 
 –(Value: 0x64) The numeric keypad 4 key.
- KeyCode_VK_NUMPAD5 
 –(Value: 0x65) The numeric keypad 5 key.
- KeyCode_VK_NUMPAD6 
 –(Value: 0x66) The numeric keypad 6 key.
- KeyCode_VK_NUMPAD7 
 –(Value: 0x67) The numeric keypad 7 key.
- KeyCode_VK_NUMPAD8 
 –(Value: 0x68) The numeric keypad 8 key.
- KeyCode_VK_NUMPAD9 
 –(Value: 0x69) The numeric keypad 9 key.
- KeyCode_VK_O 
 –(Value: 0x4F) The O key.
- KeyCode_VK_P 
 –(Value: 0x50) The P key.
- KeyCode_VK_PAUSE 
 –(Value: 0x13) The Pause key.
- KeyCode_VK_PRINT 
 –(Value: 0x2A) The Print key.
- KeyCode_VK_PRIOR 
 –(Value: 0x21) The Page Up key.
- KeyCode_VK_Q 
 –(Value: 0x51) The Q key.
- KeyCode_VK_R 
 –(Value: 0x52) The R key.
- KeyCode_VK_RETURN 
 –(Value: 0x0D) The Enter key.
- KeyCode_VK_RIGHT 
 –(Value: 0x27) The Right Arrow key.
- KeyCode_VK_RWIN 
 –(Value: 0x5C) The Right Microsoft Windows key.
- KeyCode_VK_S 
 –(Value: 0x53) The S key.
- KeyCode_VK_SCROLL 
 –(Value: 0x91) The Scroll Lock key.
- KeyCode_VK_SELECT 
 –(Value: 0x29) The Select key.
- KeyCode_VK_SEPARATOR 
 –(Value: 0x6C) The Separator key.
- KeyCode_VK_SHIFT 
 –(Value: 0x10) The Shift key.
- KeyCode_VK_SNAPSHOT 
 –(Value: 0x2C) The Snapshot key.
- KeyCode_VK_SPACE 
 –(Value: 0x20) The Space key.
- KeyCode_VK_SUBTRACT 
 –(Value: 0x6D) The Subtract key.
- KeyCode_VK_T 
 –(Value: 0x54) The T key.
- KeyCode_VK_TAB 
 –(Value: 0x09) The Tab key.
- KeyCode_VK_U 
 –(Value: 0x55) The U key.
- KeyCode_VK_UP 
 –(Value: 0x26) The Up Arrow key.
- KeyCode_VK_V 
 –(Value: 0x56) The V key.
- KeyCode_VK_W 
 –(Value: 0x57) The W key.
- KeyCode_VK_X 
 –(Value: 0x58) The X key.
- KeyCode_VK_Y 
 –(Value: 0x59) The Y key.
- KeyCode_VK_Z 
 –(Value: 0x5A) The Z key.

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/keymodifiers.html language=enus -->
## TOPIC 05192: KeyModifiers

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/keymodifiers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/keymodifiers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify the state of the <Shift>, <Ctrl>, and <Alt> keys for the KeyDown , KeyUp , MouseDown , MouseUp , and MouseMove events. KeyModifier_Alt –(Value: 0x4) The <Alt> key is pressed. KeyModifier_Control –(Value: 0x2) The <Ctrl> key is pressed. KeyModifier_None –(Value: 0x0) The <Shif

### KeyModifiers

These constants specify the state of the <Shift>, <Ctrl>, and <Alt> keys for the
 KeyDown
 ,
 KeyUp
 ,
 MouseDown
 ,
 MouseUp
 , and
 MouseMove
 events.

- KeyModifier_Alt 
 –(Value: 0x4) The <Alt> key is pressed.
- KeyModifier_Control 
 –(Value: 0x2) The <Ctrl> key is pressed.
- KeyModifier_None 
 –(Value: 0x0) The <Shift>, <Ctrl>, and <Alt> keys are not pressed.
- KeyModifier_Shift 
 –(Value: 0x1) The <Shift> key is pressed.

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-alignment.html language=enus -->
## TOPIC 05193: Label.Alignment

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-alignment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-alignment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.Alignment Data Type AlignmentStyles Use the following constants with this data type: AlignmentStyle_Center –(Value: 2) Text is centered. AlignmentStyle_LeftJustify –(Value: 0) Text is left-aligned. AlignmentStyle_RightJustify –(Value: 1) Text is right-aligned. Purpose Specifies the alig

### Label.Alignment

#### Syntax

[Label](label.html).Alignment

#### Data Type

[AlignmentStyles](alignmentstyles.html)

Use the following constants with this data type:

- AlignmentStyle_Center 
 –(Value: 2) Text is centered.
- AlignmentStyle_LeftJustify 
 –(Value: 0) Text is left-aligned.
- AlignmentStyle_RightJustify 
 –(Value: 1) Text is right-aligned.

#### Purpose

Specifies the alignment of the text in the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-autosize.html language=enus -->
## TOPIC 05194: Label.AutoSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-autosize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-autosize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.AutoSize Data Type Boolean Purpose The control automatically resizes to display all the content when this property is True . The direction in which the control resizes varies depending on the alignment of the text and the value of the Label.WordWrap property. See Also Label.Alignment La

### Label.AutoSize

#### Syntax

[Label](label.html).AutoSize

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control automatically resizes to display all the content when this property is
 True
 . The direction in which the control resizes varies depending on the alignment of the text and the value of the
 [Label.WordWrap](label-wordwrap.html)
 property.

#### See Also

[Label.Alignment](label-alignment.html)

[Label.Caption](label-caption.html)

[Label.WordWrap](label-wordwrap.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-backcolor.html language=enus -->
## TOPIC 05195: Label.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.BackColor Data Type Color Purpose Specifies the background color for the control. See Also Label.ForeColor

### Label.BackColor

#### Syntax

[Label](label.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color for the control.

#### See Also

[Label.ForeColor](label-forecolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-borderstyle.html language=enus -->
## TOPIC 05196: Label.BorderStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-borderstyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-borderstyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.BorderStyle Data Type BorderStyles Use the following constants with this data type: BorderStyle_Fixed3D –(Value: 1) Specifies that the control draws a three-dimensional border. BorderStyle_FixedSingle –(Value: 2) Specifies that the control draws a single-line border. BorderStyle_NoBorde

### Label.BorderStyle

#### Syntax

[Label](label.html).BorderStyle

#### Data Type

[BorderStyles](borderstyles.html)

Use the following constants with this data type:

- BorderStyle_Fixed3D 
 –(Value: 1) Specifies that the control draws a three-dimensional border.
- BorderStyle_FixedSingle 
 –(Value: 2) Specifies that the control draws a single-line border.
- BorderStyle_NoBorder 
 –(Value: 0) Specifies that the control does not draw a border.

#### Purpose

Specifies the border style for the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-caption.html language=enus -->
## TOPIC 05197: Label.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.Caption Data Type String Purpose Specifies the text the control displays. Remarks Use this property to assign an accelerator character to a control when the Label.UseMnemonic property is True . In the caption, include an ampersand ( & ) immediately before the character you want to desig

### Label.Caption

#### Syntax

[Label](label.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the text the control displays.

#### Remarks

Use this property to assign an accelerator character to a control when the
 [Label.UseMnemonic](label-usemnemonic.html)
 property is
 True
 . In the caption, include an ampersand (
 &
 ) immediately before the character you want to designate as the accelerator character. The character is now underlined. Press <Alt> plus the underlined character to move the focus to the control.

To include an ampersand in a caption without creating an accelerator character, include two ampersands (
 &&
 ). A single ampersand is visible in the caption and no characters are underlined.

#### See Also

[Label.UseMnemonic](label-usemnemonic.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-change.html language=enus -->
## TOPIC 05198: Label.Change

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-change.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-change.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Change Applies To Label Purpose Occurs when you change the contents of the control.

### Label.Change

#### Syntax

ControlName_Change

#### Applies To

[Label](label.html)

#### Purpose

Occurs when you change the contents of the control.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-click.html language=enus -->
## TOPIC 05199: Label.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To Label Purpose Occurs when you press and release the mouse on the control. See Also Label.MouseDown Label.MouseMove Label.MouseUp

### Label.Click

#### Syntax

ControlName_Click

#### Applies To

[Label](label.html)

#### Purpose

Occurs when you press and release the mouse on the control.

#### See Also

[Label.MouseDown](label-mousedown.html)

[Label.MouseMove](label-mousemove.html)

[Label.MouseUp](label-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-connectionactivity.html language=enus -->
## TOPIC 05200: Label.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To Label Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### Label.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[Label](label.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-enabled.html language=enus -->
## TOPIC 05201: Label.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.Enabled Data Type Boolean Purpose When this property is False , the caption text dims.

### Label.Enabled

#### Syntax

[Label](label.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 False
 , the caption text dims.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-font.html language=enus -->
## TOPIC 05202: Label.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.Font Data Type Font Purpose Specifies the font for the control when the value of the Label.FontSource property is FontSource_UseFontProperty . See Also FontSources Label.BackColor Label.FontSource Label.ForeColor

### Label.Font

#### Syntax

[Label](label.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [Label.FontSource](label-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[Label.BackColor](label-backcolor.html)

[Label.FontSource](label-fontsource.html)

[Label.ForeColor](label-forecolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-fontsource.html language=enus -->
## TOPIC 05203: Label.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(Val

### Label.FontSource

#### Syntax

[Label](label.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 [Label.Font](label-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[Label.Font](label-font.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-forecolor.html language=enus -->
## TOPIC 05204: Label.ForeColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-forecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-forecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.ForeColor Data Type Color Purpose Specifies the foreground color for the control. See Also Label.BackColor Label.Font

### Label.ForeColor

#### Syntax

[Label](label.html).ForeColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the foreground color for the control.

#### See Also

[Label.BackColor](label-backcolor.html)

[Label.Font](label-font.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-localize.html language=enus -->
## TOPIC 05205: Label.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.Localize( sectionName) Purpose Localizes the text caption. Remarks First, update a .ini file located in the TestStand Language directory with the required string. Second, use the string tag in the .ini file as the caption for the control. When you call this method, the control replaces

### Label.Localize

#### Syntax

[Label](label.html).Localize( sectionName)

#### Purpose

Localizes the text caption.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required string. Second, use the string tag in the
 .ini
 file as the caption for the control.

When you call this method, the control replaces the caption with the string from the
 .ini
 file. If the caption is not a tag in the
 .ini
 file, the caption does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-mousedown.html language=enus -->
## TOPIC 05206: Label.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To Label Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a c

### Label.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[Label](label.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[Label.Click](label-click.html)

[Label.MouseMove](label-mousemove.html)

[Label.MouseUp](label-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-mouseicon.html language=enus -->
## TOPIC 05207: Label.MouseIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-mouseicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-mouseicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.MouseIcon Data Type Picture Purpose Specifies a custom mouse icon for the control. Remarks The control displays the specified picture as the cursor when the value of the Label.MousePointer property is MousePointer_Custom . When you set this property to NULL , the value of the Label.Mous

### Label.MouseIcon

#### Syntax

[Label](label.html).MouseIcon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a custom mouse icon for the control.

#### Remarks

The control displays the specified picture as the cursor when the value of the
 [Label.MousePointer](label-mousepointer.html)
 property is
 MousePointer_Custom
 . When you set this property to
 NULL
 , the value of the
 Label.MousePointer
 property changes to
 MousePointer_Default
 .

Note

#### See Also

[Label.MousePointer](label-mousepointer.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-mousemove.html language=enus -->
## TOPIC 05208: Label.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To Label Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a combin

### Label.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[Label](label.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[Label.Click](label-click.html)

[Label.MouseDown](label-mousedown.html)

[Label.MouseUp](label-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-mousepointer.html language=enus -->
## TOPIC 05209: Label.MousePointer

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-mousepointer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-mousepointer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.MousePointer Data Type MousePointerStyles Use the following constants with this data type: MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(Value: 2) MousePointer_Custom –(Value: 99) MousePointer_Def

### Label.MousePointer

#### Syntax

[Label](label.html).MousePointer

#### Data Type

[MousePointerStyles](mousepointerstyles.html)

Use the following constants with this data type:

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### Purpose

Specifies the appearance of the mouse cursor when the cursor is over the control.

#### Remarks

When the parameter is
 MousePointer_Custom
 , the mouse cursor is the picture the
 [Label.MouseIcon](label-mouseicon.html)
 property specifies.

#### See Also

[Label.MouseIcon](label-mouseicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-mouseup.html language=enus -->
## TOPIC 05210: Label.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To Label Purpose Occurs when the user releases the mouse on the control. This event occurs before the Label.Click event. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButton

### Label.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[Label](label.html)

#### Purpose

Occurs when the user releases the mouse on the control. This event occurs before the
 [Label.Click](label-click.html)
 event.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[Label.Click](label-click.html)

[Label.MouseDown](label-mousedown.html)

[Label.MouseMove](label-mousemove.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-scalewithdpi.html language=enus -->
## TOPIC 05211: Label.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are design

### Label.ScaleWithDPI

#### Syntax

[Label](label.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-usemnemonic.html language=enus -->
## TOPIC 05212: Label.UseMnemonic

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-usemnemonic.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-usemnemonic.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.UseMnemonic Data Type Boolean Purpose The label interprets the character that follows an ampersand ( & ) character in the Label.Caption property as an accelerator character when this property is True . See Also Label.Caption

### Label.UseMnemonic

#### Syntax

[Label](label.html).UseMnemonic

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The label interprets the character that follows an ampersand (
 &
 ) character in the
 [Label.Caption](label-caption.html)
 property as an accelerator character when this property is
 True
 .

#### See Also

[Label.Caption](label-caption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label-wordwrap.html language=enus -->
## TOPIC 05213: Label.WordWrap

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label-wordwrap.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label-wordwrap.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Label.WordWrap Data Type Boolean Purpose When this property is True , the Label can display multiple lines of text, and the Label breaks lines before a word that would extend past the right edge of the control. When this property is False , the Label always displays one line of text. Remarks

### Label.WordWrap

#### Syntax

[Label](label.html).WordWrap

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the Label can display multiple lines of text, and the Label breaks lines before a word that would extend past the right edge of the control. When this property is
 False
 , the Label always displays one line of text.

#### Remarks

When this property is
 True
 , the
 [Label.AutoSize](label-autosize.html)
 property causes the Label to expand vertically. When this property is
 False
 , the
 Label.AutoSize
 property causes the Label to expand horizontally.

#### See Also

[Label.AutoSize](label-autosize.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/label.html language=enus -->
## TOPIC 05214: Label

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/label.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/label.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a manager control to a Label control to display text information about the application state in the label, such as the name of the current user or the status of the current unit under test. Properties Alignment AutoSize BackColor BorderStyle Caption Enabled Font FontSource ForeColor MouseIco

### Label

Connect a manager control to a Label control to display text information about the application state in the label, such as the name of the current user or the status of the current unit under test.

#### Properties

| Alignment |
| --- |
| AutoSize |
| BackColor |
| BorderStyle |
| Caption |
| Enabled |
| Font |
| FontSource |
| ForeColor |
| MouseIcon |
| MousePointer |
| ScaleWithDPI |
| UseMnemonic |
| WordWrap |

#### Method

| Localize |
| --- |

#### Events

| Change |
| --- |
| Click |
| ConnectionActivity |
| MouseDown |
| MouseMove |
| MouseUp |

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-appearance-property-page.html language=enus -->
## TOPIC 05215: ListBar Appearance Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-appearance-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-appearance-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Appearance Property Page The Appearance property page contains the following controls, which you can use to define the visual appearance of the ListBar control: Selection Style —The style to use for selected items in the ListBar control. Frame Item —Displays a frame around the selected item. Highlig

### ListBar Appearance Property Page

#### Appearance Property Page

The Appearance property page contains the following controls, which you can use to define the visual appearance of the
 ListBar
 control:

- Selection Style 
 —The style to use for selected items in the
 ListBar 
 control.
  - Frame Item 
 —Displays a frame around the selected item.
  - Highlight Item Text 
 —Highlights the text of the selected item.
- Show Items Count 
 —Enable this option to show the number of items in a page on the
 ListBarPage 
 button along with the page caption.
- Display Icons Above Text 
 —Enable this option to place item icons above the item text in the
 ListBar 
 control. When this control is disabled, item icons are placed to the left of the item text in the
 ListBar 
 control.
- Selection Tracks Mouse Cursor 
 —Enable this option to highlight items on the
 ListBar 
 control when the mouse hovers over them.
- Show Tipstrips 
 —Enable this option to show tipstrips for partially visible items in the
 ListBar 
 control.
- Button Style 
 —The style to use for buttons in the
 ListBar 
 control.
  - 3D 
 —TestStand draws ListBarPage buttons as traditional, three-dimensional buttons.
  - Flat 
 —TestStand draws ListBarPage buttons with a flat frame for their borders.
- Icon Size 
 —The size of icons in the list bar. Icons are always square. For example, when you select 32 in the Icon Size control, the icon dimensions are 32 × 32 pixels.
- Show ScrollBar 
 —The scrollbar appears.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-backcolor.html language=enus -->
## TOPIC 05216: ListBar.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.BackColor Data Type Color Purpose Specifies the background color of the ListBar control. See Also ListBar.ButtonTextColor ListBar.PageTextColor

### ListBar.BackColor

#### Syntax

[ListBar](listbar.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the ListBar control.

#### See Also

[ListBar.ButtonTextColor](listbar-buttontextcolor.html)

[ListBar.PageTextColor](listbar-pagetextcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-borderdragged.html language=enus -->
## TOPIC 05217: ListBar.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To ListBar Purpose Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable borders t

### ListBar.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable borders to track the mouse cursor. However, you can choose to modify the location or size to which you set the control. For example, you can limit the width of the control so the left edge cannot be dragged off of the visible portion of the window.

In addition to changing the size and position of the control, you might also update the sizes and positions of the other controls on the window to account for the change.

#### Remarks

If you are using LabVIEW, you must add the Horizontal and Vertical components of the origin of the LabVIEW front panel to the
 newX
 and
 newY
 event parameter values before you can use the
 newX
 and
 newY
 event parameters to set the ActiveX Container (AxCont) Left and Top properties for the control. To obtain the origin of a LabVIEW front panel, place an ActiveX property node on the block diagram of the VI, right-click the node, and select
 Link to»Pane
 from the context menu. Right-click the node again and select
 Select Property»Origin
 .

#### Parameters

bordersChanged
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies which borders the user dragged. Refer to the
 [WhichBorders](whichborders.html)
 constants for more information about draggable borders.

newX
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new x-coordinate for the control.

newY
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new y-coordinate for the control.

newWidth
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new width for the control.

newHeight
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new height for the control.

finalResize
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the event is the final event for the drag operation the user performs.

#### See Also

[Borders](borders.html)

[WhichBorders](whichborders.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-borders-property-page.html language=enus -->
## TOPIC 05218: ListBar Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### ListBar Borders Property Page

#### Borders Property Page

The property page contains the following controls:

- Control Frame 
 —This section contains the following options:
  - Visible 
 —The control displays a thin rectangular frame that surrounds the control.
  - Frame Location 
 —The location of the frame the control displays. The Frame Location ring control contains the following options:
    - Inside Borders 
 —The frame appears within the draggable borders of the control.
    - Outside Borders 
 —The frame appears around the draggable borders of the control.
  - Frame Style 
 —The appearance of the frame the control displays. The Frame Style ring control contains the following options:
    - Flat 
 —The frame appears flat.
    - Fixed Single 
 —The frame is a black line, one pixel thick.
    - Control Edge 
 —The frame has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings.
    - Raised 
 —The frame has a raised three-dimensional appearance.
    - Inset 
 —The frame has a sunken three-dimensional appearance.
- Drag Borders 
 —This section contains the following options:
  - Top Border 
 —A border at the top edge of the control.
  - Left Border 
 —A border at the left edge of the control.
  - Bottom Border 
 —A border at the bottom edge of the control.
  - Right Border 
 —A border at the right edge of the control.
  - Enable Border Drag Events 
 —The control displays a resizing cursor over the draggable borders and that the control generates
 BorderDragged 
 events when the user drags a draggable border with the mouse.
  - Edge Style 
 —The appearance of the border edge the control displays. The Edge Style contains the following options:
    - Flat 
 —The edge appears flat.
    - Fixed Single 
 —The edge is a black line, one pixel thick.
    - Control Edge 
 —The edge has the appearance of a control edge. The appearance can vary depending on the Windows appearance settings.
    - Raised 
 —The edge has a raised, three-dimensional appearance.
    - Inset 
 —The edge has a sunken, three-dimensional appearance.
  - Width 
 —The width, in pixels, of the draggable borders the control displays.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-borders.html language=enus -->
## TOPIC 05219: ListBar.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders ListBar.BorderDragged

### ListBar.Borders

#### Syntax

[ListBar](listbar.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[ListBar.BorderDragged](listbar-borderdragged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-buttonfont.html language=enus -->
## TOPIC 05220: ListBar.ButtonFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-buttonfont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-buttonfont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ButtonFont Data Type Font Purpose Specifies the font of the button text on ListBar buttons. See Also FontSources ListBar.ButtonFontSource ListBar.PageFont

### ListBar.ButtonFont

#### Syntax

[ListBar](listbar.html).ButtonFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font of the button text on ListBar buttons.

#### See Also

[FontSources](fontsources.html)

[ListBar.ButtonFontSource](listbar-buttonfontsource.html)

[ListBar.PageFont](listbar-pagefont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-buttonfontsource.html language=enus -->
## TOPIC 05221: ListBar.ButtonFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-buttonfontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-buttonfontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ButtonFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFo

### ListBar.ButtonFontSource

#### Syntax

[ListBar](listbar.html).ButtonFontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 if you expect the font the
 [ListBar.ButtonFont](listbar-buttonfont.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[ListBar.ButtonFont](listbar-buttonfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-buttonstyle.html language=enus -->
## TOPIC 05222: ListBar.ButtonStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-buttonstyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-buttonstyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ButtonStyle Data Type ListBarButtonStyles Use the following constants with this data type: ListBarButtonStyle_3D –(Value: 1) The button style is three-dimensional. ListBarButtonStyle_Flat –(Value: 2) The button style is flat. Purpose Specifies the style of buttons on the ListBar contr

### ListBar.ButtonStyle

#### Syntax

[ListBar](listbar.html).ButtonStyle

#### Data Type

[ListBarButtonStyles](listbarbuttonstyles.html)

Use the following constants with this data type:

- ListBarButtonStyle_3D 
 –(Value: 1) The button style is three-dimensional.
- ListBarButtonStyle_Flat 
 –(Value: 2) The button style is flat.

#### Purpose

Specifies the style of buttons on the ListBar control.

#### See Also

[ListBar.PageStyle](listbar-pagestyle.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-buttontextcolor.html language=enus -->
## TOPIC 05223: ListBar.ButtonTextColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-buttontextcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-buttontextcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ButtonTextColor Data Type Color Purpose Specifies the color for the page captions displayed on the buttons in the ListBar control. See Also ListBar.BackColor ListBar.PageTextColor

### ListBar.ButtonTextColor

#### Syntax

[ListBar](listbar.html).ButtonTextColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the color for the page captions displayed on the buttons in the ListBar control.

#### See Also

[ListBar.BackColor](listbar-backcolor.html)

[ListBar.PageTextColor](listbar-pagetextcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-configure-pages-property-page.html language=enus -->
## TOPIC 05224: ListBar Configure Pages Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-configure-pages-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-configure-pages-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Pages Property Page The Configure Pages property page contains the following controls: Pages —List of pages in the control. Add —Adds a new page to the Pages listbox with a default name and caption. Remove —Removes the currently selected page from the Pages listbox. Up —Moves the currently

### ListBar Configure Pages Property Page

#### Configure Pages Property Page

The Configure Pages property page contains the following controls:

- Pages 
 —List of pages in the control.
- Add 
 —Adds a new page to the Pages listbox with a default name and caption.
- Remove 
 —Removes the currently selected page from the Pages listbox.
- Up 
 —Moves the currently selected page up one position.
- Down 
 —Moves the currently selected page down one position.
- Page Properties 
 —Uses the Name and Caption text boxes to edit the currently selected page in the Pages listbox.
  - Name 
 —Edits the name of the currently selected page in the Pages listbox. You can programmatically access a page in a ListBarPages collection by index or by page name.
  - Caption 
 —Edits the caption of the currently selected page in the Pages listbox.
  - Enabled 
 —Enables or disables the list bar page. Users cannot move the cursor when the page is disabled.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-connectionactivity.html language=enus -->
## TOPIC 05225: ListBar.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity, pageIndex) Applies To ListBar Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change. pageIndex As Long [In] Specifies the i

### ListBar.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity, pageIndex)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

pageIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the ListBarPage to which the connection made a change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-createcontextmenu.html language=enus -->
## TOPIC 05226: ListBar.CreateContextMenu

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-createcontextmenu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-createcontextmenu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CreateContextMenu( menuHandle, x, y) Applies To ListBar Purpose Occurs when the user right-clicks the control so the application can build a context menu from which the user can select commands. Although you can implement context menus in most environments without using this event

### ListBar.CreateContextMenu

#### Syntax

ControlName_CreateContextMenu( menuHandle, x, y)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user right-clicks the control so the application can build a context menu from which the user can select commands. Although you can implement context menus in most environments without using this event, some environments do not provide any other way to create a context menu. Also, creating a context menu using this event can be simpler in most environments, especially when the context menu contains only TestStand commands.

#### Parameters

menuHandle
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the Microsoft Windows menu handle (HMENU). When you add menu items to the menu handle, the control displays them in a context menu. Use the
 [Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)
 method to insert TestStand commands to the menu.

You can also use the menu functions in the Windows Software Development Kit (SDK) to add other menu items. Menu items you add this way do not have an associated TestStand command. When the user selects an item that does not have a TestStand command, the control creates and executes a Command object of kind
 CommandKind_Custom
 . The control stores the menu item identifier (resource ID/command ID) as a long in the
 [Command.UserData](command-userdata.html)
 property and as a decimal string in the command display name. You can handle either the
 [ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)
 or
 [ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)
 event to receive a notification when the user selects a menu item you insert with the Windows SDK.

When the context menu closes, the control disposes of the menu items. Thus, you do not need to dispose of menu items you insert.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the horizontal position of the right-mouse click, relative to the control.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the vertical position of the right-mouse click, relative to the control.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.UserData](command-userdata.html)

[Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-curpagechanged.html language=enus -->
## TOPIC 05227: ListBar.CurPageChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-curpagechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-curpagechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CurPageChanged( currentPage) Applies To ListBar Purpose Occurs when you select a new current page. Parameters currentPage As Long [In] Specifies the index of the selected page in ListBarPages . See Also ListBarPages

### ListBar.CurPageChanged

#### Syntax

ControlName_CurPageChanged( currentPage)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when you select a new current page.

#### Parameters

currentPage
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the selected page in
 [ListBarPages](listbarpages.html)
 .

#### See Also

[ListBarPages](listbarpages.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-currentpage.html language=enus -->
## TOPIC 05228: ListBar.CurrentPage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-currentpage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-currentpage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.CurrentPage Data Type Long Purpose Specifies the zero-based index of the current page in the ListBar control. Remarks The current page is the page in the ListBar control that displays the items of the page. Only one page is current in the ListBar control at a time. Use the ListBarPage

### ListBar.CurrentPage

#### Syntax

[ListBar](listbar.html).CurrentPage

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the zero-based index of the current page in the ListBar control.

#### Remarks

The current page is the page in the ListBar control that displays the items of the page. Only one page is current in the ListBar control at a time.

Use the
 [ListBarPages](listbarpages.html)
 collection to access a ListBarPage using the page index of the ListBarPage.

#### See Also

[ListBarPage.Caption](listbarpage-caption.html)

[ListBarPage.Cursor](listbarpage-cursor.html)

[ListBarPage.Name](listbarpage-name.html)

[ListBarPages](listbarpages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-cursormoved.html language=enus -->
## TOPIC 05229: ListBar.CursorMoved

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-cursormoved.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-cursormoved.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CursorMoved( itemIdx) Applies To ListBar Purpose Occurs when the user selects a new item in the current page. Parameters itemIdx As Long [In] Specifies the index of the element that became the cursor. See Also ListBar.CurrentPage ListBarPage.Cursor

### ListBar.CursorMoved

#### Syntax

ControlName_CursorMoved( itemIdx)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user selects a new item in the current page.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the element that became the cursor.

#### See Also

[ListBar.CurrentPage](listbar-currentpage.html)

[ListBarPage.Cursor](listbarpage-cursor.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-dblclick.html language=enus -->
## TOPIC 05230: ListBar.DblClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-dblclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-dblclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DblClick Applies To ListBar Purpose Occurs when the user double-clicks the left mouse button. See Also ListBar.CurPageChanged ListBar.CursorMoved

### ListBar.DblClick

#### Syntax

ControlName_DblClick

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user double-clicks the left mouse button.

#### See Also

[ListBar.CurPageChanged](listbar-curpagechanged.html)

[ListBar.CursorMoved](listbar-cursormoved.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-fonts-and-colors-property-page.html language=enus -->
## TOPIC 05231: ListBar Fonts and Colors Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-fonts-and-colors-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-fonts-and-colors-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fonts and Colors Property Page The Fonts and Colors property page contains the following controls, which allow you to change the font and color of various items on the ListBar control: Colors —Sets the color for the following items on the ListBar control: Button Text —The color of the text located o

### ListBar Fonts and Colors Property Page

#### Fonts and Colors Property Page

The Fonts and Colors property page contains the following controls, which allow you to change the font and color of various items on the
 ListBar
 control:

- Colors 
 —Sets the color for the following items on the
 ListBar 
 control:
  - Button Text 
 —The color of the text located on the buttons in the
 ListBar 
 control.
  - Item Text 
 —The text color of the items in the
 ListBar 
 control.
  - Background 
 —The background color of the
 ListBar 
 control.
- Fonts 
 —Sets the font for various parts of the control.
  - Font for the Item 
 —Selects which part of the control to change the font in.
    - Page Buttons 
 —Changes the font of ListBarPage buttons.
    - Page Items 
 —Changes the font of the items located inside of ListBarPages.
  - Font to Use 
 —The font for the
 ListBar 
 control. Set this option to Custom Font to choose any available font. Refer to the
 FontSources 
 enumeration for more information about this option.
  - Custom Font 
 —Displays the custom font specified for the item you select in the Font for the Item control. Click the
 Change 
 button to launch the Font dialog box. This option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring control. If you change the system language or apply a font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.
  - Change 
 —Launches the Font dialog box, in which you can specify a custom font.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-hittest.html language=enus -->
## TOPIC 05232: ListBar.HitTest

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-hittest.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-hittest.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.HitTest( x, y) Return Value Long Returns the index of an item on the current page. When no item exists at the specified location, this method returns -1 . Purpose Returns which item, if any, is at the specified location. Remarks Use this method to determine which item the given coordi

### ListBar.HitTest

#### Syntax

[ListBar](listbar.html).HitTest( x, y)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

Returns the index of an item on the current page. When no item exists at the specified location, this method returns
 -1
 .

#### Purpose

Returns which item, if any, is at the specified location.

#### Remarks

Use this method to determine which item the given coordinates belong to. For example, when a user clicks a control, you might want to determine which item on the current page the user clicked.

#### Parameters

x
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the location to test, in pixels, relative to the control.

y
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the location to test, in pixels, relative to the control.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-hwnd.html language=enus -->
## TOPIC 05233: ListBar.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.hWnd Data Type Long Purpose Returns a Window handle for the ListBar control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### ListBar.hWnd

#### Syntax

[ListBar](listbar.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the ListBar control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-iconsize.html language=enus -->
## TOPIC 05234: ListBar.IconSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-iconsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-iconsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.IconSize Data Type Long Purpose Specifies the size of icons in the ListBar control. Remarks Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icon are 32 × 32 pixels.

### ListBar.IconSize

#### Syntax

[ListBar](listbar.html).IconSize

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the size of icons in the ListBar control.

#### Remarks

Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icon are 32 × 32 pixels.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-keydown.html language=enus -->
## TOPIC 05235: ListBar.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To ListBar Purpose Occurs when the user presses a key while the ListBar control has focus. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of the KeyM

### ListBar.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user presses a key while the ListBar control has focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-localize.html language=enus -->
## TOPIC 05236: ListBar.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.Localize( sectionName) Purpose Localizes the captions of all pages. Remarks First, update a .ini file located in the TestStand Language directory with the required string. Second, use the string tag in the .ini file as the caption for the control. When you call this method, the contro

### ListBar.Localize

#### Syntax

[ListBar](listbar.html).Localize( sectionName)

#### Purpose

Localizes the captions of all pages.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required string. Second, use the string tag in the
 .ini
 file as the caption for the control.

When you call this method, the control replaces the caption with the string from the
 .ini
 file. If the caption is not a tag in the
 .ini
 file, the caption does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-mousedown.html language=enus -->
## TOPIC 05237: ListBar.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To ListBar Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a

### ListBar.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[ListBar.MouseMove](listbar-mousemove.html)

[ListBar.MouseUp](listbar-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-mousemove.html language=enus -->
## TOPIC 05238: ListBar.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To ListBar Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a comb

### ListBar.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[ListBar.MouseDown](listbar-mousedown.html)

[ListBar.MouseUp](listbar-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-mouseup.html language=enus -->
## TOPIC 05239: ListBar.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To ListBar Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a c

### ListBar.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[ListBar](listbar.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[ListBar.MouseDown](listbar-mousedown.html)

[ListBar.MouseMove](listbar-mousemove.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-pagefont.html language=enus -->
## TOPIC 05240: ListBar.PageFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-pagefont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-pagefont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.PageFont Data Type Font Purpose Specifies the font for items on a ListBar page. See Also ListBar.ButtonFont ListBar.PageFontSource

### ListBar.PageFont

#### Syntax

[ListBar](listbar.html).PageFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for items on a ListBar page.

#### See Also

[ListBar.ButtonFont](listbar-buttonfont.html)

[ListBar.PageFontSource](listbar-pagefontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-pagefontsource.html language=enus -->
## TOPIC 05241: ListBar.PageFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-pagefontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-pagefontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.PageFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont

### ListBar.PageFontSource

#### Syntax

[ListBar](listbar.html).PageFontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the ListBar control uses to display text on the page. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 [ListBar.PageFont](listbar-pagefont.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[ListBar.PageFont](listbar-pagefont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-pages.html language=enus -->
## TOPIC 05242: ListBar.Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-pages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-pages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.Pages Data Type ListBarPages Purpose Returns a collection of the ListBar pages. Remarks Refer to the ListBarPages object for information about adding, removing, and accessing pages. See Also ListBarPages

### ListBar.Pages

#### Syntax

[ListBar](listbar.html).Pages

#### Data Type

[ListBarPages](listbarpages.html)

#### Purpose

Returns a collection of the ListBar pages.

#### Remarks

Refer to the
 [ListBarPages](listbarpages.html)
 object for information about adding, removing, and accessing pages.

#### See Also

[ListBarPages](listbarpages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-pagestyle.html language=enus -->
## TOPIC 05243: ListBar.PageStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-pagestyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-pagestyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.PageStyle Data Type Long Purpose Specifies the style of the pages in the ListBar control. This property can be any combination of the ListBarPageStyles constants. See Also ListBar.ButtonStyle ListBarPageStyles

### ListBar.PageStyle

#### Syntax

[ListBar](listbar.html).PageStyle

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the style of the pages in the ListBar control. This property can be any combination of the
 [ListBarPageStyles](listbarpagestyles.html)
 constants.

#### See Also

[ListBar.ButtonStyle](listbar-buttonstyle.html)

[ListBarPageStyles](listbarpagestyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-pagetextcolor.html language=enus -->
## TOPIC 05244: ListBar.PageTextColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-pagetextcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-pagetextcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.PageTextColor Data Type Color Purpose Specifies the text color for page items. See Also ListBar.BackColor ListBar.ButtonTextColor

### ListBar.PageTextColor

#### Syntax

[ListBar](listbar.html).PageTextColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the text color for page items.

#### See Also

[ListBar.BackColor](listbar-backcolor.html)

[ListBar.ButtonTextColor](listbar-buttontextcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-scalewithdpi.html language=enus -->
## TOPIC 05245: ListBar.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are desi

### ListBar.ScaleWithDPI

#### Syntax

[ListBar](listbar.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-showitemcount.html language=enus -->
## TOPIC 05246: ListBar.ShowItemCount

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-showitemcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-showitemcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ShowItemCount Data Type Boolean Purpose When this property is True , the ListBar buttons display the number of items in each page, in addition to the page captions.

### ListBar.ShowItemCount

#### Syntax

[ListBar](listbar.html).ShowItemCount

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the ListBar buttons display the number of items in each page, in addition to the page captions.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-showitemtipstrips.html language=enus -->
## TOPIC 05247: ListBar.ShowItemTipStrips

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-showitemtipstrips.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-showitemtipstrips.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ShowItemTipStrips Data Type Boolean Purpose Specifies whether to enable item tooltips. When you set this property to True , tooltips are visible. Remarks Item tooltips are the text you see when you hover over a partially visible item with the mouse. Tooltips allow you to see the full

### ListBar.ShowItemTipStrips

#### Syntax

[ListBar](listbar.html).ShowItemTipStrips

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether to enable item tooltips. When you set this property to
 True
 , tooltips are visible.

#### Remarks

Item tooltips are the text you see when you hover over a partially visible item with the mouse. Tooltips allow you to see the full caption of a partially visible item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar-showscrollbar.html language=enus -->
## TOPIC 05248: ListBar.ShowScrollBar

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar-showscrollbar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar-showscrollbar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBar.ShowScrollBar Data Type Boolean Purpose Specifies whether to display a vertical scrollbar on the ListBarPage portion of the ListBar control when not enough room exists vertically to display all items in a ListBarPage.

### ListBar.ShowScrollBar

#### Syntax

[ListBar](listbar.html).ShowScrollBar

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether to display a vertical scrollbar on the ListBarPage portion of the ListBar control when not enough room exists vertically to display all items in a ListBarPage.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbar.html language=enus -->
## TOPIC 05249: ListBar

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a ListBar control to display multiple pages, where each page contains a list of items users can view or select. Connect a SequenceFileView Manager or ExecutionView Manager control to a ListBar page so users can view and select from a list, such as the active sequence file or execution. Connect a

### ListBar

Use a ListBar control to display multiple pages, where each page contains a list of items users can view or select. Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 or
 [ExecutionView Manager](executionviewmgr.html)
 control to a ListBar page so users can view and select from a list, such as the active sequence file or execution. Connect an
 [Application Manager](applicationmgr.html)
 control to a ListBar page so users can view or select the default adapter of the TestStand Engine.

You can view the contents of a page by clicking on the page node, and you can also select a single item with the current page. Use the
 ListBar.CurrentPage
 property to determine the selected page, and use
 Pages.Item(CurrentPage).Cursor
 to determine the selected item on the current page.

#### Properties

| BackColor |
| --- |
| Borders (Read Only) |
| ButtonFont |
| ButtonFontSource |
| ButtonStyle |
| ButtonTextColor |
| CurrentPage |
| hWnd (Read Only) |
| IconSize |
| PageFont |
| PageFontSource |
| Pages (Read Only) |
| PageStyle |
| PageTextColor |
| ScaleWithDPI |
| ShowItemCount |
| ShowItemTipStrips |
| ShowScrollBar |

#### Methods

| HitTest |
| --- |
| Localize |

#### Events

| BorderDragged |
| --- |
| ConnectionActivity |
| CreateContextMenu |
| CurPageChanged |
| CursorMoved |
| DblClick |
| KeyDown |
| MouseDown |
| MouseMove |
| MouseUp |

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarbuttonstyles.html language=enus -->
## TOPIC 05250: ListBarButtonStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarbuttonstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarbuttonstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ListBar.ButtonStyle property to specify the style of the button. ListBarButtonStyle_3D –(Value: 1) The button style is three-dimensional. ListBarButtonStyle_Flat –(Value: 2) The button style is flat. See Also ListBar.ButtonStyle

### ListBarButtonStyles

Use these constants with the
 [ListBar.ButtonStyle](listbar-buttonstyle.html)
 property to specify the style of the button.

- ListBarButtonStyle_3D 
 –(Value: 1) The button style is three-dimensional.
- ListBarButtonStyle_Flat 
 –(Value: 2) The button style is flat.

#### See Also

[ListBar.ButtonStyle](listbar-buttonstyle.html)

Parent topic:

Core UI Enumerations
