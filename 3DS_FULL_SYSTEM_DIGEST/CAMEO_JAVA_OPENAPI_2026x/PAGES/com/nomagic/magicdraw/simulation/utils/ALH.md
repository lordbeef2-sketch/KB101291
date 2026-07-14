# JAVA OPENAPI: ALH (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/utils/ALH.html
- source_path: `com/nomagic/magicdraw/simulation/utils/ALH.html`
- source_sha256: `f023813000df20fd07e1a491adde2bec1d6bc38b3b3369c3d2be74ad72a552cd`
- captured_utc: `2026-07-14T16:58:04.325606+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.utils](package-summary.html)

## Class ALH

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.utils.ALH

@OpenApiAllpublic final classALH
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

An Action Language Helper for using in scripts to access values of the runtime object.

Since:
SIM 1.0

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ALH](#%3Cinit%3E())()`
Constructor.
`[ALH](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](../execution/session/SimulationSession.html) session)`
Constructor.
`[ALH](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List))([SimulationSession](../execution/session/SimulationSession.html) session,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> trace)`
Constructor.
`[ALH](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_))([SimulationSession](../execution/session/SimulationSession.html) session,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> trace,
 [Object_](../fuml/classes/Object_.html) context)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addValue](#addValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Find the matched `FeatureValue` from the specified `object`,
 and set the `value` at the last position of the value list.
`void`
`[addValueAt](#addValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object,java.lang.Integer))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) insertAt)`
Find the matched `FeatureValue` from the specified `object`,
 and set the `value` at the `insertAt` position.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callBehavior](#callBehavior(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Execute the `Behavior` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callBehavior](#callBehavior(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)`
Execute the CallBehaviorAction element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callBehavior](#callBehavior(java.lang.String,java.util.List,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchonous)`
Execute the CallBehaviorAction element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String,java.util.List,boolean))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchronous)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List,boolean))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchronous)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Execute the method of the `Operation` element that matches the specified name.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)`
Execute the method of the `Operation` element that matches the specified name.
`[ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[createList](#createList())()`
A convenience method for creating the list.
`[ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[createList](#createList(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)`
A convenience method for creating the list with one added item in the list.
`[Object_](../fuml/classes/Object_.html)`
`[createObject](#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) classifier)`
Create an `Object_` with the given type (which must be a `Class`) in the `Locus` of the active `SimulationSession`.
`[Object_](../fuml/classes/Object_.html)`
`[createObject](#createObject(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Create an `Object_` with the given `name` (which must be name of `Class`)
 as its type.
`[SignalInstance](../fuml/behaviors/communications/SignalInstance.html)`
`[createSignal](#createSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))([Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)`
Create the instance of `SignalInstance`.
`[SignalInstance](../fuml/behaviors/communications/SignalInstance.html)`
`[createSignal](#createSignal(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) keyword)`
Create the instance of `SignalInstance`.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[evaluate](#evaluate(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)`
Evaluate the string expression.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[evaluate](#evaluate(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)`
Evaluate the string expression based on the specified scripting language.
`[NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)`
`[getCaller](#getCaller())()`
Get the calling element of the script evaluation.
`[Object_](../fuml/classes/Object_.html)`
`[getContext](#getContext())()`
Get the context of ALH.
`double`
`[getCurrentTime](#getCurrentTime())()`
Gets current time.
`double`
`[getCurrentTime](#getCurrentTime(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) timeUnit)`
Gets current time in forms of the specified `timeUnit`.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getGlobalVariable](#getGlobalVariable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)`
Gets global variable from the execution.
`[SignalInstance](../fuml/behaviors/communications/SignalInstance.html)`
`[getLastSignal](#getLastSignal(com.nomagic.magicdraw.simulation.fuml.classes.Object_))([Object_](../fuml/classes/Object_.html) o)`
Get the last signal instance from the event pool.
`[State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html)`
`[getState](#getState(com.nomagic.magicdraw.simulation.fuml.classes.Object_))([Object_](../fuml/classes/Object_.html) object)`
Get the current `State` from the specified `object`.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getTagValue](#getTagValue(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Get tag value from classifier of Object, and structural feature that Object represented
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getTagValue](#getTagValue(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Get tag value from classifier of context.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTimeUnit](#getTimeUnit())()`
Gets time unit of the running execution.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getTokenValue](#getTokenValue())()`
Get Tokens values from the current context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName)`
Get the value of `FeatureValue` from the `object` that match
 the specified `StructureFeature` name.
`boolean`
`[inState](#inState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)`
Check whether the specified object is in the specified state name or not.
`boolean`
`[inState](#inState(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)`
Check whether the current runtime object is in the specified state name or not.
`[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)`
`[isGlobalVariable](#isGlobalVariable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)`
Checks whether or not the given `variableName` is global variable.
`void`
`[removeGlobalVariable](#removeGlobalVariable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)`
Removes global variable from the execution.
`void`
`[removeValue](#removeValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Value))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Value](../fuml/classes/Value.html) value)`
Find the matched `FeatureValue` from the specified `object`,
 remove the defined `value` or the value at `removeAt` position.
`void`
`[removeValueAt](#removeValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Integer))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) removeAt)`
Find the matched `FeatureValue` from the specified `object`,
 remove the defined `value` or the value at `removeAt` position.
`void`
`[sendSignal](#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_))([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [Object_](../fuml/classes/Object_.html) target)`
Send the specified `SignalInstance` to the specified target `Object_`.
`void`
`[sendSignal](#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [Object_](../fuml/classes/Object_.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)`
Send the specified `SignalInstance` to the specified target `Object_` via the specified port name.
`void`
`[sendSignal](#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,java.lang.String))([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName)`
Send the specified `SignalInstance` to the specified `targetName`.
`void`
`[sendSignal](#sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [Object_](../fuml/classes/Object_.html) target)`
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_`.
`void`
`[sendSignal](#sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [Object_](../fuml/classes/Object_.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)`
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_` via the specified port name.
`void`
`[sendSignal](#sendSignal(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName)`
Create SignalInstance instance of the specified `Signal` name, and send it to the specified `targetName`.
`void`
`[setGlobalVariable](#setGlobalVariable(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Sets global variable for the execution.
`void`
`[setValue](#setValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object))([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Find the matched `FeatureValue` from the specified `object`, and set the `value`.
`void`
`[setValue](#setValue(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Find the matched `FeatureValue` from the `context`, and set the `value`.
`boolean`
`[wasInState](#wasInState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String))([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)`
Check that the state matching with the name was already visited or not.
`boolean`
`[wasInState](#wasInState(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)`
Check that the state matching with the name was already visited or not.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ALH
public ALH()
Constructor.
ALH
public ALH([SimulationSession](../execution/session/SimulationSession.html) session)
Constructor.
Parameters:
`session` - the running session
ALH
public ALH([SimulationSession](../execution/session/SimulationSession.html) session,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> trace)
Constructor.
Parameters:
`session` - the running session
`trace` - trace
ALH
public ALH(@CheckForNull
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> trace,
 [Object_](../fuml/classes/Object_.html) context)
Constructor.
Parameters:
`session` - the running session
`trace` - trace
`context` - the context
 ============ METHOD DETAIL ========== 
Method Details
getContext
@CheckForNullpublic [Object_](../fuml/classes/Object_.html) getContext()
Get the context of ALH.
Returns:
context of ALH.
getValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName)
Get the value of `FeatureValue` from the `object` that match
 the specified `StructureFeature` name. It supports nested structural features.
Parameters:
`object` - the specified instance of `StructuredValue`(or its subclasses)
`featureName` - the specified name, it will check with StructuralFeature name, nested structural features such as "part1.part2" are allowed.
Returns:
the value of `FeatureValue`
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if `object` or `featureName` is null.
See Also:
[`fUMLHelper.getFeatureValueByName(StructuredValue, String)`](../fuml/fUMLHelper.html#getFeatureValueByName(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String))
[`fUMLHelper.getObjectFromFeatureValue(FeatureValue)`](../fuml/fUMLHelper.html#getObjectFromFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue))
setValue
public void setValue([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Find the matched `FeatureValue` from the specified `object`, and set the `value`.
 If not found, create the new `FeatureValue` and add to the specified `object`.
 It supports nested structural features.

 If want to find `FeatureValue` from `Association`(`Link`),
 use [`fUMLHelper.addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)`](../fuml/fUMLHelper.html#addFeatureValues(com.nomagic.magicdraw.simulation.fuml.loci.Locus,com.nomagic.magicdraw.simulation.fuml.classes.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.magicdraw.simulation.fuml.classes.ValueList,int,boolean))
Parameters:
`object` - the fUML runtime Object_ or SignalInstance
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`value` - the value to be set. Can be Java value or fUML Value.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if `object` or `featureName` is null.
See Also:
[`fUMLHelper.setFeatureValue(StructuredValue, StructuralFeature, Object)`](../fuml/fUMLHelper.html#setFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object))
setValue
public void setValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Find the matched `FeatureValue` from the `context`, and set the `value`.
 If not found, create the new `FeatureValue` and add to the `context`.
 It supports nested structural features.

 If want to find `FeatureValue` from `Association`(`Link`),
 use [`fUMLHelper.addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)`](../fuml/fUMLHelper.html#addFeatureValues(com.nomagic.magicdraw.simulation.fuml.loci.Locus,com.nomagic.magicdraw.simulation.fuml.classes.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.magicdraw.simulation.fuml.classes.ValueList,int,boolean))
Parameters:
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`value` - the value to be set. Can be Java value or fUML Value.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if `object` or `featureName` is null.
See Also:
[`fUMLHelper.setFeatureValue(StructuredValue, StructuralFeature, Object)`](../fuml/fUMLHelper.html#setFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object))
addValue
public void addValue([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Find the matched `FeatureValue` from the specified `object`,
 and set the `value` at the last position of the value list.
Parameters:
`object` - the fUML runtime Object_ or SignalInstance
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`value` - the value to be set. Can be Java value or fUML Value.
addValueAt
public void addValueAt([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) insertAt)
Find the matched `FeatureValue` from the specified `object`,
 and set the `value` at the `insertAt` position.
Parameters:
`object` - the fUML runtime Object_ or SignalInstance
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`value` - the value to be set. Can be Java value or fUML Value.
`insertAt` - the inserted position. if it is not more than 0, the value will be added at the last position.
removeValue
public void removeValue([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Value](../fuml/classes/Value.html) value)
Find the matched `FeatureValue` from the specified `object`,
 remove the defined `value` or the value at `removeAt` position.
Parameters:
`object` - the fUML runtime Object_ or SignalInstance
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`value` - the fUML value to be removed.
removeValueAt
public void removeValueAt([StructuredValue](../fuml/classes/StructuredValue.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) featureName,
 [Integer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html) removeAt)
Find the matched `FeatureValue` from the specified `object`,
 remove the defined `value` or the value at `removeAt` position.
Parameters:
`object` - the fUML runtime Object_ or SignalInstance
`featureName` - the name of structural feature, nested structural features such as "part1.part2" are allowed.
`removeAt` - if the removeAt is defined. it will remove the value at `removeAt` position, ignoring the `value` value
getState
@CheckForNullpublic [State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) getState([Object_](../fuml/classes/Object_.html) object)
Get the current `State` from the specified `object`.
 If `object` has more than one active states, return the first one.
Parameters:
`object` - the instance of `Object_`(or its subclasses)
Returns:
the current `State` from the specified `object`
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if `object` is null.
getTokenValue
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getTokenValue()
Get Tokens values from the current context.
Returns:
the instance of subclasses of the `Object` representing the token values of the current context
getLastSignal
public [SignalInstance](../fuml/behaviors/communications/SignalInstance.html) getLastSignal([Object_](../fuml/classes/Object_.html) o)
Get the last signal instance from the event pool.
Parameters:
`o` - the specified object
Returns:
the last signal instance from the list
createObject
@CheckForNullpublic [Object_](../fuml/classes/Object_.html) createObject([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) classifier)
Create an `Object_` with the given type (which must be a `Class`) in the `Locus` of the active `SimulationSession`.
Parameters:
`classifier` - the instance of `Class`(or its subclasses)
Returns:
the created `Object_`, or null if `classifier` is not instance of `Class`
createObject
public [Object_](../fuml/classes/Object_.html) createObject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Create an `Object_` with the given `name` (which must be name of `Class`)
 as its type. The `name` is used to search from `com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model` of the current `Project`.
Parameters:
`name` - the specified `Class` name
Returns:
the created `Object_`
See Also:
[`createObject(Class)`](#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
`SimulationModelHelper.findClassByName(Element, String)`
callOperation
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`name` - the specified name of `Operation`
Returns:
the return value of the execution.
See Also:
[`callOperation(String, List)`](#callOperation(java.lang.String,java.util.List))
callOperation
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`name` - the specified name of `Operation`
`arguments` - argument values
Returns:
the return value of the execution.
See Also:
[`callOperation(Object_, String, List)`](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List))
callOperation
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`object` - The target object to which the request is sent
`name` - the specified name of `Operation`
Returns:
the return value of the execution.
See Also:
[`callOperation(Object_, String, List)`](#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List))
callOperation
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`object` - The target object to which the request is sent
`name` - the specified name of `Operation`
`arguments` - argument values
Returns:
the return value of the execution.
See Also:
`SimulationModelHelper.findOperationByName(Element, String)`
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
callOperation
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchronous)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`object` - The target object to which the request is sent
`name` - the specified name of `Operation`
`arguments` - argument values
`isSynchronous` - true if call synchronously, false --> asynchronously
Returns:
the return value of the execution.
See Also:
`SimulationModelHelper.findOperationByName(Element, String)`
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
callOperation
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`object` - The target object to which the request is sent
`name` - the specified name of `Operation`
`portName` - port through which the operation should be called
Returns:
the return value of the execution.
See Also:
`SimulationModelHelper.findOperationByName(Element, String)`
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
callOperation
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callOperation([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchronous)
Execute the method of the `Operation` element that matches the specified name.
Parameters:
`object` - The target object to which the request is sent
`name` - the specified name of `Operation`
`portName` - port through which the operation should be called
`arguments` - argument values
`isSynchronous` - true if call synchronously, false --> asynchronously
Returns:
the return value of the execution.
See Also:
`SimulationModelHelper.findOperationByName(Element, String)`
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
callBehavior
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callBehavior([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Execute the `Behavior` element that matches the specified name.
Parameters:
`name` - the specified name of `Behavior`
Returns:
the return value of the execution.
See Also:
[`callBehavior(String, List)`](#callBehavior(java.lang.String,java.util.List))
callBehavior
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callBehavior([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments)
Execute the CallBehaviorAction element that matches the specified name.
Parameters:
`name` - the specified name of `Behavior`
`arguments` - argument values
Returns:
the return value of the execution.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if cannot find `Behavior` or size of `arguments` are not equal to in/inout parameters size.
See Also:
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
callBehavior
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) callBehavior([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<?> arguments,
 boolean isSynchonous)
Execute the CallBehaviorAction element that matches the specified name.
Parameters:
`name` - the specified name of `Behavior`
`arguments` - argument values
`isSynchonous` - true if call synchronously, false --> asynchronously
Returns:
the return value of the execution.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if cannot find `Behavior` or size of `arguments` are not equal to in/inout parameters size.
See Also:
[`fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)`](../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))
sendSignal
public void sendSignal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [Object_](../fuml/classes/Object_.html) target)
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_`.
 If `signalName` contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with `signalName`.
Parameters:
`signalName` - the specified `Signal` name
`target` - the specified target `Object_`
sendSignal
public void sendSignal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName)
Create SignalInstance instance of the specified `Signal` name, and send it to the specified `targetName`.
 If `signalName` contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with `signalName`.

 If `targetName` is defined, there are two possible cases.
 It will find target objects from all waiting objects that have their parts name matched with `targetName`
It will find target objects via connected port, which port name is matched with the specified `targetName`
Parameters:
`signalName` - the specified `Signal` name
`targetName` - the specified target object name
sendSignal
public void sendSignal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) signalName,
 [Object_](../fuml/classes/Object_.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_` via the specified port name.
 If `signalName` contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with `signalName`.
Parameters:
`signalName` - the specified `Signal` name
`target` - the specified target `Object_`
`portName` - the specified port name
sendSignal
public void sendSignal([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [Object_](../fuml/classes/Object_.html) target)
Send the specified `SignalInstance` to the specified target `Object_`.
Parameters:
`signal` - the specified `SignalInstance`
`target` - the specified target `Object_`
sendSignal
public void sendSignal([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName)
Send the specified `SignalInstance` to the specified `targetName`.
 If `targetName` is defined, there are two possible cases.
 It will find target objects from all waiting objects that have their parts name matched with `targetName`
It will find target objects via connected port, which port name is matched with the specified `targetName`
Parameters:
`signal` - the specified `SignalInstance`
`targetName` - the specified target object name
sendSignal
public void sendSignal([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal,
 [Object_](../fuml/classes/Object_.html) target,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) portName)
Send the specified `SignalInstance` to the specified target `Object_` via the specified port name.
Parameters:
`signal` - the specified `SignalInstance`
`target` - the specified target `Object_`
`portName` - the specified port name
evaluate
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) evaluate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)
Evaluate the string expression based on the specified scripting language.
Parameters:
`language` - the specified scripting language
`expression` - the specified string expression
Returns:
the evaluation result
evaluate
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) evaluate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) expression)
Evaluate the string expression.
Parameters:
`expression` - the specified string expression
Returns:
the evaluation result
createList
public [ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> createList()
A convenience method for creating the list.
 The new empty `ArrayList` is created and returned.
Returns:
the new empty `ArrayList`
createList
public [ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> createList([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)
A convenience method for creating the list with one added item in the list.
 The new empty `ArrayList` is created and being added the specified item.
Parameters:
`object` - the specified item being added to the created list
Returns:
the new empty `ArrayList` with the added item
inState
public boolean inState([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)
Check whether the current runtime object is in the specified state name or not.
Parameters:
`stateName` - the specified state name
Returns:
true if one of the active states matches with the specified state name
inState
public boolean inState([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)
Check whether the specified object is in the specified state name or not.
Parameters:
`object` - the specified object
`stateName` - the specified state name
Returns:
true if one of the active states matches with the specified state name
wasInState
public boolean wasInState([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)
Check that the state matching with the name was already visited or not.
Parameters:
`stateName` - the state name
Returns:
true, if yes
wasInState
public boolean wasInState([Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stateName)
Check that the state matching with the name was already visited or not.
Parameters:
`object` - the object
`stateName` - the state name
Returns:
true, if yes
createSignal
public [SignalInstance](../fuml/behaviors/communications/SignalInstance.html) createSignal([Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)
Create the instance of `SignalInstance`.
Parameters:
`signal` - the specified `Signal`
Returns:
the created `SignalInstance`
createSignal
@CheckForNullpublic [SignalInstance](../fuml/behaviors/communications/SignalInstance.html) createSignal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) keyword)
Create the instance of `SignalInstance`.
Parameters:
`keyword` - the keyword for find `Signal`
Returns:
the created `SignalInstance`
getTimeUnit
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTimeUnit()
Gets time unit of the running execution.
Returns:
Time unit.
getCurrentTime
public double getCurrentTime()
Gets current time.
Returns:
Current time
getCurrentTime
public double getCurrentTime([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) timeUnit)
Gets current time in forms of the specified `timeUnit`.
Parameters:
`timeUnit` - the unit of time, that the current time should be converted to. Valid parameters: "nanosecond"/"ns", "microsecond"/"µs", "millisecond"/"ms", "second"/"s",
 "minute"/"min", "hour"/"h", "day"/"d", "week"/"w", "month"/"mo", "year"/"y"
Returns:
Current time in the unit of specified `timeUnit`.
getGlobalVariable
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getGlobalVariable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)
Gets global variable from the execution.
Parameters:
`variableName` - Variable name
Returns:
global variable value. if the global variable does not exist, return null.
setGlobalVariable
public void setGlobalVariable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Sets global variable for the execution.
Parameters:
`variableName` - Variable name
`value` - Variable value
isGlobalVariable
public [Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html) isGlobalVariable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)
Checks whether or not the given `variableName` is global variable.
Parameters:
`variableName` - Variable name
Returns:
true, if the given `variableName` is global variable. Otherwise, false.
removeGlobalVariable
public void removeGlobalVariable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) variableName)
Removes global variable from the execution.
Parameters:
`variableName` - Variable name
getCaller
public [NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html) getCaller()
Get the calling element of the script evaluation.
Returns:
the calling element of the script evaluation
getTagValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getTagValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Get tag value from classifier of context.
Parameters:
`tagName` - the tag name possible to be the dot notation.
Returns:
the value of tagName as the primitive object.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - - deprecated, never thrown
getTagValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getTagValue(@CheckForNull
 [Object_](../fuml/classes/Object_.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Get tag value from classifier of Object, and structural feature that Object represented
Parameters:
`object` - the runtime object
`tagName` - the tag name possible to be the dot notation.
Returns:
the value of tagName as the primitive object.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - - deprecated, never thrown

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.utils</a></div>
<h1 class="title" title="Class ALH">Class ALH</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.utils.ALH</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ALH</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">An Action Language Helper for using in scripts to access values of the runtime object.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>SIM 1.0</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ALH</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">ALH</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List)">ALH</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; trace)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">ALH</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; trace,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> context)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object)">addValue</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 and set the <code>value</code> at the last position of the value list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object,java.lang.Integer)">addValueAt</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> insertAt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 and set the <code>value</code> at the <code>insertAt</code> position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callBehavior(java.lang.String)">callBehavior</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the <code>Behavior</code> element that matches the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callBehavior(java.lang.String,java.util.List)">callBehavior</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the CallBehaviorAction element that matches the specified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callBehavior(java.lang.String,java.util.List,boolean)">callBehavior</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchonous)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the CallBehaviorAction element that matches the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">callOperation</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String)">callOperation</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String,java.util.List,boolean)">callOperation</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchronous)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List)">callOperation</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List,boolean)">callOperation</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchronous)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(java.lang.String)">callOperation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(java.lang.String,java.util.List)">callOperation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createList()">createList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A convenience method for creating the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createList(java.lang.Object)">createList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A convenience method for creating the list with one added item in the list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">createObject</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> classifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create an <code>Object_</code> with the given type (which must be a <code>Class</code>) in the <code>Locus</code> of the active <code>SimulationSession</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObject(java.lang.String)">createObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create an <code>Object_</code> with the given <code>name</code> (which must be name of <code>Class</code>)
 as its type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">createSignal</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create the instance of <code>SignalInstance</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSignal(java.lang.String)">createSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> keyword)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create the instance of <code>SignalInstance</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(java.lang.String)">evaluate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the string expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(java.lang.String,java.lang.String)">evaluate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the string expression based on the specified scripting language.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCaller()">getCaller</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the calling element of the script evaluation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the context of ALH.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentTime()">getCurrentTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets current time.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentTime(java.lang.String)">getCurrentTime</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> timeUnit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets current time in forms of the specified <code>timeUnit</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGlobalVariable(java.lang.String)">getGlobalVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets global variable from the execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSignal(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">getLastSignal</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the last signal instance from the event pool.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getState(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">getState</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the current <code>State</code> from the specified <code>object</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTagValue(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">getTagValue</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get tag value from classifier of Object, and structural feature that Object represented</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTagValue(java.lang.String)">getTagValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get tag value from classifier of context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeUnit()">getTimeUnit</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets time unit of the running execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTokenValue()">getTokenValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Tokens values from the current context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String)">getValue</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value of <code>FeatureValue</code> from the <code>object</code> that match
 the specified <code>StructureFeature</code> name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#inState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">inState</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check whether the specified object is in the specified state name or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#inState(java.lang.String)">inState</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check whether the current runtime object is in the specified state name or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isGlobalVariable(java.lang.String)">isGlobalVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether or not the given <code>variableName</code> is global variable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeGlobalVariable(java.lang.String)">removeGlobalVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes global variable from the execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Value)">removeValue</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a href="../fuml/classes/Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 remove the defined <code>value</code> or the value at <code>removeAt</code> position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Integer)">removeValueAt</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> removeAt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 remove the defined <code>value</code> or the value at <code>removeAt</code> position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">sendSignal</a><wbr/>(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">sendSignal</a><wbr/>(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code> via the specified port name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,java.lang.String)">sendSignal</a><wbr/>(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified <code>targetName</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the target <code>Object_</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the target <code>Object_</code> via the specified port name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(java.lang.String,java.lang.String)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the specified <code>targetName</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGlobalVariable(java.lang.String,java.lang.Object)">setGlobalVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets global variable for the execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object)">setValue</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>, and set the <code>value</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.String,java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the matched <code>FeatureValue</code> from the <code>context</code>, and set the <code>value</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#wasInState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">wasInState</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check that the state matching with the name was already visited or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#wasInState(java.lang.String)">wasInState</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check that the state matching with the name was already visited or not.</div>
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
<h3>ALH</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ALH</span>()</div>
<div class="block">Constructor.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>ALH</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ALH</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List)">
<h3>ALH</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ALH</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; trace)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session</dd>
<dd><code>trace</code> - trace</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>ALH</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ALH</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; trace,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> context)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the running session</dd>
<dd><code>trace</code> - trace</dd>
<dd><code>context</code> - the context</dd>
</dl>
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
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Get the context of ALH.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>context of ALH.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</span></div>
<div class="block">Get the value of <code>FeatureValue</code> from the <code>object</code> that match
 the specified <code>StructureFeature</code> name. It supports nested structural features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified instance of <code>StructuredValue</code>(or its subclasses)</dd>
<dd><code>featureName</code> - the specified name, it will check with StructuralFeature name, nested structural features such as "part1.part2" are allowed.</dd>
<dt>Returns:</dt>
<dd>the value of <code>FeatureValue</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if <code>object</code> or <code>featureName</code> is null.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../fuml/fUMLHelper.html#getFeatureValueByName(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String)"><code>fUMLHelper.getFeatureValueByName(StructuredValue, String)</code></a></li>
<li><a href="../fuml/fUMLHelper.html#getObjectFromFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue)"><code>fUMLHelper.getObjectFromFeatureValue(FeatureValue)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>, and set the <code>value</code>.
 If not found, create the new <code>FeatureValue</code> and add to the specified <code>object</code>.
 It supports nested structural features.

 <p>If want to find <code>FeatureValue</code> from <code>Association</code>(<code>Link</code>),
 use <a href="../fuml/fUMLHelper.html#addFeatureValues(com.nomagic.magicdraw.simulation.fuml.loci.Locus,com.nomagic.magicdraw.simulation.fuml.classes.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.magicdraw.simulation.fuml.classes.ValueList,int,boolean)"><code>fUMLHelper.addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)</code></a></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime Object_ or SignalInstance</dd>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>value</code> - the value to be set. Can be Java value or fUML Value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if <code>object</code> or <code>featureName</code> is null.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../fuml/fUMLHelper.html#setFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)"><code>fUMLHelper.setFeatureValue(StructuredValue, StructuralFeature, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.String,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the <code>context</code>, and set the <code>value</code>.
 If not found, create the new <code>FeatureValue</code> and add to the <code>context</code>.
 It supports nested structural features.

 <p>If want to find <code>FeatureValue</code> from <code>Association</code>(<code>Link</code>),
 use <a href="../fuml/fUMLHelper.html#addFeatureValues(com.nomagic.magicdraw.simulation.fuml.loci.Locus,com.nomagic.magicdraw.simulation.fuml.classes.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,com.nomagic.magicdraw.simulation.fuml.classes.ValueList,int,boolean)"><code>fUMLHelper.addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)</code></a></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>value</code> - the value to be set. Can be Java value or fUML Value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if <code>object</code> or <code>featureName</code> is null.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../fuml/fUMLHelper.html#setFeatureValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)"><code>fUMLHelper.setFeatureValue(StructuredValue, StructuralFeature, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object)">
<h3>addValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addValue</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 and set the <code>value</code> at the last position of the value list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime Object_ or SignalInstance</dd>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>value</code> - the value to be set. Can be Java value or fUML Value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Object,java.lang.Integer)">
<h3>addValueAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addValueAt</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> insertAt)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 and set the <code>value</code> at the <code>insertAt</code> position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime Object_ or SignalInstance</dd>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>value</code> - the value to be set. Can be Java value or fUML Value.</dd>
<dd><code>insertAt</code> - the inserted position. if it is not more than 0, the value will be added at the last position.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeValue(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Value)">
<h3>removeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeValue</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a href="../fuml/classes/Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a> value)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 remove the defined <code>value</code> or the value at <code>removeAt</code> position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime Object_ or SignalInstance</dd>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>value</code> - the fUML value to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeValueAt(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.String,java.lang.Integer)">
<h3>removeValueAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeValueAt</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> removeAt)</span></div>
<div class="block">Find the matched <code>FeatureValue</code> from the specified <code>object</code>,
 remove the defined <code>value</code> or the value at <code>removeAt</code> position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the fUML runtime Object_ or SignalInstance</dd>
<dd><code>featureName</code> - the name of structural feature, nested structural features such as "part1.part2" are allowed.</dd>
<dd><code>removeAt</code> - if the removeAt is defined. it will remove the value at <code>removeAt</code> position, ignoring the <code>value</code> value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getState(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>getState</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">getState</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</span></div>
<div class="block">Get the current <code>State</code> from the specified <code>object</code>.
 If <code>object</code> has more than one active states, return the first one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the instance of <code>Object_</code>(or its subclasses)</dd>
<dt>Returns:</dt>
<dd>the current <code>State</code> from the specified <code>object</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if <code>object</code> is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTokenValue()">
<h3>getTokenValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTokenValue</span>()</div>
<div class="block">Get Tokens values from the current context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the instance of subclasses of the <code>Object</code> representing the token values of the current context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastSignal(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>getLastSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></span> <span class="element-name">getLastSignal</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> o)</span></div>
<div class="block">Get the last signal instance from the event pool.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - the specified object</dd>
<dt>Returns:</dt>
<dd>the last signal instance from the list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>createObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></span> <span class="element-name">createObject</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> classifier)</span></div>
<div class="block">Create an <code>Object_</code> with the given type (which must be a <code>Class</code>) in the <code>Locus</code> of the active <code>SimulationSession</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the instance of <code>Class</code>(or its subclasses)</dd>
<dt>Returns:</dt>
<dd>the created <code>Object_</code>, or null if <code>classifier</code> is not instance of <code>Class</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObject(java.lang.String)">
<h3>createObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a></span> <span class="element-name">createObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Create an <code>Object_</code> with the given <code>name</code> (which must be name of <code>Class</code>)
 as its type. The <code>name</code> is used to search from <code>com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model</code> of the current <code>Project</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified <code>Class</code> name</dd>
<dt>Returns:</dt>
<dd>the created <code>Object_</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>createObject(Class)</code></a></li>
<li><code>SimulationModelHelper.findClassByName(Element, String)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(java.lang.String)">
<h3>callOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#callOperation(java.lang.String,java.util.List)"><code>callOperation(String, List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(java.lang.String,java.util.List)">
<h3>callOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dd><code>arguments</code> - argument values</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List)"><code>callOperation(Object_, String, List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The target object to which the request is sent</dd>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List)"><code>callOperation(Object_, String, List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The target object to which the request is sent</dd>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dd><code>arguments</code> - argument values</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>SimulationModelHelper.findOperationByName(Element, String)</code></li>
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.util.List,boolean)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchronous)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The target object to which the request is sent</dd>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dd><code>arguments</code> - argument values</dd>
<dd><code>isSynchronous</code> - true if call synchronously, false --&gt; asynchronously</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>SimulationModelHelper.findOperationByName(Element, String)</code></li>
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The target object to which the request is sent</dd>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dd><code>portName</code> - port through which the operation should be called</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>SimulationModelHelper.findOperationByName(Element, String)</code></li>
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String,java.lang.String,java.util.List,boolean)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchronous)</span></div>
<div class="block">Execute the method of the <code>Operation</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The target object to which the request is sent</dd>
<dd><code>name</code> - the specified name of <code>Operation</code></dd>
<dd><code>portName</code> - port through which the operation should be called</dd>
<dd><code>arguments</code> - argument values</dd>
<dd><code>isSynchronous</code> - true if call synchronously, false --&gt; asynchronously</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>SimulationModelHelper.findOperationByName(Element, String)</code></li>
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callBehavior(java.lang.String)">
<h3>callBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callBehavior</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Execute the <code>Behavior</code> element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified name of <code>Behavior</code></dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#callBehavior(java.lang.String,java.util.List)"><code>callBehavior(String, List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callBehavior(java.lang.String,java.util.List)">
<h3>callBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callBehavior</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments)</span></div>
<div class="block">Execute the CallBehaviorAction element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified name of <code>Behavior</code></dd>
<dd><code>arguments</code> - argument values</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if cannot find <code>Behavior</code> or size of <code>arguments</code> are not equal to in/inout parameters size.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callBehavior(java.lang.String,java.util.List,boolean)">
<h3>callBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callBehavior</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 boolean isSynchonous)</span></div>
<div class="block">Execute the CallBehaviorAction element that matches the specified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the specified name of <code>Behavior</code></dd>
<dd><code>arguments</code> - argument values</dd>
<dd><code>isSynchonous</code> - true if call synchronously, false --&gt; asynchronously</dd>
<dt>Returns:</dt>
<dd>the return value of the execution.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if cannot find <code>Behavior</code> or size of <code>arguments</code> are not equal to in/inout parameters size.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../fuml/fUMLHelper.html#callBehavior(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)"><code>fUMLHelper.callBehavior(StructuredValue, Behavior, List, SimulationSession, Boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target)</span></div>
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the target <code>Object_</code>.<p></p>
 If <code>signalName</code> contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with <code>signalName</code>.<p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signalName</code> - the specified <code>Signal</code> name</dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</span></div>
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the specified <code>targetName</code>.<p></p>
 If <code>signalName</code> contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with <code>signalName</code>.<p></p>

 If <code>targetName</code> is defined, there are two possible cases.
 <ul>
<li>It will find target objects from all waiting objects that have their parts name matched with <code>targetName</code></li>
<li>It will find target objects via connected port, which port name is matched with the specified <code>targetName</code></li>
</ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signalName</code> - the specified <code>Signal</code> name</dd>
<dd><code>targetName</code> - the specified target object name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</span></div>
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the target <code>Object_</code> via the specified port name.<p></p>
 If <code>signalName</code> contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with <code>signalName</code>.<p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signalName</code> - the specified <code>Signal</code> name</dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
<dd><code>portName</code> - the specified port name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target)</span></div>
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>SignalInstance</code></dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</span></div>
<div class="block">Send the specified <code>SignalInstance</code> to the specified <code>targetName</code>.
 <p>
 If <code>targetName</code> is defined, there are two possible cases.
 <ul>
<li>It will find target objects from all waiting objects that have their parts name matched with <code>targetName</code></li>
<li>It will find target objects via connected port, which port name is matched with the specified <code>targetName</code></li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>SignalInstance</code></dd>
<dd><code>targetName</code> - the specified target object name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance,com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> portName)</span></div>
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code> via the specified port name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>SignalInstance</code></dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
<dd><code>portName</code> - the specified port name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(java.lang.String,java.lang.String)">
<h3>evaluate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</span></div>
<div class="block">Evaluate the string expression based on the specified scripting language.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - the specified scripting language</dd>
<dd><code>expression</code> - the specified string expression</dd>
<dt>Returns:</dt>
<dd>the evaluation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(java.lang.String)">
<h3>evaluate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> expression)</span></div>
<div class="block">Evaluate the string expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the specified string expression</dd>
<dt>Returns:</dt>
<dd>the evaluation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createList()">
<h3>createList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">createList</span>()</div>
<div class="block">A convenience method for creating the list.
 The new empty <code>ArrayList</code> is created and returned.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new empty <code>ArrayList</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createList(java.lang.Object)">
<h3>createList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">createList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">A convenience method for creating the list with one added item in the list.
 The new empty <code>ArrayList</code> is created and being added the specified item.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified item being added to the created list</dd>
<dt>Returns:</dt>
<dd>the new empty <code>ArrayList</code> with the added item</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="inState(java.lang.String)">
<h3>inState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">inState</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</span></div>
<div class="block">Check whether the current runtime object is in the specified state name or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateName</code> - the specified state name</dd>
<dt>Returns:</dt>
<dd>true if one of the active states matches with the specified state name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="inState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>inState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">inState</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</span></div>
<div class="block">Check whether the specified object is in the specified state name or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>stateName</code> - the specified state name</dd>
<dt>Returns:</dt>
<dd>true if one of the active states matches with the specified state name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wasInState(java.lang.String)">
<h3>wasInState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">wasInState</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</span></div>
<div class="block">Check that the state matching with the name was already visited or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateName</code> - the state name</dd>
<dt>Returns:</dt>
<dd>true, if yes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wasInState(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>wasInState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">wasInState</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateName)</span></div>
<div class="block">Check that the state matching with the name was already visited or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the object</dd>
<dd><code>stateName</code> - the state name</dd>
<dt>Returns:</dt>
<dd>true, if yes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">
<h3>createSignal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></span> <span class="element-name">createSignal</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</span></div>
<div class="block">Create the instance of <code>SignalInstance</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>Signal</code></dd>
<dt>Returns:</dt>
<dd>the created <code>SignalInstance</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSignal(java.lang.String)">
<h3>createSignal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a></span> <span class="element-name">createSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> keyword)</span></div>
<div class="block">Create the instance of <code>SignalInstance</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>keyword</code> - the keyword for find <code>Signal</code></dd>
<dt>Returns:</dt>
<dd>the created <code>SignalInstance</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeUnit()">
<h3>getTimeUnit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTimeUnit</span>()</div>
<div class="block">Gets time unit of the running execution.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Time unit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentTime()">
<h3>getCurrentTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCurrentTime</span>()</div>
<div class="block">Gets current time.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Current time</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentTime(java.lang.String)">
<h3>getCurrentTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCurrentTime</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> timeUnit)</span></div>
<div class="block">Gets current time in forms of the specified <code>timeUnit</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>timeUnit</code> - the unit of time, that the current time should be converted to. Valid parameters: "nanosecond"/"ns", "microsecond"/"µs", "millisecond"/"ms", "second"/"s",
                 "minute"/"min", "hour"/"h", "day"/"d", "week"/"w", "month"/"mo", "year"/"y"</dd>
<dt>Returns:</dt>
<dd>Current time in the unit of specified <code>timeUnit</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGlobalVariable(java.lang.String)">
<h3>getGlobalVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getGlobalVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</span></div>
<div class="block">Gets global variable from the execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variableName</code> - Variable name</dd>
<dt>Returns:</dt>
<dd>global variable value. if the global variable does not exist, return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGlobalVariable(java.lang.String,java.lang.Object)">
<h3>setGlobalVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGlobalVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets global variable for the execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variableName</code> - Variable name</dd>
<dd><code>value</code> - Variable value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isGlobalVariable(java.lang.String)">
<h3>isGlobalVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isGlobalVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</span></div>
<div class="block">Checks whether or not the given <code>variableName</code> is global variable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variableName</code> - Variable name</dd>
<dt>Returns:</dt>
<dd>true, if the given <code>variableName</code> is global variable. Otherwise, false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeGlobalVariable(java.lang.String)">
<h3>removeGlobalVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeGlobalVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variableName)</span></div>
<div class="block">Removes global variable from the execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variableName</code> - Variable name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCaller()">
<h3>getCaller</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span> <span class="element-name">getCaller</span>()</div>
<div class="block">Get the calling element of the script evaluation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the calling element of the script evaluation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTagValue(java.lang.String)">
<h3>getTagValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTagValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Get tag value from classifier of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - the tag name possible to be the dot notation.</dd>
<dt>Returns:</dt>
<dd>the value of tagName as the primitive object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - - deprecated, never thrown</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTagValue(com.nomagic.magicdraw.simulation.fuml.classes.Object_,java.lang.String)">
<h3>getTagValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTagValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Get tag value from classifier of Object, and structural feature that Object represented</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the runtime object</dd>
<dd><code>tagName</code> - the tag name possible to be the dot notation.</dd>
<dt>Returns:</dt>
<dd>the value of tagName as the primitive object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - - deprecated, never thrown</dd>
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
