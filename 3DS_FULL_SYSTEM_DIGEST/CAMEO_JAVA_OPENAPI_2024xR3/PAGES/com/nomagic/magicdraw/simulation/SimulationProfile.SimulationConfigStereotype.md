# JAVA OPENAPI: SimulationProfile.SimulationConfigStereotype (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/simulation/SimulationProfile.SimulationConfigStereotype.html
- source_path: `com/nomagic/magicdraw/simulation/SimulationProfile.SimulationConfigStereotype.html`
- source_sha256: `37e13391b5271011a1771c50d3ec4a14658d85c79288fd36814b48c1a657268b`
- captured_utc: `2026-07-14T16:55:35.271232+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation](package-summary.html)

## Class SimulationProfile.SimulationConfigStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype

Enclosing class:
[SimulationProfile](SimulationProfile.html)

public static classSimulationProfile.SimulationConfigStereotype
extends [ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADDCONTROLPANEL](#ADDCONTROLPANEL)`
If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, add simulation control panel into the web UI.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALLOWCONCURRENTALLOCATEDACTIVITIES](#ALLOWCONCURRENTALLOCATEDACTIVITIES)`
Set to true, to execute allocated Activities simultaneously.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANIMATIONSPEED](#ANIMATIONSPEED)`
A preferred animation speed of the particular configuration.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOCONVERTUNITS](#AUTOCONVERTUNITS)`
Set to true for the units of the feature values connected via Binding Connector to be automatically converted if they have compatible types selected from the QUDV library.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOMATICPARAMETRICRECALCULATION](#AUTOMATICPARAMETRICRECALCULATION)`
Set to true for parametric models to be recalculated automatically when there is a change in any structural feature value.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOSTART](#AUTOSTART)`
When true, starts execution automatically from main MagicDraw toolbar.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOSTARTACTIVEOBJECTS](#AUTOSTARTACTIVEOBJECTS)`
If value is true, asynchronously starts behaviors of active classifiers (isActive=true) right after objects creation.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOTERMINATE](#AUTOTERMINATE)`
Set to true for the simulation to terminate when it completes or after the initialization phase if autoStart is set to false.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CAPTURETIMESTAMP](#CAPTURETIMESTAMP)`
If true, timestamp is recorded into a result instance name.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLOCK_RATIO](#CLOCK_RATIO)`
Ratio of the simulated time to modeled time.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLONEREFERENCES](#CLONEREFERENCES)`
If true, create new instances for all objects recursively, if not, only first level - others remain in original locations.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONSTRAINTFAILUREASBREAKPOINT](#CONSTRAINTFAILUREASBREAKPOINT)`
If the value is true, the simulation will be paused at the element which is the cause of the constraint failure.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DECIMALPLACES](#DECIMALPLACES)`
The number of digits following the decimal point
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DURATIONSIMULATIONMODE](#DURATIONSIMULATIONMODE)`
Duration simulation mode specifies the duration which will be used in the execution of the elements that have duration constraint applied.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ENDTIME](#ENDTIME)`
If this value and "startTime" are specified, the simulation will be stopped when the simulation time reaches this time value.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ENGINESPRIORITY](#ENGINESPRIORITY)`
Allows specifying execution engines priority and availability for particular execution.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXCLUDEDELEMENTS](#EXCLUDEDELEMENTS)`
A list of elements which will be excluded and not instantiated if not ready to be used or not needed, e.g.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXECUTIONLISTENERS](#EXECUTIONLISTENERS)`
The list of execution listener which will receive event from the model execution.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXECUTIONTARGET](#EXECUTIONTARGET)`
Reference to model element to be executed.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INITIALIZEREFERENCES](#INITIALIZEREFERENCES)`
If true, references will be initialized by creating new objects, instead of referencing to existing parts of the system.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INPUTPARAMETERS](#INPUTPARAMETERS)`
Use a SelectPropertiesConfig as the predefined list of inputs parameters.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOG](#LOG)`
Optional ExecutionLog element for execution events recording into special kind of model.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFRUNS](#NUMBEROFRUNS)`
A preferred number of runs of the particular configuration, especially as sample size in Monte Carlo simulation.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFSTEPS](#NUMBEROFSTEPS)`
If "stepSize" is not specified, but "startTime", "endTime", and "numberOfSteps" are specified.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPENSIMULATIONPANE](#OPENSIMULATIONPANE)`
Set to true, to open the Simulation pane when running a Simulation Configuration.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OUTPUTPARAMETERS](#OUTPUTPARAMETERS)`
Use a SelectPropertiesConfig as the predefined list of outputs parameters.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMEMBERFAILURESTATUS](#REMEMBERFAILURESTATUS)`
If the value is true, simulation will keep the first failure status until the termination and record it as 'fail' even though it was 'pass' at the end.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RESULTLOCATION](#RESULTLOCATION)`
Specify an instance specification or a package or an instance table for execution results recording.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RUNFORKSINPARALLEL](#RUNFORKSINPARALLEL)`
If this value is "true" or "undefined", all outgoing edges from Fork will run in parallel.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWACTIVESTATEIMAGES](#SHOWACTIVESTATEIMAGES)`
Select 'On Part shapes' to show active state images on Part shapes.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWACTIVESTATESONPARTSHAPES](#SHOWACTIVESTATESONPARTSHAPES)`
If true, active states are shown on Part shapes.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWANNOTATIONS](#SHOWANNOTATIONS)`
Set to true to enable simulation annotations in diagrams.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWFLOWINGINFORMATION](#SHOWFLOWINGINFORMATION)`
Set to true to show the label of a flowing item on a path.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWHELDTOKENSINACTIVITYDIAGRAMS](#SHOWHELDTOKENSINACTIVITYDIAGRAMS)`
Set to true to display held tokens that are displayed on Pins and Activity Parameter Nodes.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWRUNTIMEVALUESONPARTSHAPES](#SHOWRUNTIMEVALUESONPARTSHAPES)`
Set to true to display runtime values on Part shapes instead of the default values.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWRUNTIMEVALUESONPORTLABELS](#SHOWRUNTIMEVALUESONPORTLABELS)`
Set to true to display runtime values on Port and Constraint Parameters labels.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SILENT](#SILENT)`
When silent = true, animation is not used and artificial slowdown is disabled.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOLVEAFTERINITIALIZATION](#SOLVEAFTERINITIALIZATION)`
When true, invokes initial solving automatically.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STARTTIME](#STARTTIME)`
If value is specified, the simulation clock will be started with this value.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STARTUPDIAGRAM](#STARTUPDIAGRAM)`
Specify the diagram that is opened automatically when running a Simulation Configuration.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STARTWEBSERVER](#STARTWEBSERVER)`
If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, UI configs will be served as HTML pages.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEPDELAY](#STEPDELAY)`
If value is specified, the simulation clock will be delayed with this value for each time step.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEPSIZE](#STEPSIZE)`
If value is specified and more than 0, the simulation clock will use this value to step to increase the simulation time.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY](#TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY)`
If set to true, a streaming activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIMEUNIT](#TIMEUNIT)`
If value is specified, it will be the unit of the simulation time.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIMEVALUE](#TIMEVALUE)`
If a value is specified, it will be used as the simulation time for the model-based clock only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIMEVARIABLENAME](#TIMEVARIABLENAME)`
The time variable name which can be referred in any scripts to access the simulation time.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TREATALLCLASSIFIERSASACTIVE](#TREATALLCLASSIFIERSASACTIVE)`
If true, isActive property of all classifier will be treated as true for execution.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UI](#UI)`
References to all UI mockup configurations to be used in this execution.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[WATCHPROPERTIES](#WATCHPROPERTIES)`
Use a SelectPropertiesConfig as the predefined list of properties to monitor in the Watch
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[SimulationConfigStereotype](#%3Cinit%3E(com.nomagic.magicdraw.simulation.SimulationProfile))([SimulationProfile](SimulationProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addExcludedElements](#addExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addExecutionListeners](#addExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addInputParameters](#addInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addOutputParameters](#addOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addUI](#addUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`protected void`
`[clear](#clear())()`

`void`
`[clearAddControlPanel](#clearAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAllowConcurrentAllocatedActivities](#clearAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAnimationSpeed](#clearAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAutoConvertUnits](#clearAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAutomaticParametricRecalculation](#clearAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAutoStart](#clearAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAutostartActiveObjects](#clearAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearAutoTerminate](#clearAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearCaptureTimestamp](#clearCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearClockratio](#clearClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearCloneReferences](#clearCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearConstraintFailureAsBreakpoint](#clearConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDecimalPlaces](#clearDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearDurationSimulationMode](#clearDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearEndTime](#clearEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearEnginesPriority](#clearEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearExcludedElements](#clearExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearExecutionListeners](#clearExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearExecutionTarget](#clearExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearInitializeReferences](#clearInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearInputParameters](#clearInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLog](#clearLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfRuns](#clearNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfSteps](#clearNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearOpenSimulationPane](#clearOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearOutputParameters](#clearOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRememberFailureStatus](#clearRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearResultLocation](#clearResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearRunForksInParallel](#clearRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowActiveStateImages](#clearShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowActiveStatesOnPartShapes](#clearShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowAnnotations](#clearShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowFlowingInformation](#clearShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowHeldTokensInActivityDiagrams](#clearShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowRuntimeValuesOnPartShapes](#clearShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowRuntimeValuesOnPortLabels](#clearShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearSilent](#clearSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearSolveAfterInitialization](#clearSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStartTime](#clearStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStartupDiagram](#clearStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStartWebServer](#clearStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStepDelay](#clearStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearStepSize](#clearStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTerminateStreamingBehaviorsByOutputParameterMultiplicity](#clearTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTimeUnit](#clearTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTimeValue](#clearTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTimeVariableName](#clearTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTreatAllClassifiersAsActive](#clearTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearUI](#clearUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearWatchProperties](#clearWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAddControlPanelProperty](#getAddControlPanelProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAllowConcurrentAllocatedActivitiesProperty](#getAllowConcurrentAllocatedActivitiesProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getAnimationSpeed](#getAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAnimationSpeedProperty](#getAnimationSpeedProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAutoConvertUnitsProperty](#getAutoConvertUnitsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAutomaticParametricRecalculationProperty](#getAutomaticParametricRecalculationProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAutostartActiveObjectsProperty](#getAutostartActiveObjectsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAutoStartProperty](#getAutoStartProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getAutoTerminateProperty](#getAutoTerminateProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getCaptureTimestampProperty](#getCaptureTimestampProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClockratio](#getClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getClockratioProperty](#getClockratioProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getCloneReferencesProperty](#getCloneReferencesProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getConstraintFailureAsBreakpointProperty](#getConstraintFailureAsBreakpointProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getDecimalPlaces](#getDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDecimalPlacesProperty](#getDecimalPlacesProperty())()`

`[SimulationProfile.DurationSimulationModeEnum](SimulationProfile.DurationSimulationModeEnum.html)`
`[getDurationSimulationMode](#getDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getDurationSimulationModeProperty](#getDurationSimulationModeProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getEndTime](#getEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getEndTimeProperty](#getEndTimeProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEnginesPriority](#getEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getEnginesPriorityProperty](#getEnginesPriorityProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getExcludedElements](#getExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getExcludedElementsProperty](#getExcludedElementsProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getExecutionListeners](#getExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getExecutionListenersProperty](#getExecutionListenersProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getExecutionTarget](#getExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getExecutionTargetProperty](#getExecutionTargetProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getInitializeReferencesProperty](#getInitializeReferencesProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getInputParameters](#getInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getInputParametersProperty](#getInputParametersProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getLog](#getLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLogProperty](#getLogProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfRuns](#getNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfRunsProperty](#getNumberOfRunsProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfSteps](#getNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfStepsProperty](#getNumberOfStepsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getOpenSimulationPaneProperty](#getOpenSimulationPaneProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getOutputParameters](#getOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getOutputParametersProperty](#getOutputParametersProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRememberFailureStatusProperty](#getRememberFailureStatusProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getResultLocation](#getResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getResultLocationProperty](#getResultLocationProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getRunForksInParallelProperty](#getRunForksInParallelProperty())()`

`[SimulationProfile.ActiveStateImagesEnum](SimulationProfile.ActiveStateImagesEnum.html)`
`[getShowActiveStateImages](#getShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowActiveStateImagesProperty](#getShowActiveStateImagesProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowActiveStatesOnPartShapesProperty](#getShowActiveStatesOnPartShapesProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowAnnotationsProperty](#getShowAnnotationsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowFlowingInformationProperty](#getShowFlowingInformationProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowHeldTokensInActivityDiagramsProperty](#getShowHeldTokensInActivityDiagramsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowRuntimeValuesOnPartShapesProperty](#getShowRuntimeValuesOnPartShapesProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowRuntimeValuesOnPortLabelsProperty](#getShowRuntimeValuesOnPortLabelsProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSilentProperty](#getSilentProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSolveAfterInitializationProperty](#getSolveAfterInitializationProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getStartTime](#getStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStartTimeProperty](#getStartTimeProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getStartupDiagram](#getStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStartupDiagramProperty](#getStartupDiagramProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStartWebServerProperty](#getStartWebServerProperty())()`

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[getStepDelay](#getStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStepDelayProperty](#getStepDelayProperty())()`

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[getStepSize](#getStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getStepSizeProperty](#getStepSizeProperty())()`

`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty](#getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty())()`

`[SimulationProfile.TimeUnitKindEnum](SimulationProfile.TimeUnitKindEnum.html)`
`[getTimeUnit](#getTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTimeUnitProperty](#getTimeUnitProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getTimeValue](#getTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTimeValueProperty](#getTimeValueProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTimeVariableName](#getTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTimeVariableNameProperty](#getTimeVariableNameProperty())()`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getTreatAllClassifiersAsActiveProperty](#getTreatAllClassifiersAsActiveProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getUI](#getUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getUIProperty](#getUIProperty())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getWatchProperties](#getWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getWatchPropertiesProperty](#getWatchPropertiesProperty())()`

`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if stereotype of this wrapper is applied to given element.
`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAddControlPanel](#isAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAllowConcurrentAllocatedActivities](#isAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAutoConvertUnits](#isAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAutomaticParametricRecalculation](#isAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAutoStart](#isAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAutostartActiveObjects](#isAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isAutoTerminate](#isAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isCaptureTimestamp](#isCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isCloneReferences](#isCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isConstraintFailureAsBreakpoint](#isConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isInitializeReferences](#isInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isOpenSimulationPane](#isOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isRememberFailureStatus](#isRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isRunForksInParallel](#isRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowActiveStatesOnPartShapes](#isShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowAnnotations](#isShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowFlowingInformation](#isShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowHeldTokensInActivityDiagrams](#isShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowRuntimeValuesOnPartShapes](#isShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowRuntimeValuesOnPortLabels](#isShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isSilent](#isSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isSolveAfterInitialization](#isSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isStartWebServer](#isStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isTerminateStreamingBehaviorsByOutputParameterMultiplicity](#isTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isTreatAllClassifiersAsActive](#isTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeExcludedElements](#removeExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeExecutionListeners](#removeExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeInputParameters](#removeInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeOutputParameters](#removeOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeUI](#removeUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setAddControlPanel](#setAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAllowConcurrentAllocatedActivities](#setAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAnimationSpeed](#setAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setAutoConvertUnits](#setAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAutomaticParametricRecalculation](#setAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAutoStart](#setAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAutostartActiveObjects](#setAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setAutoTerminate](#setAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setCaptureTimestamp](#setCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setClockratio](#setClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setCloneReferences](#setCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setConstraintFailureAsBreakpoint](#setConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setDecimalPlaces](#setDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setDurationSimulationMode](#setDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.DurationSimulationModeEnum))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [SimulationProfile.DurationSimulationModeEnum](SimulationProfile.DurationSimulationModeEnum.html) value)`

`void`
`[setEndTime](#setEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setEnginesPriority](#setEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setExcludedElements](#setExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setExecutionListeners](#setExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setExecutionTarget](#setExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setInitializeReferences](#setInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setInputParameters](#setInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setLog](#setLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setNumberOfRuns](#setNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setNumberOfSteps](#setNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setOpenSimulationPane](#setOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setOutputParameters](#setOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setRememberFailureStatus](#setRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setResultLocation](#setResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setRunForksInParallel](#setRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowActiveStateImages](#setShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.ActiveStateImagesEnum))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [SimulationProfile.ActiveStateImagesEnum](SimulationProfile.ActiveStateImagesEnum.html) value)`

`void`
`[setShowActiveStatesOnPartShapes](#setShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowAnnotations](#setShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowFlowingInformation](#setShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowHeldTokensInActivityDiagrams](#setShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowRuntimeValuesOnPartShapes](#setShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowRuntimeValuesOnPortLabels](#setShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setSilent](#setSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setSolveAfterInitialization](#setSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setStartTime](#setStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setStartupDiagram](#setStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setStartWebServer](#setStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setStepDelay](#setStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)`

`void`
`[setStepSize](#setStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)`

`void`
`[setTerminateStreamingBehaviorsByOutputParameterMultiplicity](#setTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setTimeUnit](#setTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.TimeUnitKindEnum))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [SimulationProfile.TimeUnitKindEnum](SimulationProfile.TimeUnitKindEnum.html) value)`

`void`
`[setTimeValue](#setTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setTimeVariableName](#setTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setTreatAllClassifiersAsActive](#setTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setUI](#setUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setWatchProperties](#setWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getElement](../../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)), [getTagByName](../../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [isDerivedStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [toBoolean](../../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)), [toDouble](../../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)), [toInteger](../../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)), [toString](../../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)), [unApply](../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEREOTYPE_NAME)
UI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UI
References to all UI mockup configurations to be used in this execution.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.UI)
ADDCONTROLPANEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADDCONTROLPANEL
If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, add simulation control panel into the web UI.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ADDCONTROLPANEL)
ALLOWCONCURRENTALLOCATEDACTIVITIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALLOWCONCURRENTALLOCATEDACTIVITIES
Set to true, to execute allocated Activities simultaneously. Set to false, to execute only one allocated Activity for an object represented in an Activity Partition.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ALLOWCONCURRENTALLOCATEDACTIVITIES)
ANIMATIONSPEED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANIMATIONSPEED
A preferred animation speed of the particular configuration. The value range is from 1 to 100%
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ANIMATIONSPEED)
AUTOCONVERTUNITS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOCONVERTUNITS
Set to true for the units of the feature values connected via Binding Connector to be automatically converted if they have compatible types selected from the QUDV library.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOCONVERTUNITS)
AUTOSTART
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOSTART
When true, starts execution automatically from main MagicDraw toolbar.
 Otherwise, user must click Start in Simulation Console after initialization.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOSTART)
AUTOTERMINATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOTERMINATE
Set to true for the simulation to terminate when it completes or after the initialization phase if autoStart is set to false.
 Set to false for the simulation to continue running without termination, hanging at the end or after the initialization phase if autoStart is set to false.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOTERMINATE)
AUTOMATICPARAMETRICRECALCULATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOMATICPARAMETRICRECALCULATION
Set to true for parametric models to be recalculated automatically when there is a change in any structural feature value. Set to false to recalculate parametric models manually.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOMATICPARAMETRICRECALCULATION)
AUTOSTARTACTIVEOBJECTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOSTARTACTIVEOBJECTS
If value is true, asynchronously starts behaviors of active classifiers (isActive=true) right after objects creation.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOSTARTACTIVEOBJECTS)
CAPTURETIMESTAMP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CAPTURETIMESTAMP
If true, timestamp is recorded into a result instance name.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CAPTURETIMESTAMP)
CLOCK_RATIO
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLOCK_RATIO
Ratio of the simulated time to modeled time.
 ratio = 1000 means that 1ms time expression in model will be interpreted as 1s in simulation.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CLOCK_RATIO)
CLONEREFERENCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLONEREFERENCES
If true, create new instances for all objects recursively, if not, only first level - others remain in original locations.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CLONEREFERENCES)
CONSTRAINTFAILUREASBREAKPOINT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONSTRAINTFAILUREASBREAKPOINT
If the value is true, the simulation will be paused at the element which is the cause of the constraint failure.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CONSTRAINTFAILUREASBREAKPOINT)
DECIMALPLACES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DECIMALPLACES
The number of digits following the decimal point
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.DECIMALPLACES)
DURATIONSIMULATIONMODE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DURATIONSIMULATIONMODE
Duration simulation mode specifies the duration which will be used in the execution of the elements that have duration constraint applied.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.DURATIONSIMULATIONMODE)
ENDTIME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENDTIME
If this value and "startTime" are specified, the simulation will be stopped when the simulation time reaches this time value.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ENDTIME)
ENGINESPRIORITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENGINESPRIORITY
Allows specifying execution engines priority and availability for particular execution. Overwrites global Engines Priority from Environment Options.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ENGINESPRIORITY)
EXCLUDEDELEMENTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXCLUDEDELEMENTS
A list of elements which will be excluded and not instantiated if not ready to be used or not needed, e.g. Classes, Packages, UseCases, Actors, Behaviors, Connectors, Ports, and States.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXCLUDEDELEMENTS)
EXECUTIONLISTENERS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXECUTIONLISTENERS
The list of execution listener which will receive event from the model execution. The execution listener could be SequenceDiagramGeneratorConfig.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXECUTIONLISTENERS)
EXECUTIONTARGET
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXECUTIONTARGET
Reference to model element to be executed.
 It can be Class, InstanceSpecification, StateMachine, Activity and others.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXECUTIONTARGET)
INITIALIZEREFERENCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INITIALIZEREFERENCES
If true, references will be initialized by creating new objects, instead of referencing to existing parts of the system.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.INITIALIZEREFERENCES)
INPUTPARAMETERS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INPUTPARAMETERS
Use a SelectPropertiesConfig as the predefined list of inputs parameters.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.INPUTPARAMETERS)
LOG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOG
Optional ExecutionLog element for execution events recording into special kind of model.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.LOG)
NUMBEROFRUNS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFRUNS
A preferred number of runs of the particular configuration, especially as sample size in Monte Carlo simulation. The value must be greater than or equal 1.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.NUMBEROFRUNS)
NUMBEROFSTEPS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFSTEPS
If "stepSize" is not specified, but "startTime", "endTime", and "numberOfSteps" are specified. These values will be used to calculate a step size of the simulation clock.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.NUMBEROFSTEPS)
OPENSIMULATIONPANE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPENSIMULATIONPANE
Set to true, to open the Simulation pane when running a Simulation Configuration.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.OPENSIMULATIONPANE)
OUTPUTPARAMETERS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OUTPUTPARAMETERS
Use a SelectPropertiesConfig as the predefined list of outputs parameters.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.OUTPUTPARAMETERS)
REMEMBERFAILURESTATUS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMEMBERFAILURESTATUS
If the value is true, simulation will keep the first failure status until the termination and record it as 'fail' even though it was 'pass' at the end.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.REMEMBERFAILURESTATUS)
RESULTLOCATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RESULTLOCATION
Specify an instance specification or a package or an instance table for execution results recording. In case of instance specification, it should be an instance specification of the same classifier as main execution target. In case of package, a new instance specification with timestamp will be created in the specified package. In case of instance table, only properties selected as columns will be saved or overwritten.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.RESULTLOCATION)
RUNFORKSINPARALLEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RUNFORKSINPARALLEL
If this value is "true" or "undefined", all outgoing edges from Fork will run in parallel.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.RUNFORKSINPARALLEL)
SHOWACTIVESTATEIMAGES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWACTIVESTATEIMAGES
Select 'On Part shapes' to show active state images on Part shapes. Select 'In the Simulation UI' to show active state images in the simulation UI dialog.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWACTIVESTATEIMAGES)
SHOWACTIVESTATESONPARTSHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWACTIVESTATESONPARTSHAPES
If true, active states are shown on Part shapes.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWACTIVESTATESONPARTSHAPES)
SHOWANNOTATIONS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWANNOTATIONS
Set to true to enable simulation annotations in diagrams.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWANNOTATIONS)
SHOWFLOWINGINFORMATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWFLOWINGINFORMATION
Set to true to show the label of a flowing item on a path. If the property is set to false, a path is only highlighted when an item is flowing.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWFLOWINGINFORMATION)
SHOWHELDTOKENSINACTIVITYDIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWHELDTOKENSINACTIVITYDIAGRAMS
Set to true to display held tokens that are displayed on Pins and Activity Parameter Nodes.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWHELDTOKENSINACTIVITYDIAGRAMS)
SHOWRUNTIMEVALUESONPARTSHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWRUNTIMEVALUESONPARTSHAPES
Set to true to display runtime values on Part shapes instead of the default values.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWRUNTIMEVALUESONPARTSHAPES)
SHOWRUNTIMEVALUESONPORTLABELS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWRUNTIMEVALUESONPORTLABELS
Set to true to display runtime values on Port and Constraint Parameters labels.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWRUNTIMEVALUESONPORTLABELS)
SILENT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SILENT
When silent = true, animation is not used and artificial slowdown is disabled. It is recommended to use silent execution if any timing events are used in the model.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SILENT)
SOLVEAFTERINITIALIZATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOLVEAFTERINITIALIZATION
When true, invokes initial solving automatically. Otherwise, manually invoke is required via Refresh in Variables pane or Start (F8)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SOLVEAFTERINITIALIZATION)
STARTTIME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STARTTIME
If value is specified, the simulation clock will be started with this value.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTTIME)
STARTWEBSERVER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STARTWEBSERVER
If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, UI configs will be served as HTML pages. Click on the URL in the console to open UI in a web browser.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTWEBSERVER)
STARTUPDIAGRAM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STARTUPDIAGRAM
Specify the diagram that is opened automatically when running a Simulation Configuration.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTUPDIAGRAM)
STEPDELAY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEPDELAY
If value is specified, the simulation clock will be delayed with this value for each time step.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEPDELAY)
STEPSIZE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEPSIZE
If value is specified and more than 0, the simulation clock will use this value to step to increase the simulation time.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEPSIZE)
TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY
If set to true, a streaming activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity. If set to false, a streaming activity terminates when forced by the activity final node or termination of the activity that invoked it.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY)
TIMEUNIT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIMEUNIT
If value is specified, it will be the unit of the simulation time. Otherwise, millisecond will be used.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEUNIT)
TIMEVALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIMEVALUE
If a value is specified, it will be used as the simulation time for the model-based clock only.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEVALUE)
TIMEVARIABLENAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIMEVARIABLENAME
The time variable name which can be referred in any scripts to access the simulation time.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEVARIABLENAME)
TREATALLCLASSIFIERSASACTIVE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TREATALLCLASSIFIERSASACTIVE
If true, isActive property of all classifier will be treated as true for execution.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TREATALLCLASSIFIERSASACTIVE)
WATCHPROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) WATCHPROPERTIES
Use a SelectPropertiesConfig as the predefined list of properties to monitor in the Watch
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.WATCHPROPERTIES)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationConfigStereotype
protected SimulationConfigStereotype([SimulationProfile](SimulationProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getUIProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getUIProperty()
getAddControlPanelProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAddControlPanelProperty()
getAllowConcurrentAllocatedActivitiesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAllowConcurrentAllocatedActivitiesProperty()
getAnimationSpeedProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAnimationSpeedProperty()
getAutoConvertUnitsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAutoConvertUnitsProperty()
getAutoStartProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAutoStartProperty()
getAutoTerminateProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAutoTerminateProperty()
getAutomaticParametricRecalculationProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAutomaticParametricRecalculationProperty()
getAutostartActiveObjectsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getAutostartActiveObjectsProperty()
getCaptureTimestampProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getCaptureTimestampProperty()
getClockratioProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getClockratioProperty()
getCloneReferencesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getCloneReferencesProperty()
getConstraintFailureAsBreakpointProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getConstraintFailureAsBreakpointProperty()
getDecimalPlacesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDecimalPlacesProperty()
getDurationSimulationModeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getDurationSimulationModeProperty()
getEndTimeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getEndTimeProperty()
getEnginesPriorityProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getEnginesPriorityProperty()
getExcludedElementsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getExcludedElementsProperty()
getExecutionListenersProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getExecutionListenersProperty()
getExecutionTargetProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getExecutionTargetProperty()
getInitializeReferencesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getInitializeReferencesProperty()
getInputParametersProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getInputParametersProperty()
getLogProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLogProperty()
getNumberOfRunsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfRunsProperty()
getNumberOfStepsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfStepsProperty()
getOpenSimulationPaneProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getOpenSimulationPaneProperty()
getOutputParametersProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getOutputParametersProperty()
getRememberFailureStatusProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRememberFailureStatusProperty()
getResultLocationProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getResultLocationProperty()
getRunForksInParallelProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getRunForksInParallelProperty()
getShowActiveStateImagesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowActiveStateImagesProperty()
getShowActiveStatesOnPartShapesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowActiveStatesOnPartShapesProperty()
getShowAnnotationsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowAnnotationsProperty()
getShowFlowingInformationProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowFlowingInformationProperty()
getShowHeldTokensInActivityDiagramsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowHeldTokensInActivityDiagramsProperty()
getShowRuntimeValuesOnPartShapesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowRuntimeValuesOnPartShapesProperty()
getShowRuntimeValuesOnPortLabelsProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getShowRuntimeValuesOnPortLabelsProperty()
getSilentProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSilentProperty()
getSolveAfterInitializationProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSolveAfterInitializationProperty()
getStartTimeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStartTimeProperty()
getStartWebServerProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStartWebServerProperty()
getStartupDiagramProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStartupDiagramProperty()
getStepDelayProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStepDelayProperty()
getStepSizeProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getStepSizeProperty()
getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty()
getTimeUnitProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTimeUnitProperty()
getTimeValueProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTimeValueProperty()
getTimeVariableNameProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTimeVariableNameProperty()
getTreatAllClassifiersAsActiveProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getTreatAllClassifiersAsActiveProperty()
getWatchPropertiesProperty
@CheckForNullpublic [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getWatchPropertiesProperty()
setUI
public void setUI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearUI
public void clearUI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addUI
public void addUI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeUI
public void removeUI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getUI
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getUI([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAddControlPanel
public void setAddControlPanel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAddControlPanel
public void clearAddControlPanel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAddControlPanel
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAddControlPanel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAllowConcurrentAllocatedActivities
public void setAllowConcurrentAllocatedActivities([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAllowConcurrentAllocatedActivities
public void clearAllowConcurrentAllocatedActivities([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAllowConcurrentAllocatedActivities
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAllowConcurrentAllocatedActivities([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAnimationSpeed
public void setAnimationSpeed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearAnimationSpeed
public void clearAnimationSpeed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getAnimationSpeed
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getAnimationSpeed([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAutoConvertUnits
public void setAutoConvertUnits([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAutoConvertUnits
public void clearAutoConvertUnits([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAutoConvertUnits
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAutoConvertUnits([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAutoStart
public void setAutoStart([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAutoStart
public void clearAutoStart([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAutoStart
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAutoStart([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAutoTerminate
public void setAutoTerminate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAutoTerminate
public void clearAutoTerminate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAutoTerminate
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAutoTerminate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAutomaticParametricRecalculation
public void setAutomaticParametricRecalculation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAutomaticParametricRecalculation
public void clearAutomaticParametricRecalculation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAutomaticParametricRecalculation
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAutomaticParametricRecalculation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setAutostartActiveObjects
public void setAutostartActiveObjects([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearAutostartActiveObjects
public void clearAutostartActiveObjects([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isAutostartActiveObjects
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isAutostartActiveObjects([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setCaptureTimestamp
public void setCaptureTimestamp([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearCaptureTimestamp
public void clearCaptureTimestamp([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isCaptureTimestamp
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isCaptureTimestamp([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setClockratio
public void setClockratio([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearClockratio
public void clearClockratio([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getClockratio
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClockratio([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setCloneReferences
public void setCloneReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearCloneReferences
public void clearCloneReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isCloneReferences
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isCloneReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setConstraintFailureAsBreakpoint
public void setConstraintFailureAsBreakpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearConstraintFailureAsBreakpoint
public void clearConstraintFailureAsBreakpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isConstraintFailureAsBreakpoint
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isConstraintFailureAsBreakpoint([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDecimalPlaces
public void setDecimalPlaces([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearDecimalPlaces
public void clearDecimalPlaces([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getDecimalPlaces
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getDecimalPlaces([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setDurationSimulationMode
public void setDurationSimulationMode([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [SimulationProfile.DurationSimulationModeEnum](SimulationProfile.DurationSimulationModeEnum.html) value)
clearDurationSimulationMode
public void clearDurationSimulationMode([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getDurationSimulationMode
@CheckForNullpublic [SimulationProfile.DurationSimulationModeEnum](SimulationProfile.DurationSimulationModeEnum.html) getDurationSimulationMode([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setEndTime
public void setEndTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearEndTime
public void clearEndTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getEndTime
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getEndTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setEnginesPriority
public void setEnginesPriority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearEnginesPriority
public void clearEnginesPriority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getEnginesPriority
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEnginesPriority([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setExcludedElements
public void setExcludedElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearExcludedElements
public void clearExcludedElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addExcludedElements
public void addExcludedElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeExcludedElements
public void removeExcludedElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getExcludedElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getExcludedElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setExecutionListeners
public void setExecutionListeners([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearExecutionListeners
public void clearExecutionListeners([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addExecutionListeners
public void addExecutionListeners([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeExecutionListeners
public void removeExecutionListeners([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getExecutionListeners
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getExecutionListeners([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setExecutionTarget
public void setExecutionTarget([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearExecutionTarget
public void clearExecutionTarget([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getExecutionTarget
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getExecutionTarget([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setInitializeReferences
public void setInitializeReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearInitializeReferences
public void clearInitializeReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isInitializeReferences
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isInitializeReferences([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setInputParameters
public void setInputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearInputParameters
public void clearInputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addInputParameters
public void addInputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeInputParameters
public void removeInputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getInputParameters
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getInputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLog
public void setLog([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearLog
public void clearLog([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLog
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getLog([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfRuns
public void setNumberOfRuns([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfRuns
public void clearNumberOfRuns([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfRuns
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfRuns([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfSteps
public void setNumberOfSteps([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfSteps
public void clearNumberOfSteps([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfSteps
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfSteps([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setOpenSimulationPane
public void setOpenSimulationPane([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearOpenSimulationPane
public void clearOpenSimulationPane([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isOpenSimulationPane
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isOpenSimulationPane([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setOutputParameters
public void setOutputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearOutputParameters
public void clearOutputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addOutputParameters
public void addOutputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeOutputParameters
public void removeOutputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getOutputParameters
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getOutputParameters([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRememberFailureStatus
public void setRememberFailureStatus([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearRememberFailureStatus
public void clearRememberFailureStatus([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isRememberFailureStatus
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isRememberFailureStatus([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setResultLocation
public void setResultLocation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearResultLocation
public void clearResultLocation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getResultLocation
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getResultLocation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setRunForksInParallel
public void setRunForksInParallel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearRunForksInParallel
public void clearRunForksInParallel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isRunForksInParallel
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isRunForksInParallel([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowActiveStateImages
public void setShowActiveStateImages([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [SimulationProfile.ActiveStateImagesEnum](SimulationProfile.ActiveStateImagesEnum.html) value)
clearShowActiveStateImages
public void clearShowActiveStateImages([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getShowActiveStateImages
@CheckForNullpublic [SimulationProfile.ActiveStateImagesEnum](SimulationProfile.ActiveStateImagesEnum.html) getShowActiveStateImages([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowActiveStatesOnPartShapes
public void setShowActiveStatesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowActiveStatesOnPartShapes
public void clearShowActiveStatesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowActiveStatesOnPartShapes
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowActiveStatesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowAnnotations
public void setShowAnnotations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowAnnotations
public void clearShowAnnotations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowAnnotations
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowAnnotations([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowFlowingInformation
public void setShowFlowingInformation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowFlowingInformation
public void clearShowFlowingInformation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowFlowingInformation
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowFlowingInformation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowHeldTokensInActivityDiagrams
public void setShowHeldTokensInActivityDiagrams([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowHeldTokensInActivityDiagrams
public void clearShowHeldTokensInActivityDiagrams([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowHeldTokensInActivityDiagrams
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowHeldTokensInActivityDiagrams([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowRuntimeValuesOnPartShapes
public void setShowRuntimeValuesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowRuntimeValuesOnPartShapes
public void clearShowRuntimeValuesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowRuntimeValuesOnPartShapes
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowRuntimeValuesOnPartShapes([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setShowRuntimeValuesOnPortLabels
public void setShowRuntimeValuesOnPortLabels([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowRuntimeValuesOnPortLabels
public void clearShowRuntimeValuesOnPortLabels([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isShowRuntimeValuesOnPortLabels
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowRuntimeValuesOnPortLabels([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setSilent
public void setSilent([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearSilent
public void clearSilent([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isSilent
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isSilent([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setSolveAfterInitialization
public void setSolveAfterInitialization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearSolveAfterInitialization
public void clearSolveAfterInitialization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isSolveAfterInitialization
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isSolveAfterInitialization([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStartTime
public void setStartTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearStartTime
public void clearStartTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getStartTime
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getStartTime([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStartWebServer
public void setStartWebServer([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearStartWebServer
public void clearStartWebServer([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isStartWebServer
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isStartWebServer([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStartupDiagram
public void setStartupDiagram([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearStartupDiagram
public void clearStartupDiagram([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getStartupDiagram
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getStartupDiagram([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStepDelay
public void setStepDelay([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)
clearStepDelay
public void clearStepDelay([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getStepDelay
@CheckForNullpublic [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getStepDelay([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setStepSize
public void setStepSize([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)
clearStepSize
public void clearStepSize([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getStepSize
@CheckForNullpublic [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getStepSize([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTerminateStreamingBehaviorsByOutputParameterMultiplicity
public void setTerminateStreamingBehaviorsByOutputParameterMultiplicity([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearTerminateStreamingBehaviorsByOutputParameterMultiplicity
public void clearTerminateStreamingBehaviorsByOutputParameterMultiplicity([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isTerminateStreamingBehaviorsByOutputParameterMultiplicity
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isTerminateStreamingBehaviorsByOutputParameterMultiplicity([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTimeUnit
public void setTimeUnit([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [SimulationProfile.TimeUnitKindEnum](SimulationProfile.TimeUnitKindEnum.html) value)
clearTimeUnit
public void clearTimeUnit([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getTimeUnit
@CheckForNullpublic [SimulationProfile.TimeUnitKindEnum](SimulationProfile.TimeUnitKindEnum.html) getTimeUnit([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTimeValue
public void setTimeValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearTimeValue
public void clearTimeValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getTimeValue
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getTimeValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTimeVariableName
public void setTimeVariableName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearTimeVariableName
public void clearTimeVariableName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getTimeVariableName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTimeVariableName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setTreatAllClassifiersAsActive
public void setTreatAllClassifiersAsActive([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearTreatAllClassifiersAsActive
public void clearTreatAllClassifiersAsActive([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isTreatAllClassifiersAsActive
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isTreatAllClassifiersAsActive([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setWatchProperties
public void setWatchProperties([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearWatchProperties
public void clearWatchProperties([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getWatchProperties
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getWatchProperties([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Checks if stereotype of this wrapper is applied to given element.
Specified by:
`[is](../../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)`
Parameters:
`element` - element
Returns:
true if stereotype of this wrapper is applied to given element
isInstance
public static boolean isInstance(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation</a></div>
<h1 class="title" title="Class SimulationProfile.SimulationConfigStereotype">Class SimulationProfile.SimulationConfigStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">SimulationProfile.SimulationConfigStereotype</span>
<span class="extends-implements">extends <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ADDCONTROLPANEL">ADDCONTROLPANEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, add simulation control panel into the web UI.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ALLOWCONCURRENTALLOCATEDACTIVITIES">ALLOWCONCURRENTALLOCATEDACTIVITIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true, to execute allocated Activities simultaneously.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANIMATIONSPEED">ANIMATIONSPEED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A preferred animation speed of the particular configuration.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTOCONVERTUNITS">AUTOCONVERTUNITS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true for the units of the feature values connected via Binding Connector to be automatically converted if they have compatible types selected from the QUDV library.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTOMATICPARAMETRICRECALCULATION">AUTOMATICPARAMETRICRECALCULATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to true for parametric models to be recalculated automatically when there is a change in any structural feature value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTOSTART">AUTOSTART</a></code></div>
<div class="col-last odd-row-color">
<div class="block">When true, starts execution automatically from main MagicDraw toolbar.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTOSTARTACTIVEOBJECTS">AUTOSTARTACTIVEOBJECTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">If value is true, asynchronously starts behaviors of active classifiers (isActive=true) right after objects creation.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTOTERMINATE">AUTOTERMINATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true for the simulation to terminate when it completes or after the initialization phase if autoStart is set to false.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CAPTURETIMESTAMP">CAPTURETIMESTAMP</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, timestamp is recorded into a result instance name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLOCK_RATIO">CLOCK_RATIO</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Ratio of the simulated time to modeled time.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLONEREFERENCES">CLONEREFERENCES</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, create new instances for all objects recursively, if not, only first level - others remain in original locations.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONSTRAINTFAILUREASBREAKPOINT">CONSTRAINTFAILUREASBREAKPOINT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If the value is true, the simulation will be paused at the element which is the cause of the constraint failure.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DECIMALPLACES">DECIMALPLACES</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of digits following the decimal point</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DURATIONSIMULATIONMODE">DURATIONSIMULATIONMODE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Duration simulation mode specifies the duration which will be used in the execution of the elements that have duration constraint applied.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENDTIME">ENDTIME</a></code></div>
<div class="col-last even-row-color">
<div class="block">If this value and "startTime" are specified, the simulation will be stopped when the simulation time reaches this time value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENGINESPRIORITY">ENGINESPRIORITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Allows specifying execution engines priority and availability for particular execution.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXCLUDEDELEMENTS">EXCLUDEDELEMENTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A list of elements which will be excluded and not instantiated if not ready to be used or not needed, e.g.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXECUTIONLISTENERS">EXECUTIONLISTENERS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of execution listener which will receive event from the model execution.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXECUTIONTARGET">EXECUTIONTARGET</a></code></div>
<div class="col-last even-row-color">
<div class="block">Reference to model element to be executed.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INITIALIZEREFERENCES">INITIALIZEREFERENCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, references will be initialized by creating new objects, instead of referencing to existing parts of the system.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INPUTPARAMETERS">INPUTPARAMETERS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of inputs parameters.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOG">LOG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional ExecutionLog element for execution events recording into special kind of model.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBEROFRUNS">NUMBEROFRUNS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A preferred number of runs of the particular configuration, especially as sample size in Monte Carlo simulation.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBEROFSTEPS">NUMBEROFSTEPS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If "stepSize" is not specified, but "startTime", "endTime", and "numberOfSteps" are specified.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPENSIMULATIONPANE">OPENSIMULATIONPANE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to true, to open the Simulation pane when running a Simulation Configuration.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OUTPUTPARAMETERS">OUTPUTPARAMETERS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of outputs parameters.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REMEMBERFAILURESTATUS">REMEMBERFAILURESTATUS</a></code></div>
<div class="col-last even-row-color">
<div class="block">If the value is true, simulation will keep the first failure status until the termination and record it as 'fail' even though it was 'pass' at the end.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RESULTLOCATION">RESULTLOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specify an instance specification or a package or an instance table for execution results recording.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RUNFORKSINPARALLEL">RUNFORKSINPARALLEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">If this value is "true" or "undefined", all outgoing edges from Fork will run in parallel.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWACTIVESTATEIMAGES">SHOWACTIVESTATEIMAGES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Select 'On Part shapes' to show active state images on Part shapes.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWACTIVESTATESONPARTSHAPES">SHOWACTIVESTATESONPARTSHAPES</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, active states are shown on Part shapes.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWANNOTATIONS">SHOWANNOTATIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true to enable simulation annotations in diagrams.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWFLOWINGINFORMATION">SHOWFLOWINGINFORMATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to true to show the label of a flowing item on a path.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWHELDTOKENSINACTIVITYDIAGRAMS">SHOWHELDTOKENSINACTIVITYDIAGRAMS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true to display held tokens that are displayed on Pins and Activity Parameter Nodes.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWRUNTIMEVALUESONPARTSHAPES">SHOWRUNTIMEVALUESONPARTSHAPES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Set to true to display runtime values on Part shapes instead of the default values.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWRUNTIMEVALUESONPORTLABELS">SHOWRUNTIMEVALUESONPORTLABELS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set to true to display runtime values on Port and Constraint Parameters labels.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SILENT">SILENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">When silent = true, animation is not used and artificial slowdown is disabled.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOLVEAFTERINITIALIZATION">SOLVEAFTERINITIALIZATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">When true, invokes initial solving automatically.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STARTTIME">STARTTIME</a></code></div>
<div class="col-last even-row-color">
<div class="block">If value is specified, the simulation clock will be started with this value.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STARTUPDIAGRAM">STARTUPDIAGRAM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specify the diagram that is opened automatically when running a Simulation Configuration.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STARTWEBSERVER">STARTWEBSERVER</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, UI configs will be served as HTML pages.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEPDELAY">STEPDELAY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If value is specified, the simulation clock will be delayed with this value for each time step.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEPSIZE">STEPSIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">If value is specified and more than 0, the simulation clock will use this value to step to increase the simulation time.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY">TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">If set to true, a streaming activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIMEUNIT">TIMEUNIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If value is specified, it will be the unit of the simulation time.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TIMEVALUE">TIMEVALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">If a value is specified, it will be used as the simulation time for the model-based clock only.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIMEVARIABLENAME">TIMEVARIABLENAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The time variable name which can be referred in any scripts to access the simulation time.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TREATALLCLASSIFIERSASACTIVE">TREATALLCLASSIFIERSASACTIVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, isActive property of all classifier will be treated as true for execution.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UI">UI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">References to all UI mockup configurations to be used in this execution.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WATCHPROPERTIES">WATCHPROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of properties to monitor in the Watch</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.SimulationProfile)">SimulationConfigStereotype</a><wbr/>(<a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addExcludedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addExecutionListeners</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addInputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addOutputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addUI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAddControlPanel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAllowConcurrentAllocatedActivities</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAnimationSpeed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAutoConvertUnits</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAutomaticParametricRecalculation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAutoStart</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAutostartActiveObjects</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAutoTerminate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearCaptureTimestamp</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearClockratio</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearCloneReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearConstraintFailureAsBreakpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDecimalPlaces</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearDurationSimulationMode</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearEndTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearEnginesPriority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearExcludedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearExecutionListeners</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearExecutionTarget</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearInitializeReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearInputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLog</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfRuns</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfSteps</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearOpenSimulationPane</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearOutputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRememberFailureStatus</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearResultLocation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearRunForksInParallel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowActiveStateImages</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowActiveStatesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowAnnotations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowFlowingInformation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowHeldTokensInActivityDiagrams</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowRuntimeValuesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowRuntimeValuesOnPortLabels</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearSilent</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearSolveAfterInitialization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStartTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStartupDiagram</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStartWebServer</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStepDelay</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearStepSize</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTerminateStreamingBehaviorsByOutputParameterMultiplicity</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTimeUnit</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTimeValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTimeVariableName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTreatAllClassifiersAsActive</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearUI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearWatchProperties</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAddControlPanelProperty()">getAddControlPanelProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllowConcurrentAllocatedActivitiesProperty()">getAllowConcurrentAllocatedActivitiesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAnimationSpeed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnimationSpeedProperty()">getAnimationSpeedProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoConvertUnitsProperty()">getAutoConvertUnitsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutomaticParametricRecalculationProperty()">getAutomaticParametricRecalculationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutostartActiveObjectsProperty()">getAutostartActiveObjectsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoStartProperty()">getAutoStartProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoTerminateProperty()">getAutoTerminateProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCaptureTimestampProperty()">getCaptureTimestampProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClockratio</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClockratioProperty()">getClockratioProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCloneReferencesProperty()">getCloneReferencesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstraintFailureAsBreakpointProperty()">getConstraintFailureAsBreakpointProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDecimalPlaces</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDecimalPlacesProperty()">getDecimalPlacesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.DurationSimulationModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DurationSimulationModeEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDurationSimulationMode</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDurationSimulationModeProperty()">getDurationSimulationModeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getEndTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndTimeProperty()">getEndTimeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getEnginesPriority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnginesPriorityProperty()">getEnginesPriorityProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getExcludedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExcludedElementsProperty()">getExcludedElementsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getExecutionListeners</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionListenersProperty()">getExecutionListenersProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getExecutionTarget</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutionTargetProperty()">getExecutionTargetProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInitializeReferencesProperty()">getInitializeReferencesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getInputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInputParametersProperty()">getInputParametersProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLog</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLogProperty()">getLogProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfRuns</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfRunsProperty()">getNumberOfRunsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfSteps</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfStepsProperty()">getNumberOfStepsProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpenSimulationPaneProperty()">getOpenSimulationPaneProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOutputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputParametersProperty()">getOutputParametersProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRememberFailureStatusProperty()">getRememberFailureStatusProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getResultLocation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResultLocationProperty()">getResultLocationProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRunForksInParallelProperty()">getRunForksInParallelProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.ActiveStateImagesEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveStateImagesEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getShowActiveStateImages</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowActiveStateImagesProperty()">getShowActiveStateImagesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowActiveStatesOnPartShapesProperty()">getShowActiveStatesOnPartShapesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowAnnotationsProperty()">getShowAnnotationsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowFlowingInformationProperty()">getShowFlowingInformationProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowHeldTokensInActivityDiagramsProperty()">getShowHeldTokensInActivityDiagramsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowRuntimeValuesOnPartShapesProperty()">getShowRuntimeValuesOnPartShapesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowRuntimeValuesOnPortLabelsProperty()">getShowRuntimeValuesOnPortLabelsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSilentProperty()">getSilentProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSolveAfterInitializationProperty()">getSolveAfterInitializationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStartTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartTimeProperty()">getStartTimeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStartupDiagram</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartupDiagramProperty()">getStartupDiagramProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartWebServerProperty()">getStartWebServerProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStepDelay</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStepDelayProperty()">getStepDelayProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStepSize</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStepSizeProperty()">getStepSizeProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty()">getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SimulationProfile.TimeUnitKindEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeUnitKindEnum</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTimeUnit</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeUnitProperty()">getTimeUnitProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTimeValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeValueProperty()">getTimeValueProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTimeVariableName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeVariableNameProperty()">getTimeVariableNameProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreatAllClassifiersAsActiveProperty()">getTreatAllClassifiersAsActiveProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getUI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUIProperty()">getUIProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getWatchProperties</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWatchPropertiesProperty()">getWatchPropertiesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAddControlPanel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAllowConcurrentAllocatedActivities</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAutoConvertUnits</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAutomaticParametricRecalculation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAutoStart</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAutostartActiveObjects</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAutoTerminate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isCaptureTimestamp</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isCloneReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isConstraintFailureAsBreakpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInitializeReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isOpenSimulationPane</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRememberFailureStatus</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRunForksInParallel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowActiveStatesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowAnnotations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowFlowingInformation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowHeldTokensInActivityDiagrams</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowRuntimeValuesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowRuntimeValuesOnPortLabels</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSilent</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSolveAfterInitialization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isStartWebServer</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isTerminateStreamingBehaviorsByOutputParameterMultiplicity</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isTreatAllClassifiersAsActive</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeExcludedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeExecutionListeners</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeInputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeOutputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeUI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAddControlPanel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAllowConcurrentAllocatedActivities</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setAnimationSpeed</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAutoConvertUnits</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAutomaticParametricRecalculation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAutoStart</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAutostartActiveObjects</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setAutoTerminate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setCaptureTimestamp</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setClockratio</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setCloneReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setConstraintFailureAsBreakpoint</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setDecimalPlaces</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.DurationSimulationModeEnum)">setDurationSimulationMode</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="SimulationProfile.DurationSimulationModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DurationSimulationModeEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setEndTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setEnginesPriority</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setExcludedElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setExecutionListeners</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setExecutionTarget</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setInitializeReferences</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setInputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setLog</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfRuns</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfSteps</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setOpenSimulationPane</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setOutputParameters</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setRememberFailureStatus</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setResultLocation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setRunForksInParallel</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.ActiveStateImagesEnum)">setShowActiveStateImages</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="SimulationProfile.ActiveStateImagesEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveStateImagesEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowActiveStatesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowAnnotations</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowFlowingInformation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowHeldTokensInActivityDiagrams</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowRuntimeValuesOnPartShapes</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowRuntimeValuesOnPortLabels</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setSilent</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setSolveAfterInitialization</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setStartTime</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setStartupDiagram</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setStartWebServer</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double)">setStepDelay</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double)">setStepSize</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setTerminateStreamingBehaviorsByOutputParameterMultiplicity</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.TimeUnitKindEnum)">setTimeUnit</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="SimulationProfile.TimeUnitKindEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeUnitKindEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setTimeValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setTimeVariableName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setTreatAllClassifiersAsActive</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setUI</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setWatchProperties</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)">getElement</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTagByName</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)">toBoolean</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)">toDouble</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)">toInteger</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)">toString</a>, <a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UI">
<h3>UI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UI</span></div>
<div class="block">References to all UI mockup configurations to be used in this execution.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.UI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADDCONTROLPANEL">
<h3>ADDCONTROLPANEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADDCONTROLPANEL</span></div>
<div class="block">If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, add simulation control panel into the web UI.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ADDCONTROLPANEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALLOWCONCURRENTALLOCATEDACTIVITIES">
<h3>ALLOWCONCURRENTALLOCATEDACTIVITIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALLOWCONCURRENTALLOCATEDACTIVITIES</span></div>
<div class="block">Set to true, to execute allocated Activities simultaneously. Set to false, to execute only one allocated Activity for an object represented in an Activity Partition.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ALLOWCONCURRENTALLOCATEDACTIVITIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANIMATIONSPEED">
<h3>ANIMATIONSPEED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANIMATIONSPEED</span></div>
<div class="block">A preferred animation speed of the particular configuration. The value range is from 1 to 100%</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ANIMATIONSPEED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOCONVERTUNITS">
<h3>AUTOCONVERTUNITS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOCONVERTUNITS</span></div>
<div class="block">Set to true for the units of the feature values connected via Binding Connector to be automatically converted if they have compatible types selected from the QUDV library.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOCONVERTUNITS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOSTART">
<h3>AUTOSTART</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOSTART</span></div>
<div class="block">When true, starts execution automatically from main MagicDraw toolbar.
                 Otherwise, user must click Start in Simulation Console after initialization.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOSTART">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOTERMINATE">
<h3>AUTOTERMINATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOTERMINATE</span></div>
<div class="block">Set to true for the simulation to terminate when it completes or after the initialization phase if autoStart is set to false.
                 Set to false for the simulation to continue running without termination, hanging at the end or after the initialization phase if autoStart is set to false.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOTERMINATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOMATICPARAMETRICRECALCULATION">
<h3>AUTOMATICPARAMETRICRECALCULATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOMATICPARAMETRICRECALCULATION</span></div>
<div class="block">Set to true for parametric models to be recalculated automatically when there is a change in any structural feature value. Set to false to recalculate parametric models manually.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOMATICPARAMETRICRECALCULATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOSTARTACTIVEOBJECTS">
<h3>AUTOSTARTACTIVEOBJECTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOSTARTACTIVEOBJECTS</span></div>
<div class="block">If value is true, asynchronously starts behaviors of active classifiers (isActive=true) right after objects creation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.AUTOSTARTACTIVEOBJECTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CAPTURETIMESTAMP">
<h3>CAPTURETIMESTAMP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CAPTURETIMESTAMP</span></div>
<div class="block">If true, timestamp is recorded into a result instance name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CAPTURETIMESTAMP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLOCK_RATIO">
<h3>CLOCK_RATIO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLOCK_RATIO</span></div>
<div class="block">Ratio of the simulated time to modeled time.
                 ratio = 1000 means that 1ms time expression in model will be interpreted as 1s in simulation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CLOCK_RATIO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLONEREFERENCES">
<h3>CLONEREFERENCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLONEREFERENCES</span></div>
<div class="block">If true, create new instances for all objects recursively, if not, only first level - others remain in original locations.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CLONEREFERENCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINTFAILUREASBREAKPOINT">
<h3>CONSTRAINTFAILUREASBREAKPOINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONSTRAINTFAILUREASBREAKPOINT</span></div>
<div class="block">If the value is true, the simulation will be paused at the element which is the cause of the constraint failure.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.CONSTRAINTFAILUREASBREAKPOINT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DECIMALPLACES">
<h3>DECIMALPLACES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DECIMALPLACES</span></div>
<div class="block">The number of digits following the decimal point</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.DECIMALPLACES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DURATIONSIMULATIONMODE">
<h3>DURATIONSIMULATIONMODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DURATIONSIMULATIONMODE</span></div>
<div class="block">Duration simulation mode specifies the duration which will be used in the execution of the elements that have duration constraint applied.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.DURATIONSIMULATIONMODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDTIME">
<h3>ENDTIME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENDTIME</span></div>
<div class="block">If this value and "startTime" are specified, the simulation will be stopped when the simulation time reaches this time value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ENDTIME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENGINESPRIORITY">
<h3>ENGINESPRIORITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENGINESPRIORITY</span></div>
<div class="block">Allows specifying execution engines priority and availability for particular execution. Overwrites global Engines Priority from Environment Options.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.ENGINESPRIORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXCLUDEDELEMENTS">
<h3>EXCLUDEDELEMENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXCLUDEDELEMENTS</span></div>
<div class="block">A list of elements which will be excluded and not instantiated if not ready to be used or not needed, e.g. Classes, Packages, UseCases, Actors, Behaviors, Connectors, Ports, and States.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXCLUDEDELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXECUTIONLISTENERS">
<h3>EXECUTIONLISTENERS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXECUTIONLISTENERS</span></div>
<div class="block">The list of execution listener which will receive event from the model execution. The execution listener could be SequenceDiagramGeneratorConfig.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXECUTIONLISTENERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXECUTIONTARGET">
<h3>EXECUTIONTARGET</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXECUTIONTARGET</span></div>
<div class="block">Reference to model element to be executed.
                 It can be Class, InstanceSpecification, StateMachine, Activity and others.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.EXECUTIONTARGET">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INITIALIZEREFERENCES">
<h3>INITIALIZEREFERENCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INITIALIZEREFERENCES</span></div>
<div class="block">If true, references will be initialized by creating new objects, instead of referencing to existing parts of the system.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.INITIALIZEREFERENCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INPUTPARAMETERS">
<h3>INPUTPARAMETERS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INPUTPARAMETERS</span></div>
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of inputs parameters.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.INPUTPARAMETERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOG">
<h3>LOG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOG</span></div>
<div class="block">Optional ExecutionLog element for execution events recording into special kind of model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.LOG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFRUNS">
<h3>NUMBEROFRUNS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFRUNS</span></div>
<div class="block">A preferred number of runs of the particular configuration, especially as sample size in Monte Carlo simulation. The value must be greater than or equal 1.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.NUMBEROFRUNS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFSTEPS">
<h3>NUMBEROFSTEPS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFSTEPS</span></div>
<div class="block">If "stepSize" is not specified, but "startTime", "endTime", and "numberOfSteps" are specified. These values will be used to calculate a step size of the simulation clock.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.NUMBEROFSTEPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPENSIMULATIONPANE">
<h3>OPENSIMULATIONPANE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPENSIMULATIONPANE</span></div>
<div class="block">Set to true, to open the Simulation pane when running a Simulation Configuration.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.OPENSIMULATIONPANE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OUTPUTPARAMETERS">
<h3>OUTPUTPARAMETERS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OUTPUTPARAMETERS</span></div>
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of outputs parameters.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.OUTPUTPARAMETERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMEMBERFAILURESTATUS">
<h3>REMEMBERFAILURESTATUS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMEMBERFAILURESTATUS</span></div>
<div class="block">If the value is true, simulation will keep the first failure status until the termination and record it as 'fail' even though it was 'pass' at the end.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.REMEMBERFAILURESTATUS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RESULTLOCATION">
<h3>RESULTLOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RESULTLOCATION</span></div>
<div class="block">Specify an instance specification or a package or an instance table for execution results recording. In case of instance specification, it should be an instance specification of the same classifier as main execution target. In case of package, a new instance specification with timestamp will be created in the specified package. In case of instance table, only properties selected as columns will be saved or overwritten.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.RESULTLOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RUNFORKSINPARALLEL">
<h3>RUNFORKSINPARALLEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RUNFORKSINPARALLEL</span></div>
<div class="block">If this value is "true" or "undefined", all outgoing edges from Fork will run in parallel.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.RUNFORKSINPARALLEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWACTIVESTATEIMAGES">
<h3>SHOWACTIVESTATEIMAGES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWACTIVESTATEIMAGES</span></div>
<div class="block">Select 'On Part shapes' to show active state images on Part shapes. Select 'In the Simulation UI' to show active state images in the simulation UI dialog.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWACTIVESTATEIMAGES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWACTIVESTATESONPARTSHAPES">
<h3>SHOWACTIVESTATESONPARTSHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWACTIVESTATESONPARTSHAPES</span></div>
<div class="block">If true, active states are shown on Part shapes.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWACTIVESTATESONPARTSHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWANNOTATIONS">
<h3>SHOWANNOTATIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWANNOTATIONS</span></div>
<div class="block">Set to true to enable simulation annotations in diagrams.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWANNOTATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWFLOWINGINFORMATION">
<h3>SHOWFLOWINGINFORMATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWFLOWINGINFORMATION</span></div>
<div class="block">Set to true to show the label of a flowing item on a path. If the property is set to false, a path is only highlighted when an item is flowing.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWFLOWINGINFORMATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWHELDTOKENSINACTIVITYDIAGRAMS">
<h3>SHOWHELDTOKENSINACTIVITYDIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWHELDTOKENSINACTIVITYDIAGRAMS</span></div>
<div class="block">Set to true to display held tokens that are displayed on Pins and Activity Parameter Nodes.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWHELDTOKENSINACTIVITYDIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWRUNTIMEVALUESONPARTSHAPES">
<h3>SHOWRUNTIMEVALUESONPARTSHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWRUNTIMEVALUESONPARTSHAPES</span></div>
<div class="block">Set to true to display runtime values on Part shapes instead of the default values.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWRUNTIMEVALUESONPARTSHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWRUNTIMEVALUESONPORTLABELS">
<h3>SHOWRUNTIMEVALUESONPORTLABELS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWRUNTIMEVALUESONPORTLABELS</span></div>
<div class="block">Set to true to display runtime values on Port and Constraint Parameters labels.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SHOWRUNTIMEVALUESONPORTLABELS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SILENT">
<h3>SILENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SILENT</span></div>
<div class="block">When silent = true, animation is not used and artificial slowdown is disabled. It is recommended to use silent execution if any timing events are used in the model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SILENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOLVEAFTERINITIALIZATION">
<h3>SOLVEAFTERINITIALIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOLVEAFTERINITIALIZATION</span></div>
<div class="block">When true, invokes initial solving automatically. Otherwise, manually invoke is required via Refresh in Variables pane or Start (F8)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.SOLVEAFTERINITIALIZATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTTIME">
<h3>STARTTIME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STARTTIME</span></div>
<div class="block">If value is specified, the simulation clock will be started with this value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTTIME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTWEBSERVER">
<h3>STARTWEBSERVER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STARTWEBSERVER</span></div>
<div class="block">If true and "Web Server for Cameo Simulation Toolkit" plugin is installed, UI configs will be served as HTML pages. Click on the URL in the console to open UI in a web browser.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTWEBSERVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTUPDIAGRAM">
<h3>STARTUPDIAGRAM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STARTUPDIAGRAM</span></div>
<div class="block">Specify the diagram that is opened automatically when running a Simulation Configuration.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STARTUPDIAGRAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STEPDELAY">
<h3>STEPDELAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEPDELAY</span></div>
<div class="block">If value is specified, the simulation clock will be delayed with this value for each time step.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEPDELAY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STEPSIZE">
<h3>STEPSIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEPSIZE</span></div>
<div class="block">If value is specified and more than 0, the simulation clock will use this value to step to increase the simulation time.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.STEPSIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY">
<h3>TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY</span></div>
<div class="block">If set to true, a streaming activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity. If set to false, a streaming activity terminates when forced by the activity final node or termination of the activity that invoked it.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TERMINATESTREAMINGBEHAVIORSBYOUTPUTPARAMETERMULTIPLICITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMEUNIT">
<h3>TIMEUNIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIMEUNIT</span></div>
<div class="block">If value is specified, it will be the unit of the simulation time. Otherwise, millisecond will be used.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEUNIT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMEVALUE">
<h3>TIMEVALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIMEVALUE</span></div>
<div class="block">If a value is specified, it will be used as the simulation time for the model-based clock only.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEVALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIMEVARIABLENAME">
<h3>TIMEVARIABLENAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIMEVARIABLENAME</span></div>
<div class="block">The time variable name which can be referred in any scripts to access the simulation time.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TIMEVARIABLENAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TREATALLCLASSIFIERSASACTIVE">
<h3>TREATALLCLASSIFIERSASACTIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TREATALLCLASSIFIERSASACTIVE</span></div>
<div class="block">If true, isActive property of all classifier will be treated as true for execution.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.TREATALLCLASSIFIERSASACTIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WATCHPROPERTIES">
<h3>WATCHPROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">WATCHPROPERTIES</span></div>
<div class="block">Use a   SelectPropertiesConfig   as the predefined list of properties to monitor in the Watch</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.simulation.SimulationProfile.SimulationConfigStereotype.WATCHPROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.SimulationProfile)">
<h3>SimulationConfigStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">SimulationConfigStereotype</span><wbr/><span class="parameters">(<a href="SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a> profile)</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUIProperty()">
<h3>getUIProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getUIProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAddControlPanelProperty()">
<h3>getAddControlPanelProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAddControlPanelProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAllowConcurrentAllocatedActivitiesProperty()">
<h3>getAllowConcurrentAllocatedActivitiesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAllowConcurrentAllocatedActivitiesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAnimationSpeedProperty()">
<h3>getAnimationSpeedProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAnimationSpeedProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutoConvertUnitsProperty()">
<h3>getAutoConvertUnitsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAutoConvertUnitsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutoStartProperty()">
<h3>getAutoStartProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAutoStartProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutoTerminateProperty()">
<h3>getAutoTerminateProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAutoTerminateProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutomaticParametricRecalculationProperty()">
<h3>getAutomaticParametricRecalculationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAutomaticParametricRecalculationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAutostartActiveObjectsProperty()">
<h3>getAutostartActiveObjectsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAutostartActiveObjectsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCaptureTimestampProperty()">
<h3>getCaptureTimestampProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getCaptureTimestampProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getClockratioProperty()">
<h3>getClockratioProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getClockratioProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCloneReferencesProperty()">
<h3>getCloneReferencesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getCloneReferencesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConstraintFailureAsBreakpointProperty()">
<h3>getConstraintFailureAsBreakpointProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getConstraintFailureAsBreakpointProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDecimalPlacesProperty()">
<h3>getDecimalPlacesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDecimalPlacesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDurationSimulationModeProperty()">
<h3>getDurationSimulationModeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getDurationSimulationModeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEndTimeProperty()">
<h3>getEndTimeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getEndTimeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEnginesPriorityProperty()">
<h3>getEnginesPriorityProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getEnginesPriorityProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExcludedElementsProperty()">
<h3>getExcludedElementsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getExcludedElementsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExecutionListenersProperty()">
<h3>getExecutionListenersProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getExecutionListenersProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExecutionTargetProperty()">
<h3>getExecutionTargetProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getExecutionTargetProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInitializeReferencesProperty()">
<h3>getInitializeReferencesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getInitializeReferencesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInputParametersProperty()">
<h3>getInputParametersProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getInputParametersProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLogProperty()">
<h3>getLogProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLogProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfRunsProperty()">
<h3>getNumberOfRunsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfRunsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfStepsProperty()">
<h3>getNumberOfStepsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfStepsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOpenSimulationPaneProperty()">
<h3>getOpenSimulationPaneProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOpenSimulationPaneProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOutputParametersProperty()">
<h3>getOutputParametersProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOutputParametersProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRememberFailureStatusProperty()">
<h3>getRememberFailureStatusProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRememberFailureStatusProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getResultLocationProperty()">
<h3>getResultLocationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getResultLocationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRunForksInParallelProperty()">
<h3>getRunForksInParallelProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getRunForksInParallelProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowActiveStateImagesProperty()">
<h3>getShowActiveStateImagesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowActiveStateImagesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowActiveStatesOnPartShapesProperty()">
<h3>getShowActiveStatesOnPartShapesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowActiveStatesOnPartShapesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowAnnotationsProperty()">
<h3>getShowAnnotationsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowAnnotationsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowFlowingInformationProperty()">
<h3>getShowFlowingInformationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowFlowingInformationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowHeldTokensInActivityDiagramsProperty()">
<h3>getShowHeldTokensInActivityDiagramsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowHeldTokensInActivityDiagramsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowRuntimeValuesOnPartShapesProperty()">
<h3>getShowRuntimeValuesOnPartShapesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowRuntimeValuesOnPartShapesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowRuntimeValuesOnPortLabelsProperty()">
<h3>getShowRuntimeValuesOnPortLabelsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowRuntimeValuesOnPortLabelsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSilentProperty()">
<h3>getSilentProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSilentProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSolveAfterInitializationProperty()">
<h3>getSolveAfterInitializationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSolveAfterInitializationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStartTimeProperty()">
<h3>getStartTimeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStartTimeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStartWebServerProperty()">
<h3>getStartWebServerProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStartWebServerProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStartupDiagramProperty()">
<h3>getStartupDiagramProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStartupDiagramProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStepDelayProperty()">
<h3>getStepDelayProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStepDelayProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStepSizeProperty()">
<h3>getStepSizeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getStepSizeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty()">
<h3>getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTerminateStreamingBehaviorsByOutputParameterMultiplicityProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTimeUnitProperty()">
<h3>getTimeUnitProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTimeUnitProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTimeValueProperty()">
<h3>getTimeValueProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTimeValueProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTimeVariableNameProperty()">
<h3>getTimeVariableNameProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTimeVariableNameProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTreatAllClassifiersAsActiveProperty()">
<h3>getTreatAllClassifiersAsActiveProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTreatAllClassifiersAsActiveProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getWatchPropertiesProperty()">
<h3>getWatchPropertiesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getWatchPropertiesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearUI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addUI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeUI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getUI(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getUI</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAddControlPanel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAddControlPanel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAddControlPanel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAddControlPanel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAddControlPanel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAddControlPanel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAddControlPanel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAllowConcurrentAllocatedActivities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAllowConcurrentAllocatedActivities</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAllowConcurrentAllocatedActivities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAllowConcurrentAllocatedActivities</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAllowConcurrentAllocatedActivities(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAllowConcurrentAllocatedActivities</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAllowConcurrentAllocatedActivities</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setAnimationSpeed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnimationSpeed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAnimationSpeed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAnimationSpeed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAnimationSpeed(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAnimationSpeed</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getAnimationSpeed</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAutoConvertUnits</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoConvertUnits</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAutoConvertUnits</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAutoConvertUnits</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutoConvertUnits(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAutoConvertUnits</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAutoConvertUnits</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAutoStart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoStart</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAutoStart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAutoStart</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutoStart(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAutoStart</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAutoStart</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAutoTerminate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoTerminate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAutoTerminate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAutoTerminate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutoTerminate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAutoTerminate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAutoTerminate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAutomaticParametricRecalculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutomaticParametricRecalculation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAutomaticParametricRecalculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAutomaticParametricRecalculation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutomaticParametricRecalculation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAutomaticParametricRecalculation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAutomaticParametricRecalculation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setAutostartActiveObjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutostartActiveObjects</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAutostartActiveObjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAutostartActiveObjects</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutostartActiveObjects(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAutostartActiveObjects</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isAutostartActiveObjects</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setCaptureTimestamp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCaptureTimestamp</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearCaptureTimestamp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCaptureTimestamp</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCaptureTimestamp(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isCaptureTimestamp</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isCaptureTimestamp</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setClockratio</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClockratio</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearClockratio</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearClockratio</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getClockratio(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getClockratio</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClockratio</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setCloneReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCloneReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearCloneReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCloneReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCloneReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isCloneReferences</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isCloneReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setConstraintFailureAsBreakpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConstraintFailureAsBreakpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearConstraintFailureAsBreakpoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearConstraintFailureAsBreakpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isConstraintFailureAsBreakpoint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isConstraintFailureAsBreakpoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isConstraintFailureAsBreakpoint</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setDecimalPlaces</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDecimalPlaces</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDecimalPlaces</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDecimalPlaces</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDecimalPlaces(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDecimalPlaces</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getDecimalPlaces</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.DurationSimulationModeEnum)">
<h3>setDurationSimulationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDurationSimulationMode</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="SimulationProfile.DurationSimulationModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DurationSimulationModeEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearDurationSimulationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDurationSimulationMode</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDurationSimulationMode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDurationSimulationMode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.DurationSimulationModeEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.DurationSimulationModeEnum</a></span> <span class="element-name">getDurationSimulationMode</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setEndTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEndTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearEndTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearEndTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEndTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getEndTime</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getEndTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setEnginesPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnginesPriority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearEnginesPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearEnginesPriority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEnginesPriority(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getEnginesPriority</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEnginesPriority</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setExcludedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExcludedElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearExcludedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearExcludedElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addExcludedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExcludedElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeExcludedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExcludedElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExcludedElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getExcludedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getExcludedElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExecutionListeners</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearExecutionListeners</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addExecutionListeners</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeExecutionListeners</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExecutionListeners(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getExecutionListeners</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setExecutionTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExecutionTarget</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearExecutionTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearExecutionTarget</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getExecutionTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getExecutionTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getExecutionTarget</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setInitializeReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitializeReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearInitializeReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearInitializeReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInitializeReferences(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInitializeReferences</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isInitializeReferences</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setInputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearInputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearInputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addInputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeInputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeInputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getInputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getInputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setLog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLog</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLog</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLog(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLog</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getLog</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfRuns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfRuns</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfRuns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfRuns</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfRuns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfRuns</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfRuns</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfSteps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfSteps</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfSteps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfSteps</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfSteps(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfSteps</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfSteps</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setOpenSimulationPane</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpenSimulationPane</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearOpenSimulationPane</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearOpenSimulationPane</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isOpenSimulationPane(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isOpenSimulationPane</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isOpenSimulationPane</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearOutputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOutputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeOutputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOutputParameters(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getOutputParameters</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setRememberFailureStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRememberFailureStatus</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRememberFailureStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRememberFailureStatus</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isRememberFailureStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRememberFailureStatus</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isRememberFailureStatus</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setResultLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setResultLocation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearResultLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearResultLocation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getResultLocation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getResultLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getResultLocation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setRunForksInParallel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRunForksInParallel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearRunForksInParallel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRunForksInParallel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isRunForksInParallel(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRunForksInParallel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isRunForksInParallel</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.ActiveStateImagesEnum)">
<h3>setShowActiveStateImages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowActiveStateImages</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="SimulationProfile.ActiveStateImagesEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveStateImagesEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowActiveStateImages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowActiveStateImages</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getShowActiveStateImages(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getShowActiveStateImages</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.ActiveStateImagesEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.ActiveStateImagesEnum</a></span> <span class="element-name">getShowActiveStateImages</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowActiveStatesOnPartShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowActiveStatesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowActiveStatesOnPartShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowActiveStatesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowActiveStatesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowActiveStatesOnPartShapes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowActiveStatesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowAnnotations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowAnnotations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowAnnotations(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowAnnotations</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowAnnotations</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowFlowingInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowFlowingInformation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowFlowingInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowFlowingInformation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowFlowingInformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowFlowingInformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowFlowingInformation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowHeldTokensInActivityDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowHeldTokensInActivityDiagrams</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowHeldTokensInActivityDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowHeldTokensInActivityDiagrams</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowHeldTokensInActivityDiagrams(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowHeldTokensInActivityDiagrams</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowHeldTokensInActivityDiagrams</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowRuntimeValuesOnPartShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowRuntimeValuesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowRuntimeValuesOnPartShapes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowRuntimeValuesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowRuntimeValuesOnPartShapes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowRuntimeValuesOnPartShapes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowRuntimeValuesOnPartShapes</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowRuntimeValuesOnPortLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowRuntimeValuesOnPortLabels</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowRuntimeValuesOnPortLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowRuntimeValuesOnPortLabels</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowRuntimeValuesOnPortLabels(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowRuntimeValuesOnPortLabels</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowRuntimeValuesOnPortLabels</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setSilent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSilent</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearSilent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSilent</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSilent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSilent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isSilent</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setSolveAfterInitialization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSolveAfterInitialization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearSolveAfterInitialization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSolveAfterInitialization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSolveAfterInitialization(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSolveAfterInitialization</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isSolveAfterInitialization</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setStartTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStartTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStartTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStartTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStartTime</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getStartTime</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setStartWebServer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartWebServer</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStartWebServer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStartWebServer</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isStartWebServer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isStartWebServer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isStartWebServer</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setStartupDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartupDiagram</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStartupDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStartupDiagram</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStartupDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStartupDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getStartupDiagram</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double)">
<h3>setStepDelay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStepDelay</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStepDelay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStepDelay</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStepDelay(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStepDelay</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getStepDelay</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Double)">
<h3>setStepSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStepSize</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearStepSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearStepSize</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStepSize(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStepSize</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getStepSize</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setTerminateStreamingBehaviorsByOutputParameterMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTerminateStreamingBehaviorsByOutputParameterMultiplicity</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTerminateStreamingBehaviorsByOutputParameterMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTerminateStreamingBehaviorsByOutputParameterMultiplicity</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTerminateStreamingBehaviorsByOutputParameterMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isTerminateStreamingBehaviorsByOutputParameterMultiplicity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isTerminateStreamingBehaviorsByOutputParameterMultiplicity</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.SimulationProfile.TimeUnitKindEnum)">
<h3>setTimeUnit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimeUnit</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="SimulationProfile.TimeUnitKindEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeUnitKindEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTimeUnit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTimeUnit</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTimeUnit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTimeUnit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="SimulationProfile.TimeUnitKindEnum.html" title="enum class in com.nomagic.magicdraw.simulation">SimulationProfile.TimeUnitKindEnum</a></span> <span class="element-name">getTimeUnit</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setTimeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimeValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTimeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTimeValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTimeValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTimeValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getTimeValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setTimeVariableName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimeVariableName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTimeVariableName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTimeVariableName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTimeVariableName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTimeVariableName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTimeVariableName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setTreatAllClassifiersAsActive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTreatAllClassifiersAsActive</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTreatAllClassifiersAsActive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTreatAllClassifiersAsActive</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTreatAllClassifiersAsActive(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isTreatAllClassifiersAsActive</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isTreatAllClassifiersAsActive</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setWatchProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWatchProperties</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearWatchProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearWatchProperties</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getWatchProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getWatchProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getWatchProperties</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a></code> in class <code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if stereotype of this wrapper is applied to given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
