# JAVA OPENAPI: BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/cbm/profiles/BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.html
- source_path: `com/nomagic/magicdraw/cbm/profiles/BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.html`
- source_sha256: `31c0d7304b3dd8fc27308b4d7de45a1a7a7106538f21e0efaf6d93d3bed56b9f`
- captured_utc: `2026-07-14T16:51:08.024031+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.cbm.profiles](package-summary.html)

## Class BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype

Enclosing class:
[BPMN2Profile](BPMN2Profile.html)

public static classBPMN2Profile.MultiInstanceLoopCharacteristicsStereotype
extends [ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BEHAVIOR](#BEHAVIOR)`
The attribute behavior acts as a shortcut for specifying when events shall be thrown from an Activity instance that is about to complete.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPLETIONCONDITION](#COMPLETIONCONDITION)`
This attribute defines a Boolean Expression that when evaluated to true, cancels the remaining Activity instances and produces a token.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPLEXBEHAVIORDEFINTION](#COMPLEXBEHAVIORDEFINTION)`
Controls when and which Events are thrown in case behavior is set to complex.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INPUTDATAITEM](#INPUTDATAITEM)`
A Data Input, representing for every Activity instance the single item of the collection stored in the loopDataInput.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ISSEQUENTIAL](#ISSEQUENTIAL)`
This attribute is a flag that controls whether the Activity
 instances will execute sequentially or in parallel.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOOPCARDINALITY](#LOOPCARDINALITY)`
A numeric Expression that controls the number of Activity instances that will be created.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOOPCOUNTER](#LOOPCOUNTER)`
The LoopCounter attribute is used at runtime to count the number of loops and is automatically updated by the process engine.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOOPDATAINPUTREF](#LOOPDATAINPUTREF)`
A reference to a DataInput which is part of the Activity s InputOutputSpecification.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOOPDATAOUTPUTREF](#LOOPDATAOUTPUTREF)`
This ItemAwareElement specifies the collection of data, which will be produced by the multi-instance.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NONEBEHAVIOREVENTREF](#NONEBEHAVIOREVENTREF)`
The EventDefinition which is thrown when the behavior is set to none and an internal Activity instance has completed
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFACTIVEINSTANCES](#NUMBEROFACTIVEINSTANCES)`
This attribute is provided for the outer instance of the Multi-Instance Activity only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFCOMPLETEDINSTANCES](#NUMBEROFCOMPLETEDINSTANCES)`
This attribute is provided for the outer instance of the Multi-Instance Activity only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFINSTANCES](#NUMBEROFINSTANCES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROFTERMINATEDINSTANCES](#NUMBEROFTERMINATEDINSTANCES)`
This attribute is provided for the outer instance of the Multi-Instance Activity only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ONEBEHAVIOREVENTREF](#ONEBEHAVIOREVENTREF)`
The EventDefinition which is thrown when behavior is set to one and the first internal Activity instance has completed.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OUTPUTDATAITEM](#OUTPUTDATAITEM)`
A Data Output, representing for every Activity instance the single item
 of the collection stored in the loopDataOutput.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[MultiInstanceLoopCharacteristicsStereotype](#%3Cinit%3E(com.nomagic.magicdraw.cbm.profiles.BPMN2Profile))([BPMN2Profile](BPMN2Profile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addComplexBehaviorDefintion](#addComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`protected void`
`[clear](#clear())()`

`void`
`[clearBehavior](#clearBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearCompletionCondition](#clearCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearComplexBehaviorDefintion](#clearComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearInputDataItem](#clearInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearIsSequential](#clearIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLoopCardinality](#clearLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLoopCounter](#clearLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLoopDataInputRef](#clearLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearLoopDataOutputRef](#clearLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNoneBehaviorEventRef](#clearNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfActiveInstances](#clearNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfCompletedInstances](#clearNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfInstances](#clearNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearNumberOfTerminatedInstances](#clearNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearOneBehaviorEventRef](#clearOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearOutputDataItem](#clearOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[BPMN2Profile.MultiInstanceBehaviorEnum](BPMN2Profile.MultiInstanceBehaviorEnum.html)`
`[getBehavior](#getBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getBehaviorProperty](#getBehaviorProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCompletionCondition](#getCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getCompletionConditionProperty](#getCompletionConditionProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getComplexBehaviorDefintion](#getComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getComplexBehaviorDefintionProperty](#getComplexBehaviorDefintionProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getInputDataItem](#getInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getInputDataItemProperty](#getInputDataItemProperty())()`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getIsSequentialProperty](#getIsSequentialProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLoopCardinality](#getLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLoopCardinalityProperty](#getLoopCardinalityProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getLoopCounter](#getLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLoopCounterProperty](#getLoopCounterProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getLoopDataInputRef](#getLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLoopDataInputRefProperty](#getLoopDataInputRefProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getLoopDataOutputRef](#getLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getLoopDataOutputRefProperty](#getLoopDataOutputRefProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getNoneBehaviorEventRef](#getNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNoneBehaviorEventRefProperty](#getNoneBehaviorEventRefProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfActiveInstances](#getNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfActiveInstancesProperty](#getNumberOfActiveInstancesProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfCompletedInstances](#getNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfCompletedInstancesProperty](#getNumberOfCompletedInstancesProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfInstances](#getNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfInstancesProperty](#getNumberOfInstancesProperty())()`

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[getNumberOfTerminatedInstances](#getNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getNumberOfTerminatedInstancesProperty](#getNumberOfTerminatedInstancesProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getOneBehaviorEventRef](#getOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getOneBehaviorEventRefProperty](#getOneBehaviorEventRefProperty())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getOutputDataItem](#getOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getOutputDataItemProperty](#getOutputDataItemProperty())()`

`[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isIsSequential](#isIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeComplexBehaviorDefintion](#removeComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setBehavior](#setBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceBehaviorEnum))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [BPMN2Profile.MultiInstanceBehaviorEnum](BPMN2Profile.MultiInstanceBehaviorEnum.html) value)`

`void`
`[setCompletionCondition](#setCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setComplexBehaviorDefintion](#setComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setInputDataItem](#setInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setIsSequential](#setIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setLoopCardinality](#setLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setLoopCounter](#setLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setLoopDataInputRef](#setLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setLoopDataOutputRef](#setLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setNoneBehaviorEventRef](#setNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setNumberOfActiveInstances](#setNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setNumberOfCompletedInstances](#setNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setNumberOfInstances](#setNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setNumberOfTerminatedInstances](#setNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)`

`void`
`[setOneBehaviorEventRef](#setOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setOutputDataItem](#setOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDerivedStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [unApply](../../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.STEREOTYPE_NAME)
BEHAVIOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BEHAVIOR
The attribute behavior acts as a shortcut for specifying when events shall be thrown from an Activity instance that is about to complete. It can assume values of none, one, all, and complex, resulting in the following behavior:
 - None: the EventDefinition which is associated through the noneEvent association will be thrown for each instance completing;
 - One: the EventDefinition referenced through the oneEvent association will be thrown upon the first instance completing;
 - All: no Event is ever thrown; a token is produced after completion of all instances
 - Complex: the complexBehaviorDefinitions are consulted to determine if and which Events to throw.
 For the behaviors of none and one, a default SignalEventDefinition will be thrown which automatically carries the current runtime attributes of the MI Activity. Any thrown Events can be caught by boundary Events on the Multi-Instance Activity.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.BEHAVIOR)
COMPLETIONCONDITION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPLETIONCONDITION
This attribute defines a Boolean Expression that when evaluated to true, cancels the remaining Activity instances and produces a token.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.COMPLETIONCONDITION)
COMPLEXBEHAVIORDEFINTION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPLEXBEHAVIORDEFINTION
Controls when and which Events are thrown in case behavior is set to complex.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.COMPLEXBEHAVIORDEFINTION)
INPUTDATAITEM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INPUTDATAITEM
A Data Input, representing for every Activity instance the single item of the collection stored in the loopDataInput. This Data Input can be the source of DataInputAssociation to a data input of the Activity s InputOutputSpecification. The type of this Data Input MUST the scalar of the type defined for the loopDataInput.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.INPUTDATAITEM)
ISSEQUENTIAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ISSEQUENTIAL
This attribute is a flag that controls whether the Activity
 instances will execute sequentially or in parallel.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.ISSEQUENTIAL)
LOOPCARDINALITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOOPCARDINALITY
A numeric Expression that controls the number of Activity instances that will be created. This Expression MUST evaluate to an integer.
 This may be underspecified, meaning that the modeler may simply document the condition. In such a case the loop cannot be formally executed.
 In order to initialize a valid multi-instance, either the
 loopCardinality Expression or the loopDataInput MUST be specified.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPCARDINALITY)
LOOPCOUNTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOOPCOUNTER
The LoopCounter attribute is used at runtime to count the number of loops and is automatically updated by the process engine.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPCOUNTER)
LOOPDATAINPUTREF
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOOPDATAINPUTREF
A reference to a DataInput which is part of the Activity s InputOutputSpecification. This DataInput is used to determine the number of Activity instances, one Activity instance per item in the collection of data stored in that DataInput element.
 In order to initialize a valid multi-instance, either the loopCardinality Expression or the loopDataInput MUST be specified.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPDATAINPUTREF)
LOOPDATAOUTPUTREF
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOOPDATAOUTPUTREF
This ItemAwareElement specifies the collection of data, which will be produced by the multi-instance.
 For Tasks it is a reference to a Data Output which is part of the Activity s InputOutputSpecification.
 For Sub-Processes it is a reference to a collection-valued Data Object in the context that is visible to the Sub-Processes.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPDATAOUTPUTREF)
NONEBEHAVIOREVENTREF
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NONEBEHAVIOREVENTREF
The EventDefinition which is thrown when the behavior is set to none and an internal Activity instance has completed
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NONEBEHAVIOREVENTREF)
NUMBEROFACTIVEINSTANCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFACTIVEINSTANCES
This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of currently active inner instances for the Multi-Instance Activity. In case of a sequential Multi-Instance Activity, this value can t be greater than 1. For parallel Multi-Instance Activities, this value can t be greater than the value contained in numberOfInstances.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFACTIVEINSTANCES)
NUMBEROFCOMPLETEDINSTANCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFCOMPLETEDINSTANCES
This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of already completed inner instances for the Multi-Instance Activity.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFCOMPLETEDINSTANCES)
NUMBEROFINSTANCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFINSTANCES
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFINSTANCES)
NUMBEROFTERMINATEDINSTANCES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROFTERMINATEDINSTANCES
This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of terminated inner instances for the Multi-Instance Activity. The sum of numberOfTerminatedInstances, numberOfCompletedInstances, and numberOfActiveInstances always sums up to numberOfInstances.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFTERMINATEDINSTANCES)
ONEBEHAVIOREVENTREF
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ONEBEHAVIOREVENTREF
The EventDefinition which is thrown when behavior is set to one and the first internal Activity instance has completed.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.ONEBEHAVIOREVENTREF)
OUTPUTDATAITEM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OUTPUTDATAITEM
A Data Output, representing for every Activity instance the single item
 of the collection stored in the loopDataOutput. This Data Output can
 be the target of DataOutputAssociation to a data output of the
 Activity s InputOutputSpecification. The type of this Data
 Output MUST the scalar of the type defined for the loopDataOutput.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.OUTPUTDATAITEM)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MultiInstanceLoopCharacteristicsStereotype
protected MultiInstanceLoopCharacteristicsStereotype([BPMN2Profile](BPMN2Profile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getBehaviorProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getBehaviorProperty()
getCompletionConditionProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getCompletionConditionProperty()
getComplexBehaviorDefintionProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getComplexBehaviorDefintionProperty()
getInputDataItemProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getInputDataItemProperty()
getIsSequentialProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getIsSequentialProperty()
getLoopCardinalityProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLoopCardinalityProperty()
getLoopCounterProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLoopCounterProperty()
getLoopDataInputRefProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLoopDataInputRefProperty()
getLoopDataOutputRefProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getLoopDataOutputRefProperty()
getNoneBehaviorEventRefProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNoneBehaviorEventRefProperty()
getNumberOfActiveInstancesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfActiveInstancesProperty()
getNumberOfCompletedInstancesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfCompletedInstancesProperty()
getNumberOfInstancesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfInstancesProperty()
getNumberOfTerminatedInstancesProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getNumberOfTerminatedInstancesProperty()
getOneBehaviorEventRefProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getOneBehaviorEventRefProperty()
getOutputDataItemProperty
@CheckForNullpublic [Property](../../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getOutputDataItemProperty()
setBehavior
public void setBehavior([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [BPMN2Profile.MultiInstanceBehaviorEnum](BPMN2Profile.MultiInstanceBehaviorEnum.html) value)
clearBehavior
public void clearBehavior([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getBehavior
@CheckForNullpublic [BPMN2Profile.MultiInstanceBehaviorEnum](BPMN2Profile.MultiInstanceBehaviorEnum.html) getBehavior([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setCompletionCondition
public void setCompletionCondition([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearCompletionCondition
public void clearCompletionCondition([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getCompletionCondition
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCompletionCondition([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setComplexBehaviorDefintion
public void setComplexBehaviorDefintion([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> value)
clearComplexBehaviorDefintion
public void clearComplexBehaviorDefintion([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
addComplexBehaviorDefintion
public void addComplexBehaviorDefintion([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
removeComplexBehaviorDefintion
public void removeComplexBehaviorDefintion([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
getComplexBehaviorDefintion
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getComplexBehaviorDefintion([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setInputDataItem
public void setInputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearInputDataItem
public void clearInputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getInputDataItem
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getInputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setIsSequential
public void setIsSequential([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearIsSequential
public void clearIsSequential([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isIsSequential
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isIsSequential([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLoopCardinality
public void setLoopCardinality([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearLoopCardinality
public void clearLoopCardinality([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLoopCardinality
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLoopCardinality([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLoopCounter
public void setLoopCounter([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearLoopCounter
public void clearLoopCounter([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLoopCounter
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getLoopCounter([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLoopDataInputRef
public void setLoopDataInputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearLoopDataInputRef
public void clearLoopDataInputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLoopDataInputRef
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getLoopDataInputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setLoopDataOutputRef
public void setLoopDataOutputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearLoopDataOutputRef
public void clearLoopDataOutputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getLoopDataOutputRef
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getLoopDataOutputRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNoneBehaviorEventRef
public void setNoneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearNoneBehaviorEventRef
public void clearNoneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNoneBehaviorEventRef
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getNoneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfActiveInstances
public void setNumberOfActiveInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfActiveInstances
public void clearNumberOfActiveInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfActiveInstances
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfActiveInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfCompletedInstances
public void setNumberOfCompletedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfCompletedInstances
public void clearNumberOfCompletedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfCompletedInstances
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfCompletedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfInstances
public void setNumberOfInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfInstances
public void clearNumberOfInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfInstances
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setNumberOfTerminatedInstances
public void setNumberOfTerminatedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) value)
clearNumberOfTerminatedInstances
public void clearNumberOfTerminatedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getNumberOfTerminatedInstances
@CheckForNullpublic [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getNumberOfTerminatedInstances([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setOneBehaviorEventRef
public void setOneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearOneBehaviorEventRef
public void clearOneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getOneBehaviorEventRef
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getOneBehaviorEventRef([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
setOutputDataItem
public void setOutputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
clearOutputDataItem
public void clearOutputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getOutputDataItem
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getOutputDataItem([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
isInstance
public static boolean isInstance(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.cbm.profiles</a></div>
<h1 class="title" title="Class BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype">Class BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="BPMN2Profile.html" title="class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype</span>
<span class="extends-implements">extends <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BEHAVIOR">BEHAVIOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">The attribute behavior acts as a shortcut for specifying when events shall be thrown from an Activity instance that is about to complete.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPLETIONCONDITION">COMPLETIONCONDITION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This attribute defines a Boolean Expression that when evaluated to true, cancels the remaining Activity instances and produces a token.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPLEXBEHAVIORDEFINTION">COMPLEXBEHAVIORDEFINTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Controls when and which Events are thrown in case behavior is set to complex.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INPUTDATAITEM">INPUTDATAITEM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A Data Input, representing for every Activity instance the single item of the collection stored in the loopDataInput.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ISSEQUENTIAL">ISSEQUENTIAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">This attribute is a flag that controls whether the Activity
                 instances will execute sequentially or in parallel.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOOPCARDINALITY">LOOPCARDINALITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A numeric Expression that controls the number of Activity instances that will be created.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOOPCOUNTER">LOOPCOUNTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">The LoopCounter attribute is used at runtime to count the number of loops and is automatically updated by the process engine.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOOPDATAINPUTREF">LOOPDATAINPUTREF</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A reference to a DataInput which is part of the Activity   s InputOutputSpecification.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOOPDATAOUTPUTREF">LOOPDATAOUTPUTREF</a></code></div>
<div class="col-last even-row-color">
<div class="block">This ItemAwareElement specifies the collection of data, which will be produced by the multi-instance.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NONEBEHAVIOREVENTREF">NONEBEHAVIOREVENTREF</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The EventDefinition which is thrown when the behavior is set to none and an internal Activity instance has completed</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBEROFACTIVEINSTANCES">NUMBEROFACTIVEINSTANCES</a></code></div>
<div class="col-last even-row-color">
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBEROFCOMPLETEDINSTANCES">NUMBEROFCOMPLETEDINSTANCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBEROFINSTANCES">NUMBEROFINSTANCES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBEROFTERMINATEDINSTANCES">NUMBEROFTERMINATEDINSTANCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ONEBEHAVIOREVENTREF">ONEBEHAVIOREVENTREF</a></code></div>
<div class="col-last even-row-color">
<div class="block">The EventDefinition which is thrown when behavior is set to one and the first internal Activity instance has completed.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OUTPUTDATAITEM">OUTPUTDATAITEM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A Data Output, representing for every Activity instance the single item
                 of the collection stored in the loopDataOutput.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.cbm.profiles.BPMN2Profile)">MultiInstanceLoopCharacteristicsStereotype</a><wbr/>(<a href="BPMN2Profile.html" title="class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile</a> profile)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addComplexBehaviorDefintion</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearBehavior</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearCompletionCondition</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearComplexBehaviorDefintion</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearInputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearIsSequential</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLoopCardinality</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLoopCounter</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLoopDataInputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearLoopDataOutputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNoneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfActiveInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfCompletedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearNumberOfTerminatedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearOneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearOutputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BPMN2Profile.MultiInstanceBehaviorEnum.html" title="enum class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile.MultiInstanceBehaviorEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getBehavior</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehaviorProperty()">getBehaviorProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCompletionCondition</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompletionConditionProperty()">getCompletionConditionProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComplexBehaviorDefintion</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComplexBehaviorDefintionProperty()">getComplexBehaviorDefintionProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getInputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInputDataItemProperty()">getInputDataItemProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIsSequentialProperty()">getIsSequentialProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLoopCardinality</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopCardinalityProperty()">getLoopCardinalityProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLoopCounter</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopCounterProperty()">getLoopCounterProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLoopDataInputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopDataInputRefProperty()">getLoopDataInputRefProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLoopDataOutputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoopDataOutputRefProperty()">getLoopDataOutputRefProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNoneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoneBehaviorEventRefProperty()">getNoneBehaviorEventRefProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfActiveInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfActiveInstancesProperty()">getNumberOfActiveInstancesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfCompletedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfCompletedInstancesProperty()">getNumberOfCompletedInstancesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfInstancesProperty()">getNumberOfInstancesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getNumberOfTerminatedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberOfTerminatedInstancesProperty()">getNumberOfTerminatedInstancesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOneBehaviorEventRefProperty()">getOneBehaviorEventRefProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOutputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputDataItemProperty()">getOutputDataItemProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isIsSequential</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeComplexBehaviorDefintion</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceBehaviorEnum)">setBehavior</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="BPMN2Profile.MultiInstanceBehaviorEnum.html" title="enum class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile.MultiInstanceBehaviorEnum</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setCompletionCondition</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setComplexBehaviorDefintion</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setInputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setIsSequential</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setLoopCardinality</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setLoopCounter</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setLoopDataInputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setLoopDataOutputRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setNoneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfActiveInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfCompletedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">setNumberOfTerminatedInstances</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOneBehaviorEventRef</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOutputDataItem</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BEHAVIOR">
<h3>BEHAVIOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BEHAVIOR</span></div>
<div class="block">The attribute behavior acts as a shortcut for specifying when events shall be thrown from an Activity instance that is about to complete. It can assume values of none, one, all, and complex, resulting in the following behavior:
                 - None: the EventDefinition which is associated through the noneEvent association will be thrown for each instance completing;
                 - One: the EventDefinition referenced through the oneEvent association will be thrown upon the first instance completing;
                 - All: no Event is ever thrown; a token is produced after completion of all instances
                 - Complex: the complexBehaviorDefinitions are consulted to determine if and which Events to throw.
                 For the behaviors of none and one, a default SignalEventDefinition will be thrown which automatically carries the current runtime attributes of the MI Activity. Any thrown Events can be caught by boundary Events on the Multi-Instance Activity.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.BEHAVIOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPLETIONCONDITION">
<h3>COMPLETIONCONDITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPLETIONCONDITION</span></div>
<div class="block">This attribute defines a Boolean Expression that when evaluated to true, cancels the remaining Activity instances and produces a token.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.COMPLETIONCONDITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPLEXBEHAVIORDEFINTION">
<h3>COMPLEXBEHAVIORDEFINTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPLEXBEHAVIORDEFINTION</span></div>
<div class="block">Controls when and which Events are thrown in case behavior is set to complex.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.COMPLEXBEHAVIORDEFINTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INPUTDATAITEM">
<h3>INPUTDATAITEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INPUTDATAITEM</span></div>
<div class="block">A Data Input, representing for every Activity instance the single item of the collection stored in the loopDataInput. This Data Input can be the source of DataInputAssociation to a data input of the Activity   s InputOutputSpecification. The type of this Data Input MUST the scalar of the type defined for the loopDataInput.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.INPUTDATAITEM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ISSEQUENTIAL">
<h3>ISSEQUENTIAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ISSEQUENTIAL</span></div>
<div class="block">This attribute is a flag that controls whether the Activity
                 instances will execute sequentially or in parallel.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.ISSEQUENTIAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOOPCARDINALITY">
<h3>LOOPCARDINALITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOOPCARDINALITY</span></div>
<div class="block">A numeric Expression that controls the number of Activity instances that will be created. This Expression MUST evaluate to an integer.
                 This may be underspecified, meaning that the modeler may simply document the condition. In such a case the loop cannot be formally executed.
                 In order to initialize a valid multi-instance, either the
                 loopCardinality Expression or the loopDataInput MUST be specified.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPCARDINALITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOOPCOUNTER">
<h3>LOOPCOUNTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOOPCOUNTER</span></div>
<div class="block">The LoopCounter attribute is used at runtime to count the number of loops and is automatically updated by the process engine.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPCOUNTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOOPDATAINPUTREF">
<h3>LOOPDATAINPUTREF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOOPDATAINPUTREF</span></div>
<div class="block">A reference to a DataInput which is part of the Activity   s InputOutputSpecification. This DataInput is used to determine the number of Activity instances, one Activity instance per item in the collection of data stored in that DataInput element.
                 In order to initialize a valid multi-instance, either the loopCardinality Expression or the loopDataInput MUST be specified.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPDATAINPUTREF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOOPDATAOUTPUTREF">
<h3>LOOPDATAOUTPUTREF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOOPDATAOUTPUTREF</span></div>
<div class="block">This ItemAwareElement specifies the collection of data, which will be produced by the multi-instance.
                 For Tasks it is a reference to a Data Output which is part of the Activity   s InputOutputSpecification.
                 For Sub-Processes it is a reference to a collection-valued Data Object in the context that is visible to the Sub-Processes.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.LOOPDATAOUTPUTREF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NONEBEHAVIOREVENTREF">
<h3>NONEBEHAVIOREVENTREF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NONEBEHAVIOREVENTREF</span></div>
<div class="block">The EventDefinition which is thrown when the behavior is set to none and an internal Activity instance has completed</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NONEBEHAVIOREVENTREF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFACTIVEINSTANCES">
<h3>NUMBEROFACTIVEINSTANCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFACTIVEINSTANCES</span></div>
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of currently active inner instances for the Multi-Instance Activity. In case of a sequential Multi-Instance Activity, this value can   t be greater than 1. For parallel Multi-Instance Activities, this value can   t be greater than the value contained in numberOfInstances.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFACTIVEINSTANCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFCOMPLETEDINSTANCES">
<h3>NUMBEROFCOMPLETEDINSTANCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFCOMPLETEDINSTANCES</span></div>
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of already completed inner instances for the Multi-Instance Activity.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFCOMPLETEDINSTANCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFINSTANCES">
<h3>NUMBEROFINSTANCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFINSTANCES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFINSTANCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROFTERMINATEDINSTANCES">
<h3>NUMBEROFTERMINATEDINSTANCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROFTERMINATEDINSTANCES</span></div>
<div class="block">This attribute is provided for the outer instance of the Multi-Instance Activity only. This attribute contains the number of terminated inner instances for the Multi-Instance Activity. The sum of numberOfTerminatedInstances, numberOfCompletedInstances, and numberOfActiveInstances always sums up to numberOfInstances.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.NUMBEROFTERMINATEDINSTANCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ONEBEHAVIOREVENTREF">
<h3>ONEBEHAVIOREVENTREF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ONEBEHAVIOREVENTREF</span></div>
<div class="block">The EventDefinition which is thrown when behavior is set to one and the first internal Activity instance has completed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.ONEBEHAVIOREVENTREF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OUTPUTDATAITEM">
<h3>OUTPUTDATAITEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OUTPUTDATAITEM</span></div>
<div class="block">A Data Output, representing for every Activity instance the single item
                 of the collection stored in the loopDataOutput. This Data Output can
                 be the target of DataOutputAssociation to a data output of the
                 Activity   s InputOutputSpecification. The type of this Data
                 Output MUST the scalar of the type defined for the loopDataOutput.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceLoopCharacteristicsStereotype.OUTPUTDATAITEM">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.cbm.profiles.BPMN2Profile)">
<h3>MultiInstanceLoopCharacteristicsStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">MultiInstanceLoopCharacteristicsStereotype</span><wbr/><span class="parameters">(<a href="BPMN2Profile.html" title="class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile</a> profile)</span></div>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehaviorProperty()">
<h3>getBehaviorProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getBehaviorProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCompletionConditionProperty()">
<h3>getCompletionConditionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getCompletionConditionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getComplexBehaviorDefintionProperty()">
<h3>getComplexBehaviorDefintionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getComplexBehaviorDefintionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInputDataItemProperty()">
<h3>getInputDataItemProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getInputDataItemProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIsSequentialProperty()">
<h3>getIsSequentialProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getIsSequentialProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLoopCardinalityProperty()">
<h3>getLoopCardinalityProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLoopCardinalityProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLoopCounterProperty()">
<h3>getLoopCounterProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLoopCounterProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLoopDataInputRefProperty()">
<h3>getLoopDataInputRefProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLoopDataInputRefProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLoopDataOutputRefProperty()">
<h3>getLoopDataOutputRefProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getLoopDataOutputRefProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNoneBehaviorEventRefProperty()">
<h3>getNoneBehaviorEventRefProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNoneBehaviorEventRefProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfActiveInstancesProperty()">
<h3>getNumberOfActiveInstancesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfActiveInstancesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfCompletedInstancesProperty()">
<h3>getNumberOfCompletedInstancesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfCompletedInstancesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfInstancesProperty()">
<h3>getNumberOfInstancesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfInstancesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfTerminatedInstancesProperty()">
<h3>getNumberOfTerminatedInstancesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getNumberOfTerminatedInstancesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOneBehaviorEventRefProperty()">
<h3>getOneBehaviorEventRefProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOneBehaviorEventRefProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOutputDataItemProperty()">
<h3>getOutputDataItemProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOutputDataItemProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.cbm.profiles.BPMN2Profile.MultiInstanceBehaviorEnum)">
<h3>setBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBehavior</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="BPMN2Profile.MultiInstanceBehaviorEnum.html" title="enum class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile.MultiInstanceBehaviorEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearBehavior</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBehavior(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getBehavior</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="BPMN2Profile.MultiInstanceBehaviorEnum.html" title="enum class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile.MultiInstanceBehaviorEnum</a></span> <span class="element-name">getBehavior</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setCompletionCondition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCompletionCondition</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearCompletionCondition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCompletionCondition</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCompletionCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCompletionCondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCompletionCondition</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setComplexBehaviorDefintion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setComplexBehaviorDefintion</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearComplexBehaviorDefintion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearComplexBehaviorDefintion</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addComplexBehaviorDefintion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addComplexBehaviorDefintion</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeComplexBehaviorDefintion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeComplexBehaviorDefintion</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getComplexBehaviorDefintion(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getComplexBehaviorDefintion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getComplexBehaviorDefintion</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setInputDataItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearInputDataItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearInputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getInputDataItem</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getInputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setIsSequential</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIsSequential</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearIsSequential</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearIsSequential</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isIsSequential(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isIsSequential</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isIsSequential</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setLoopCardinality</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoopCardinality</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLoopCardinality</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLoopCardinality</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLoopCardinality(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLoopCardinality</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLoopCardinality</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setLoopCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoopCounter</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLoopCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLoopCounter</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLoopCounter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLoopCounter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getLoopCounter</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setLoopDataInputRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoopDataInputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLoopDataInputRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLoopDataInputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLoopDataInputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLoopDataInputRef</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getLoopDataInputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setLoopDataOutputRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoopDataOutputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearLoopDataOutputRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLoopDataOutputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLoopDataOutputRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLoopDataOutputRef</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getLoopDataOutputRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setNoneBehaviorEventRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNoneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNoneBehaviorEventRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNoneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNoneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNoneBehaviorEventRef</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getNoneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfActiveInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfActiveInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfActiveInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfActiveInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfActiveInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfActiveInstances</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfActiveInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfCompletedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfCompletedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfCompletedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfCompletedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfCompletedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfCompletedInstances</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfCompletedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfInstances</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Integer)">
<h3>setNumberOfTerminatedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberOfTerminatedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearNumberOfTerminatedInstances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearNumberOfTerminatedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberOfTerminatedInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getNumberOfTerminatedInstances</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getNumberOfTerminatedInstances</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setOneBehaviorEventRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearOneBehaviorEventRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearOneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOneBehaviorEventRef(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOneBehaviorEventRef</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getOneBehaviorEventRef</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setOutputDataItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearOutputDataItem</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearOutputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOutputDataItem(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getOutputDataItem</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getOutputDataItem</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
