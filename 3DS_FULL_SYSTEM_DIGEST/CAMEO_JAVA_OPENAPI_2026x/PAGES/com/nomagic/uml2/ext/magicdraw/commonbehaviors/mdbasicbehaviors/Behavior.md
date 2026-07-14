# JAVA OPENAPI: Behavior (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html
- source_path: `com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html`
- source_sha256: `0bdfd704e844456b08c2b9ad714c57ba2861dd931509761862f46a8a0599d505`
- captured_utc: `2026-07-14T16:58:55.015480+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors](package-summary.html)

## Interface Behavior

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[BehavioredClassifier](BehavioredClassifier.html)`, `[Class](../../classes/mdkernel/Class.html)`, `[Classifier](../../classes/mdkernel/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](../../classes/mdkernel/Type.html)`

All Known Subinterfaces:
`[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[FunctionBehavior](FunctionBehavior.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[OpaqueBehavior](OpaqueBehavior.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`

public interfaceBehaviorextends [Class](../../classes/mdkernel/Class.html)

begin-user-doc 
 A representation of the model object '***Behavior***'.
 end-user-doc 
begin-model-doc 
 Behavior is a specification of how its context BehavioredClassifier changes state over time. This specification may be either a definition of possible behavior
 execution or emergent behavior, or a selective illustration of an interesting subset of possible executions. The latter form is typically used for capturing
 examples, such as a trace of a particular execution.
 end-model-doc 
The following features are supported:
 [`*Context*`](#getContext())
[`*Reentrant*`](#isReentrant())
[`*Owned Parameter*`](#getOwnedParameter())
[`*transition Of Effect*`](#get_transitionOfEffect())
[`*Specification*`](#getSpecification())
[`*Owned Parameter Set*`](#getOwnedParameterSet())
[`*connector Of Contract*`](#get_connectorOfContract())
[`*reduce Action Of Reducer*`](#get_reduceActionOfReducer())
[`*Event*`](#getEvent())
[`*opaque Expression Of Behavior*`](#get_opaqueExpressionOfBehavior())
[`*Postcondition*`](#getPostcondition())
[`*Precondition*`](#getPrecondition())
[`*state Of Do Activity*`](#get_stateOfDoActivity())
[`*state Of Entry*`](#get_stateOfEntry())
[`*state Of Exit*`](#get_stateOfExit())
[`*object Node Of Selection*`](#get_objectNodeOfSelection())
[`*Observation*`](#getObservation())
[`*Redefined Behavior*`](#getRedefinedBehavior())
[`*behavior Of Redefined Behavior*`](#get_behaviorOfRedefinedBehavior())
[`*object Flow Of Transformation*`](#get_objectFlowOfTransformation())
[`*object Flow Of Selection*`](#get_objectFlowOfSelection())
[`*decision Node Of Decision Input*`](#get_decisionNodeOfDecisionInput())
[`*behavior Execution Specification Of Behavior*`](#get_behaviorExecutionSpecificationOfBehavior())
[`*behaviored Classifier Of Owned Behavior*`](#get_behavioredClassifierOfOwnedBehavior())
[`*call Behavior Action Of Behavior*`](#get_callBehaviorActionOfBehavior())
[`*behaviored Classifier Of Classifier Behavior*`](#get_behavioredClassifierOfClassifierBehavior())

See Also:
[`UMLPackage.getBehavior()`](../../metadata/UMLPackage.html#getBehavior())
Model:
abstract="true"
 annotation="MOF package='commonbehaviors.mdbasicbehaviors'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[BehavioredClassifier](BehavioredClassifier.html)`
`[get_behavioredClassifierOfClassifierBehavior](#get_behavioredClassifierOfClassifierBehavior())()`
Returns the value of the '***behaviored Classifier Of Classifier Behavior***' reference.
`[BehavioredClassifier](BehavioredClassifier.html)`
`[get_behavioredClassifierOfOwnedBehavior](#get_behavioredClassifierOfOwnedBehavior())()`
Returns the value of the '***behaviored Classifier Of Owned Behavior***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[BehaviorExecutionSpecification](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)>`
`[get_behaviorExecutionSpecificationOfBehavior](#get_behaviorExecutionSpecificationOfBehavior())()`
Returns the value of the '***behavior Execution Specification Of Behavior***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](Behavior.html)>`
`[get_behaviorOfRedefinedBehavior](#get_behaviorOfRedefinedBehavior())()`
Returns the value of the '***behavior Of Redefined Behavior***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)>`
`[get_callBehaviorActionOfBehavior](#get_callBehaviorActionOfBehavior())()`
Returns the value of the '***call Behavior Action Of Behavior***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](../../compositestructures/mdinternalstructures/Connector.html)>`
`[get_connectorOfContract](#get_connectorOfContract())()`
Returns the value of the '***connector Of Contract***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DecisionNode](../../activities/mdintermediateactivities/DecisionNode.html)>`
`[get_decisionNodeOfDecisionInput](#get_decisionNodeOfDecisionInput())()`
Returns the value of the '***decision Node Of Decision Input***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)>`
`[get_objectFlowOfSelection](#get_objectFlowOfSelection())()`
Returns the value of the '***object Flow Of Selection***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)>`
`[get_objectFlowOfTransformation](#get_objectFlowOfTransformation())()`
Returns the value of the '***object Flow Of Transformation***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)>`
`[get_objectNodeOfSelection](#get_objectNodeOfSelection())()`
Returns the value of the '***object Node Of Selection***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[OpaqueExpression](../../classes/mdkernel/OpaqueExpression.html)>`
`[get_opaqueExpressionOfBehavior](#get_opaqueExpressionOfBehavior())()`
Returns the value of the '***opaque Expression Of Behavior***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)>`
`[get_reduceActionOfReducer](#get_reduceActionOfReducer())()`
Returns the value of the '***reduce Action Of Reducer***' reference list.
`[State](../../statemachines/mdbehaviorstatemachines/State.html)`
`[get_stateOfDoActivity](#get_stateOfDoActivity())()`
Returns the value of the '***state Of Do Activity***' container reference.
`[State](../../statemachines/mdbehaviorstatemachines/State.html)`
`[get_stateOfEntry](#get_stateOfEntry())()`
Returns the value of the '***state Of Entry***' container reference.
`[State](../../statemachines/mdbehaviorstatemachines/State.html)`
`[get_stateOfExit](#get_stateOfExit())()`
Returns the value of the '***state Of Exit***' container reference.
`[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`
`[get_transitionOfEffect](#get_transitionOfEffect())()`
Returns the value of the '***transition Of Effect***' container reference.
`[BehavioredClassifier](BehavioredClassifier.html)`
`[getContext](#getContext())()`
Returns the value of the '***Context***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Event](../mdcommunications/Event.html)>`
`[getEvent](#getEvent())()`
Returns the value of the '***Event***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Observation](../mdsimpletime/Observation.html)>`
`[getObservation](#getObservation())()`
Returns the value of the '***Observation***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../classes/mdkernel/Parameter.html)>`
`[getOwnedParameter](#getOwnedParameter())()`
Returns the value of the '***Owned Parameter***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)>`
`[getOwnedParameterSet](#getOwnedParameterSet())()`
Returns the value of the '***Owned Parameter Set***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)>`
`[getPostcondition](#getPostcondition())()`
Returns the value of the '***Postcondition***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)>`
`[getPrecondition](#getPrecondition())()`
Returns the value of the '***Precondition***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](Behavior.html)>`
`[getRedefinedBehavior](#getRedefinedBehavior())()`
Returns the value of the '***Redefined Behavior***' reference list.
`[BehavioralFeature](../../classes/mdkernel/BehavioralFeature.html)`
`[getSpecification](#getSpecification())()`
Returns the value of the '***Specification***' reference.
`boolean`
`[has_behaviorExecutionSpecificationOfBehavior](#has_behaviorExecutionSpecificationOfBehavior())()`

`boolean`
`[has_behaviorOfRedefinedBehavior](#has_behaviorOfRedefinedBehavior())()`

`boolean`
`[has_callBehaviorActionOfBehavior](#has_callBehaviorActionOfBehavior())()`

`boolean`
`[has_connectorOfContract](#has_connectorOfContract())()`

`boolean`
`[has_decisionNodeOfDecisionInput](#has_decisionNodeOfDecisionInput())()`

`boolean`
`[has_objectFlowOfSelection](#has_objectFlowOfSelection())()`

`boolean`
`[has_objectFlowOfTransformation](#has_objectFlowOfTransformation())()`

`boolean`
`[has_objectNodeOfSelection](#has_objectNodeOfSelection())()`

`boolean`
`[has_opaqueExpressionOfBehavior](#has_opaqueExpressionOfBehavior())()`

`boolean`
`[has_reduceActionOfReducer](#has_reduceActionOfReducer())()`

`boolean`
`[hasEvent](#hasEvent())()`

`boolean`
`[hasObservation](#hasObservation())()`

`boolean`
`[hasOwnedParameter](#hasOwnedParameter())()`

`boolean`
`[hasOwnedParameterSet](#hasOwnedParameterSet())()`

`boolean`
`[hasPostcondition](#hasPostcondition())()`

`boolean`
`[hasPrecondition](#hasPrecondition())()`

`boolean`
`[hasRedefinedBehavior](#hasRedefinedBehavior())()`

`boolean`
`[isReentrant](#isReentrant())()`
Returns the value of the '***Reentrant***' attribute.
`void`
`[set_behavioredClassifierOfClassifierBehavior](#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](BehavioredClassifier.html) value)`
Sets the value of the '[`*behaviored Classifier Of Classifier Behavior*`](#get_behavioredClassifierOfClassifierBehavior())' reference.
`void`
`[set_behavioredClassifierOfOwnedBehavior](#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))([BehavioredClassifier](BehavioredClassifier.html) value)`
Sets the value of the '[`*behaviored
 Classifier Of Owned Behavior*`](#get_behavioredClassifierOfOwnedBehavior())' container reference.
`void`
`[set_stateOfDoActivity](#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../statemachines/mdbehaviorstatemachines/State.html) value)`
Sets the value of the '[`*state Of Do Activity*`](#get_stateOfDoActivity())'
 container reference.
`void`
`[set_stateOfEntry](#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../statemachines/mdbehaviorstatemachines/State.html) value)`
Sets the value of the '[`*state Of Entry*`](#get_stateOfEntry())' container
 reference.
`void`
`[set_stateOfExit](#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../statemachines/mdbehaviorstatemachines/State.html) value)`
Sets the value of the '[`*state Of Exit*`](#get_stateOfExit())' container
 reference.
`void`
`[set_transitionOfEffect](#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)`
Sets the value of the '[`*transition Of Effect*`](#get_transitionOfEffect())'
 container reference.
`void`
`[setReentrant](#setReentrant(boolean))(boolean value)`
Sets the value of the '[`*Reentrant*`](#isReentrant())' attribute.
`void`
`[setSpecification](#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))([BehavioralFeature](../../classes/mdkernel/BehavioralFeature.html) value)`
Sets the value of the '[`*Specification*`](#getSpecification())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.[BehavioredClassifier](BehavioredClassifier.html)
`[getClassifierBehavior](BehavioredClassifier.html#getClassifierBehavior()), [getInterfaceRealization](BehavioredClassifier.html#getInterfaceRealization()), [getOwnedBehavior](BehavioredClassifier.html#getOwnedBehavior()), [hasInterfaceRealization](BehavioredClassifier.html#hasInterfaceRealization()), [hasOwnedBehavior](BehavioredClassifier.html#hasOwnedBehavior()), [setClassifierBehavior](BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Class](../../classes/mdkernel/Class.html)
`[getExtension](../../classes/mdkernel/Class.html#getExtension()), [getNestedClassifier](../../classes/mdkernel/Class.html#getNestedClassifier()), [getOwnedAttribute](../../classes/mdkernel/Class.html#getOwnedAttribute()), [getOwnedOperation](../../classes/mdkernel/Class.html#getOwnedOperation()), [getOwnedReception](../../classes/mdkernel/Class.html#getOwnedReception()), [getSuperClass](../../classes/mdkernel/Class.html#getSuperClass()), [hasExtension](../../classes/mdkernel/Class.html#hasExtension()), [hasNestedClassifier](../../classes/mdkernel/Class.html#hasNestedClassifier()), [hasOwnedOperation](../../classes/mdkernel/Class.html#hasOwnedOperation()), [hasOwnedReception](../../classes/mdkernel/Class.html#hasOwnedReception()), [hasSuperClass](../../classes/mdkernel/Class.html#hasSuperClass()), [isAbstract](../../classes/mdkernel/Class.html#isAbstract()), [isActive](../../classes/mdkernel/Class.html#isActive()), [setAbstract](../../classes/mdkernel/Class.html#setAbstract(boolean)), [setActive](../../classes/mdkernel/Class.html#setActive(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](../../classes/mdkernel/Classifier.html)
`[get_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](../../classes/mdkernel/Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](../../classes/mdkernel/Classifier.html#getAttribute()), [getCollaborationUse](../../classes/mdkernel/Classifier.html#getCollaborationUse()), [getFeature](../../classes/mdkernel/Classifier.html#getFeature()), [getGeneral](../../classes/mdkernel/Classifier.html#getGeneral()), [getGeneralization](../../classes/mdkernel/Classifier.html#getGeneralization()), [getInheritedMember](../../classes/mdkernel/Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](../../classes/mdkernel/Classifier.html#getOwnedUseCase()), [getPowertypeExtent](../../classes/mdkernel/Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](../../classes/mdkernel/Classifier.html#getRedefinedClassifier()), [getRepresentation](../../classes/mdkernel/Classifier.html#getRepresentation()), [getSubstitution](../../classes/mdkernel/Classifier.html#getSubstitution()), [getTemplateParameter](../../classes/mdkernel/Classifier.html#getTemplateParameter()), [getUMLClass](../../classes/mdkernel/Classifier.html#getUMLClass()), [getUseCase](../../classes/mdkernel/Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](../../classes/mdkernel/Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](../../classes/mdkernel/Classifier.html#hasAttribute()), [hasCollaborationUse](../../classes/mdkernel/Classifier.html#hasCollaborationUse()), [hasFeature](../../classes/mdkernel/Classifier.html#hasFeature()), [hasGeneral](../../classes/mdkernel/Classifier.html#hasGeneral()), [hasGeneralization](../../classes/mdkernel/Classifier.html#hasGeneralization()), [hasInheritedMember](../../classes/mdkernel/Classifier.html#hasInheritedMember()), [hasOwnedUseCase](../../classes/mdkernel/Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](../../classes/mdkernel/Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()), [hasSubstitution](../../classes/mdkernel/Classifier.html#hasSubstitution()), [hasUseCase](../../classes/mdkernel/Classifier.html#hasUseCase()), [isFinalSpecialization](../../classes/mdkernel/Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setFinalSpecialization](../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)
`[getOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#getOwnedPort()), [hasOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#hasOwnedPort())`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../../classes/mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../../classes/mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../../classes/mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)
`[getOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()), [getPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()), [getRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()), [hasOwnedAttribute](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()), [hasOwnedConnector](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()), [hasPart](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()), [hasRole](../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Type](../../classes/mdkernel/Type.html)
`[get_associationOfEndType](../../classes/mdkernel/Type.html#get_associationOfEndType()), [get_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#get_behavioralFeatureOfRaisedException()), [get_operationOfRaisedException](../../classes/mdkernel/Type.html#get_operationOfRaisedException()), [get_typedElementOfType](../../classes/mdkernel/Type.html#get_typedElementOfType()), [getPackage](../../classes/mdkernel/Type.html#getPackage()), [has_associationOfEndType](../../classes/mdkernel/Type.html#has_associationOfEndType()), [has_behavioralFeatureOfRaisedException](../../classes/mdkernel/Type.html#has_behavioralFeatureOfRaisedException()), [has_operationOfRaisedException](../../classes/mdkernel/Type.html#has_operationOfRaisedException()), [has_typedElementOfType](../../classes/mdkernel/Type.html#has_typedElementOfType()), [setPackage](../../classes/mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))`

============ METHOD DETAIL ========== 
Method Details
getEvent
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Event](../mdcommunications/Event.html)> getEvent()
Returns the value of the '***Event***' containment reference list.
 The list contents are of type [`Event`](../mdcommunications/Event.html).
 It is bidirectional and its opposite is '[`*Behavior*`](../mdcommunications/Event.html#getBehavior())'.
 begin-user-doc 
If the meaning of the '*Event*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Event*' containment reference list.
See Also:
[`UMLPackage.getBehavior_Event()`](../../metadata/UMLPackage.html#getBehavior_Event())
[`Event.getBehavior()`](../mdcommunications/Event.html#getBehavior())
Model:
opposite="behavior" containment="true" resolveProxies="true" ordered="false"
Generated:
getObservation
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Observation](../mdsimpletime/Observation.html)> getObservation()
Returns the value of the '***Observation***' containment reference list.
 The list contents are of type [`Observation`](../mdsimpletime/Observation.html).
 It is bidirectional and its opposite is '[`*Behavior*`](../mdsimpletime/Observation.html#getBehavior())'.
 begin-user-doc 
If the meaning of the '*Observation*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Observation*' containment reference list.
See Also:
[`UMLPackage.getBehavior_Observation()`](../../metadata/UMLPackage.html#getBehavior_Observation())
[`Observation.getBehavior()`](../mdsimpletime/Observation.html#getBehavior())
Model:
opposite="behavior" containment="true" resolveProxies="true" ordered="false"
Generated:
get_behavioredClassifierOfOwnedBehavior
@CheckForNull[BehavioredClassifier](BehavioredClassifier.html) get_behavioredClassifierOfOwnedBehavior()
Returns the value of the '***behaviored Classifier Of Owned Behavior***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Behavior*`](BehavioredClassifier.html#getOwnedBehavior())'.
 begin-user-doc 
If the meaning of the '*behaviored Classifier Of Owned Behavior*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behaviored Classifier Of Owned Behavior*' container reference.
See Also:
[`set_behavioredClassifierOfOwnedBehavior(BehavioredClassifier)`](#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))
[`UMLPackage.getBehavior__behavioredClassifierOfOwnedBehavior()`](../../metadata/UMLPackage.html#getBehavior__behavioredClassifierOfOwnedBehavior())
[`BehavioredClassifier.getOwnedBehavior()`](BehavioredClassifier.html#getOwnedBehavior())
Model:
opposite="ownedBehavior" transient="false" ordered="false"
Generated:
set_behavioredClassifierOfOwnedBehavior
void set_behavioredClassifierOfOwnedBehavior(@CheckForNull
 [BehavioredClassifier](BehavioredClassifier.html) value)
Sets the value of the '[`*behaviored
 Classifier Of Owned Behavior*`](#get_behavioredClassifierOfOwnedBehavior())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*behaviored Classifier Of Owned Behavior*' container reference.
See Also:
[`get_behavioredClassifierOfOwnedBehavior()`](#get_behavioredClassifierOfOwnedBehavior())
Generated:
get_behavioredClassifierOfClassifierBehavior
@CheckForNull[BehavioredClassifier](BehavioredClassifier.html) get_behavioredClassifierOfClassifierBehavior()
Returns the value of the '***behaviored Classifier Of Classifier Behavior***' reference.
 It is bidirectional and its opposite is
 '[`*Classifier Behavior*`](BehavioredClassifier.html#getClassifierBehavior())'.
 begin-user-doc 
If the meaning of the '*behaviored Classifier Of Classifier Behavior*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behaviored Classifier Of Classifier Behavior*' reference.
See Also:
[`set_behavioredClassifierOfClassifierBehavior(BehavioredClassifier)`](#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier))
[`UMLPackage.getBehavior__behavioredClassifierOfClassifierBehavior()`](../../metadata/UMLPackage.html#getBehavior__behavioredClassifierOfClassifierBehavior())
[`BehavioredClassifier.getClassifierBehavior()`](BehavioredClassifier.html#getClassifierBehavior())
Model:
opposite="classifierBehavior" ordered="false"
Generated:
set_behavioredClassifierOfClassifierBehavior
void set_behavioredClassifierOfClassifierBehavior(@CheckForNull
 [BehavioredClassifier](BehavioredClassifier.html) value)
Sets the value of the '[`*behaviored Classifier Of Classifier Behavior*`](#get_behavioredClassifierOfClassifierBehavior())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*behaviored Classifier Of Classifier Behavior*' reference.
See Also:
[`get_behavioredClassifierOfClassifierBehavior()`](#get_behavioredClassifierOfClassifierBehavior())
Generated:
getContext
@CheckForNull[BehavioredClassifier](BehavioredClassifier.html) getContext()
Returns the value of the '***Context***' reference.
 It is bidirectional and its opposite is
 '
invalid reference
`*behavior Of Context*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The BehavioredClassifier that is the context for the execution of the Behavior. A Behavior that is directly owned as a nestedClassifier does not have a context.
 Otherwise, to determine the context of a Behavior, find the first BehavioredClassifier reached by following the chain of owner relationships from the Behavior,
 if any. If there is such a BehavioredClassifier, then it is the context, unless it is itself a Behavior with a non-empty context, in which case that is also the
 context for the original Behavior. For example, following this algorithm, the context of an entry Behavior in a StateMachine is the BehavioredClassifier that
 owns the StateMachine. The features of the context BehavioredClassifier as well as the Elements visible to the context Classifier are visible to the Behavior.
 end-model-doc
Returns:
the value of the '*Context*' reference.
See Also:
[`UMLPackage.getBehavior_Context()`](../../metadata/UMLPackage.html#getBehavior_Context())
invalid reference
`com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier#get_behaviorOfContext`
Model:
opposite="_behaviorOfContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isReentrant
boolean isReentrant()
Returns the value of the '***Reentrant***' attribute.
 The default value is `"true"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Tells whether the Behavior can be invoked while it is still executing from a previous invocation.
 end-model-doc
Returns:
the value of the '*Reentrant*' attribute.
See Also:
[`setReentrant(boolean)`](#setReentrant(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getBehavior_Reentrant()`
Model:
default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setReentrant
void setReentrant(boolean value)
Sets the value of the '[`*Reentrant*`](#isReentrant())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Reentrant*' attribute.
See Also:
[`isReentrant()`](#isReentrant())
Generated:
get_decisionNodeOfDecisionInput
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DecisionNode](../../activities/mdintermediateactivities/DecisionNode.html)> get_decisionNodeOfDecisionInput()
Returns the value of the '***decision Node Of Decision Input***' reference list.
 The list contents are of type [`DecisionNode`](../../activities/mdintermediateactivities/DecisionNode.html).
 It is bidirectional and its opposite is
 '[`*Decision Input*`](../../activities/mdintermediateactivities/DecisionNode.html#getDecisionInput())'.
 begin-user-doc 
If the meaning of the '*decision Node Of Decision Input*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*decision Node Of Decision Input*' reference list.
See Also:
[`UMLPackage.getBehavior__decisionNodeOfDecisionInput()`](../../metadata/UMLPackage.html#getBehavior__decisionNodeOfDecisionInput())
[`DecisionNode.getDecisionInput()`](../../activities/mdintermediateactivities/DecisionNode.html#getDecisionInput())
Model:
opposite="decisionInput" ordered="false"
Generated:
get_objectFlowOfTransformation
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)> get_objectFlowOfTransformation()
Returns the value of the '***object Flow Of Transformation***' reference list.
 The list contents are of type [`ObjectFlow`](../../activities/mdbasicactivities/ObjectFlow.html).
 It is bidirectional and its opposite is
 '[`*Transformation*`](../../activities/mdbasicactivities/ObjectFlow.html#getTransformation())'.
 begin-user-doc 
If the meaning of the '*object Flow Of Transformation*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*object Flow Of Transformation*' reference list.
See Also:
[`UMLPackage.getBehavior__objectFlowOfTransformation()`](../../metadata/UMLPackage.html#getBehavior__objectFlowOfTransformation())
[`ObjectFlow.getTransformation()`](../../activities/mdbasicactivities/ObjectFlow.html#getTransformation())
Model:
opposite="transformation" ordered="false"
Generated:
get_objectFlowOfSelection
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)> get_objectFlowOfSelection()
Returns the value of the '***object Flow Of Selection***' reference list.
 The list contents are of type [`ObjectFlow`](../../activities/mdbasicactivities/ObjectFlow.html).
 It is bidirectional and its opposite is '[`*Selection*`](../../activities/mdbasicactivities/ObjectFlow.html#getSelection())'.
 begin-user-doc 
If the meaning of the '*object Flow Of Selection*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*object Flow Of Selection*' reference list.
See Also:
[`UMLPackage.getBehavior__objectFlowOfSelection()`](../../metadata/UMLPackage.html#getBehavior__objectFlowOfSelection())
[`ObjectFlow.getSelection()`](../../activities/mdbasicactivities/ObjectFlow.html#getSelection())
Model:
opposite="selection" ordered="false"
Generated:
getOwnedParameterSet
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)> getOwnedParameterSet()
Returns the value of the '***Owned Parameter Set***' containment reference list.
 The list contents are of type [`ParameterSet`](../../activities/mdcompleteactivities/ParameterSet.html).
 It is bidirectional and its opposite is '[`*behavior Of Owned Parameter Set*`](../../activities/mdcompleteactivities/ParameterSet.html#get_behaviorOfOwnedParameterSet())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterSets owned by this Behavior.
 end-model-doc
Returns:
the value of the '*Owned Parameter Set*' containment reference list.
See Also:
[`UMLPackage.getBehavior_OwnedParameterSet()`](../../metadata/UMLPackage.html#getBehavior_OwnedParameterSet())
[`ParameterSet.get_behaviorOfOwnedParameterSet()`](../../activities/mdcompleteactivities/ParameterSet.html#get_behaviorOfOwnedParameterSet())
Model:
opposite="_behaviorOfOwnedParameterSet" containment="true" resolveProxies="true" ordered="false"
Generated:
get_reduceActionOfReducer
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)> get_reduceActionOfReducer()
Returns the value of the '***reduce Action Of Reducer***' reference list.
 The list contents are of type [`ReduceAction`](../../actions/mdcompleteactions/ReduceAction.html).
 It is bidirectional and its opposite is '[`*Reducer*`](../../actions/mdcompleteactions/ReduceAction.html#getReducer())'.
 begin-user-doc 
If the meaning of the '*reduce Action Of Reducer*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reduce Action Of Reducer*' reference list.
See Also:
[`UMLPackage.getBehavior__reduceActionOfReducer()`](../../metadata/UMLPackage.html#getBehavior__reduceActionOfReducer())
[`ReduceAction.getReducer()`](../../actions/mdcompleteactions/ReduceAction.html#getReducer())
Model:
opposite="reducer" ordered="false"
Generated:
get_behaviorExecutionSpecificationOfBehavior
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[BehaviorExecutionSpecification](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html)> get_behaviorExecutionSpecificationOfBehavior()
Returns the value of the '***behavior Execution Specification Of Behavior***' reference list.
 The list contents are of type [`BehaviorExecutionSpecification`](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html).
 It is bidirectional and its opposite is
 '[`*Behavior*`](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html#getBehavior())'.
 begin-user-doc 
If the meaning of the '*behavior Execution Specification Of Behavior*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behavior Execution Specification Of Behavior*' reference list.
See Also:
[`UMLPackage.getBehavior__behaviorExecutionSpecificationOfBehavior()`](../../metadata/UMLPackage.html#getBehavior__behaviorExecutionSpecificationOfBehavior())
[`BehaviorExecutionSpecification.getBehavior()`](../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html#getBehavior())
Model:
opposite="behavior" ordered="false"
Generated:
get_transitionOfEffect
@CheckForNull[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) get_transitionOfEffect()
Returns the value of the '***transition Of Effect***' container reference.
 It is bidirectional and its opposite is '[`*Effect*`](../../statemachines/mdbehaviorstatemachines/Transition.html#getEffect())'.
 begin-user-doc 
If the meaning of the '*transition Of Effect*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*transition Of Effect*' container reference.
See Also:
[`set_transitionOfEffect(Transition)`](#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))
[`UMLPackage.getBehavior__transitionOfEffect()`](../../metadata/UMLPackage.html#getBehavior__transitionOfEffect())
[`Transition.getEffect()`](../../statemachines/mdbehaviorstatemachines/Transition.html#getEffect())
Model:
opposite="effect" transient="false" ordered="false"
Generated:
set_transitionOfEffect
void set_transitionOfEffect(@CheckForNull
 [Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)
Sets the value of the '[`*transition Of Effect*`](#get_transitionOfEffect())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*transition Of Effect*' container reference.
See Also:
[`get_transitionOfEffect()`](#get_transitionOfEffect())
Generated:
get_stateOfEntry
@CheckForNull[State](../../statemachines/mdbehaviorstatemachines/State.html) get_stateOfEntry()
Returns the value of the '***state Of Entry***' container reference.
 It is bidirectional and its opposite is '[`*Entry*`](../../statemachines/mdbehaviorstatemachines/State.html#getEntry())'.
 begin-user-doc 
If the meaning of the '*state Of Entry*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Of Entry*' container reference.
See Also:
[`set_stateOfEntry(State)`](#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getBehavior__stateOfEntry()`](../../metadata/UMLPackage.html#getBehavior__stateOfEntry())
[`State.getEntry()`](../../statemachines/mdbehaviorstatemachines/State.html#getEntry())
Model:
opposite="entry" transient="false" ordered="false"
Generated:
set_stateOfEntry
void set_stateOfEntry(@CheckForNull
 [State](../../statemachines/mdbehaviorstatemachines/State.html) value)
Sets the value of the '[`*state Of Entry*`](#get_stateOfEntry())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*state Of Entry*' container reference.
See Also:
[`get_stateOfEntry()`](#get_stateOfEntry())
Generated:
get_stateOfExit
@CheckForNull[State](../../statemachines/mdbehaviorstatemachines/State.html) get_stateOfExit()
Returns the value of the '***state Of Exit***' container reference.
 It is bidirectional and its opposite is '[`*Exit*`](../../statemachines/mdbehaviorstatemachines/State.html#getExit())'.
 begin-user-doc 
If the meaning of the '*state Of Exit*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Of Exit*' container reference.
See Also:
[`set_stateOfExit(State)`](#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getBehavior__stateOfExit()`](../../metadata/UMLPackage.html#getBehavior__stateOfExit())
[`State.getExit()`](../../statemachines/mdbehaviorstatemachines/State.html#getExit())
Model:
opposite="exit" transient="false" ordered="false"
Generated:
set_stateOfExit
void set_stateOfExit(@CheckForNull
 [State](../../statemachines/mdbehaviorstatemachines/State.html) value)
Sets the value of the '[`*state Of Exit*`](#get_stateOfExit())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*state Of Exit*' container reference.
See Also:
[`get_stateOfExit()`](#get_stateOfExit())
Generated:
get_stateOfDoActivity
@CheckForNull[State](../../statemachines/mdbehaviorstatemachines/State.html) get_stateOfDoActivity()
Returns the value of the '***state Of Do Activity***' container reference.
 It is bidirectional and its opposite is '[`*Do Activity*`](../../statemachines/mdbehaviorstatemachines/State.html#getDoActivity())'.
 begin-user-doc 
If the meaning of the '*state Of Do Activity*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Of Do Activity*' container reference.
See Also:
[`set_stateOfDoActivity(State)`](#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getBehavior__stateOfDoActivity()`](../../metadata/UMLPackage.html#getBehavior__stateOfDoActivity())
[`State.getDoActivity()`](../../statemachines/mdbehaviorstatemachines/State.html#getDoActivity())
Model:
opposite="doActivity" transient="false" ordered="false"
Generated:
set_stateOfDoActivity
void set_stateOfDoActivity(@CheckForNull
 [State](../../statemachines/mdbehaviorstatemachines/State.html) value)
Sets the value of the '[`*state Of Do Activity*`](#get_stateOfDoActivity())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*state Of Do Activity*' container reference.
See Also:
[`get_stateOfDoActivity()`](#get_stateOfDoActivity())
Generated:
getRedefinedBehavior
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](Behavior.html)> getRedefinedBehavior()
Returns the value of the '***Redefined Behavior***' reference list.
 The list contents are of type [`Behavior`](Behavior.html).
 It is bidirectional and its opposite is
 '[`*behavior Of Redefined Behavior*`](#get_behaviorOfRedefinedBehavior())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Behavior that this Behavior redefines. A subtype of Behavior may redefine any other subtype of Behavior. If the Behavior implements a
 BehavioralFeature, it replaces the redefined Behavior. If the Behavior is a classifierBehavior, it extends the redefined Behavior.
 end-model-doc
Returns:
the value of the '*Redefined Behavior*' reference list.
See Also:
[`UMLPackage.getBehavior_RedefinedBehavior()`](../../metadata/UMLPackage.html#getBehavior_RedefinedBehavior())
[`get_behaviorOfRedefinedBehavior()`](#get_behaviorOfRedefinedBehavior())
Model:
opposite="_behaviorOfRedefinedBehavior" ordered="false"
Generated:
get_behaviorOfRedefinedBehavior
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Behavior](Behavior.html)> get_behaviorOfRedefinedBehavior()
Returns the value of the '***behavior Of Redefined Behavior***' reference list.
 The list contents are of type [`Behavior`](Behavior.html).
 It is bidirectional and its opposite is
 '[`*Redefined Behavior*`](#getRedefinedBehavior())'.
 begin-user-doc 
If the meaning of the '*behavior Of Redefined Behavior*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behavior Of Redefined Behavior*' reference list.
See Also:
[`UMLPackage.getBehavior__behaviorOfRedefinedBehavior()`](../../metadata/UMLPackage.html#getBehavior__behaviorOfRedefinedBehavior())
[`getRedefinedBehavior()`](#getRedefinedBehavior())
Model:
opposite="redefinedBehavior" ordered="false"
Generated:
getSpecification
@CheckForNull[BehavioralFeature](../../classes/mdkernel/BehavioralFeature.html) getSpecification()
Returns the value of the '***Specification***' reference.
 It is bidirectional and its opposite is '[`*Method*`](../../classes/mdkernel/BehavioralFeature.html#getMethod())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Designates a BehavioralFeature that the Behavior implements. The BehavioralFeature must be owned by the BehavioredClassifier that owns the Behavior or be
 inherited by it. The Parameters of the BehavioralFeature and the implementing Behavior must match. A Behavior does not need to have a specification, in which
 case it either is the classifierBehavior of a BehavioredClassifier or it can only be invoked by another Behavior of the Classifier.
 end-model-doc
Returns:
the value of the '*Specification*' reference.
See Also:
[`setSpecification(BehavioralFeature)`](#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))
[`UMLPackage.getBehavior_Specification()`](../../metadata/UMLPackage.html#getBehavior_Specification())
[`BehavioralFeature.getMethod()`](../../classes/mdkernel/BehavioralFeature.html#getMethod())
Model:
opposite="method" ordered="false"
Generated:
setSpecification
void setSpecification(@CheckForNull
 [BehavioralFeature](../../classes/mdkernel/BehavioralFeature.html) value)
Sets the value of the '[`*Specification*`](#getSpecification())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Specification*' reference.
See Also:
[`getSpecification()`](#getSpecification())
Generated:
getOwnedParameter
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Parameter](../../classes/mdkernel/Parameter.html)> getOwnedParameter()
Returns the value of the '***Owned Parameter***' containment reference list.
 The list contents are of type [`Parameter`](../../classes/mdkernel/Parameter.html).
 It is bidirectional and its opposite is
 '[`*behavior Of Owned Parameter*`](../../classes/mdkernel/Parameter.html#get_behaviorOfOwnedParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References a list of Parameters to the Behavior which describes the order and type of arguments that can be given when the Behavior is invoked and of the values
 which will be returned when the Behavior completes its execution.
 end-model-doc
Returns:
the value of the '*Owned Parameter*' containment reference list.
See Also:
[`UMLPackage.getBehavior_OwnedParameter()`](../../metadata/UMLPackage.html#getBehavior_OwnedParameter())
[`Parameter.get_behaviorOfOwnedParameter()`](../../classes/mdkernel/Parameter.html#get_behaviorOfOwnedParameter())
Model:
opposite="_behaviorOfOwnedParameter" containment="true" resolveProxies="true"
Generated:
getPrecondition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)> getPrecondition()
Returns the value of the '***Precondition***' reference list.
 The list contents are of type [`Constraint`](../../classes/mdkernel/Constraint.html).
 It is bidirectional and its opposite is
 '[`*behavior Of Precondition*`](../../classes/mdkernel/Constraint.html#get_behaviorOfPrecondition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional set of Constraints specifying what must be fulfilled before the Behavior is invoked.
 end-model-doc
Returns:
the value of the '*Precondition*' reference list.
See Also:
[`UMLPackage.getBehavior_Precondition()`](../../metadata/UMLPackage.html#getBehavior_Precondition())
[`Constraint.get_behaviorOfPrecondition()`](../../classes/mdkernel/Constraint.html#get_behaviorOfPrecondition())
Model:
opposite="_behaviorOfPrecondition" ordered="false"
Generated:
getPostcondition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)> getPostcondition()
Returns the value of the '***Postcondition***' reference list.
 The list contents are of type [`Constraint`](../../classes/mdkernel/Constraint.html).
 It is bidirectional and its opposite is
 '[`*behavior Of Postcondition*`](../../classes/mdkernel/Constraint.html#get_behaviorOfPostcondition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional set of Constraints specifying what is fulfilled after the execution of the Behavior is completed, if its precondition was fulfilled before its
 invocation.
 end-model-doc
Returns:
the value of the '*Postcondition*' reference list.
See Also:
[`UMLPackage.getBehavior_Postcondition()`](../../metadata/UMLPackage.html#getBehavior_Postcondition())
[`Constraint.get_behaviorOfPostcondition()`](../../classes/mdkernel/Constraint.html#get_behaviorOfPostcondition())
Model:
opposite="_behaviorOfPostcondition" ordered="false"
Generated:
get_callBehaviorActionOfBehavior
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)> get_callBehaviorActionOfBehavior()
Returns the value of the '***call Behavior Action Of Behavior***' reference list.
 The list contents are of type [`CallBehaviorAction`](../../actions/mdbasicactions/CallBehaviorAction.html).
 It is bidirectional and its opposite is '[`*Behavior*`](../../actions/mdbasicactions/CallBehaviorAction.html#getBehavior())'.
 begin-user-doc 
If the meaning of the '*call Behavior Action Of Behavior*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*call Behavior Action Of Behavior*' reference list.
See Also:
[`UMLPackage.getBehavior__callBehaviorActionOfBehavior()`](../../metadata/UMLPackage.html#getBehavior__callBehaviorActionOfBehavior())
[`CallBehaviorAction.getBehavior()`](../../actions/mdbasicactions/CallBehaviorAction.html#getBehavior())
Model:
opposite="behavior" ordered="false"
Generated:
get_connectorOfContract
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](../../compositestructures/mdinternalstructures/Connector.html)> get_connectorOfContract()
Returns the value of the '***connector Of Contract***' reference list.
 The list contents are of type [`Connector`](../../compositestructures/mdinternalstructures/Connector.html).
 It is bidirectional and its opposite is '[`*Contract*`](../../compositestructures/mdinternalstructures/Connector.html#getContract())'.
 begin-user-doc 
If the meaning of the '*connector Of Contract*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*connector Of Contract*' reference list.
See Also:
[`UMLPackage.getBehavior__connectorOfContract()`](../../metadata/UMLPackage.html#getBehavior__connectorOfContract())
[`Connector.getContract()`](../../compositestructures/mdinternalstructures/Connector.html#getContract())
Model:
opposite="contract" ordered="false"
Generated:
get_objectNodeOfSelection
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)> get_objectNodeOfSelection()
Returns the value of the '***object Node Of Selection***' reference list.
 The list contents are of type [`ObjectNode`](../../activities/mdbasicactivities/ObjectNode.html).
 It is bidirectional and its opposite is '[`*Selection*`](../../activities/mdbasicactivities/ObjectNode.html#getSelection())'.
 begin-user-doc 
If the meaning of the '*object Node Of Selection*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*object Node Of Selection*' reference list.
See Also:
[`UMLPackage.getBehavior__objectNodeOfSelection()`](../../metadata/UMLPackage.html#getBehavior__objectNodeOfSelection())
[`ObjectNode.getSelection()`](../../activities/mdbasicactivities/ObjectNode.html#getSelection())
Model:
opposite="selection" ordered="false"
Generated:
get_opaqueExpressionOfBehavior
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[OpaqueExpression](../../classes/mdkernel/OpaqueExpression.html)> get_opaqueExpressionOfBehavior()
Returns the value of the '***opaque Expression Of Behavior***' reference list.
 The list contents are of type [`OpaqueExpression`](../../classes/mdkernel/OpaqueExpression.html).
 It is bidirectional and its opposite is '[`*Behavior*`](../../classes/mdkernel/OpaqueExpression.html#getBehavior())'.
 begin-user-doc 
If the meaning of the '*opaque Expression Of Behavior*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*opaque Expression Of Behavior*' reference list.
See Also:
[`UMLPackage.getBehavior__opaqueExpressionOfBehavior()`](../../metadata/UMLPackage.html#getBehavior__opaqueExpressionOfBehavior())
[`OpaqueExpression.getBehavior()`](../../classes/mdkernel/OpaqueExpression.html#getBehavior())
Model:
opposite="behavior" ordered="false"
Generated:
hasEvent
boolean hasEvent()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasObservation
boolean hasObservation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_decisionNodeOfDecisionInput
boolean has_decisionNodeOfDecisionInput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_objectFlowOfTransformation
boolean has_objectFlowOfTransformation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_objectFlowOfSelection
boolean has_objectFlowOfSelection()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedParameterSet
boolean hasOwnedParameterSet()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_reduceActionOfReducer
boolean has_reduceActionOfReducer()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_behaviorExecutionSpecificationOfBehavior
boolean has_behaviorExecutionSpecificationOfBehavior()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedBehavior
boolean hasRedefinedBehavior()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_behaviorOfRedefinedBehavior
boolean has_behaviorOfRedefinedBehavior()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedParameter
boolean hasOwnedParameter()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPrecondition
boolean hasPrecondition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPostcondition
boolean hasPostcondition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_callBehaviorActionOfBehavior
boolean has_callBehaviorActionOfBehavior()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_connectorOfContract
boolean has_connectorOfContract()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_objectNodeOfSelection
boolean has_objectNodeOfSelection()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_opaqueExpressionOfBehavior
boolean has_opaqueExpressionOfBehavior()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors</a></div>
<h1 class="title" title="Interface Behavior">Interface Behavior</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Behavior</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Behavior</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 Behavior is a specification of how its context BehavioredClassifier changes state over time. This specification may be either a definition of possible behavior
 execution or emergent behavior, or a selective illustration of an interesting subset of possible executions. The latter form is typically used for capturing
 examples, such as a trace of a particular execution.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getContext()"><code><em>Context</em></code></a></li>
<li><a href="#isReentrant()"><code><em>Reentrant</em></code></a></li>
<li><a href="#getOwnedParameter()"><code><em>Owned Parameter</em></code></a></li>
<li><a href="#get_transitionOfEffect()"><code><em>transition Of Effect</em></code></a></li>
<li><a href="#getSpecification()"><code><em>Specification</em></code></a></li>
<li><a href="#getOwnedParameterSet()"><code><em>Owned Parameter Set</em></code></a></li>
<li><a href="#get_connectorOfContract()"><code><em>connector Of Contract</em></code></a></li>
<li><a href="#get_reduceActionOfReducer()"><code><em>reduce Action Of Reducer</em></code></a></li>
<li><a href="#getEvent()"><code><em>Event</em></code></a></li>
<li><a href="#get_opaqueExpressionOfBehavior()"><code><em>opaque Expression Of Behavior</em></code></a></li>
<li><a href="#getPostcondition()"><code><em>Postcondition</em></code></a></li>
<li><a href="#getPrecondition()"><code><em>Precondition</em></code></a></li>
<li><a href="#get_stateOfDoActivity()"><code><em>state Of Do Activity</em></code></a></li>
<li><a href="#get_stateOfEntry()"><code><em>state Of Entry</em></code></a></li>
<li><a href="#get_stateOfExit()"><code><em>state Of Exit</em></code></a></li>
<li><a href="#get_objectNodeOfSelection()"><code><em>object Node Of Selection</em></code></a></li>
<li><a href="#getObservation()"><code><em>Observation</em></code></a></li>
<li><a href="#getRedefinedBehavior()"><code><em>Redefined Behavior</em></code></a></li>
<li><a href="#get_behaviorOfRedefinedBehavior()"><code><em>behavior Of Redefined Behavior</em></code></a></li>
<li><a href="#get_objectFlowOfTransformation()"><code><em>object Flow Of Transformation</em></code></a></li>
<li><a href="#get_objectFlowOfSelection()"><code><em>object Flow Of Selection</em></code></a></li>
<li><a href="#get_decisionNodeOfDecisionInput()"><code><em>decision Node Of Decision Input</em></code></a></li>
<li><a href="#get_behaviorExecutionSpecificationOfBehavior()"><code><em>behavior Execution Specification Of Behavior</em></code></a></li>
<li><a href="#get_behavioredClassifierOfOwnedBehavior()"><code><em>behaviored Classifier Of Owned Behavior</em></code></a></li>
<li><a href="#get_callBehaviorActionOfBehavior()"><code><em>call Behavior Action Of Behavior</em></code></a></li>
<li><a href="#get_behavioredClassifierOfClassifierBehavior()"><code><em>behaviored Classifier Of Classifier Behavior</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getBehavior()"><code>UMLPackage.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='commonbehaviors.mdbasicbehaviors'"</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behavioredClassifierOfClassifierBehavior()">get_behavioredClassifierOfClassifierBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behaviored Classifier Of Classifier Behavior</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behavioredClassifierOfOwnedBehavior()">get_behavioredClassifierOfOwnedBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behaviored Classifier Of Owned Behavior</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behaviorExecutionSpecificationOfBehavior()">get_behaviorExecutionSpecificationOfBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behavior Execution Specification Of Behavior</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behaviorOfRedefinedBehavior()">get_behaviorOfRedefinedBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behavior Of Redefined Behavior</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_callBehaviorActionOfBehavior()">get_callBehaviorActionOfBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>call Behavior Action Of Behavior</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_connectorOfContract()">get_connectorOfContract</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>connector Of Contract</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_decisionNodeOfDecisionInput()">get_decisionNodeOfDecisionInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>decision Node Of Decision Input</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_objectFlowOfSelection()">get_objectFlowOfSelection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>object Flow Of Selection</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_objectFlowOfTransformation()">get_objectFlowOfTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>object Flow Of Transformation</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_objectNodeOfSelection()">get_objectNodeOfSelection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>object Node Of Selection</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_opaqueExpressionOfBehavior()">get_opaqueExpressionOfBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>opaque Expression Of Behavior</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reduceActionOfReducer()">get_reduceActionOfReducer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reduce Action Of Reducer</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateOfDoActivity()">get_stateOfDoActivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Of Do Activity</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateOfEntry()">get_stateOfEntry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Of Entry</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateOfExit()">get_stateOfExit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Of Exit</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_transitionOfEffect()">get_transitionOfEffect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>transition Of Effect</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Context</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEvent()">getEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Event</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getObservation()">getObservation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Observation</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedParameter()">getOwnedParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Parameter</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedParameterSet()">getOwnedParameterSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Parameter Set</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPostcondition()">getPostcondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Postcondition</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrecondition()">getPrecondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Precondition</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedBehavior()">getRedefinedBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Behavior</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpecification()">getSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Specification</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_behaviorExecutionSpecificationOfBehavior()">has_behaviorExecutionSpecificationOfBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_behaviorOfRedefinedBehavior()">has_behaviorOfRedefinedBehavior</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_callBehaviorActionOfBehavior()">has_callBehaviorActionOfBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_connectorOfContract()">has_connectorOfContract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_decisionNodeOfDecisionInput()">has_decisionNodeOfDecisionInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_objectFlowOfSelection()">has_objectFlowOfSelection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_objectFlowOfTransformation()">has_objectFlowOfTransformation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_objectNodeOfSelection()">has_objectNodeOfSelection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_opaqueExpressionOfBehavior()">has_opaqueExpressionOfBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_reduceActionOfReducer()">has_reduceActionOfReducer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEvent()">hasEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasObservation()">hasObservation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedParameter()">hasOwnedParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedParameterSet()">hasOwnedParameterSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPostcondition()">hasPostcondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPrecondition()">hasPrecondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedBehavior()">hasRedefinedBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReentrant()">isReentrant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Reentrant</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">set_behavioredClassifierOfClassifierBehavior</a><wbr/>(<a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_behavioredClassifierOfClassifierBehavior()"><code><em>behaviored Classifier Of Classifier Behavior</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">set_behavioredClassifierOfOwnedBehavior</a><wbr/>(<a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_behavioredClassifierOfOwnedBehavior()"><code><em>behaviored
 Classifier Of Owned Behavior</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfDoActivity</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_stateOfDoActivity()"><code><em>state Of Do Activity</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfEntry</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_stateOfEntry()"><code><em>state Of Entry</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfExit</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_stateOfExit()"><code><em>state Of Exit</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">set_transitionOfEffect</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_transitionOfEffect()"><code><em>transition Of Effect</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReentrant(boolean)">setReentrant</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isReentrant()"><code><em>Reentrant</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">setSpecification</a><wbr/>(<a href="../../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSpecification()"><code><em>Specification</em></code></a>' reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.<a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></h3>
<code><a href="BehavioredClassifier.html#getClassifierBehavior()">getClassifierBehavior</a>, <a href="BehavioredClassifier.html#getInterfaceRealization()">getInterfaceRealization</a>, <a href="BehavioredClassifier.html#getOwnedBehavior()">getOwnedBehavior</a>, <a href="BehavioredClassifier.html#hasInterfaceRealization()">hasInterfaceRealization</a>, <a href="BehavioredClassifier.html#hasOwnedBehavior()">hasOwnedBehavior</a>, <a href="BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setClassifierBehavior</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></h3>
<code><a href="../../classes/mdkernel/Class.html#getExtension()">getExtension</a>, <a href="../../classes/mdkernel/Class.html#getNestedClassifier()">getNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#getOwnedAttribute()">getOwnedAttribute</a>, <a href="../../classes/mdkernel/Class.html#getOwnedOperation()">getOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#getOwnedReception()">getOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#getSuperClass()">getSuperClass</a>, <a href="../../classes/mdkernel/Class.html#hasExtension()">hasExtension</a>, <a href="../../classes/mdkernel/Class.html#hasNestedClassifier()">hasNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedOperation()">hasOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedReception()">hasOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#hasSuperClass()">hasSuperClass</a>, <a href="../../classes/mdkernel/Class.html#isAbstract()">isAbstract</a>, <a href="../../classes/mdkernel/Class.html#isActive()">isActive</a>, <a href="../../classes/mdkernel/Class.html#setAbstract(boolean)">setAbstract</a>, <a href="../../classes/mdkernel/Class.html#setActive(boolean)">setActive</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#getAttribute()">getAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#getFeature()">getFeature</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneral()">getGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneralization()">getGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#getRepresentation()">getRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#getSubstitution()">getSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#getUMLClass()">getUMLClass</a>, <a href="../../classes/mdkernel/Classifier.html#getUseCase()">getUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#hasAttribute()">hasAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#hasFeature()">hasFeature</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneral()">hasGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#hasUseCase()">hasUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.<a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></h3>
<code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html#getOwnedPort()">getOwnedPort</a>, <a href="../../compositestructures/mdports/EncapsulatedClassifier.html#hasOwnedPort()">hasOwnedPort</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.StructuredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.<a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></h3>
<code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getOwnedConnector()">getOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getPart()">getPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#getRole()">getRole</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedAttribute()">hasOwnedAttribute</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasOwnedConnector()">hasOwnedConnector</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasPart()">hasPart</a>, <a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html#hasRole()">hasRole</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()">getTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()">hasTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">setOwnedTemplateSignature</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></h3>
<code><a href="../../classes/mdkernel/Type.html#get_associationOfEndType()">get_associationOfEndType</a>, <a href="../../classes/mdkernel/Type.html#get_behavioralFeatureOfRaisedException()">get_behavioralFeatureOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#get_operationOfRaisedException()">get_operationOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#get_typedElementOfType()">get_typedElementOfType</a>, <a href="../../classes/mdkernel/Type.html#getPackage()">getPackage</a>, <a href="../../classes/mdkernel/Type.html#has_associationOfEndType()">has_associationOfEndType</a>, <a href="../../classes/mdkernel/Type.html#has_behavioralFeatureOfRaisedException()">has_behavioralFeatureOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#has_operationOfRaisedException()">has_operationOfRaisedException</a>, <a href="../../classes/mdkernel/Type.html#has_typedElementOfType()">has_typedElementOfType</a>, <a href="../../classes/mdkernel/Type.html#setPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setPackage</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getEvent()">
<h3>getEvent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a>&gt;</span> <span class="element-name">getEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>Event</b></em>' containment reference list.
 The list contents are of type <a href="../mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Event</code></a>.
 It is bidirectional and its opposite is '<a href="../mdcommunications/Event.html#getBehavior()"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Event</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Event</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getBehavior_Event()"><code>UMLPackage.getBehavior_Event()</code></a></li>
<li><a href="../mdcommunications/Event.html#getBehavior()"><code>Event.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="behavior" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObservation()">
<h3>getObservation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a>&gt;</span> <span class="element-name">getObservation</span>()</div>
<div class="block">Returns the value of the '<em><b>Observation</b></em>' containment reference list.
 The list contents are of type <a href="../mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Observation</code></a>.
 It is bidirectional and its opposite is '<a href="../mdsimpletime/Observation.html#getBehavior()"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Observation</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Observation</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_Observation()"><code>UMLPackage.getBehavior_Observation()</code></a></li>
<li><a href="../mdsimpletime/Observation.html#getBehavior()"><code>Observation.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="behavior" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behavioredClassifierOfOwnedBehavior()">
<h3>get_behavioredClassifierOfOwnedBehavior</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span> <span class="element-name">get_behavioredClassifierOfOwnedBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>behaviored Classifier Of Owned Behavior</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="BehavioredClassifier.html#getOwnedBehavior()"><code><em>Owned Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behaviored Classifier Of Owned Behavior</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behaviored Classifier Of Owned Behavior</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)"><code>set_behavioredClassifierOfOwnedBehavior(BehavioredClassifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__behavioredClassifierOfOwnedBehavior()"><code>UMLPackage.getBehavior__behavioredClassifierOfOwnedBehavior()</code></a></li>
<li><a href="BehavioredClassifier.html#getOwnedBehavior()"><code>BehavioredClassifier.getOwnedBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedBehavior" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>set_behavioredClassifierOfOwnedBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_behavioredClassifierOfOwnedBehavior</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_behavioredClassifierOfOwnedBehavior()"><code><em>behaviored
 Classifier Of Owned Behavior</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>behaviored Classifier Of Owned Behavior</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_behavioredClassifierOfOwnedBehavior()"><code>get_behavioredClassifierOfOwnedBehavior()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behavioredClassifierOfClassifierBehavior()">
<h3>get_behavioredClassifierOfClassifierBehavior</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span> <span class="element-name">get_behavioredClassifierOfClassifierBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>behaviored Classifier Of Classifier Behavior</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="BehavioredClassifier.html#getClassifierBehavior()"><code><em>Classifier Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behaviored Classifier Of Classifier Behavior</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behaviored Classifier Of Classifier Behavior</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)"><code>set_behavioredClassifierOfClassifierBehavior(BehavioredClassifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__behavioredClassifierOfClassifierBehavior()"><code>UMLPackage.getBehavior__behavioredClassifierOfClassifierBehavior()</code></a></li>
<li><a href="BehavioredClassifier.html#getClassifierBehavior()"><code>BehavioredClassifier.getClassifierBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="classifierBehavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">
<h3>set_behavioredClassifierOfClassifierBehavior</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_behavioredClassifierOfClassifierBehavior</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_behavioredClassifierOfClassifierBehavior()"><code><em>behaviored Classifier Of Classifier Behavior</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>behaviored Classifier Of Classifier Behavior</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_behavioredClassifierOfClassifierBehavior()"><code>get_behavioredClassifierOfClassifierBehavior()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Context</b></em>' reference.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>behavior Of Context</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The BehavioredClassifier that is the context for the execution of the Behavior. A Behavior that is directly owned as a nestedClassifier does not have a context.
 Otherwise, to determine the context of a Behavior, find the first BehavioredClassifier reached by following the chain of owner relationships from the Behavior,
 if any. If there is such a BehavioredClassifier, then it is the context, unless it is itself a Behavior with a non-empty context, in which case that is also the
 context for the original Behavior. For example, following this algorithm, the context of an entry Behavior in a StateMachine is the BehavioredClassifier that
 owns the StateMachine. The features of the context BehavioredClassifier as well as the Elements visible to the context Classifier are visible to the Behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_Context()"><code>UMLPackage.getBehavior_Context()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier#get_behaviorOfContext</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReentrant()">
<h3>isReentrant</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReentrant</span>()</div>
<div class="block">Returns the value of the '<em><b>Reentrant</b></em>' attribute.
 The default value is <code>"true"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Tells whether the Behavior can be invoked while it is still executing from a previous invocation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Reentrant</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setReentrant(boolean)"><code>setReentrant(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getBehavior_Reentrant()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="true" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReentrant(boolean)">
<h3>setReentrant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReentrant</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isReentrant()"><code><em>Reentrant</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Reentrant</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isReentrant()"><code>isReentrant()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_decisionNodeOfDecisionInput()">
<h3>get_decisionNodeOfDecisionInput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a>&gt;</span> <span class="element-name">get_decisionNodeOfDecisionInput</span>()</div>
<div class="block">Returns the value of the '<em><b>decision Node Of Decision Input</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>DecisionNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdintermediateactivities/DecisionNode.html#getDecisionInput()"><code><em>Decision Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>decision Node Of Decision Input</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>decision Node Of Decision Input</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__decisionNodeOfDecisionInput()"><code>UMLPackage.getBehavior__decisionNodeOfDecisionInput()</code></a></li>
<li><a href="../../activities/mdintermediateactivities/DecisionNode.html#getDecisionInput()"><code>DecisionNode.getDecisionInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="decisionInput" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_objectFlowOfTransformation()">
<h3>get_objectFlowOfTransformation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a>&gt;</span> <span class="element-name">get_objectFlowOfTransformation</span>()</div>
<div class="block">Returns the value of the '<em><b>object Flow Of Transformation</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdbasicactivities/ObjectFlow.html#getTransformation()"><code><em>Transformation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>object Flow Of Transformation</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>object Flow Of Transformation</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__objectFlowOfTransformation()"><code>UMLPackage.getBehavior__objectFlowOfTransformation()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ObjectFlow.html#getTransformation()"><code>ObjectFlow.getTransformation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="transformation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_objectFlowOfSelection()">
<h3>get_objectFlowOfSelection</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a>&gt;</span> <span class="element-name">get_objectFlowOfSelection</span>()</div>
<div class="block">Returns the value of the '<em><b>object Flow Of Selection</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectFlow</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ObjectFlow.html#getSelection()"><code><em>Selection</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>object Flow Of Selection</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>object Flow Of Selection</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__objectFlowOfSelection()"><code>UMLPackage.getBehavior__objectFlowOfSelection()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ObjectFlow.html#getSelection()"><code>ObjectFlow.getSelection()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="selection" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedParameterSet()">
<h3>getOwnedParameterSet</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a>&gt;</span> <span class="element-name">getOwnedParameterSet</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Parameter Set</b></em>' containment reference list.
 The list contents are of type <a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ParameterSet</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdcompleteactivities/ParameterSet.html#get_behaviorOfOwnedParameterSet()"><code><em>behavior Of Owned Parameter Set</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterSets owned by this Behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Parameter Set</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_OwnedParameterSet()"><code>UMLPackage.getBehavior_OwnedParameterSet()</code></a></li>
<li><a href="../../activities/mdcompleteactivities/ParameterSet.html#get_behaviorOfOwnedParameterSet()"><code>ParameterSet.get_behaviorOfOwnedParameterSet()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfOwnedParameterSet" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reduceActionOfReducer()">
<h3>get_reduceActionOfReducer</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a>&gt;</span> <span class="element-name">get_reduceActionOfReducer</span>()</div>
<div class="block">Returns the value of the '<em><b>reduce Action Of Reducer</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReduceAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/ReduceAction.html#getReducer()"><code><em>Reducer</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reduce Action Of Reducer</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reduce Action Of Reducer</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__reduceActionOfReducer()"><code>UMLPackage.getBehavior__reduceActionOfReducer()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReduceAction.html#getReducer()"><code>ReduceAction.getReducer()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="reducer" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behaviorExecutionSpecificationOfBehavior()">
<h3>get_behaviorExecutionSpecificationOfBehavior</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">BehaviorExecutionSpecification</a>&gt;</span> <span class="element-name">get_behaviorExecutionSpecificationOfBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>behavior Execution Specification Of Behavior</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>BehaviorExecutionSpecification</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html#getBehavior()"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behavior Execution Specification Of Behavior</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behavior Execution Specification Of Behavior</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__behaviorExecutionSpecificationOfBehavior()"><code>UMLPackage.getBehavior__behaviorExecutionSpecificationOfBehavior()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/BehaviorExecutionSpecification.html#getBehavior()"><code>BehaviorExecutionSpecification.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="behavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_transitionOfEffect()">
<h3>get_transitionOfEffect</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">get_transitionOfEffect</span>()</div>
<div class="block">Returns the value of the '<em><b>transition Of Effect</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getEffect()"><code><em>Effect</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>transition Of Effect</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>transition Of Effect</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)"><code>set_transitionOfEffect(Transition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__transitionOfEffect()"><code>UMLPackage.getBehavior__transitionOfEffect()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getEffect()"><code>Transition.getEffect()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="effect" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>set_transitionOfEffect</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_transitionOfEffect</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_transitionOfEffect()"><code><em>transition Of Effect</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>transition Of Effect</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_transitionOfEffect()"><code>get_transitionOfEffect()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateOfEntry()">
<h3>get_stateOfEntry</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">get_stateOfEntry</span>()</div>
<div class="block">Returns the value of the '<em><b>state Of Entry</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/State.html#getEntry()"><code><em>Entry</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Of Entry</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Of Entry</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>set_stateOfEntry(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__stateOfEntry()"><code>UMLPackage.getBehavior__stateOfEntry()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#getEntry()"><code>State.getEntry()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="entry" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>set_stateOfEntry</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stateOfEntry</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_stateOfEntry()"><code><em>state Of Entry</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>state Of Entry</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_stateOfEntry()"><code>get_stateOfEntry()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateOfExit()">
<h3>get_stateOfExit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">get_stateOfExit</span>()</div>
<div class="block">Returns the value of the '<em><b>state Of Exit</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/State.html#getExit()"><code><em>Exit</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Of Exit</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Of Exit</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>set_stateOfExit(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__stateOfExit()"><code>UMLPackage.getBehavior__stateOfExit()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#getExit()"><code>State.getExit()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="exit" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>set_stateOfExit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stateOfExit</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_stateOfExit()"><code><em>state Of Exit</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>state Of Exit</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_stateOfExit()"><code>get_stateOfExit()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateOfDoActivity()">
<h3>get_stateOfDoActivity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">get_stateOfDoActivity</span>()</div>
<div class="block">Returns the value of the '<em><b>state Of Do Activity</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/State.html#getDoActivity()"><code><em>Do Activity</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Of Do Activity</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Of Do Activity</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>set_stateOfDoActivity(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior__stateOfDoActivity()"><code>UMLPackage.getBehavior__stateOfDoActivity()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#getDoActivity()"><code>State.getDoActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="doActivity" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>set_stateOfDoActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stateOfDoActivity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_stateOfDoActivity()"><code><em>state Of Do Activity</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>state Of Do Activity</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_stateOfDoActivity()"><code>get_stateOfDoActivity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedBehavior()">
<h3>getRedefinedBehavior</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</span> <span class="element-name">getRedefinedBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Behavior</b></em>' reference list.
 The list contents are of type <a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_behaviorOfRedefinedBehavior()"><code><em>behavior Of Redefined Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Behavior that this Behavior redefines. A subtype of Behavior may redefine any other subtype of Behavior. If the Behavior implements a
 BehavioralFeature, it replaces the redefined Behavior. If the Behavior is a classifierBehavior, it extends the redefined Behavior.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Behavior</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_RedefinedBehavior()"><code>UMLPackage.getBehavior_RedefinedBehavior()</code></a></li>
<li><a href="#get_behaviorOfRedefinedBehavior()"><code>get_behaviorOfRedefinedBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfRedefinedBehavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behaviorOfRedefinedBehavior()">
<h3>get_behaviorOfRedefinedBehavior</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a>&gt;</span> <span class="element-name">get_behaviorOfRedefinedBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>behavior Of Redefined Behavior</b></em>' reference list.
 The list contents are of type <a href="Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedBehavior()"><code><em>Redefined Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behavior Of Redefined Behavior</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behavior Of Redefined Behavior</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__behaviorOfRedefinedBehavior()"><code>UMLPackage.getBehavior__behaviorOfRedefinedBehavior()</code></a></li>
<li><a href="#getRedefinedBehavior()"><code>getRedefinedBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedBehavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecification()">
<h3>getSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></span> <span class="element-name">getSpecification</span>()</div>
<div class="block">Returns the value of the '<em><b>Specification</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/BehavioralFeature.html#getMethod()"><code><em>Method</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Designates a BehavioralFeature that the Behavior implements. The BehavioralFeature must be owned by the BehavioredClassifier that owns the Behavior or be
 inherited by it. The Parameters of the BehavioralFeature and the implementing Behavior must match. A Behavior does not need to have a specification, in which
 case it either is the classifierBehavior of a BehavioredClassifier or it can only be invoked by another Behavior of the Classifier.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Specification</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)"><code>setSpecification(BehavioralFeature)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getBehavior_Specification()"><code>UMLPackage.getBehavior_Specification()</code></a></li>
<li><a href="../../classes/mdkernel/BehavioralFeature.html#getMethod()"><code>BehavioralFeature.getMethod()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="method" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">
<h3>setSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSpecification()"><code><em>Specification</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Specification</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSpecification()"><code>getSpecification()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedParameter()">
<h3>getOwnedParameter</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</span> <span class="element-name">getOwnedParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Parameter</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Parameter.html#get_behaviorOfOwnedParameter()"><code><em>behavior Of Owned Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References a list of Parameters to the Behavior which describes the order and type of arguments that can be given when the Behavior is invoked and of the values
 which will be returned when the Behavior completes its execution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Parameter</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_OwnedParameter()"><code>UMLPackage.getBehavior_OwnedParameter()</code></a></li>
<li><a href="../../classes/mdkernel/Parameter.html#get_behaviorOfOwnedParameter()"><code>Parameter.get_behaviorOfOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfOwnedParameter" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrecondition()">
<h3>getPrecondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getPrecondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Precondition</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Constraint.html#get_behaviorOfPrecondition()"><code><em>behavior Of Precondition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional set of Constraints specifying what must be fulfilled before the Behavior is invoked.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Precondition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_Precondition()"><code>UMLPackage.getBehavior_Precondition()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_behaviorOfPrecondition()"><code>Constraint.get_behaviorOfPrecondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfPrecondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostcondition()">
<h3>getPostcondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getPostcondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Postcondition</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Constraint.html#get_behaviorOfPostcondition()"><code><em>behavior Of Postcondition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional set of Constraints specifying what is fulfilled after the execution of the Behavior is completed, if its precondition was fulfilled before its
 invocation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Postcondition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior_Postcondition()"><code>UMLPackage.getBehavior_Postcondition()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_behaviorOfPostcondition()"><code>Constraint.get_behaviorOfPostcondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_behaviorOfPostcondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_callBehaviorActionOfBehavior()">
<h3>get_callBehaviorActionOfBehavior</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a>&gt;</span> <span class="element-name">get_callBehaviorActionOfBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>call Behavior Action Of Behavior</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallBehaviorAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/CallBehaviorAction.html#getBehavior()"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>call Behavior Action Of Behavior</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>call Behavior Action Of Behavior</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__callBehaviorActionOfBehavior()"><code>UMLPackage.getBehavior__callBehaviorActionOfBehavior()</code></a></li>
<li><a href="../../actions/mdbasicactions/CallBehaviorAction.html#getBehavior()"><code>CallBehaviorAction.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="behavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_connectorOfContract()">
<h3>get_connectorOfContract</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a>&gt;</span> <span class="element-name">get_connectorOfContract</span>()</div>
<div class="block">Returns the value of the '<em><b>connector Of Contract</b></em>' reference list.
 The list contents are of type <a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures"><code>Connector</code></a>.
 It is bidirectional and its opposite is '<a href="../../compositestructures/mdinternalstructures/Connector.html#getContract()"><code><em>Contract</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>connector Of Contract</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>connector Of Contract</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__connectorOfContract()"><code>UMLPackage.getBehavior__connectorOfContract()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/Connector.html#getContract()"><code>Connector.getContract()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="contract" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_objectNodeOfSelection()">
<h3>get_objectNodeOfSelection</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a>&gt;</span> <span class="element-name">get_objectNodeOfSelection</span>()</div>
<div class="block">Returns the value of the '<em><b>object Node Of Selection</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ObjectNode.html#getSelection()"><code><em>Selection</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>object Node Of Selection</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>object Node Of Selection</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__objectNodeOfSelection()"><code>UMLPackage.getBehavior__objectNodeOfSelection()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ObjectNode.html#getSelection()"><code>ObjectNode.getSelection()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="selection" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_opaqueExpressionOfBehavior()">
<h3>get_opaqueExpressionOfBehavior</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a>&gt;</span> <span class="element-name">get_opaqueExpressionOfBehavior</span>()</div>
<div class="block">Returns the value of the '<em><b>opaque Expression Of Behavior</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>OpaqueExpression</code></a>.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/OpaqueExpression.html#getBehavior()"><code><em>Behavior</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>opaque Expression Of Behavior</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>opaque Expression Of Behavior</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getBehavior__opaqueExpressionOfBehavior()"><code>UMLPackage.getBehavior__opaqueExpressionOfBehavior()</code></a></li>
<li><a href="../../classes/mdkernel/OpaqueExpression.html#getBehavior()"><code>OpaqueExpression.getBehavior()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="behavior" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasEvent()">
<h3>hasEvent</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasEvent</span>()
          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasObservation()">
<h3>hasObservation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasObservation</span>()
                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_decisionNodeOfDecisionInput()">
<h3>has_decisionNodeOfDecisionInput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_decisionNodeOfDecisionInput</span>()
                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_objectFlowOfTransformation()">
<h3>has_objectFlowOfTransformation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_objectFlowOfTransformation</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_objectFlowOfSelection()">
<h3>has_objectFlowOfSelection</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_objectFlowOfSelection</span>()
                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedParameterSet()">
<h3>hasOwnedParameterSet</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedParameterSet</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_reduceActionOfReducer()">
<h3>has_reduceActionOfReducer</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_reduceActionOfReducer</span>()
                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_behaviorExecutionSpecificationOfBehavior()">
<h3>has_behaviorExecutionSpecificationOfBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_behaviorExecutionSpecificationOfBehavior</span>()
                                              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedBehavior()">
<h3>hasRedefinedBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedBehavior</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_behaviorOfRedefinedBehavior()">
<h3>has_behaviorOfRedefinedBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_behaviorOfRedefinedBehavior</span>()
                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedParameter()">
<h3>hasOwnedParameter</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedParameter</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPrecondition()">
<h3>hasPrecondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPrecondition</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPostcondition()">
<h3>hasPostcondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPostcondition</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_callBehaviorActionOfBehavior()">
<h3>has_callBehaviorActionOfBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_callBehaviorActionOfBehavior</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_connectorOfContract()">
<h3>has_connectorOfContract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_connectorOfContract</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_objectNodeOfSelection()">
<h3>has_objectNodeOfSelection</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_objectNodeOfSelection</span>()
                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_opaqueExpressionOfBehavior()">
<h3>has_opaqueExpressionOfBehavior</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_opaqueExpressionOfBehavior</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
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
