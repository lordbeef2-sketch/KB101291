# JAVA OPENAPI: SimulationManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/SimulationManager.html
- source_path: `com/nomagic/magicdraw/simulation/SimulationManager.html`
- source_sha256: `69c68bb60ce62a5b6134d751933b447e5f61092ee8fa15bdaafb29e5ebd94789`
- captured_utc: `2026-07-14T16:58:02.070581+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation](package-summary.html)

## Class SimulationManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.SimulationManager

@OpenApiAllpublic final classSimulationManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
API for running and stopping simulations and registering simulation listeners

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [SimulationResult](execution/SimulationResult.html)`
`[execute](#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean start)`
Non-blocking method for executing the specific element.
`static [SimulationResult](execution/SimulationResult.html)`
`[executeWithConfig](#executeWithConfig(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 boolean start)`
Executes the target element with a specific simulation config.
`static [Object_](fuml/classes/Object_.html)`
`[getContext](#getContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](execution/session/SimulationSession.html) session)`
Get the context of the running session.
`static [SimulationSession](execution/session/SimulationSession.html)`
`[getRefSession](#getRefSession(com.nomagic.magicdraw.simulation.fuml.classes.Object_))([Object_](fuml/classes/Object_.html) object)`
Deprecated.
use object.getRefSession()
`static [Object_](fuml/classes/Object_.html)`
`[getRootContext](#getRootContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](execution/session/SimulationSession.html) session)`
Get the root context of the running session.
`static [SimulationSession](execution/session/SimulationSession.html)`
`[getSession](#getSession(com.nomagic.magicdraw.simulation.execution.SimulationResult))([SimulationResult](execution/SimulationResult.html) result)`
Retrieves simulation session from simulation result.
`static boolean`
`[isSilentSimulation](#isSilentSimulation(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](execution/session/SimulationSession.html) session)`
Deprecated.
session.getExecution().getOptions().is(SimulationOptions.SILENT);
`static void`
`[logConsoleDebug](#logConsoleDebug(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Log the specified message to the simulation console with "DEBUG" log level.
`static void`
`[logConsoleError](#logConsoleError(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Log the specified message to the simulation console with "ERROR" log level.
`static void`
`[logConsoleInfo](#logConsoleInfo(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Log the specified message to the simulation console with "INFO" log level.
`static void`
`[logConsoleWarn](#logConsoleWarn(com.nomagic.magicdraw.uml.BaseElement,java.lang.String))([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Log the specified message to the simulation console with "WARN" log level.
`static void`
`[registerEngine](#registerEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor))([ExecutionEngineDescriptor](engine/ExecutionEngineDescriptor.html) engineDescriptor)`
Registers an engine descriptor to the simulation framework.
`static void`
`[registerSimulationExecutionListener](#registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener))([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener)`
Register the simulation execution listener.
`static void`
`[registerSimulationExecutionListener](#registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener,
 [SimulationExecution](execution/SimulationExecution.html) execution)`
Register the simulation execution listener dynamically to the specified SimulationExecution.
`static void`
`[registerSimulationOptionsProvider](#registerSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider))([SimulationOptionsProvider](execution/SimulationOptionsProvider.html) optionsProvider)`
Register the simulation options provider.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.Object...))([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) simulationConfigKeyword,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String%5B%5D,java.lang.Object...))([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) simulationConfigKeyword,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,java.lang.String%5B%5D,java.lang.Object...))([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) configKeyword,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetKeyword,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the target element with a specific simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig)`
Executes the simulation config and waits for execution to complete.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the target element with a specific simulation config with initial custom values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the target element with a specific simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)`
Executes the target element with a specific simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the simulation config with custom initial values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Executes the simulation config with initial custom values.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[simulate](#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)`
Executes the simulation config or an element with custom initial values.
`static [SimulationResult](execution/SimulationResult.html)`
`[simulateAsync](#simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)`
Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
`static [SimulationResult](execution/SimulationResult.html)`
`[simulateAsync](#simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)`
Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
`static void`
`[terminate](#terminate(com.nomagic.magicdraw.simulation.execution.SimulationResult))([SimulationResult](execution/SimulationResult.html) result)`
Terminates the running execution, represented by the result object;
`static void`
`[terminateSession](#terminateSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](execution/session/SimulationSession.html) session)`
Terminate the running session.
`static void`
`[unregisterEngine](#unregisterEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor))([ExecutionEngineDescriptor](engine/ExecutionEngineDescriptor.html) engineDescriptor)`
Unregisters an engine descriptor from the simulation framework.
`static void`
`[unregisterSimulationExecutionListener](#unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener))([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener)`
Unregister the simulation execution listener.
`static void`
`[unregisterSimulationExecutionListener](#unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener,
 [SimulationExecution](execution/SimulationExecution.html) execution)`
unregister the simulation execution listener dynamically from the specified SimulationExecution.
`static void`
`[unregisterSimulationOptionsProvider](#unregisterSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider))([SimulationOptionsProvider](execution/SimulationOptionsProvider.html) optionsProvider)`
Unregister the simulation options provider.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationManager
public SimulationManager()
 ============ METHOD DETAIL ========== 
Method Details
registerEngine
public static void registerEngine([ExecutionEngineDescriptor](engine/ExecutionEngineDescriptor.html) engineDescriptor)
Registers an engine descriptor to the simulation framework.
Parameters:
`engineDescriptor` - an engine descriptor.
unregisterEngine
public static void unregisterEngine([ExecutionEngineDescriptor](engine/ExecutionEngineDescriptor.html) engineDescriptor)
Unregisters an engine descriptor from the simulation framework.
Parameters:
`engineDescriptor` - an engine descriptor.
execute
public static [SimulationResult](execution/SimulationResult.html) execute([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean start)
Non-blocking method for executing the specific element.
Parameters:
`element` - the element to be executed, e.g. Class, Activity or a SimulationConfig with a target set
`start` - if this flag is true, it will auto start the session.
 if the element is SimulationConfig, this flag will be ignored, it will use value inside SimulationConfig instead.
Returns:
the created SimulationResult. If this method is called in EDT, the returned SimulationResult will not be completed yet, it requires to release EDT for
 values completion.
executeWithConfig
public static [SimulationResult](execution/SimulationResult.html) executeWithConfig([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 boolean start)
Executes the target element with a specific simulation config. Non-blocking method.
Parameters:
`target` - target element to execute, for example InstanceSpecification
`simulationConfig` - config that is compatible with the target element
`start` - if this flag is true, it will auto start the session.
Returns:
the created SimulationResult.
isSilentSimulation
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSilentSimulation([SimulationSession](execution/session/SimulationSession.html) session)
Deprecated.
session.getExecution().getOptions().is(SimulationOptions.SILENT);
terminateSession
public static void terminateSession(@CheckForNull
 [SimulationSession](execution/session/SimulationSession.html) session)
Terminate the running session.
Parameters:
`session` - the session being terminated
terminate
public static void terminate(@CheckForNull
 [SimulationResult](execution/SimulationResult.html) result)
Terminates the running execution, represented by the result object;
registerSimulationExecutionListener
public static void registerSimulationExecutionListener([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener)
Register the simulation execution listener.
Parameters:
`listener` - the registered simulation execution listener
registerSimulationExecutionListener
public static void registerSimulationExecutionListener([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener,
 [SimulationExecution](execution/SimulationExecution.html) execution)
Register the simulation execution listener dynamically to the specified SimulationExecution.
Parameters:
`listener` - the registered simulation execution listener
`execution` - the simulation execution
registerSimulationOptionsProvider
public static void registerSimulationOptionsProvider([SimulationOptionsProvider](execution/SimulationOptionsProvider.html) optionsProvider)
Register the simulation options provider.
Parameters:
`optionsProvider` - the registered simulation options provider
unregisterSimulationExecutionListener
public static void unregisterSimulationExecutionListener([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener)
Unregister the simulation execution listener.
Parameters:
`listener` - the unregistered simulation execution listener
unregisterSimulationExecutionListener
public static void unregisterSimulationExecutionListener([SimulationExecutionListener](execution/SimulationExecutionListener.html) listener,
 [SimulationExecution](execution/SimulationExecution.html) execution)
unregister the simulation execution listener dynamically from the specified SimulationExecution.
Parameters:
`listener` - the unregistered simulation execution listener
`execution` - the simulation execution
unregisterSimulationOptionsProvider
public static void unregisterSimulationOptionsProvider([SimulationOptionsProvider](execution/SimulationOptionsProvider.html) optionsProvider)
Unregister the simulation options provider.
Parameters:
`optionsProvider` - the registered simulation options provider
logConsoleDebug
public static void logConsoleDebug([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Log the specified message to the simulation console with "DEBUG" log level.
Parameters:
`element` - an element of the running simulation
`message` - the specified message
logConsoleInfo
public static void logConsoleInfo([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Log the specified message to the simulation console with "INFO" log level.
Parameters:
`element` - an element of the running simulation
`message` - the specified message
logConsoleWarn
public static void logConsoleWarn([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Log the specified message to the simulation console with "WARN" log level.
Parameters:
`element` - an element of the running simulation
`message` - the specified message
logConsoleError
public static void logConsoleError([BaseElement](../uml/BaseElement.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Log the specified message to the simulation console with "ERROR" log level.
Parameters:
`element` - an element of the running simulation
`message` - the specified message
getRefSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [SimulationSession](execution/session/SimulationSession.html) getRefSession([Object_](fuml/classes/Object_.html) object)
Deprecated.
use object.getRefSession()
getSession
@CheckForNullpublic static [SimulationSession](execution/session/SimulationSession.html) getSession([SimulationResult](execution/SimulationResult.html) result)
Retrieves simulation session from simulation result.
Returns:
session retrieved from simulation result
getRootContext
@CheckForNullpublic static [Object_](fuml/classes/Object_.html) getRootContext([SimulationSession](execution/session/SimulationSession.html) session)
Get the root context of the running session.
Parameters:
`session` - the running session
Returns:
the root context
getContext
@CheckForNullpublic static [Object_](fuml/classes/Object_.html) getContext([SimulationSession](execution/session/SimulationSession.html) session)
Get the context of the running session.
Parameters:
`session` - the running session
Returns:
the context of the running session
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) configKeyword,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetKeyword,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the target element with a specific simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`context` - search context where to look simulationConfigKeyword and targetKeyword
`configKeyword` - config name or id that is compatible with the target element
`targetKeyword` - the target element name or id to execute, for example InstanceSpecification
`outputs` - array of parameters names which will be returned
`inputs` - key-value pair of parameters values which will be used in simulation
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) simulationConfigKeyword,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`context` - search context where to look simulationConfigKeyword
`simulationConfigKeyword` - simulation config name or id
`inputs` - key-value pair of parameters values which will be used in simulation
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([BaseElement](../uml/BaseElement.html) context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) simulationConfigKeyword,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`context` - search context where to look simulation config
`simulationConfigKeyword` - simulation configuration name or id
`outputs` - array of parameters names which will be returned
`inputs` - key-value pair of parameters values which will be used in simulation
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the target element with a specific simulation config with initial custom values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`simulationConfig` - that is compatible with the target element
`target` - the element to execute, for example InstanceSpecification
`inputs` - key-value pair of parameters values which will be used in simulation
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig)
Executes the simulation config and waits for execution to complete.
Parameters:
`simulationConfig` - the element to execute
Returns:
all system values at end time.
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the simulation config with custom initial values.
Parameters:
`simulationConfig` - the element to execute
`inputs` - key value pair-of parameters values which will be used in simulation
Returns:
all system values at end time.
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the simulation config with initial custom values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`element` - the element to execute - either a SimulationConfig, or a Classifier/Behavior directly.
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the simulation config or an element with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`element` - the element to execute - either a SimulationConfig, or a Classifier/Behavior directly.
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the target element with a specific simulation config with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`simulationConfig` - that is compatible with the target element
`target` - the target element to execute, for example InstanceSpecification
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulate
public static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> simulate([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Executes the target element with a specific simulation config with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`simulationConfig` - that is compatible with the target element
`target` - the target element to execute with the specified config, for example InstanceSpecification
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the simulation parameters values
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulateAsync
public static [SimulationResult](execution/SimulationResult.html) simulateAsync([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] outputs,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`simulationConfig` - config that is compatible with the target element
`target` - target element to execute, for example InstanceSpecification
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the created SimulationResult
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing
simulateAsync
public static [SimulationResult](execution/SimulationResult.html) simulateAsync([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) simulationConfig,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> outputs,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> inputs)
 throws [SimulationInputValuesException](exceptions/SimulationInputValuesException.html)
Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.
Parameters:
`simulationConfig` - config that is compatible with the target element
`target` - target element to execute, for example InstanceSpecification
`outputs` - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.
`inputs` - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
 as described in the model.
Returns:
the created SimulationResult
Throws:
`[SimulationInputValuesException](exceptions/SimulationInputValuesException.html)` - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation</a></div>
<h1 class="title" title="Class SimulationManager">Class SimulationManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.SimulationManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SimulationManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">API for running and stopping simulations and registering simulation listeners</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimulationManager</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">execute</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean start)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Non-blocking method for executing the specific element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#executeWithConfig(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">executeWithConfig</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 boolean start)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the target element with a specific simulation config.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">getContext</a><wbr/>(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the context of the running session.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRefSession(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">getRefSession</a><wbr/>(<a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use object.getRefSession()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">getRootContext</a><wbr/>(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the root context of the running session.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSession(com.nomagic.magicdraw.simulation.execution.SimulationResult)">getSession</a><wbr/>(<a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a> result)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves simulation session from simulation result.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSilentSimulation(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">isSilentSimulation</a><wbr/>(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">session.getExecution().getOptions().is(SimulationOptions.SILENT);</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#logConsoleDebug(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">logConsoleDebug</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Log the specified message to the simulation console with "DEBUG" log level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#logConsoleError(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">logConsoleError</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Log the specified message to the simulation console with "ERROR" log level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#logConsoleInfo(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">logConsoleInfo</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Log the specified message to the simulation console with "INFO" log level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#logConsoleWarn(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">logConsoleWarn</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Log the specified message to the simulation console with "WARN" log level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">registerEngine</a><wbr/>(<a href="engine/ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers an engine descriptor to the simulation framework.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">registerSimulationExecutionListener</a><wbr/>(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register the simulation execution listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">registerSimulationExecutionListener</a><wbr/>(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener,
 <a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register the simulation execution listener dynamically to the specified SimulationExecution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider)">registerSimulationOptionsProvider</a><wbr/>(<a href="execution/SimulationOptionsProvider.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationOptionsProvider</a> optionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register the simulation options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.Object...)">simulate</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> simulationConfigKeyword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config with custom initial values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String%5B%5D,java.lang.Object...)">simulate</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> simulationConfigKeyword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config with custom initial values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,java.lang.String%5B%5D,java.lang.Object...)">simulate</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configKeyword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetKeyword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the target element with a specific simulation config with custom initial values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config and waits for execution to complete.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the target element with a specific simulation config with initial custom values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the target element with a specific simulation config with custom initial values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the target element with a specific simulation config with custom initial values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config with custom initial values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config with initial custom values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">simulate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes the simulation config or an element with custom initial values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.Object...)">simulateAsync</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Asynchronously executes the target element with a specific simulation config with custom initial parameters values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">simulateAsync</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Asynchronously executes the target element with a specific simulation config with custom initial parameters values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#terminate(com.nomagic.magicdraw.simulation.execution.SimulationResult)">terminate</a><wbr/>(<a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a> result)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Terminates the running execution, represented by the result object;</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#terminateSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">terminateSession</a><wbr/>(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Terminate the running session.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">unregisterEngine</a><wbr/>(<a href="engine/ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregisters an engine descriptor from the simulation framework.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">unregisterSimulationExecutionListener</a><wbr/>(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregister the simulation execution listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">unregisterSimulationExecutionListener</a><wbr/>(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener,
 <a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">unregister the simulation execution listener dynamically from the specified SimulationExecution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider)">unregisterSimulationOptionsProvider</a><wbr/>(<a href="execution/SimulationOptionsProvider.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationOptionsProvider</a> optionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregister the simulation options provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>SimulationManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationManager</span>()</div>
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
<section class="detail" id="registerEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">
<h3>registerEngine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerEngine</span><wbr/><span class="parameters">(<a href="engine/ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</span></div>
<div class="block">Registers an engine descriptor to the simulation framework.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineDescriptor</code> - an engine descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">
<h3>unregisterEngine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterEngine</span><wbr/><span class="parameters">(<a href="engine/ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</span></div>
<div class="block">Unregisters an engine descriptor from the simulation framework.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineDescriptor</code> - an engine descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean start)</span></div>
<div class="block">Non-blocking method for executing the specific element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to be executed, e.g. Class, Activity or a SimulationConfig with a target set</dd>
<dd><code>start</code> - if this flag is true, it will auto start the session.
                if the element is SimulationConfig, this flag will be ignored, it will use value inside SimulationConfig instead.</dd>
<dt>Returns:</dt>
<dd>the created SimulationResult. If this method is called in EDT, the returned SimulationResult will not be completed yet, it requires to release EDT for
 values completion.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeWithConfig(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>executeWithConfig</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></span> <span class="element-name">executeWithConfig</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 boolean start)</span></div>
<div class="block">Executes the target element with a specific simulation config. Non-blocking method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target element to execute, for example InstanceSpecification</dd>
<dd><code>simulationConfig</code> - config that is compatible with the target element</dd>
<dd><code>start</code> - if this flag is true, it will auto start the session.</dd>
<dt>Returns:</dt>
<dd>the created SimulationResult.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSilentSimulation(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>isSilentSimulation</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSilentSimulation</span><wbr/><span class="parameters">(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">session.getExecution().getOptions().is(SimulationOptions.SILENT);</div>
</div>
</section>
</li>
<li>
<section class="detail" id="terminateSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>terminateSession</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">terminateSession</span><wbr/><span class="parameters">(@CheckForNull
 <a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">Terminate the running session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the session being terminated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="terminate(com.nomagic.magicdraw.simulation.execution.SimulationResult)">
<h3>terminate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">terminate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a> result)</span></div>
<div class="block">Terminates the running execution, represented by the result object;</div>
</section>
</li>
<li>
<section class="detail" id="registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">
<h3>registerSimulationExecutionListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerSimulationExecutionListener</span><wbr/><span class="parameters">(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</span></div>
<div class="block">Register the simulation execution listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the registered simulation execution listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>registerSimulationExecutionListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerSimulationExecutionListener</span><wbr/><span class="parameters">(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener,
 <a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Register the simulation execution listener dynamically to the specified SimulationExecution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the registered simulation execution listener</dd>
<dd><code>execution</code> - the simulation execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider)">
<h3>registerSimulationOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerSimulationOptionsProvider</span><wbr/><span class="parameters">(<a href="execution/SimulationOptionsProvider.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationOptionsProvider</a> optionsProvider)</span></div>
<div class="block">Register the simulation options provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionsProvider</code> - the registered simulation options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">
<h3>unregisterSimulationExecutionListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterSimulationExecutionListener</span><wbr/><span class="parameters">(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</span></div>
<div class="block">Unregister the simulation execution listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the unregistered simulation execution listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterSimulationExecutionListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>unregisterSimulationExecutionListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterSimulationExecutionListener</span><wbr/><span class="parameters">(<a href="execution/SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener,
 <a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">unregister the simulation execution listener dynamically from the specified SimulationExecution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the unregistered simulation execution listener</dd>
<dd><code>execution</code> - the simulation execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterSimulationOptionsProvider(com.nomagic.magicdraw.simulation.execution.SimulationOptionsProvider)">
<h3>unregisterSimulationOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterSimulationOptionsProvider</span><wbr/><span class="parameters">(<a href="execution/SimulationOptionsProvider.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationOptionsProvider</a> optionsProvider)</span></div>
<div class="block">Unregister the simulation options provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionsProvider</code> - the registered simulation options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logConsoleDebug(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>logConsoleDebug</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">logConsoleDebug</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Log the specified message to the simulation console with "DEBUG" log level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element of the running simulation</dd>
<dd><code>message</code> - the specified message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logConsoleInfo(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>logConsoleInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">logConsoleInfo</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Log the specified message to the simulation console with "INFO" log level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element of the running simulation</dd>
<dd><code>message</code> - the specified message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logConsoleWarn(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>logConsoleWarn</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">logConsoleWarn</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Log the specified message to the simulation console with "WARN" log level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element of the running simulation</dd>
<dd><code>message</code> - the specified message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logConsoleError(com.nomagic.magicdraw.uml.BaseElement,java.lang.String)">
<h3>logConsoleError</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">logConsoleError</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Log the specified message to the simulation console with "ERROR" log level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an element of the running simulation</dd>
<dd><code>message</code> - the specified message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRefSession(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>getRefSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getRefSession</span><wbr/><span class="parameters">(<a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use object.getRefSession()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSession(com.nomagic.magicdraw.simulation.execution.SimulationResult)">
<h3>getSession</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getSession</span><wbr/><span class="parameters">(<a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a> result)</span></div>
<div class="block">Retrieves simulation session from simulation result.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>session retrieved from simulation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>getRootContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></span> <span class="element-name">getRootContext</span><wbr/><span class="parameters">(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">Get the root context of the running session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session</dd>
<dt>Returns:</dt>
<dd>the root context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></span> <span class="element-name">getContext</span><wbr/><span class="parameters">(<a href="execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">Get the context of the running session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session</dd>
<dt>Returns:</dt>
<dd>the context of the running session</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String,java.lang.String[],java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configKeyword,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetKeyword,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the target element with a specific simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - search context where to look simulationConfigKeyword and targetKeyword</dd>
<dd><code>configKeyword</code> - config name or id that is compatible with the target element</dd>
<dd><code>targetKeyword</code> - the target element name or id to execute, for example InstanceSpecification</dd>
<dd><code>outputs</code> - array of parameters names which will be returned</dd>
<dd><code>inputs</code> - key-value pair of parameters values which will be used in simulation</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> simulationConfigKeyword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - search context where to look simulationConfigKeyword</dd>
<dd><code>simulationConfigKeyword</code> - simulation config name or id</dd>
<dd><code>inputs</code> - key-value pair of parameters values which will be used in simulation</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.magicdraw.uml.BaseElement,java.lang.String,java.lang.String[],java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> simulationConfigKeyword,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the simulation config with custom initial values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - search context where to look simulation config</dd>
<dd><code>simulationConfigKeyword</code> - simulation configuration name or id</dd>
<dd><code>outputs</code> - array of parameters names which will be returned</dd>
<dd><code>inputs</code> - key-value pair of parameters values which will be used in simulation</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the target element with a specific simulation config with initial custom values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - that is compatible with the target element</dd>
<dd><code>target</code> - the element to execute, for example InstanceSpecification</dd>
<dd><code>inputs</code> - key-value pair of parameters values which will be used in simulation</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig)</span></div>
<div class="block">Executes the simulation config and waits for execution to complete.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - the element to execute</dd>
<dt>Returns:</dt>
<dd>all system values at end time.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the simulation config with custom initial values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - the element to execute</dd>
<dd><code>inputs</code> - key value pair-of parameters values which will be used in simulation</dd>
<dt>Returns:</dt>
<dd>all system values at end time.</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String[],java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the simulation config with initial custom values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to execute - either a SimulationConfig, or a Classifier/Behavior directly.</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                as described in the model.</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the simulation config or an element with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to execute - either a SimulationConfig, or a Classifier/Behavior directly.</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                as described in the model.</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String[],java.lang.Object...)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the target element with a specific simulation config with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - that is compatible with the target element</dd>
<dd><code>target</code> - the target element to execute, for example InstanceSpecification</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                         as described in the model.</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">
<h3>simulate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">simulate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</span>
                                   throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Executes the target element with a specific simulation config with custom initial values. This is a blocking method.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - that is compatible with the target element</dd>
<dd><code>target</code> - the target element to execute with the specified config, for example InstanceSpecification</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                         as described in the model.</dd>
<dt>Returns:</dt>
<dd>the simulation parameters values</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String[],java.lang.Object...)">
<h3>simulateAsync</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></span> <span class="element-name">simulateAsync</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputs)</span>
                                      throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - config that is compatible with the target element</dd>
<dd><code>target</code> - target element to execute, for example InstanceSpecification</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                         as described in the model.</dd>
<dt>Returns:</dt>
<dd>the created SimulationResult</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simulateAsync(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,java.util.Map)">
<h3>simulateAsync</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="execution/SimulationResult.html" title="interface in com.nomagic.magicdraw.simulation.execution">SimulationResult</a></span> <span class="element-name">simulateAsync</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> simulationConfig,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; outputs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; inputs)</span>
                                      throws <span class="exceptions"><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></span></div>
<div class="block">Asynchronously executes the target element with a specific simulation config with custom initial parameters values.
 Returns specified simulation parameters values, or all simulation values if it isn't specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>simulationConfig</code> - config that is compatible with the target element</dd>
<dd><code>target</code> - target element to execute, for example InstanceSpecification</dd>
<dd><code>outputs</code> - names of parameter runtime values to be returned when simulation completes. When null is provided, all values will be returned.</dd>
<dd><code>inputs</code> - key-value map of values which will be used as initial values for the execution. When null is provided, execution will be initialized with values
                         as described in the model.</dd>
<dt>Returns:</dt>
<dd>the created SimulationResult</dd>
<dt>Throws:</dt>
<dd><code><a href="exceptions/SimulationInputValuesException.html" title="class in com.nomagic.magicdraw.simulation.exceptions">SimulationInputValuesException</a></code> - if inputs value type mismatch, not all input values was replaced or inputs key value parameter is missing</dd>
</dl>
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
