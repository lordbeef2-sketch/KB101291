# JAVA OPENAPI: fUMLHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/simulation/fuml/fUMLHelper.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/fUMLHelper.html`
- source_sha256: `2c1edfaf9407d87bffd725100337b66b59245d1f14428d51521be82ff2ffaf6e`
- captured_utc: `2026-07-14T16:55:34.972229+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml](package-summary.html)

## Class fUMLHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.fuml.fUMLHelper

@OpenApiAllpublic classfUMLHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The class contains helper methods for create, access, and modify the fUML object.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[fUMLHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[addFeatureValues](#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean))(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 fUML.Semantics.Classes.Kernel.ValueList inputValues,
 int insertAt,
 boolean replaceAll)`
Add the specified `ValueList` to the `FeatureValue`(matched with the specified `StructuralFeature`).
`static boolean`
`[addObjectToValueList](#addObjectToValueList(fUML.Semantics.Classes.Kernel.ValueList,java.lang.Object,java.lang.Object))(fUML.Semantics.Classes.Kernel.ValueList vList,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner)`
Create the new `Value` from the `object`,
 and add to the last position of the specified `ValueList`.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[buildStringFor](#buildStringFor(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Builds String representation for the given object.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[buildStringFor](#buildStringFor(java.lang.Object,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params)`
Builds String representation for the given object.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[buildStringFor](#buildStringFor(java.util.Collection,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams,java.util.Map))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html),[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)> colors)`
Builds String representation for the given collection.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[callBehavior](#callBehavior(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous)`
Create the `Execution` based on the specified `Behavior`, and execute.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous)`
Call the specified `Operation`.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[callOperation](#callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean,fUML.Semantics.Classes.Kernel.StructuredValue))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous,
 fUML.Semantics.Classes.Kernel.StructuredValue caller)`
Call the specified `Operation`.
`static fUML.Semantics.Classes.Kernel.Object_`
`[createObject](#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,fUML.Semantics.Classes.Kernel.Object_))([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) classifier,
 fUML.Semantics.Classes.Kernel.Object_ context)`
Create the runtime object from the specified classifier.
`static fUML.Semantics.Classes.Kernel.Value`
`[createValue](#createValue(java.lang.Object,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner,
 fUML.Semantics.Loci.LociL1.Locus locus)`
Create the fUML value object with the specified object.
`static fUML.Semantics.Classes.Kernel.ValueList`
`[createValueList](#createValueList(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner)`
A convenience method for creating the instance of `ValueList` with assigned values, and return it.
`static fUML.Semantics.Classes.Kernel.ValueList`
`[createValueList](#createValueList(java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner,
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)`
A convenience method for creating the instance of `ValueList` with assigned values, and return it.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.Object_>`
`[getConnectedObjectsViaPort](#getConnectedObjectsViaPort(fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.simulation.execution.session.SimulationSession))(fUML.Semantics.Classes.Kernel.Value value,
 [Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 [SimulationSession](../execution/session/SimulationSession.html) session)`
Collect all connected objects via the specified `port` from the specified `value`.
`static [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)`
`[getFeatureByName](#getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)`
Returns the `StructuralFeature` of the specified `CompoundValue`
 with the specified structural feature name.
`static fUML.Semantics.Classes.Kernel.FeatureValue`
`[getFeatureValue](#getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature)`
Deprecated.
use `StructuredValue.getFeatureValue(StructuralFeature)`
`static fUML.Semantics.Classes.Kernel.FeatureValue`
`[getFeatureValue](#getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Loci.LociL1.Locus))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 fUML.Semantics.Loci.LociL1.Locus locus)`
Deprecated.
use `StructuredValue.getFeatureValue(StructuralFeature)`
`static fUML.Semantics.Classes.Kernel.FeatureValue`
`[getFeatureValueByName](#getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the `FeatureValue` from the specified `StructuredValue` with the specified name.
`static fUML.Semantics.Classes.Kernel.FeatureValue`
`[getFeatureValueByName](#getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,fUML.Semantics.Loci.LociL1.Locus))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 fUML.Semantics.Loci.LociL1.Locus locus)`
Deprecated.
use shorter version without Locus argument
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getFirstObjectFromValueList](#getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList))(fUML.Semantics.Classes.Kernel.ValueList valueList)`
Returns the first object in the given valueList if existed.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getFirstObjectFromValueList](#getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,boolean))(fUML.Semantics.Classes.Kernel.ValueList valueList,
 boolean returnReference)`
Returns the first object in the given valueList if existed.
`static void`
`[getNormativeValue](#getNormativeValue(java.lang.Object,java.util.Collection))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> normative)`
Gets the normative value.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNormativeValues](#getNormativeValues(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)`
Get fUML normative values.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromFeatureValue](#getObjectFromFeatureValue(fUML.Semantics.Classes.Kernel.FeatureValue))(fUML.Semantics.Classes.Kernel.FeatureValue featureValue)`
Return the value or value list from the feature value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromParameterValue](#getObjectFromParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue))(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue)`
Return the value or value list from the parameter value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromToken](#getObjectFromToken(fUML.Semantics.Activities.IntermediateActivities.Token))(fUML.Semantics.Activities.IntermediateActivities.Token token)`
The `Object` value from the specified `Token`.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromTokenList](#getObjectFromTokenList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Activities.IntermediateActivities.Token> tokenList)`
Return the value or value list from the `TokenList`.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromValue](#getObjectFromValue(fUML.Semantics.Classes.Kernel.Value))(fUML.Semantics.Classes.Kernel.Value value)`
Return the value of the specified fUML value object.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromValueList](#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int))(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity)`
Return the value or value list from the fUML value list.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromValueList](#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement))(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity,
 [TypedElement](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) convertToTypeOf)`
Return the value or value list from the fUML value list.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getObjectFromValueList](#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,int))(fUML.Semantics.Classes.Kernel.ValueList valueList,
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 int upperMultiplicity)`
Deprecated.
kept for backwards compatibility.
`static [Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html)`
`[getParameterByName](#getParameterByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String))(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the instance of `Parameter` from the specified `Execution` and parameter's name.
`static fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue`
`[getParameterValueByName](#getParameterValueByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String))(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the parameter value of the `Execution`.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)>`
`[getSignalsFromExecution](#getSignalsFromExecution(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution))(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution)`
Collect the list of signals from the execution.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)>`
`[getSignalsFromObject](#getSignalsFromObject(fUML.Semantics.Classes.Kernel.Object_))(fUML.Semantics.Classes.Kernel.Object_ object)`
Return the list of signal with the specified object.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue>`
`[getValue](#getValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) structuralFeature)`
Returns the list `FeatureValue` from the specified `StructuredValue` with the specified structural feature.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue>`
`[getValue](#getValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)`
Returns the list `FeatureValue` from the specified `StructuredValue` with the specified feature name.
`static void`
`[removeFeatureValue](#removeFeatureValue(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.Value,int,boolean))(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 fUML.Semantics.Classes.Kernel.Value value,
 int removeAt,
 boolean isRemoveDuplicates)`
Removes the specified `value` from the `FeatureValue` that is matched with the specified `feature`.
`static boolean`
`[saveValueToInstance](#saveValueToInstance(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Save the runtime values of the given object to the slots of the given InstanceSpecification.
`static void`
`[sendSignal](#sendSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,fUML.Semantics.Classes.Kernel.Object_))([Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 fUML.Semantics.Classes.Kernel.Object_ target)`
Create SignalInstance instance of the specified `Signal` , and send it to the target `Object_`.
`static void`
`[sendSignal](#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_))(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target)`
Send the specified `SignalInstance` to the specified target `Object_`.
`static void`
`[sendSignal](#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_,java.lang.String))(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetPortName)`
Send the specified `SignalInstance` to the specified `target` and `targetPortName`.
`static void`
`[sendSignal](#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,java.lang.String))(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetName)`
Send the specified `SignalInstance` to the specified `targetName`.
`static void`
`[sendSignal](#sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 fUML.Semantics.Classes.Kernel.Object_ target)`
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_`.
`static void`
`[sendSignal](#sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 fUML.Semantics.Classes.Kernel.Object_ target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetPortName)`
Create SignalInstance instance of the specified `Signal` name, and send it to the specified `target` and `targetPortName`.
`static void`
`[sendSignal](#sendSignal(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetName)`
Deprecated.
use any other overloaded version which provides target Object_ or/and SignalInstance
`static void`
`[setFeatureValue](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Find the `FeatureValue`, and set its value with the `value`.
`static void`
`[setFeatureValue](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 fUML.Semantics.Loci.LociL1.Locus locus)`
Find the `FeatureValue`, and set its value with the `value`.
`static void`
`[setFeatureValue](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Object))(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Find the `StructuralFeature` from the specified object with the specified structural feature name,
 and delegates to [`setFeatureValue(StructuredValue, StructuralFeature, Object)`](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)).
`static void`
`[setParameterValue](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object))(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 [Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Find the `ParameterValue`.
`static void`
`[setParameterValue](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String,java.lang.Object))(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Find the `Parameter` by name from the specified `Execution`,
 and delegate to [`setParameterValue(Execution, Parameter, Object)`](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)).
`static void`
`[setParameterValue](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue,java.lang.Object,boolean))(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean isReplaceAll)`
Set the value to the specified `ParameterValue`.
`static boolean`
`[setValue](#setValue(fUML.Semantics.Classes.Kernel.Value,java.lang.Object))(fUML.Semantics.Classes.Kernel.Value value,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Set the specified value to the fUML value object.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
fUMLHelper
public fUMLHelper()
 ============ METHOD DETAIL ========== 
Method Details
getFeatureValueByName
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.FeatureValue getFeatureValueByName(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the `FeatureValue` from the specified `StructuredValue` with the specified name.
 Find the `StructuralFeature` by [`getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue, java.lang.String)`](#getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String))
Parameters:
`object` - the specified `StructuredValue`
`name` - feature value name
Returns:
The matched `FeatureValue` from the specified `CompoundValue`
 or `null` if not found
getFeatureValueByName
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.FeatureValue getFeatureValueByName(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 fUML.Semantics.Loci.LociL1.Locus locus)
Deprecated.
use shorter version without Locus argument
getFeatureValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.FeatureValue getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 fUML.Semantics.Loci.LociL1.Locus locus)
Deprecated.
use `StructuredValue.getFeatureValue(StructuralFeature)`
getFeatureValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.FeatureValue getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature)
Deprecated.
use `StructuredValue.getFeatureValue(StructuralFeature)`
getParameterValueByName
@CheckForNullpublic static fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue getParameterValueByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the parameter value of the `Execution`.
Parameters:
`object` - the specified `Execution`
`name` - the parameter value name
Returns:
the parameter value of the object
getParameterByName
@CheckForNullpublic static [Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) getParameterByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the instance of `Parameter` from the specified `Execution` and parameter's name.
Parameters:
`object` - the specified `Execution`
`name` - the parameter name
Returns:
the instance of matched `Parameter`
createValue
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.Value createValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner,
 @CheckForNull
 fUML.Semantics.Loci.LociL1.Locus locus)
Create the fUML value object with the specified object.
Parameters:
`o` - the specified object
`owner` - the specified owner
`locus` - locus
Returns:
the fUML value object
createValueList
public static fUML.Semantics.Classes.Kernel.ValueList createValueList(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner)
A convenience method for creating the instance of `ValueList` with assigned values, and return it.
 If `value` is instance of `ValueList`, just return `value`
Parameters:
`value` - the specified value, It can be collections, arrays, or even the single value.
`owner` - of the created value
Returns:
`ValueList` with assigned values.
createValueList
public static fUML.Semantics.Classes.Kernel.ValueList createValueList([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner,
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)
A convenience method for creating the instance of `ValueList` with assigned values, and return it.
 If `value` is instance of `ValueList`, just return `value`
Parameters:
`value` - the specified value, It can be collections, arrays, or even the single value.
`owner` - of the created value
`type` - Type of value
Returns:
`ValueList` with assigned values.
getObjectFromValueList
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity)
Return the value or value list from the fUML value list.
Parameters:
`valueList` - the specified fUML value list
`upperMultiplicity` - upper multiplicity
Returns:
the value if the size of the value list is 1, otherwise returns the value list
getObjectFromValueList
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList valueList,
 @CheckForNull
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 int upperMultiplicity)
Deprecated.
kept for backwards compatibility. Type argument is not used.
 Use [`getObjectFromValueList(ValueList, int, TypedElement)`](#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)) instead, if primitive type conversion is needed.
 Use [`getObjectFromValueList(ValueList, int)`](#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int)) to retrieve actual values from fUML model.
getObjectFromValueList
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity,
 @CheckForNull
 [TypedElement](../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) convertToTypeOf)
Return the value or value list from the fUML value list.
Parameters:
`valueList` - the specified fUML value list
`convertToTypeOf` - in case of the PrimitiveValue, converts the value to the type of this TypedElement. Providing null will return actual value from the list.
`upperMultiplicity` - upper multiplicity
Returns:
the value if the size of the value list is 1, otherwise returns the value list
getObjectFromFeatureValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromFeatureValue(fUML.Semantics.Classes.Kernel.FeatureValue featureValue)
Return the value or value list from the feature value.
Parameters:
`featureValue` - the specified feature value
Returns:
the value if the size of the value list of the feature value is 1, otherwise returns the value list
getObjectFromParameterValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue)
Return the value or value list from the parameter value.
Parameters:
`parameterValue` - the specified parameter value
Returns:
the value if the size of the value list of the parameter value is 1, otherwise returns the value list
getObjectFromValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromValue(@CheckForNull
 fUML.Semantics.Classes.Kernel.Value value)
Return the value of the specified fUML value object.
Parameters:
`value` - the fUML object value
Returns:
the value of the specified fUML value object
getFirstObjectFromValueList
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList valueList)
Returns the first object in the given valueList if existed.
Parameters:
`valueList` - ValueList
Returns:
the first object in the given valueList if existed
getFirstObjectFromValueList
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList valueList,
 boolean returnReference)
Returns the first object in the given valueList if existed.
Parameters:
`valueList` - ValueList
`returnReference` - if this flag is true, if the value is Object_, it will return Reference of that Object_ instead
Returns:
the first object in the given valueList if existed
getSignalsFromObject
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)> getSignalsFromObject(fUML.Semantics.Classes.Kernel.Object_ object)
Return the list of signal with the specified object.
Parameters:
`object` - the specified object
Returns:
the list of signal
getSignalsFromExecution
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)> getSignalsFromExecution(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution)
Collect the list of signals from the execution. It will find a behavior from the execution and collect signals
 from that behavior.
Parameters:
`execution` - the specified execution
Returns:
the list of signals
getFeatureByName
@CheckForNullpublic static [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) getFeatureByName(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)
Returns the `StructuralFeature` of the specified `CompoundValue`
 with the specified structural feature name.
Parameters:
`object` - the specified `CompoundValue`(or subclasses) to be used
`featureName` - the structural feature name
Returns:
the `StructuralFeature` of the specified `CompoundValue`
setFeatureValue
public static void setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Find the `FeatureValue`, and set its value with the `value`.
 If `value` is instance of `ValueList`, set `value` to the found `FeatureValue`,
 otherwise create the new `ValueList` and its value and set to the found `FeatureValue`.
 If want to find `FeatureValue` from `Association`(`Link`),
 use [`addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)`](#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean))
Parameters:
`object` - the specified object
`feature` - the structural feature
`value` - the specified value
See Also:
[`addFeatureValues(Locus, Value, StructuralFeature, ValueList, int, boolean)`](#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean))
setFeatureValue
public static void setFeatureValue(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 fUML.Semantics.Loci.LociL1.Locus locus)
Find the `FeatureValue`, and set its value with the `value`.
 If `value` is instance of `ValueList`, set `value` to the found `FeatureValue`,
 otherwise create the new `ValueList` and its value and set to the found `FeatureValue`.
Parameters:
`object` - the specified object
`feature` - the structural feature
`value` - the specified value
`locus` - execution locus
setFeatureValue
public static void setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Find the `StructuralFeature` from the specified object with the specified structural feature name,
 and delegates to [`setFeatureValue(StructuredValue, StructuralFeature, Object)`](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)).
Parameters:
`object` - the specified object
`featureName` - the structural feature name
`value` - the specified value
See Also:
[`setFeatureValue(StructuredValue, StructuralFeature, Object)`](#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object))
setValue
public static boolean setValue(fUML.Semantics.Classes.Kernel.Value value,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Set the specified value to the fUML value object.
Parameters:
`value` - the fUML value object
`o` - the specified value
Returns:
true if value was actually set, false if value was not compatible
callBehavior
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) callBehavior(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous)
Create the `Execution` based on the specified `Behavior`, and execute.
 The arguments are passed to create the parameter value of the created `Execution`.
Parameters:
`object` - a context
`behavior` - an instance of subclasses of `Behavior`
`arguments` - argument lists
`session` - the specified session
`synchronous` - true if call synchronously.
Returns:
the return value of this execution
callOperation
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) callOperation(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous)
Call the specified `Operation`.
Parameters:
`object` - the specified object
`operation` - the specified `Operation`
`arguments` - argument lists
`session` - the running session
`synchronous` - is synchronous or not
Returns:
the return value of this execution
callOperation
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) callOperation(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [SimulationSession](../execution/session/SimulationSession.html) session,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) synchronous,
 fUML.Semantics.Classes.Kernel.StructuredValue caller)
Call the specified `Operation`.
Parameters:
`object` - the specified object
`operation` - the specified `Operation`
`arguments` - argument lists
`session` - the running session
`synchronous` - is synchronous or not
`caller` - the specified calling `Object_`
Returns:
the return value of this execution
createObject
@CheckForNullpublic static fUML.Semantics.Classes.Kernel.Object_ createObject([Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) classifier,
 fUML.Semantics.Classes.Kernel.Object_ context)
Create the runtime object from the specified classifier.
Parameters:
`classifier` - the specified classifier
`context` - the creating object
Returns:
the created runtime object
setParameterValue
public static void setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Find the `Parameter` by name from the specified `Execution`,
 and delegate to [`setParameterValue(Execution, Parameter, Object)`](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)).
Parameters:
`execution` - the specified `Execution`
`name` - name
`value` - value
See Also:
[`setParameterValue(Execution, Parameter, Object)`](#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object))
setParameterValue
public static void setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 [Parameter](../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html) parameter,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Find the `ParameterValue`. The new `ValueList` is created
 from `value` and set to the found `Parameter`.
Parameters:
`execution` - the specified execution
`parameter` - the specified parameter
`value` - the value to be set to `ParameterValue`
setParameterValue
public static void setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 boolean isReplaceAll)
Set the value to the specified `ParameterValue`. Now it supports only isReplaceAll == true.
Parameters:
`parameterValue` - the specified `ParameterValue`.
`object` - the specified value
`isReplaceAll` - if true, replace all existing value
getObjectFromTokenList
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromTokenList([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Activities.IntermediateActivities.Token> tokenList)
Return the value or value list from the `TokenList`.
Parameters:
`tokenList` - the specified fUML token list
Returns:
the value if the size of the value list is 1, otherwise returns the value list
getObjectFromToken
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getObjectFromToken(fUML.Semantics.Activities.IntermediateActivities.Token token)
The `Object` value from the specified `Token`.
Parameters:
`token` - the specified `Token`
Returns:
the `Object` value
addObjectToValueList
public static boolean addObjectToValueList(fUML.Semantics.Classes.Kernel.ValueList vList,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) owner)
Create the new `Value` from the `object`,
 and add to the last position of the specified `ValueList`.
Parameters:
`vList` - the specified `ValueList`
`object` - the object being used to create `Value`
`owner` - the specified owner
Returns:
true (as specified by [`Collection.add(E)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)))
addFeatureValues
public static void addFeatureValues(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 fUML.Semantics.Classes.Kernel.ValueList inputValues,
 int insertAt,
 boolean replaceAll)
Add the specified `ValueList` to the `FeatureValue`(matched with the specified `StructuralFeature`).
 This method supports insertAt, and replaceAll.
Parameters:
`locus` - the specified locus
`valueOwner` - Value
`feature` - StructuralFeature
`inputValues` - ValueList
`insertAt` - the added position
`replaceAll` - if true, remove all existing values.
getNormativeValues
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNormativeValues([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)
Get fUML normative values.
Parameters:
`values` - the specified `values`
Returns:
the collection of String representing the specified `values`
buildStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) buildStringFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Builds String representation for the given object.
Parameters:
`object` - Object
Returns:
String representation of the given object
buildStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) buildStringFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params)
Builds String representation for the given object.
Parameters:
`object` - Object
`params` - representation parameters
Returns:
String representation of the given object
buildStringFor
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) buildStringFor([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html),[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)> colors)
Builds String representation for the given collection.
Parameters:
`collection` - Collection<?>
`params` - representation parameters
Returns:
String representation of the given collection
getConnectedObjectsViaPort
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.Object_> getConnectedObjectsViaPort(fUML.Semantics.Classes.Kernel.Value value,
 [Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 [SimulationSession](../execution/session/SimulationSession.html) session)
Collect all connected objects via the specified `port` from the specified `value`.
Parameters:
`value` - the specified `value`
`port` - the specified `port`
`session` - the specified session
Returns:
all connected objects
getNormativeValue
public static void getNormativeValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> normative)
Gets the normative value.
Parameters:
`object` - the object
`normative` - the normative
removeFeatureValue
public static void removeFeatureValue(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature,
 @CheckForNull
 fUML.Semantics.Classes.Kernel.Value value,
 int removeAt,
 boolean isRemoveDuplicates)
Removes the specified `value` from the `FeatureValue` that is matched with the specified `feature`.
Parameters:
`locus` - Locus
`valueOwner` - Value
`feature` - StructuralFeature
`value` - Value
`removeAt` - int
`isRemoveDuplicates` - boolean
getValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue> getValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)
Returns the list `FeatureValue` from the specified `StructuredValue` with the specified feature name.
 FeatureValue from multiple `Link` can be collected.
Parameters:
`object` - the specified `StructuredValue`
`featureName` - feature name
Returns:
The list of matched `FeatureValue` from the specified `StructuredValue`
 or `null` if not found
getValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue> getValue(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [StructuralFeature](../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) structuralFeature)
Returns the list `FeatureValue` from the specified `StructuredValue` with the specified structural feature.
 FeatureValue from multiple `Link` can be collected.
Parameters:
`object` - the specified `StructuredValue`
`structuralFeature` - structuralFeature
Returns:
The list of matched `FeatureValue` from the specified `StructuredValue`
 or `null` if not found
saveValueToInstance
public static boolean saveValueToInstance(fUML.Semantics.Classes.Kernel.StructuredValue object,
 [InstanceSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Save the runtime values of the given object to the slots of the given InstanceSpecification.
Parameters:
`object` - is the given runtime object, whose values will be saved to the InstanceSpecification.
`instance` - is the given InstanceSpecification for storing the runtime values to its slots.
Returns:
true if the runtime values are saved to the given InstanceSpecification successfully.
 Otherwise, false is returned.
sendSignal
public static void sendSignal([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 fUML.Semantics.Classes.Kernel.Object_ target)
Create SignalInstance instance of the specified `Signal` name, and send it to the target `Object_`.
 If `signalName` contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with `signalName`.
Parameters:
`signalName` - the specified `Signal` name
`target` - the specified target `Object_`
sendSignal
public static void sendSignal([Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) signal,
 fUML.Semantics.Classes.Kernel.Object_ target)
Create SignalInstance instance of the specified `Signal` , and send it to the target `Object_`.
Parameters:
`signal` - the specified `Signal` element
`target` - the specified target `Object_`
sendSignal
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void sendSignal([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetName)
Deprecated.
use any other overloaded version which provides target Object_ or/and SignalInstance
To be removed
sendSignal
public static void sendSignal([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) signalName,
 fUML.Semantics.Classes.Kernel.Object_ target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetPortName)
Create SignalInstance instance of the specified `Signal` name, and send it to the specified `target` and `targetPortName`.
 
 If `signalName` contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with `signalName`.
Parameters:
`signalName` - the specified `Signal` name
`target` - the specified target
`targetPortName` - the specified target port name
sendSignal
public static void sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target)
Send the specified `SignalInstance` to the specified target `Object_`.
Parameters:
`signal` - the specified `SignalInstance`
`target` - the specified target `Object_`
sendSignal
public static void sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetName)
Send the specified `SignalInstance` to the specified `targetName`.
 If `targetName` is defined, there are two possible cases.
 It will find target objects from all waiting objects that have their parts name matched with `targetName`
It will find target objects via connected port, which port name is matched with the specified `targetName`
Parameters:
`signal` - the specified `SignalInstance`
`targetName` - the specified target object name
sendSignal
public static void sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) targetPortName)
Send the specified `SignalInstance` to the specified `target` and `targetPortName`.
Parameters:
`signal` - the specified `SignalInstance`
`target` - the specified target
`targetPortName` - the specified target port name

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml</a></div>
<h1 class="title" title="Class fUMLHelper">Class fUMLHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.fUMLHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">fUMLHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The class contains helper methods for create, access, and modify the fUML object.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">fUMLHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean)">addFeatureValues</a><wbr/>(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 fUML.Semantics.Classes.Kernel.ValueList inputValues,
 int insertAt,
 boolean replaceAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add the specified <code>ValueList</code> to the <code>FeatureValue</code>(matched with the specified <code>StructuralFeature</code>).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addObjectToValueList(fUML.Semantics.Classes.Kernel.ValueList,java.lang.Object,java.lang.Object)">addObjectToValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList vList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create the new <code>Value</code> from the <code>object</code>,
 and add to the last position of the specified <code>ValueList</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#buildStringFor(java.lang.Object)">buildStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Builds String representation for the given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#buildStringFor(java.lang.Object,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams)">buildStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Builds String representation for the given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#buildStringFor(java.util.Collection,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams,java.util.Map)">buildStringFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a>&gt; colors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Builds String representation for the given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#callBehavior(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)">callBehavior</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create the <code>Execution</code> based on the specified <code>Behavior</code>, and execute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)">callOperation</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Call the specified <code>Operation</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean,fUML.Semantics.Classes.Kernel.StructuredValue)">callOperation</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous,
 fUML.Semantics.Classes.Kernel.StructuredValue caller)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Call the specified <code>Operation</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.Classes.Kernel.Object_</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,fUML.Semantics.Classes.Kernel.Object_)">createObject</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> classifier,
 fUML.Semantics.Classes.Kernel.Object_ context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create the runtime object from the specified classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.Classes.Kernel.Value</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValue(java.lang.Object,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus)">createValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner,
 fUML.Semantics.Loci.LociL1.Locus locus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create the fUML value object with the specified object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueList(java.lang.Object,java.lang.Object)">createValueList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A convenience method for creating the instance of <code>ValueList</code> with assigned values, and return it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.Classes.Kernel.ValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueList(java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">createValueList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A convenience method for creating the instance  of <code>ValueList</code> with assigned values, and return it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.Object_&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedObjectsViaPort(fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">getConnectedObjectsViaPort</a><wbr/>(fUML.Semantics.Classes.Kernel.Value value,
 <a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all connected objects via the specified <code>port</code> from the specified <code>value</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">getFeatureByName</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the <code>StructuralFeature</code> of the specified <code>CompoundValue</code>
 with the specified structural feature name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static fUML.Semantics.Classes.Kernel.FeatureValue</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">getFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>StructuredValue.getFeatureValue(StructuralFeature)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static fUML.Semantics.Classes.Kernel.FeatureValue</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Loci.LociL1.Locus)">getFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 fUML.Semantics.Loci.LociL1.Locus locus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>StructuredValue.getFeatureValue(StructuralFeature)</code></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.Classes.Kernel.FeatureValue</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">getFeatureValueByName</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static fUML.Semantics.Classes.Kernel.FeatureValue</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,fUML.Semantics.Loci.LociL1.Locus)">getFeatureValueByName</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 fUML.Semantics.Loci.LociL1.Locus locus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use shorter version without Locus argument</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList)">getFirstObjectFromValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList valueList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first object in the given valueList if existed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,boolean)">getFirstObjectFromValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList valueList,
 boolean returnReference)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first object in the given valueList if existed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNormativeValue(java.lang.Object,java.util.Collection)">getNormativeValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; normative)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the normative value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNormativeValues(java.util.Collection)">getNormativeValues</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get fUML normative values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromFeatureValue(fUML.Semantics.Classes.Kernel.FeatureValue)">getObjectFromFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.FeatureValue featureValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value or value list from the feature value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue)">getObjectFromParameterValue</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value or value list from the parameter value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromToken(fUML.Semantics.Activities.IntermediateActivities.Token)">getObjectFromToken</a><wbr/>(fUML.Semantics.Activities.IntermediateActivities.Token token)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">The <code>Object</code> value from the specified <code>Token</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromTokenList(java.util.List)">getObjectFromTokenList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Activities.IntermediateActivities.Token&gt; tokenList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value or value list from the <code>TokenList</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromValue(fUML.Semantics.Classes.Kernel.Value)">getObjectFromValue</a><wbr/>(fUML.Semantics.Classes.Kernel.Value value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value of the specified fUML value object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int)">getObjectFromValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value or value list from the fUML value list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">getObjectFromValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> convertToTypeOf)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the value or value list from the fUML value list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,int)">getObjectFromValueList</a><wbr/>(fUML.Semantics.Classes.Kernel.ValueList valueList,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 int upperMultiplicity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">kept for backwards compatibility.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String)">getParameterByName</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the instance of <code>Parameter</code> from the specified <code>Execution</code> and parameter's name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameterValueByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String)">getParameterValueByName</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the parameter value of the <code>Execution</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalsFromExecution(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution)">getSignalsFromExecution</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect the list of signals from the execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalsFromObject(fUML.Semantics.Classes.Kernel.Object_)">getSignalsFromObject</a><wbr/>(fUML.Semantics.Classes.Kernel.Object_ object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the list of signal with the specified object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">getValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> structuralFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the list <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified structural feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">getValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the list <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified feature name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFeatureValue(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.Value,int,boolean)">removeFeatureValue</a><wbr/>(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 fUML.Semantics.Classes.Kernel.Value value,
 int removeAt,
 boolean isRemoveDuplicates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the specified <code>value</code> from the <code>FeatureValue</code> that is matched with the specified <code>feature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#saveValueToInstance(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">saveValueToInstance</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Save the runtime values of the given object to the slots of the given InstanceSpecification.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,fUML.Semantics.Classes.Kernel.Object_)">sendSignal</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 fUML.Semantics.Classes.Kernel.Object_ target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> , and send it to the target <code>Object_</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_)">sendSignal</a><wbr/>(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_,java.lang.String)">sendSignal</a><wbr/>(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetPortName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified <code>target</code> and <code>targetPortName</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,java.lang.String)">sendSignal</a><wbr/>(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Send the specified <code>SignalInstance</code> to the specified <code>targetName</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 fUML.Semantics.Classes.Kernel.Object_ target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the target <code>Object_</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_,java.lang.String)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 fUML.Semantics.Classes.Kernel.Object_ target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetPortName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the specified <code>target</code> and <code>targetPortName</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#sendSignal(java.lang.String,java.lang.String)">sendSignal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use any other overloaded version which provides target Object_ or/and SignalInstance</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)">setFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find the <code>FeatureValue</code>, and set its value with the <code>value</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus)">setFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 fUML.Semantics.Loci.LociL1.Locus locus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find the <code>FeatureValue</code>, and set its value with the <code>value</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Object)">setFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find the <code>StructuralFeature</code> from the specified object with the specified structural feature name,
 and delegates to <a href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)"><code>setFeatureValue(StructuredValue, StructuralFeature, Object)</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)">setParameterValue</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find the <code>ParameterValue</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String,java.lang.Object)">setParameterValue</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find the <code>Parameter</code> by name from the specified <code>Execution</code>,
 and delegate to <a href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)"><code>setParameterValue(Execution, Parameter, Object)</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue,java.lang.Object,boolean)">setParameterValue</a><wbr/>(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean isReplaceAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set the value to the specified <code>ParameterValue</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(fUML.Semantics.Classes.Kernel.Value,java.lang.Object)">setValue</a><wbr/>(fUML.Semantics.Classes.Kernel.Value value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set the specified value to the fUML value object.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>fUMLHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">fUMLHelper</span>()</div>
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
<section class="detail" id="getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">
<h3>getFeatureValueByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.FeatureValue</span> <span class="element-name">getFeatureValueByName</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified name.
 Find the <code>StructuralFeature</code> by <a href="#getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)"><code>getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue, java.lang.String)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>StructuredValue</code></dd>
<dd><code>name</code> - feature value name</dd>
<dt>Returns:</dt>
<dd>The matched <code>FeatureValue</code> from the specified <code>CompoundValue</code>
                or <code>null</code> if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureValueByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,fUML.Semantics.Loci.LociL1.Locus)">
<h3>getFeatureValueByName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.FeatureValue</span> <span class="element-name">getFeatureValueByName</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 fUML.Semantics.Loci.LociL1.Locus locus)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use shorter version without Locus argument</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Loci.LociL1.Locus)">
<h3>getFeatureValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.FeatureValue</span> <span class="element-name">getFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 fUML.Semantics.Loci.LociL1.Locus locus)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>StructuredValue.getFeatureValue(StructuralFeature)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">
<h3>getFeatureValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.FeatureValue</span> <span class="element-name">getFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>StructuredValue.getFeatureValue(StructuralFeature)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getParameterValueByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String)">
<h3>getParameterValueByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue</span> <span class="element-name">getParameterValueByName</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the parameter value of the <code>Execution</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>Execution</code></dd>
<dd><code>name</code> - the parameter value name</dd>
<dt>Returns:</dt>
<dd>the parameter value of the object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameterByName(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String)">
<h3>getParameterByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getParameterByName</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the instance of <code>Parameter</code> from the specified <code>Execution</code> and parameter's name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>Execution</code></dd>
<dd><code>name</code> - the parameter name</dd>
<dt>Returns:</dt>
<dd>the instance of matched <code>Parameter</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValue(java.lang.Object,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus)">
<h3>createValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.Value</span> <span class="element-name">createValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner,
 @CheckForNull
 fUML.Semantics.Loci.LociL1.Locus locus)</span></div>
<div class="block">Create the fUML value object with the specified object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - the specified object</dd>
<dd><code>owner</code> - the specified owner</dd>
<dd><code>locus</code> - locus</dd>
<dt>Returns:</dt>
<dd>the fUML value object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueList(java.lang.Object,java.lang.Object)">
<h3>createValueList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">createValueList</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner)</span></div>
<div class="block">A convenience method for creating the instance of <code>ValueList</code> with assigned values, and return it.
 If <code>value</code> is instance of <code>ValueList</code>, just return <code>value</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the specified value, It can be collections, arrays, or even the single value.</dd>
<dd><code>owner</code> - of the created value</dd>
<dt>Returns:</dt>
<dd><code>ValueList</code> with assigned values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueList(java.lang.Object,java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>createValueList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.ValueList</span> <span class="element-name">createValueList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
<div class="block">A convenience method for creating the instance  of <code>ValueList</code> with assigned values, and return it.
 If <code>value</code> is instance of <code>ValueList</code>, just return <code>value</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the specified value, It can be collections, arrays, or even the single value.</dd>
<dd><code>owner</code> - of the created value</dd>
<dd><code>type</code> - Type of value</dd>
<dt>Returns:</dt>
<dd><code>ValueList</code> with assigned values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int)">
<h3>getObjectFromValueList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity)</span></div>
<div class="block">Return the value or value list from the fUML value list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueList</code> - the specified fUML value list</dd>
<dd><code>upperMultiplicity</code> - upper multiplicity</dd>
<dt>Returns:</dt>
<dd>the value if the size of the value list is 1, otherwise returns the value list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,int)">
<h3>getObjectFromValueList</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList valueList,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 int upperMultiplicity)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">kept for backwards compatibility. Type argument is not used.
 Use <a href="#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)"><code>getObjectFromValueList(ValueList, int, TypedElement)</code></a> instead, if primitive type conversion is needed.
 Use <a href="#getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int)"><code>getObjectFromValueList(ValueList, int)</code></a> to retrieve actual values from fUML model.</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">
<h3>getObjectFromValueList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList valueList,
 int upperMultiplicity,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> convertToTypeOf)</span></div>
<div class="block">Return the value or value list from the fUML value list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueList</code> - the specified fUML value list</dd>
<dd><code>convertToTypeOf</code> - in case of the PrimitiveValue, converts the value to the type of this TypedElement. Providing null will return actual value from the list.</dd>
<dd><code>upperMultiplicity</code> - upper multiplicity</dd>
<dt>Returns:</dt>
<dd>the value if the size of the value list is 1, otherwise returns the value list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromFeatureValue(fUML.Semantics.Classes.Kernel.FeatureValue)">
<h3>getObjectFromFeatureValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.FeatureValue featureValue)</span></div>
<div class="block">Return the value or value list from the feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>featureValue</code> - the specified feature value</dd>
<dt>Returns:</dt>
<dd>the value if the size of the value list of the feature value is 1, otherwise returns the value list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue)">
<h3>getObjectFromParameterValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromParameterValue</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue)</span></div>
<div class="block">Return the value or value list from the parameter value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterValue</code> - the specified parameter value</dd>
<dt>Returns:</dt>
<dd>the value if the size of the value list of the parameter value is 1, otherwise returns the value list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromValue(fUML.Semantics.Classes.Kernel.Value)">
<h3>getObjectFromValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromValue</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.Value value)</span></div>
<div class="block">Return the value of the specified fUML value object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the fUML object value</dd>
<dt>Returns:</dt>
<dd>the value of the specified fUML value object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList)">
<h3>getFirstObjectFromValueList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getFirstObjectFromValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList valueList)</span></div>
<div class="block">Returns the first object in the given valueList if existed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueList</code> - ValueList</dd>
<dt>Returns:</dt>
<dd>the first object in the given valueList if existed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstObjectFromValueList(fUML.Semantics.Classes.Kernel.ValueList,boolean)">
<h3>getFirstObjectFromValueList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getFirstObjectFromValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList valueList,
 boolean returnReference)</span></div>
<div class="block">Returns the first object in the given valueList if existed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueList</code> - ValueList</dd>
<dd><code>returnReference</code> - if this flag is true, if the value is Object_, it will return Reference of that Object_ instead</dd>
<dt>Returns:</dt>
<dd>the first object in the given valueList if existed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalsFromObject(fUML.Semantics.Classes.Kernel.Object_)">
<h3>getSignalsFromObject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</span> <span class="element-name">getSignalsFromObject</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.Object_ object)</span></div>
<div class="block">Return the list of signal with the specified object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dt>Returns:</dt>
<dd>the list of signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalsFromExecution(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution)">
<h3>getSignalsFromExecution</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</span> <span class="element-name">getSignalsFromExecution</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution)</span></div>
<div class="block">Collect the list of signals from the execution. It will find a behavior from the execution and collect signals
 from that behavior.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the specified execution</dd>
<dt>Returns:</dt>
<dd>the list of signals</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureByName(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">
<h3>getFeatureByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></span> <span class="element-name">getFeatureByName</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</span></div>
<div class="block">Returns the <code>StructuralFeature</code> of the specified <code>CompoundValue</code>
 with the specified structural feature name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>CompoundValue</code>(or subclasses) to be used</dd>
<dd><code>featureName</code> - the structural feature name</dd>
<dt>Returns:</dt>
<dd>the <code>StructuralFeature</code> of the specified <code>CompoundValue</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)">
<h3>setFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the <code>FeatureValue</code>, and set its value with the <code>value</code>.
 If <code>value</code> is instance of <code>ValueList</code>, set <code>value</code> to the found <code>FeatureValue</code>,
 otherwise create the new <code>ValueList</code> and its value and set to the found <code>FeatureValue</code>.
 <p>
 If want to find <code>FeatureValue</code> from <code>Association</code>(<code>Link</code>),
 use <a href="#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean)"><code>addFeatureValues(Locus locus, Value valueOwner, StructuralFeature feature, ValueList inputValues, int insertAt, boolean replaceAll)</code></a></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>feature</code> - the structural feature</dd>
<dd><code>value</code> - the specified value</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean)"><code>addFeatureValues(Locus, Value, StructuralFeature, ValueList, int, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object,fUML.Semantics.Loci.LociL1.Locus)">
<h3>setFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFeatureValue</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 fUML.Semantics.Loci.LociL1.Locus locus)</span></div>
<div class="block">Find the <code>FeatureValue</code>, and set its value with the <code>value</code>.
 If <code>value</code> is instance of <code>ValueList</code>, set <code>value</code> to the found <code>FeatureValue</code>,
 otherwise create the new <code>ValueList</code> and its value and set to the found <code>FeatureValue</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>feature</code> - the structural feature</dd>
<dd><code>value</code> - the specified value</dd>
<dd><code>locus</code> - execution locus</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String,java.lang.Object)">
<h3>setFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the <code>StructuralFeature</code> from the specified object with the specified structural feature name,
 and delegates to <a href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)"><code>setFeatureValue(StructuredValue, StructuralFeature, Object)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>featureName</code> - the structural feature name</dd>
<dd><code>value</code> - the specified value</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setFeatureValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,java.lang.Object)"><code>setFeatureValue(StructuredValue, StructuralFeature, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(fUML.Semantics.Classes.Kernel.Value,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.Value value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Set the specified value to the fUML value object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the fUML value object</dd>
<dd><code>o</code> - the specified value</dd>
<dt>Returns:</dt>
<dd>true if value was actually set, false if value was not compatible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callBehavior(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)">
<h3>callBehavior</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callBehavior</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous)</span></div>
<div class="block">Create the <code>Execution</code> based on the specified <code>Behavior</code>, and execute.
 The arguments are passed to create the parameter value of the created <code>Execution</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - a context</dd>
<dd><code>behavior</code> - an instance of subclasses of <code>Behavior</code></dd>
<dd><code>arguments</code> - argument lists</dd>
<dd><code>session</code> - the specified session</dd>
<dd><code>synchronous</code> - true if call synchronously.</dd>
<dt>Returns:</dt>
<dd>the return value of this execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous)</span></div>
<div class="block">Call the specified <code>Operation</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>operation</code> - the specified <code>Operation</code></dd>
<dd><code>arguments</code> - argument lists</dd>
<dd><code>session</code> - the running session</dd>
<dd><code>synchronous</code> - is synchronous or not</dd>
<dt>Returns:</dt>
<dd>the return value of this execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callOperation(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.execution.session.SimulationSession,java.lang.Boolean,fUML.Semantics.Classes.Kernel.StructuredValue)">
<h3>callOperation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">callOperation</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> synchronous,
 fUML.Semantics.Classes.Kernel.StructuredValue caller)</span></div>
<div class="block">Call the specified <code>Operation</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified object</dd>
<dd><code>operation</code> - the specified <code>Operation</code></dd>
<dd><code>arguments</code> - argument lists</dd>
<dd><code>session</code> - the running session</dd>
<dd><code>synchronous</code> - is synchronous or not</dd>
<dd><code>caller</code> - the specified calling <code>Object_</code></dd>
<dt>Returns:</dt>
<dd>the return value of this execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class,fUML.Semantics.Classes.Kernel.Object_)">
<h3>createObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">fUML.Semantics.Classes.Kernel.Object_</span> <span class="element-name">createObject</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> classifier,
 fUML.Semantics.Classes.Kernel.Object_ context)</span></div>
<div class="block">Create the runtime object from the specified classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - the specified classifier</dd>
<dd><code>context</code> - the creating object</dd>
<dt>Returns:</dt>
<dd>the created runtime object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,java.lang.String,java.lang.Object)">
<h3>setParameterValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setParameterValue</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the <code>Parameter</code> by name from the specified <code>Execution</code>,
 and delegate to <a href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)"><code>setParameterValue(Execution, Parameter, Object)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the specified <code>Execution</code></dd>
<dd><code>name</code> - name</dd>
<dd><code>value</code> - value</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)"><code>setParameterValue(Execution, Parameter, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter,java.lang.Object)">
<h3>setParameterValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setParameterValue</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.Execution execution,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Find the <code>ParameterValue</code>. The new <code>ValueList</code> is created
 from <code>value</code> and set to the found <code>Parameter</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the specified execution</dd>
<dd><code>parameter</code> - the specified parameter</dd>
<dd><code>value</code> - the value to be set to <code>ParameterValue</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParameterValue(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue,java.lang.Object,boolean)">
<h3>setParameterValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setParameterValue</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.BasicBehaviors.ParameterValue parameterValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 boolean isReplaceAll)</span></div>
<div class="block">Set the value to the specified <code>ParameterValue</code>. Now it supports only isReplaceAll == true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterValue</code> - the specified <code>ParameterValue</code>.</dd>
<dd><code>object</code> - the specified value</dd>
<dd><code>isReplaceAll</code> - if true, replace all existing value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromTokenList(java.util.List)">
<h3>getObjectFromTokenList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromTokenList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Activities.IntermediateActivities.Token&gt; tokenList)</span></div>
<div class="block">Return the value or value list from the <code>TokenList</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tokenList</code> - the specified fUML token list</dd>
<dt>Returns:</dt>
<dd>the value if the size of the value list is 1, otherwise returns the value list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectFromToken(fUML.Semantics.Activities.IntermediateActivities.Token)">
<h3>getObjectFromToken</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getObjectFromToken</span><wbr/><span class="parameters">(fUML.Semantics.Activities.IntermediateActivities.Token token)</span></div>
<div class="block">The <code>Object</code> value from the specified <code>Token</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>token</code> - the specified <code>Token</code></dd>
<dt>Returns:</dt>
<dd>the <code>Object</code> value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addObjectToValueList(fUML.Semantics.Classes.Kernel.ValueList,java.lang.Object,java.lang.Object)">
<h3>addObjectToValueList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">addObjectToValueList</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.ValueList vList,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> owner)</span></div>
<div class="block">Create the new <code>Value</code> from the <code>object</code>,
 and add to the last position of the specified <code>ValueList</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vList</code> - the specified <code>ValueList</code></dd>
<dd><code>object</code> - the object being used to create <code>Value</code></dd>
<dd><code>owner</code> - the specified owner</dd>
<dt>Returns:</dt>
<dd><tt>true</tt> (as specified by <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util"><code>Collection.add(E)</code></a>)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFeatureValues(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.ValueList,int,boolean)">
<h3>addFeatureValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addFeatureValues</span><wbr/><span class="parameters">(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 fUML.Semantics.Classes.Kernel.ValueList inputValues,
 int insertAt,
 boolean replaceAll)</span></div>
<div class="block">Add the specified <code>ValueList</code> to the <code>FeatureValue</code>(matched with the specified <code>StructuralFeature</code>).
 This method supports insertAt, and replaceAll.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locus</code> - the specified locus</dd>
<dd><code>valueOwner</code> - Value</dd>
<dd><code>feature</code> - StructuralFeature</dd>
<dd><code>inputValues</code> - ValueList</dd>
<dd><code>insertAt</code> - the added position</dd>
<dd><code>replaceAll</code> - if true, remove all existing values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNormativeValues(java.util.Collection)">
<h3>getNormativeValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNormativeValues</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="block">Get fUML normative values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>values</code> - the specified <code>values</code></dd>
<dt>Returns:</dt>
<dd>the collection of String representing the specified <code>values</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="buildStringFor(java.lang.Object)">
<h3>buildStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">buildStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Builds String representation for the given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - Object</dd>
<dt>Returns:</dt>
<dd>String representation of the given object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="buildStringFor(java.lang.Object,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams)">
<h3>buildStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">buildStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params)</span></div>
<div class="block">Builds String representation for the given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - Object</dd>
<dd><code>params</code> - representation parameters</dd>
<dt>Returns:</dt>
<dd>String representation of the given object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="buildStringFor(java.util.Collection,com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams,java.util.Map)">
<h3>buildStringFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">buildStringFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection,
 com.nomagic.magicdraw.simulation.utils.ValueRepresentationParams params,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a>&gt; colors)</span></div>
<div class="block">Builds String representation for the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - Collection&lt;?&gt;</dd>
<dd><code>params</code> - representation parameters</dd>
<dt>Returns:</dt>
<dd>String representation of the given collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedObjectsViaPort(fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>getConnectedObjectsViaPort</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.Object_&gt;</span> <span class="element-name">getConnectedObjectsViaPort</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.Value value,
 <a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block">Collect all connected objects via the specified <code>port</code> from the specified <code>value</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the specified <code>value</code></dd>
<dd><code>port</code> - the specified <code>port</code></dd>
<dd><code>session</code> - the specified session</dd>
<dt>Returns:</dt>
<dd>all connected objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNormativeValue(java.lang.Object,java.util.Collection)">
<h3>getNormativeValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">getNormativeValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; normative)</span></div>
<div class="block">Gets the normative value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the object</dd>
<dd><code>normative</code> - the normative</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeFeatureValue(fUML.Semantics.Loci.LociL1.Locus,fUML.Semantics.Classes.Kernel.Value,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature,fUML.Semantics.Classes.Kernel.Value,int,boolean)">
<h3>removeFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Loci.LociL1.Locus locus,
 fUML.Semantics.Classes.Kernel.Value valueOwner,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature,
 @CheckForNull
 fUML.Semantics.Classes.Kernel.Value value,
 int removeAt,
 boolean isRemoveDuplicates)</span></div>
<div class="block">Removes the specified <code>value</code> from the <code>FeatureValue</code> that is matched with the specified <code>feature</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locus</code> - Locus</dd>
<dd><code>valueOwner</code> - Value</dd>
<dd><code>feature</code> - StructuralFeature</dd>
<dd><code>value</code> - Value</dd>
<dd><code>removeAt</code> - int</dd>
<dd><code>isRemoveDuplicates</code> - boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(fUML.Semantics.Classes.Kernel.StructuredValue,java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</span> <span class="element-name">getValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</span></div>
<div class="block">Returns the list <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified feature name.
 FeatureValue from multiple <code>Link</code> can be collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>StructuredValue</code></dd>
<dd><code>featureName</code> - feature name</dd>
<dt>Returns:</dt>
<dd>The list of matched <code>FeatureValue</code> from the specified <code>StructuredValue</code>
                or <code>null</code> if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</span> <span class="element-name">getValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> structuralFeature)</span></div>
<div class="block">Returns the list <code>FeatureValue</code> from the specified <code>StructuredValue</code> with the specified structural feature.
 FeatureValue from multiple <code>Link</code> can be collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the specified <code>StructuredValue</code></dd>
<dd><code>structuralFeature</code> - structuralFeature</dd>
<dt>Returns:</dt>
<dd>The list of matched <code>FeatureValue</code> from the specified <code>StructuredValue</code>
                or <code>null</code> if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveValueToInstance(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>saveValueToInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">saveValueToInstance</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.StructuredValue object,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Save the runtime values of the given object to the slots of the given InstanceSpecification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - is the given runtime object, whose values will be saved to the InstanceSpecification.</dd>
<dd><code>instance</code> - is the given InstanceSpecification for storing the runtime values to its slots.</dd>
<dt>Returns:</dt>
<dd>true if the runtime values are saved to the given InstanceSpecification successfully.
 Otherwise, false is returned.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 fUML.Semantics.Classes.Kernel.Object_ target)</span></div>
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
<section class="detail" id="sendSignal(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal,fUML.Semantics.Classes.Kernel.Object_)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal,
 fUML.Semantics.Classes.Kernel.Object_ target)</span></div>
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> , and send it to the target <code>Object_</code>.<p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>Signal</code> element</dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use any other overloaded version which provides target Object_ or/and SignalInstance</div>
</div>
<div class="block">To be removed</div>
</section>
</li>
<li>
<section class="detail" id="sendSignal(java.lang.String,fUML.Semantics.Classes.Kernel.Object_,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> signalName,
 fUML.Semantics.Classes.Kernel.Object_ target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetPortName)</span></div>
<div class="block">Create SignalInstance instance of the specified <code>Signal</code> name, and send it to the specified <code>target</code> and <code>targetPortName</code>.
 <p></p>
 If <code>signalName</code> contains "::", it will find the signal from the qualified name, the signal is found if its qualified name is ended with <code>signalName</code>.
 <p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signalName</code> - the specified <code>Signal</code> name</dd>
<dd><code>target</code> - the specified target</dd>
<dd><code>targetPortName</code> - the specified target port name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target)</span></div>
<div class="block">Send the specified <code>SignalInstance</code> to the specified target <code>Object_</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>SignalInstance</code></dd>
<dd><code>target</code> - the specified target <code>Object_</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName)</span></div>
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
<section class="detail" id="sendSignal(fUML.Semantics.CommonBehaviors.Communications.SignalInstance,fUML.Semantics.Classes.Kernel.Object_,java.lang.String)">
<h3>sendSignal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendSignal</span><wbr/><span class="parameters">(fUML.Semantics.CommonBehaviors.Communications.SignalInstance signal,
 fUML.Semantics.Classes.Kernel.Object_ target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetPortName)</span></div>
<div class="block">Send the specified <code>SignalInstance</code> to the specified <code>target</code> and <code>targetPortName</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the specified <code>SignalInstance</code></dd>
<dd><code>target</code> - the specified target</dd>
<dd><code>targetPortName</code> - the specified target port name</dd>
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
