# JAVA OPENAPI: SimulationOptions (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/simulation/execution/SimulationOptions.html
- source_path: `com/nomagic/magicdraw/simulation/execution/SimulationOptions.html`
- source_sha256: `7669a2f2f919d8589a3042b91e33b4247fbb7f7774d5e5fb8108a8870d0af724`
- captured_utc: `2026-07-14T16:51:31.680343+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.execution](package-summary.html)

## Class SimulationOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.execution.SimulationOptions

@OpenApiAllpublic classSimulationOptions
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A class that maintains the option values being used during the execution simulation.
 Also provides out-of-the-box option key constants to retrieve the option values by.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIVE_COLOR](#ACTIVE_COLOR)`
Active symbol color option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADD_CONTROL_PANEL](#ADD_CONTROL_PANEL)`
Add Control Panel option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES](#ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES)`
Allow Concurrent Allocated Activities option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANIMATION_SPEED](#ANIMATION_SPEED)`
Animation Speed option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_CONVERT_UNITS](#AUTO_CONVERT_UNITS)`
Turns on live unit conversion during simulation.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN](#AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN)`
Auto Create fUML Object of Output Pin option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_OPEN_DIAGRAMS](#AUTO_OPEN_DIAGRAMS)`
Auto open diagrams option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_START](#AUTO_START)`
Auto start execution option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_START_ACTIVE_OPTIONS](#AUTO_START_ACTIVE_OPTIONS)`
Auto Start Active Objects option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTO_TERMINATE](#AUTO_TERMINATE)`
Auto terminate execution option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTOMATIC_PARAMETRIC_RECALCULATION](#AUTOMATIC_PARAMETRIC_RECALCULATION)`
Automatic Parametric Recalculation option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BREAKPOINT_COLOR](#BREAKPOINT_COLOR)`
Breakpoint symbol color option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CAPTURE_TIMESTAMP](#CAPTURE_TIMESTAMP)`
Capture timestamp of result instance option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHECK_MODEL_BEFORE_EXECUTION](#CHECK_MODEL_BEFORE_EXECUTION)`
Check Model Before Execution option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLOCK_RATIO](#CLOCK_RATIO)`
Clock Ratio option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLONE_REFERENCES](#CLONE_REFERENCES)`
Clone References option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONSTRAINT_FAILURE_AS_BREAKPOINT](#CONSTRAINT_FAILURE_AS_BREAKPOINT)`
Constraint Failure as Breakpoint option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DECIMAL_PLACES](#DECIMAL_PLACES)`
Decimal Places option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_LANGUAGE](#DEFAULT_LANGUAGE)`
Default Evaluation Language option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_PARAMETRIC_EVALUATOR](#DEFAULT_PARAMETRIC_EVALUATOR)`
Default Parametric Evaluator option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DURATION_SIMULATION_MODE](#DURATION_SIMULATION_MODE)`
Duration Simulation Mode option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ENDTIME](#ENDTIME)`
Endtime option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ENGINES_PRIORITY](#ENGINES_PRIORITY)`
Registered execution engine priority option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXCLUDED_ELEMENTS](#EXCLUDED_ELEMENTS)`
Excluded Elements option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXECUTION_LISTENERS](#EXECUTION_LISTENERS)`
Execution Listeners option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXECUTION_TARGET](#EXECUTION_TARGET)`
Execution Target option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXTERNAL_LIBRARIES](#EXTERNAL_LIBRARIES)`
External Libraries option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXTERNAL_SOLVER_TIMEOUT](#EXTERNAL_SOLVER_TIMEOUT)`
External Solver Timeout option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INITIALIZE_NUMERICAL_VALUE](#INITIALIZE_NUMERICAL_VALUE)`
Initialize Empty Values to 0 option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INITIALIZE_REFERENCES](#INITIALIZE_REFERENCES)`
Initialize References option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAST_VISITED_COLOR](#LAST_VISITED_COLOR)`
Last visited symbol color option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOG](#LOG)`
Log option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBER_OF_RUNS](#NUMBER_OF_RUNS)`
Number of Runs option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBER_OF_STEPS](#NUMBER_OF_STEPS)`
Number of Steps option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPEN_SIMULATION_PANE](#OPEN_SIMULATION_PANE)`
Display Simulation Dashboard Window option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PASS_CALLER_CONTEXT](#PASS_CALLER_CONTEXT)`
Pass Caller Context option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECORD_STATE_CHANGE](#RECORD_STATE_CHANGE)`
Record State Change option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECORD_TIMESTAMP](#RECORD_TIMESTAMP)`
Record Timestamp option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECORD_VALUE_CHANGE](#RECORD_VALUE_CHANGE)`
Record Value Change option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMEMBER_FAILURE_STATUS](#REMEMBER_FAILURE_STATUS)`
Remember Failure Status option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RESULT_LOCATION](#RESULT_LOCATION)`
Result Location option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RUN_FORKS_IN_PARALLEL](#RUN_FORKS_IN_PARALLEL)`
Run Forks in Parallel option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES](#RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES)`
Runtime Value Text Color on Part Shapes option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_ACTIVE_STATE_IMAGES](#SHOW_ACTIVE_STATE_IMAGES)`
Show Active State Images option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES](#SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES)`
Show Active State Images on Part Shapes option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_ACTIVE_STATES_ON_PART_SHAPES](#SHOW_ACTIVE_STATES_ON_PART_SHAPES)`
Show Active States on Part Shapes option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_ANNOTATIONS](#SHOW_ANNOTATIONS)`
Show Annotations option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_FLOWING_INFORMATION](#SHOW_FLOWING_INFORMATION)`
Show Flowing Information option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM](#SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM)`
Show Held Tokens in Activity Diagram option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_RUNTIME_VALUES_ON_PART_SHAPES](#SHOW_RUNTIME_VALUES_ON_PART_SHAPES)`
Show Runtime Values on Part Shapes option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOW_RUNTIME_VALUES_ON_PORT_LABELS](#SHOW_RUNTIME_VALUES_ON_PORT_LABELS)`
Show Runtime Values on Part Shapes option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SILENT](#SILENT)`
Silent execution option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOLVE_AFTER_INITIALIZATION](#SOLVE_AFTER_INITIALIZATION)`
Solve After Initialization option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[START_TIME](#START_TIME)`
Start Time option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[START_WEB_SERVER](#START_WEB_SERVER)`
Start Web Server option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STARTUP_DIAGRAM](#STARTUP_DIAGRAM)`
Startup Diagram option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEP_DELAY](#STEP_DELAY)`
Step Delay option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEP_SIZE](#STEP_SIZE)`
Step Size option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN](#TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN)`
Terminate Behavior on Exception Thrown option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TERMINATE_NESTED_BEHAVIORS](#TERMINATE_NESTED_BEHAVIORS)`
Terminate Nested Behaviors option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY](#TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY)`
Terminate Streaming Behaviors by Output Parameter Multiplicity option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIME_UNIT](#TIME_UNIT)`
Time Unit option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIME_VALUE](#TIME_VALUE)`
Time Value option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TIME_VARIABLE_NAME](#TIME_VARIABLE_NAME)`
Time Variable Name option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TREAT_ALL_CLASSIFIERS_AS_ACTIVE](#TREAT_ALL_CLASSIFIERS_AS_ACTIVE)`
Treat All Objects as Active option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UI](#UI)`
UI option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[USE_FUML_DECISION_SEMANTICS](#USE_FUML_DECISION_SEMANTICS)`
Use fUML Decision Semantics option key
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VISITED_COLOR](#VISITED_COLOR)`
Visited symbol color option key
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationOptions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addOption](#addOption(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) optionValue)`
Deprecated.
use [`set(String, Object)`](#set(java.lang.String,java.lang.Object)) instead
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)`
Get the option value from the specified option name.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getOption](#getOption(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)`
Deprecated.
use shorter and more convenient [`get(String)`](#get(java.lang.String))
`boolean`
`[is](#is(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)`
Get the Boolean option value from the specified option name.
`void`
`[set](#set(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Add the option.
`void`
`[setIfAbsent](#setIfAbsent(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets without overwriting: the provided value is only set when no non-null value exists by this key yet
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ACTIVE_COLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIVE_COLOR
Active symbol color option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ACTIVE_COLOR)
VISITED_COLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VISITED_COLOR
Visited symbol color option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.VISITED_COLOR)
BREAKPOINT_COLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BREAKPOINT_COLOR
Breakpoint symbol color option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.BREAKPOINT_COLOR)
LAST_VISITED_COLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAST_VISITED_COLOR
Last visited symbol color option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.LAST_VISITED_COLOR)
AUTO_OPEN_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_OPEN_DIAGRAMS
Auto open diagrams option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_OPEN_DIAGRAMS)
SILENT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SILENT
Silent execution option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SILENT)
DEFAULT_LANGUAGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEFAULT_LANGUAGE
Default Evaluation Language option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DEFAULT_LANGUAGE)
ENGINES_PRIORITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENGINES_PRIORITY
Registered execution engine priority option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ENGINES_PRIORITY)
AUTO_START
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_START
Auto start execution option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_START)
AUTO_START_ACTIVE_OPTIONS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_START_ACTIVE_OPTIONS
Auto Start Active Objects option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_START_ACTIVE_OPTIONS)
TREAT_ALL_CLASSIFIERS_AS_ACTIVE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TREAT_ALL_CLASSIFIERS_AS_ACTIVE
Treat All Objects as Active option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TREAT_ALL_CLASSIFIERS_AS_ACTIVE)
TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN
Terminate Behavior on Exception Thrown option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN)
INITIALIZE_NUMERICAL_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INITIALIZE_NUMERICAL_VALUE
Initialize Empty Values to 0 option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.INITIALIZE_NUMERICAL_VALUE)
RECORD_STATE_CHANGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECORD_STATE_CHANGE
Record State Change option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_STATE_CHANGE)
RECORD_VALUE_CHANGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECORD_VALUE_CHANGE
Record Value Change option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_VALUE_CHANGE)
RECORD_TIMESTAMP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECORD_TIMESTAMP
Record Timestamp option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_TIMESTAMP)
USE_FUML_DECISION_SEMANTICS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) USE_FUML_DECISION_SEMANTICS
Use fUML Decision Semantics option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.USE_FUML_DECISION_SEMANTICS)
AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN
Auto Create fUML Object of Output Pin option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN)
SOLVE_AFTER_INITIALIZATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOLVE_AFTER_INITIALIZATION
Solve After Initialization option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SOLVE_AFTER_INITIALIZATION)
DEFAULT_PARAMETRIC_EVALUATOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEFAULT_PARAMETRIC_EVALUATOR
Default Parametric Evaluator option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DEFAULT_PARAMETRIC_EVALUATOR)
EXTERNAL_SOLVER_TIMEOUT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXTERNAL_SOLVER_TIMEOUT
External Solver Timeout option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXTERNAL_SOLVER_TIMEOUT)
EXTERNAL_LIBRARIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXTERNAL_LIBRARIES
External Libraries option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXTERNAL_LIBRARIES)
CHECK_MODEL_BEFORE_EXECUTION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHECK_MODEL_BEFORE_EXECUTION
Check Model Before Execution option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CHECK_MODEL_BEFORE_EXECUTION)
SHOW_FLOWING_INFORMATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_FLOWING_INFORMATION
Show Flowing Information option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_FLOWING_INFORMATION)
RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES
Runtime Value Text Color on Part Shapes option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES)
SHOW_ACTIVE_STATES_ON_PART_SHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_ACTIVE_STATES_ON_PART_SHAPES
Show Active States on Part Shapes option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATES_ON_PART_SHAPES)
SHOW_RUNTIME_VALUES_ON_PART_SHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_RUNTIME_VALUES_ON_PART_SHAPES
Show Runtime Values on Part Shapes option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_RUNTIME_VALUES_ON_PART_SHAPES)
SHOW_RUNTIME_VALUES_ON_PORT_LABELS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_RUNTIME_VALUES_ON_PORT_LABELS
Show Runtime Values on Part Shapes option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_RUNTIME_VALUES_ON_PORT_LABELS)
SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES
Show Active State Images on Part Shapes option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES)
SHOW_ACTIVE_STATE_IMAGES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_ACTIVE_STATE_IMAGES
Show Active State Images option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATE_IMAGES)
SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM
Show Held Tokens in Activity Diagram option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM)
SHOW_ANNOTATIONS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOW_ANNOTATIONS
Show Annotations option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ANNOTATIONS)
PASS_CALLER_CONTEXT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PASS_CALLER_CONTEXT
Pass Caller Context option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.PASS_CALLER_CONTEXT)
TERMINATE_NESTED_BEHAVIORS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TERMINATE_NESTED_BEHAVIORS
Terminate Nested Behaviors option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_NESTED_BEHAVIORS)
TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY
Terminate Streaming Behaviors by Output Parameter Multiplicity option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY)
ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES
Allow Concurrent Allocated Activities option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES)
AUTO_CONVERT_UNITS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_CONVERT_UNITS
Turns on live unit conversion during simulation.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_CONVERT_UNITS)
UI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UI
UI option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.UI)
ADD_CONTROL_PANEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADD_CONTROL_PANEL
Add Control Panel option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ADD_CONTROL_PANEL)
ANIMATION_SPEED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANIMATION_SPEED
Animation Speed option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ANIMATION_SPEED)
CLONE_REFERENCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLONE_REFERENCES
Clone References option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CLONE_REFERENCES)
CONSTRAINT_FAILURE_AS_BREAKPOINT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONSTRAINT_FAILURE_AS_BREAKPOINT
Constraint Failure as Breakpoint option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CONSTRAINT_FAILURE_AS_BREAKPOINT)
DECIMAL_PLACES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DECIMAL_PLACES
Decimal Places option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DECIMAL_PLACES)
DURATION_SIMULATION_MODE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DURATION_SIMULATION_MODE
Duration Simulation Mode option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DURATION_SIMULATION_MODE)
ENDTIME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENDTIME
Endtime option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ENDTIME)
EXCLUDED_ELEMENTS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXCLUDED_ELEMENTS
Excluded Elements option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXCLUDED_ELEMENTS)
EXECUTION_LISTENERS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXECUTION_LISTENERS
Execution Listeners option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXECUTION_LISTENERS)
EXECUTION_TARGET
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXECUTION_TARGET
Execution Target option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXECUTION_TARGET)
AUTOMATIC_PARAMETRIC_RECALCULATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTOMATIC_PARAMETRIC_RECALCULATION
Automatic Parametric Recalculation option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTOMATIC_PARAMETRIC_RECALCULATION)
INITIALIZE_REFERENCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INITIALIZE_REFERENCES
Initialize References option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.INITIALIZE_REFERENCES)
LOG
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOG
Log option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.LOG)
NUMBER_OF_RUNS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBER_OF_RUNS
Number of Runs option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.NUMBER_OF_RUNS)
NUMBER_OF_STEPS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBER_OF_STEPS
Number of Steps option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.NUMBER_OF_STEPS)
OPEN_SIMULATION_PANE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPEN_SIMULATION_PANE
Display Simulation Dashboard Window option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.OPEN_SIMULATION_PANE)
REMEMBER_FAILURE_STATUS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMEMBER_FAILURE_STATUS
Remember Failure Status option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.REMEMBER_FAILURE_STATUS)
RESULT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RESULT_LOCATION
Result Location option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RESULT_LOCATION)
RUN_FORKS_IN_PARALLEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RUN_FORKS_IN_PARALLEL
Run Forks in Parallel option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RUN_FORKS_IN_PARALLEL)
START_TIME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) START_TIME
Start Time option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.START_TIME)
START_WEB_SERVER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) START_WEB_SERVER
Start Web Server option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.START_WEB_SERVER)
STARTUP_DIAGRAM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STARTUP_DIAGRAM
Startup Diagram option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STARTUP_DIAGRAM)
STEP_DELAY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEP_DELAY
Step Delay option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STEP_DELAY)
STEP_SIZE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEP_SIZE
Step Size option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STEP_SIZE)
TIME_UNIT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIME_UNIT
Time Unit option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_UNIT)
TIME_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIME_VALUE
Time Value option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_VALUE)
TIME_VARIABLE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TIME_VARIABLE_NAME
Time Variable Name option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_VARIABLE_NAME)
CLOCK_RATIO
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLOCK_RATIO
Clock Ratio option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CLOCK_RATIO)
AUTO_TERMINATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTO_TERMINATE
Auto terminate execution option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_TERMINATE)
CAPTURE_TIMESTAMP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CAPTURE_TIMESTAMP
Capture timestamp of result instance option key
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CAPTURE_TIMESTAMP)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationOptions
public SimulationOptions()
 ============ METHOD DETAIL ========== 
Method Details
set
public void set([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Add the option.
Parameters:
`optionName` - the option name
`value` - the option value
setIfAbsent
public void setIfAbsent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets without overwriting: the provided value is only set when no non-null value exists by this key yet
Parameters:
`optionName` - the option name
`value` - the option value
get
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)
Get the option value from the specified option name.
Parameters:
`optionName` - the option name
Returns:
the option value from the specified option name
is
public boolean is([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)
Get the Boolean option value from the specified option name.
Parameters:
`optionName` - the option name
Returns:
true if value of given option value is equal to [`Boolean.TRUE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#TRUE)
addOption
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void addOption([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) optionValue)
Deprecated.
use [`set(String, Object)`](#set(java.lang.String,java.lang.Object)) instead
getOption
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getOption([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionName)
Deprecated.
use shorter and more convenient [`get(String)`](#get(java.lang.String))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.execution</a></div>
<h1 class="title" title="Class SimulationOptions">Class SimulationOptions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.execution.SimulationOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SimulationOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">A class that maintains the option values being used during the execution simulation.
 Also provides out-of-the-box option key constants to retrieve the option values by.
 <p></p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVE_COLOR">ACTIVE_COLOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Active symbol color option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ADD_CONTROL_PANEL">ADD_CONTROL_PANEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Add Control Panel option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES">ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Allow Concurrent Allocated Activities option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANIMATION_SPEED">ANIMATION_SPEED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Animation Speed option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTO_CONVERT_UNITS">AUTO_CONVERT_UNITS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Turns on live unit conversion during simulation.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN">AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto Create fUML Object of Output Pin option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTO_OPEN_DIAGRAMS">AUTO_OPEN_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto open diagrams option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTO_START">AUTO_START</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto start execution option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTO_START_ACTIVE_OPTIONS">AUTO_START_ACTIVE_OPTIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto Start Active Objects option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTO_TERMINATE">AUTO_TERMINATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto terminate execution option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AUTOMATIC_PARAMETRIC_RECALCULATION">AUTOMATIC_PARAMETRIC_RECALCULATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Automatic Parametric Recalculation option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BREAKPOINT_COLOR">BREAKPOINT_COLOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Breakpoint symbol color option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CAPTURE_TIMESTAMP">CAPTURE_TIMESTAMP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Capture timestamp of result instance option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CHECK_MODEL_BEFORE_EXECUTION">CHECK_MODEL_BEFORE_EXECUTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Check Model Before Execution option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLOCK_RATIO">CLOCK_RATIO</a></code></div>
<div class="col-last even-row-color">
<div class="block">Clock Ratio option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLONE_REFERENCES">CLONE_REFERENCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Clone References option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONSTRAINT_FAILURE_AS_BREAKPOINT">CONSTRAINT_FAILURE_AS_BREAKPOINT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constraint Failure as Breakpoint option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DECIMAL_PLACES">DECIMAL_PLACES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Decimal Places option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_LANGUAGE">DEFAULT_LANGUAGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default Evaluation Language option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_PARAMETRIC_EVALUATOR">DEFAULT_PARAMETRIC_EVALUATOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Default Parametric Evaluator option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DURATION_SIMULATION_MODE">DURATION_SIMULATION_MODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Duration Simulation Mode option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENDTIME">ENDTIME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Endtime option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENGINES_PRIORITY">ENGINES_PRIORITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Registered execution engine priority option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXCLUDED_ELEMENTS">EXCLUDED_ELEMENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Excluded Elements option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXECUTION_LISTENERS">EXECUTION_LISTENERS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Execution Listeners option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXECUTION_TARGET">EXECUTION_TARGET</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Execution Target option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTERNAL_LIBRARIES">EXTERNAL_LIBRARIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">External Libraries option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXTERNAL_SOLVER_TIMEOUT">EXTERNAL_SOLVER_TIMEOUT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">External Solver Timeout option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INITIALIZE_NUMERICAL_VALUE">INITIALIZE_NUMERICAL_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Initialize Empty Values to 0 option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INITIALIZE_REFERENCES">INITIALIZE_REFERENCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Initialize References option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAST_VISITED_COLOR">LAST_VISITED_COLOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Last visited symbol color option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOG">LOG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Log option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBER_OF_RUNS">NUMBER_OF_RUNS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of Runs option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBER_OF_STEPS">NUMBER_OF_STEPS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of Steps option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPEN_SIMULATION_PANE">OPEN_SIMULATION_PANE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Display Simulation Dashboard Window option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PASS_CALLER_CONTEXT">PASS_CALLER_CONTEXT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Pass Caller Context option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RECORD_STATE_CHANGE">RECORD_STATE_CHANGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Record State Change option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECORD_TIMESTAMP">RECORD_TIMESTAMP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Record Timestamp option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RECORD_VALUE_CHANGE">RECORD_VALUE_CHANGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Record Value Change option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REMEMBER_FAILURE_STATUS">REMEMBER_FAILURE_STATUS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Remember Failure Status option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RESULT_LOCATION">RESULT_LOCATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Result Location option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RUN_FORKS_IN_PARALLEL">RUN_FORKS_IN_PARALLEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Run Forks in Parallel option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES">RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Runtime Value Text Color on Part Shapes option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOW_ACTIVE_STATE_IMAGES">SHOW_ACTIVE_STATE_IMAGES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show Active State Images option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES">SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show Active State Images on Part Shapes option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOW_ACTIVE_STATES_ON_PART_SHAPES">SHOW_ACTIVE_STATES_ON_PART_SHAPES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show Active States on Part Shapes option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOW_ANNOTATIONS">SHOW_ANNOTATIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show Annotations option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOW_FLOWING_INFORMATION">SHOW_FLOWING_INFORMATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show Flowing Information option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM">SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show Held Tokens in Activity Diagram option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOW_RUNTIME_VALUES_ON_PART_SHAPES">SHOW_RUNTIME_VALUES_ON_PART_SHAPES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Show Runtime Values on Part Shapes option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOW_RUNTIME_VALUES_ON_PORT_LABELS">SHOW_RUNTIME_VALUES_ON_PORT_LABELS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show Runtime Values on Part Shapes option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SILENT">SILENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Silent execution option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOLVE_AFTER_INITIALIZATION">SOLVE_AFTER_INITIALIZATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Solve After Initialization option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#START_TIME">START_TIME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Start Time option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#START_WEB_SERVER">START_WEB_SERVER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Start Web Server option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STARTUP_DIAGRAM">STARTUP_DIAGRAM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Startup Diagram option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEP_DELAY">STEP_DELAY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Step Delay option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEP_SIZE">STEP_SIZE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Step Size option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN">TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Terminate Behavior on Exception Thrown option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TERMINATE_NESTED_BEHAVIORS">TERMINATE_NESTED_BEHAVIORS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Terminate Nested Behaviors option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY">TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Terminate Streaming Behaviors by Output Parameter Multiplicity option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIME_UNIT">TIME_UNIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Time Unit option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TIME_VALUE">TIME_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Time Value option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TIME_VARIABLE_NAME">TIME_VARIABLE_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Time Variable Name option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TREAT_ALL_CLASSIFIERS_AS_ACTIVE">TREAT_ALL_CLASSIFIERS_AS_ACTIVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Treat All Objects as Active option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UI">UI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">UI option key</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USE_FUML_DECISION_SEMANTICS">USE_FUML_DECISION_SEMANTICS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Use fUML Decision Semantics option key</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VISITED_COLOR">VISITED_COLOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Visited symbol color option key</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimulationOptions</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addOption(java.lang.String,java.lang.Object)">addOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> optionValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#set(java.lang.String,java.lang.Object)"><code>set(String, Object)</code></a> instead</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the option value from the specified option name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getOption(java.lang.String)">getOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use shorter and more convenient <a href="#get(java.lang.String)"><code>get(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(java.lang.String)">is</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the Boolean option value from the specified option name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#set(java.lang.String,java.lang.Object)">set</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIfAbsent(java.lang.String,java.lang.Object)">setIfAbsent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets without overwriting: the provided value is only set when no non-null value exists by this key yet</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="ACTIVE_COLOR">
<h3>ACTIVE_COLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIVE_COLOR</span></div>
<div class="block">Active symbol color option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ACTIVE_COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VISITED_COLOR">
<h3>VISITED_COLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VISITED_COLOR</span></div>
<div class="block">Visited symbol color option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.VISITED_COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BREAKPOINT_COLOR">
<h3>BREAKPOINT_COLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BREAKPOINT_COLOR</span></div>
<div class="block">Breakpoint symbol color option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.BREAKPOINT_COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAST_VISITED_COLOR">
<h3>LAST_VISITED_COLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAST_VISITED_COLOR</span></div>
<div class="block">Last visited symbol color option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.LAST_VISITED_COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_OPEN_DIAGRAMS">
<h3>AUTO_OPEN_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_OPEN_DIAGRAMS</span></div>
<div class="block">Auto open diagrams option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_OPEN_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SILENT">
<h3>SILENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SILENT</span></div>
<div class="block">Silent execution option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SILENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_LANGUAGE">
<h3>DEFAULT_LANGUAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_LANGUAGE</span></div>
<div class="block">Default Evaluation Language option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DEFAULT_LANGUAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENGINES_PRIORITY">
<h3>ENGINES_PRIORITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENGINES_PRIORITY</span></div>
<div class="block">Registered execution engine priority option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ENGINES_PRIORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_START">
<h3>AUTO_START</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_START</span></div>
<div class="block">Auto start execution option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_START">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_START_ACTIVE_OPTIONS">
<h3>AUTO_START_ACTIVE_OPTIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_START_ACTIVE_OPTIONS</span></div>
<div class="block">Auto Start Active Objects option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_START_ACTIVE_OPTIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TREAT_ALL_CLASSIFIERS_AS_ACTIVE">
<h3>TREAT_ALL_CLASSIFIERS_AS_ACTIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TREAT_ALL_CLASSIFIERS_AS_ACTIVE</span></div>
<div class="block">Treat All Objects as Active option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TREAT_ALL_CLASSIFIERS_AS_ACTIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN">
<h3>TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN</span></div>
<div class="block">Terminate Behavior on Exception Thrown option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INITIALIZE_NUMERICAL_VALUE">
<h3>INITIALIZE_NUMERICAL_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INITIALIZE_NUMERICAL_VALUE</span></div>
<div class="block">Initialize Empty Values to 0 option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.INITIALIZE_NUMERICAL_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECORD_STATE_CHANGE">
<h3>RECORD_STATE_CHANGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECORD_STATE_CHANGE</span></div>
<div class="block">Record State Change option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_STATE_CHANGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECORD_VALUE_CHANGE">
<h3>RECORD_VALUE_CHANGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECORD_VALUE_CHANGE</span></div>
<div class="block">Record Value Change option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_VALUE_CHANGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECORD_TIMESTAMP">
<h3>RECORD_TIMESTAMP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECORD_TIMESTAMP</span></div>
<div class="block">Record Timestamp option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RECORD_TIMESTAMP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USE_FUML_DECISION_SEMANTICS">
<h3>USE_FUML_DECISION_SEMANTICS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USE_FUML_DECISION_SEMANTICS</span></div>
<div class="block">Use fUML Decision Semantics option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.USE_FUML_DECISION_SEMANTICS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN">
<h3>AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN</span></div>
<div class="block">Auto Create fUML Object of Output Pin option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOLVE_AFTER_INITIALIZATION">
<h3>SOLVE_AFTER_INITIALIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOLVE_AFTER_INITIALIZATION</span></div>
<div class="block">Solve After Initialization option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SOLVE_AFTER_INITIALIZATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_PARAMETRIC_EVALUATOR">
<h3>DEFAULT_PARAMETRIC_EVALUATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_PARAMETRIC_EVALUATOR</span></div>
<div class="block">Default Parametric Evaluator option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DEFAULT_PARAMETRIC_EVALUATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTERNAL_SOLVER_TIMEOUT">
<h3>EXTERNAL_SOLVER_TIMEOUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTERNAL_SOLVER_TIMEOUT</span></div>
<div class="block">External Solver Timeout option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXTERNAL_SOLVER_TIMEOUT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTERNAL_LIBRARIES">
<h3>EXTERNAL_LIBRARIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTERNAL_LIBRARIES</span></div>
<div class="block">External Libraries option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXTERNAL_LIBRARIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHECK_MODEL_BEFORE_EXECUTION">
<h3>CHECK_MODEL_BEFORE_EXECUTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHECK_MODEL_BEFORE_EXECUTION</span></div>
<div class="block">Check Model Before Execution option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CHECK_MODEL_BEFORE_EXECUTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_FLOWING_INFORMATION">
<h3>SHOW_FLOWING_INFORMATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_FLOWING_INFORMATION</span></div>
<div class="block">Show Flowing Information option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_FLOWING_INFORMATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES">
<h3>RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES</span></div>
<div class="block">Runtime Value Text Color on Part Shapes option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RUNTIME_VALUE_TEXT_COLOR_ON_PART_SHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_ACTIVE_STATES_ON_PART_SHAPES">
<h3>SHOW_ACTIVE_STATES_ON_PART_SHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_ACTIVE_STATES_ON_PART_SHAPES</span></div>
<div class="block">Show Active States on Part Shapes option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATES_ON_PART_SHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_RUNTIME_VALUES_ON_PART_SHAPES">
<h3>SHOW_RUNTIME_VALUES_ON_PART_SHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_RUNTIME_VALUES_ON_PART_SHAPES</span></div>
<div class="block">Show Runtime Values on Part Shapes option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_RUNTIME_VALUES_ON_PART_SHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_RUNTIME_VALUES_ON_PORT_LABELS">
<h3>SHOW_RUNTIME_VALUES_ON_PORT_LABELS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_RUNTIME_VALUES_ON_PORT_LABELS</span></div>
<div class="block">Show Runtime Values on Part Shapes option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_RUNTIME_VALUES_ON_PORT_LABELS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES">
<h3>SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES</span></div>
<div class="block">Show Active State Images on Part Shapes option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATE_IMAGES_ON_PART_SHAPES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_ACTIVE_STATE_IMAGES">
<h3>SHOW_ACTIVE_STATE_IMAGES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_ACTIVE_STATE_IMAGES</span></div>
<div class="block">Show Active State Images option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ACTIVE_STATE_IMAGES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM">
<h3>SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM</span></div>
<div class="block">Show Held Tokens in Activity Diagram option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_HELD_TOKENS_IN_ACTIVITY_DIAGRAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOW_ANNOTATIONS">
<h3>SHOW_ANNOTATIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOW_ANNOTATIONS</span></div>
<div class="block">Show Annotations option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.SHOW_ANNOTATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PASS_CALLER_CONTEXT">
<h3>PASS_CALLER_CONTEXT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PASS_CALLER_CONTEXT</span></div>
<div class="block">Pass Caller Context option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.PASS_CALLER_CONTEXT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TERMINATE_NESTED_BEHAVIORS">
<h3>TERMINATE_NESTED_BEHAVIORS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TERMINATE_NESTED_BEHAVIORS</span></div>
<div class="block">Terminate Nested Behaviors option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_NESTED_BEHAVIORS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY">
<h3>TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY</span></div>
<div class="block">Terminate Streaming Behaviors by Output Parameter Multiplicity option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES">
<h3>ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES</span></div>
<div class="block">Allow Concurrent Allocated Activities option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_CONVERT_UNITS">
<h3>AUTO_CONVERT_UNITS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_CONVERT_UNITS</span></div>
<div class="block">Turns on live unit conversion during simulation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_CONVERT_UNITS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UI">
<h3>UI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UI</span></div>
<div class="block">UI option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.UI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADD_CONTROL_PANEL">
<h3>ADD_CONTROL_PANEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADD_CONTROL_PANEL</span></div>
<div class="block">Add Control Panel option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ADD_CONTROL_PANEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANIMATION_SPEED">
<h3>ANIMATION_SPEED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANIMATION_SPEED</span></div>
<div class="block">Animation Speed option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ANIMATION_SPEED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLONE_REFERENCES">
<h3>CLONE_REFERENCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLONE_REFERENCES</span></div>
<div class="block">Clone References option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CLONE_REFERENCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINT_FAILURE_AS_BREAKPOINT">
<h3>CONSTRAINT_FAILURE_AS_BREAKPOINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONSTRAINT_FAILURE_AS_BREAKPOINT</span></div>
<div class="block">Constraint Failure as Breakpoint option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CONSTRAINT_FAILURE_AS_BREAKPOINT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DECIMAL_PLACES">
<h3>DECIMAL_PLACES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DECIMAL_PLACES</span></div>
<div class="block">Decimal Places option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DECIMAL_PLACES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DURATION_SIMULATION_MODE">
<h3>DURATION_SIMULATION_MODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DURATION_SIMULATION_MODE</span></div>
<div class="block">Duration Simulation Mode option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.DURATION_SIMULATION_MODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDTIME">
<h3>ENDTIME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENDTIME</span></div>
<div class="block">Endtime option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.ENDTIME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXCLUDED_ELEMENTS">
<h3>EXCLUDED_ELEMENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXCLUDED_ELEMENTS</span></div>
<div class="block">Excluded Elements option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXCLUDED_ELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXECUTION_LISTENERS">
<h3>EXECUTION_LISTENERS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXECUTION_LISTENERS</span></div>
<div class="block">Execution Listeners option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXECUTION_LISTENERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXECUTION_TARGET">
<h3>EXECUTION_TARGET</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXECUTION_TARGET</span></div>
<div class="block">Execution Target option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.EXECUTION_TARGET">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTOMATIC_PARAMETRIC_RECALCULATION">
<h3>AUTOMATIC_PARAMETRIC_RECALCULATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTOMATIC_PARAMETRIC_RECALCULATION</span></div>
<div class="block">Automatic Parametric Recalculation option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTOMATIC_PARAMETRIC_RECALCULATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INITIALIZE_REFERENCES">
<h3>INITIALIZE_REFERENCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INITIALIZE_REFERENCES</span></div>
<div class="block">Initialize References option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.INITIALIZE_REFERENCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOG">
<h3>LOG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOG</span></div>
<div class="block">Log option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.LOG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBER_OF_RUNS">
<h3>NUMBER_OF_RUNS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBER_OF_RUNS</span></div>
<div class="block">Number of Runs option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.NUMBER_OF_RUNS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBER_OF_STEPS">
<h3>NUMBER_OF_STEPS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBER_OF_STEPS</span></div>
<div class="block">Number of Steps option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.NUMBER_OF_STEPS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPEN_SIMULATION_PANE">
<h3>OPEN_SIMULATION_PANE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPEN_SIMULATION_PANE</span></div>
<div class="block">Display Simulation Dashboard Window option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.OPEN_SIMULATION_PANE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMEMBER_FAILURE_STATUS">
<h3>REMEMBER_FAILURE_STATUS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMEMBER_FAILURE_STATUS</span></div>
<div class="block">Remember Failure Status option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.REMEMBER_FAILURE_STATUS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RESULT_LOCATION">
<h3>RESULT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RESULT_LOCATION</span></div>
<div class="block">Result Location option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RESULT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RUN_FORKS_IN_PARALLEL">
<h3>RUN_FORKS_IN_PARALLEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RUN_FORKS_IN_PARALLEL</span></div>
<div class="block">Run Forks in Parallel option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.RUN_FORKS_IN_PARALLEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="START_TIME">
<h3>START_TIME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">START_TIME</span></div>
<div class="block">Start Time option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.START_TIME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="START_WEB_SERVER">
<h3>START_WEB_SERVER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">START_WEB_SERVER</span></div>
<div class="block">Start Web Server option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.START_WEB_SERVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTUP_DIAGRAM">
<h3>STARTUP_DIAGRAM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STARTUP_DIAGRAM</span></div>
<div class="block">Startup Diagram option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STARTUP_DIAGRAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STEP_DELAY">
<h3>STEP_DELAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEP_DELAY</span></div>
<div class="block">Step Delay option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STEP_DELAY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STEP_SIZE">
<h3>STEP_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEP_SIZE</span></div>
<div class="block">Step Size option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.STEP_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIME_UNIT">
<h3>TIME_UNIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIME_UNIT</span></div>
<div class="block">Time Unit option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_UNIT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIME_VALUE">
<h3>TIME_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIME_VALUE</span></div>
<div class="block">Time Value option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TIME_VARIABLE_NAME">
<h3>TIME_VARIABLE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TIME_VARIABLE_NAME</span></div>
<div class="block">Time Variable Name option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.TIME_VARIABLE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLOCK_RATIO">
<h3>CLOCK_RATIO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLOCK_RATIO</span></div>
<div class="block">Clock Ratio option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CLOCK_RATIO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AUTO_TERMINATE">
<h3>AUTO_TERMINATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTO_TERMINATE</span></div>
<div class="block">Auto terminate execution option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.AUTO_TERMINATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CAPTURE_TIMESTAMP">
<h3>CAPTURE_TIMESTAMP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CAPTURE_TIMESTAMP</span></div>
<div class="block">Capture timestamp of result instance option key</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.simulation.execution.SimulationOptions.CAPTURE_TIMESTAMP">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>SimulationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationOptions</span>()</div>
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
<section class="detail" id="set(java.lang.String,java.lang.Object)">
<h3>set</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">set</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Add the option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionName</code> - the option name</dd>
<dd><code>value</code> - the option value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIfAbsent(java.lang.String,java.lang.Object)">
<h3>setIfAbsent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIfAbsent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets without overwriting: the provided value is only set when no non-null value exists by this key yet</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionName</code> - the option name</dd>
<dd><code>value</code> - the option value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</span></div>
<div class="block">Get the option value from the specified option name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionName</code> - the option name</dd>
<dt>Returns:</dt>
<dd>the option value from the specified option name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="is(java.lang.String)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</span></div>
<div class="block">Get the Boolean option value from the specified option name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionName</code> - the option name</dd>
<dt>Returns:</dt>
<dd>true if value of given option value is equal to <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#TRUE" title="class or interface in java.lang"><code>Boolean.TRUE</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addOption(java.lang.String,java.lang.Object)">
<h3>addOption</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> optionValue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#set(java.lang.String,java.lang.Object)"><code>set(String, Object)</code></a> instead</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getOption(java.lang.String)">
<h3>getOption</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use shorter and more convenient <a href="#get(java.lang.String)"><code>get(String)</code></a></div>
</div>
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
