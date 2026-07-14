# JAVA OPENAPI: Activity (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html`
- source_sha256: `631c4c0d0d0e80cfd35f9baebee58bed609a4ee26ee5159ce980ad7e840e6d0b`
- captured_utc: `2026-07-14T16:56:14.042666+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities](package-summary.html)

## Interface Activity

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[Class](../../classes/mdkernel/Class.html)`, `[Classifier](../../classes/mdkernel/Classifier.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`, `[Type](../../classes/mdkernel/Type.html)`

public interfaceActivityextends [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)

begin-user-doc 
 A representation of the model object '***Activity***'.
 end-user-doc 
begin-model-doc 
 An Activity is the specification of parameterized Behavior as the coordinated sequencing of subordinate units.
 end-model-doc 
The following features are supported:
 [`*Edge*`](#getEdge())
[`*Group*`](#getGroup())
[`*Partition*`](#getPartition())
[`*Structured Node*`](#getStructuredNode())
[`*Read Only*`](#isReadOnly())
[`*Single Execution*`](#isSingleExecution())
[`*Variable*`](#getVariable())
[`*Node*`](#getNode())

See Also:
[`UMLPackage.getActivity()`](../../metadata/UMLPackage.html#getActivity())
Model:
annotation="MOF package='activities.mdfundamentalactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)>`
`[getEdge](#getEdge())()`
Returns the value of the '***Edge***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityGroup](ActivityGroup.html)>`
`[getGroup](#getGroup())()`
Returns the value of the '***Group***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityNode](ActivityNode.html)>`
`[getNode](#getNode())()`
Returns the value of the '***Node***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../mdintermediateactivities/ActivityPartition.html)>`
`[getPartition](#getPartition())()`
Returns the value of the '***Partition***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html)>`
`[getStructuredNode](#getStructuredNode())()`
Returns the value of the '***Structured Node***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Variable](../mdstructuredactivities/Variable.html)>`
`[getVariable](#getVariable())()`
Returns the value of the '***Variable***' containment reference list.
`boolean`
`[hasEdge](#hasEdge())()`

`boolean`
`[hasGroup](#hasGroup())()`

`boolean`
`[hasNode](#hasNode())()`

`boolean`
`[hasPartition](#hasPartition())()`

`boolean`
`[hasStructuredNode](#hasStructuredNode())()`

`boolean`
`[hasVariable](#hasVariable())()`

`boolean`
`[isReadOnly](#isReadOnly())()`
Returns the value of the '***Read Only***' attribute.
`boolean`
`[isSingleExecution](#isSingleExecution())()`
Returns the value of the '***Single Execution***' attribute.
`void`
`[setReadOnly](#setReadOnly(boolean))(boolean value)`
Sets the value of the '[`*Read Only*`](#isReadOnly())' attribute.
`void`
`[setSingleExecution](#setSingleExecution(boolean))(boolean value)`
Sets the value of the '[`*Single Execution*`](#isSingleExecution())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)
`[get_behavioredClassifierOfClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behavioredClassifierOfClassifierBehavior()), [get_behavioredClassifierOfOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behavioredClassifierOfOwnedBehavior()), [get_behaviorExecutionSpecificationOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behaviorExecutionSpecificationOfBehavior()), [get_behaviorOfRedefinedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behaviorOfRedefinedBehavior()), [get_callBehaviorActionOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_callBehaviorActionOfBehavior()), [get_connectorOfContract](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract()), [get_decisionNodeOfDecisionInput](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_decisionNodeOfDecisionInput()), [get_objectFlowOfSelection](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectFlowOfSelection()), [get_objectFlowOfTransformation](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectFlowOfTransformation()), [get_objectNodeOfSelection](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection()), [get_opaqueExpressionOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_opaqueExpressionOfBehavior()), [get_reduceActionOfReducer](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_reduceActionOfReducer()), [get_stateOfDoActivity](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity()), [get_stateOfEntry](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry()), [get_stateOfExit](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit()), [get_transitionOfEffect](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect()), [getContext](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getContext()), [getEvent](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getEvent()), [getObservation](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getObservation()), [getOwnedParameter](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter()), [getOwnedParameterSet](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameterSet()), [getPostcondition](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition()), [getPrecondition](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition()), [getRedefinedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getRedefinedBehavior()), [getSpecification](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getSpecification()), [has_behaviorExecutionSpecificationOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_behaviorExecutionSpecificationOfBehavior()), [has_behaviorOfRedefinedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_behaviorOfRedefinedBehavior()), [has_callBehaviorActionOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_callBehaviorActionOfBehavior()), [has_connectorOfContract](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_connectorOfContract()), [has_decisionNodeOfDecisionInput](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_decisionNodeOfDecisionInput()), [has_objectFlowOfSelection](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectFlowOfSelection()), [has_objectFlowOfTransformation](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectFlowOfTransformation()), [has_objectNodeOfSelection](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectNodeOfSelection()), [has_opaqueExpressionOfBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_opaqueExpressionOfBehavior()), [has_reduceActionOfReducer](../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_reduceActionOfReducer()), [hasEvent](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasEvent()), [hasObservation](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasObservation()), [hasOwnedParameter](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasOwnedParameter()), [hasOwnedParameterSet](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasOwnedParameterSet()), [hasPostcondition](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasPostcondition()), [hasPrecondition](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasPrecondition()), [hasRedefinedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasRedefinedBehavior()), [isReentrant](../../commonbehaviors/mdbasicbehaviors/Behavior.html#isReentrant()), [set_behavioredClassifierOfClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)), [set_behavioredClassifierOfOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)), [set_stateOfDoActivity](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)), [set_stateOfEntry](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)), [set_stateOfExit](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)), [set_transitionOfEffect](../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)), [setReentrant](../../commonbehaviors/mdbasicbehaviors/Behavior.html#setReentrant(boolean)), [setSpecification](../../commonbehaviors/mdbasicbehaviors/Behavior.html#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)
`[getClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getClassifierBehavior()), [getInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()), [getOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getOwnedBehavior()), [hasInterfaceRealization](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasInterfaceRealization()), [hasOwnedBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasOwnedBehavior()), [setClassifierBehavior](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Class](../../classes/mdkernel/Class.html)
`[getExtension](../../classes/mdkernel/Class.html#getExtension()), [getNestedClassifier](../../classes/mdkernel/Class.html#getNestedClassifier()), [getOwnedAttribute](../../classes/mdkernel/Class.html#getOwnedAttribute()), [getOwnedOperation](../../classes/mdkernel/Class.html#getOwnedOperation()), [getOwnedReception](../../classes/mdkernel/Class.html#getOwnedReception()), [getSuperClass](../../classes/mdkernel/Class.html#getSuperClass()), [hasExtension](../../classes/mdkernel/Class.html#hasExtension()), [hasNestedClassifier](../../classes/mdkernel/Class.html#hasNestedClassifier()), [hasOwnedOperation](../../classes/mdkernel/Class.html#hasOwnedOperation()), [hasOwnedReception](../../classes/mdkernel/Class.html#hasOwnedReception()), [hasSuperClass](../../classes/mdkernel/Class.html#hasSuperClass()), [isAbstract](../../classes/mdkernel/Class.html#isAbstract()), [isActive](../../classes/mdkernel/Class.html#isActive()), [setAbstract](../../classes/mdkernel/Class.html#setAbstract(boolean)), [setActive](../../classes/mdkernel/Class.html#setActive(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Classifier](../../classes/mdkernel/Classifier.html)
`[get_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()), [get_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()), [get_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()), [get_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()), [get_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()), [get_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()), [get_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()), [get_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()), [get_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()), [get_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()), [get_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()), [get_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()), [get_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()), [get_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()), [get_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()), [get_substitutionOfContract](../../classes/mdkernel/Classifier.html#get_substitutionOfContract()), [get_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()), [getAttribute](../../classes/mdkernel/Classifier.html#getAttribute()), [getCollaborationUse](../../classes/mdkernel/Classifier.html#getCollaborationUse()), [getFeature](../../classes/mdkernel/Classifier.html#getFeature()), [getGeneral](../../classes/mdkernel/Classifier.html#getGeneral()), [getGeneralization](../../classes/mdkernel/Classifier.html#getGeneralization()), [getInheritedMember](../../classes/mdkernel/Classifier.html#getInheritedMember()), [getOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()), [getOwnedUseCase](../../classes/mdkernel/Classifier.html#getOwnedUseCase()), [getPowertypeExtent](../../classes/mdkernel/Classifier.html#getPowertypeExtent()), [getRedefinedClassifier](../../classes/mdkernel/Classifier.html#getRedefinedClassifier()), [getRepresentation](../../classes/mdkernel/Classifier.html#getRepresentation()), [getSubstitution](../../classes/mdkernel/Classifier.html#getSubstitution()), [getTemplateParameter](../../classes/mdkernel/Classifier.html#getTemplateParameter()), [getUMLClass](../../classes/mdkernel/Classifier.html#getUMLClass()), [getUseCase](../../classes/mdkernel/Classifier.html#getUseCase()), [has_classifierOfRedefinedClassifier](../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()), [has_classifierTemplateParameterOfConstrainingClassifier](../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()), [has_componentRealizationOfRealizingClassifier](../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()), [has_createObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()), [has_exceptionHandlerOfExceptionType](../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()), [has_generalizationOfGeneral](../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()), [has_informationFlowOfConveyed](../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()), [has_informationItemOfRepresented](../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()), [has_instanceSpecificationOfClassifier](../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()), [has_readExtentActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()), [has_readIsClassifiedObjectActionOfClassifier](../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()), [has_reclassifyObjectActionOfNewClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()), [has_reclassifyObjectActionOfOldClassifier](../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()), [has_redefinableElementOfRedefinitionContext](../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()), [has_substitutionOfContract](../../classes/mdkernel/Classifier.html#has_substitutionOfContract()), [has_unmarshallActionOfUnmarshallType](../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()), [hasAttribute](../../classes/mdkernel/Classifier.html#hasAttribute()), [hasCollaborationUse](../../classes/mdkernel/Classifier.html#hasCollaborationUse()), [hasFeature](../../classes/mdkernel/Classifier.html#hasFeature()), [hasGeneral](../../classes/mdkernel/Classifier.html#hasGeneral()), [hasGeneralization](../../classes/mdkernel/Classifier.html#hasGeneralization()), [hasInheritedMember](../../classes/mdkernel/Classifier.html#hasInheritedMember()), [hasOwnedUseCase](../../classes/mdkernel/Classifier.html#hasOwnedUseCase()), [hasPowertypeExtent](../../classes/mdkernel/Classifier.html#hasPowertypeExtent()), [hasRedefinedClassifier](../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()), [hasSubstitution](../../classes/mdkernel/Classifier.html#hasSubstitution()), [hasUseCase](../../classes/mdkernel/Classifier.html#hasUseCase()), [isFinalSpecialization](../../classes/mdkernel/Classifier.html#isFinalSpecialization()), [set_interfaceOfNestedClassifier](../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)), [setFinalSpecialization](../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)), [setOwnedTemplateSignature](../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)), [setRepresentation](../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)), [setTemplateParameter](../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)), [setUMLClass](../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)
`[getOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#getOwnedPort()), [hasOwnedPort](../../compositestructures/mdports/EncapsulatedClassifier.html#hasOwnedPort())`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
getEdge
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](../mdbasicactivities/ActivityEdge.html)> getEdge()
Returns the value of the '***Edge***' containment reference list.
 The list contents are of type [`ActivityEdge`](../mdbasicactivities/ActivityEdge.html).
 It is bidirectional and its opposite is '[`*Activity*`](../mdbasicactivities/ActivityEdge.html#getActivity())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityEdges expressing flow between the nodes of the Activity.
 end-model-doc
Returns:
the value of the '*Edge*' containment reference list.
See Also:
[`UMLPackage.getActivity_Edge()`](../../metadata/UMLPackage.html#getActivity_Edge())
[`ActivityEdge.getActivity()`](../mdbasicactivities/ActivityEdge.html#getActivity())
Model:
opposite="activity" containment="true" resolveProxies="true" ordered="false"
Generated:
getGroup
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityGroup](ActivityGroup.html)> getGroup()
Returns the value of the '***Group***' containment reference list.
 The list contents are of type [`ActivityGroup`](ActivityGroup.html).
 It is bidirectional and its opposite is
 '[`*In Activity*`](ActivityGroup.html#getInActivity())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Top-level ActivityGroups in the Activity.
 end-model-doc
Returns:
the value of the '*Group*' containment reference list.
See Also:
[`UMLPackage.getActivity_Group()`](../../metadata/UMLPackage.html#getActivity_Group())
[`ActivityGroup.getInActivity()`](ActivityGroup.html#getInActivity())
Model:
opposite="inActivity" containment="true" resolveProxies="true" ordered="false"
Generated:
isReadOnly
boolean isReadOnly()
Returns the value of the '***Read Only***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, this Activity must not make any changes to objects. The default is false (an Activity may make nonlocal changes). (This is an assertion, not an
 executable property. It may be used by an execution engine to optimize model execution. If the assertion is violated by the Activity, then the model is
 ill-formed.)
 end-model-doc
Returns:
the value of the '*Read Only*' attribute.
See Also:
[`setReadOnly(boolean)`](#setReadOnly(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivity_ReadOnly()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setReadOnly
void setReadOnly(boolean value)
Sets the value of the '[`*Read Only*`](#isReadOnly())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Read Only*' attribute.
See Also:
[`isReadOnly()`](#isReadOnly())
Generated:
isSingleExecution
boolean isSingleExecution()
Returns the value of the '***Single Execution***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, all invocations of the Activity are handled by the same execution.
 end-model-doc
Returns:
the value of the '*Single Execution*' attribute.
See Also:
[`setSingleExecution(boolean)`](#setSingleExecution(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivity_SingleExecution()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setSingleExecution
void setSingleExecution(boolean value)
Sets the value of the '[`*Single Execution*`](#isSingleExecution())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Single Execution*' attribute.
See Also:
[`isSingleExecution()`](#isSingleExecution())
Generated:
getPartition
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../mdintermediateactivities/ActivityPartition.html)> getPartition()
Returns the value of the '***Partition***' reference list.
 The list contents are of type [`ActivityPartition`](../mdintermediateactivities/ActivityPartition.html).
 It is bidirectional and its opposite is
 '[`*activity Of Partition*`](../mdintermediateactivities/ActivityPartition.html#get_activityOfPartition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Top-level ActivityPartitions in the Activity.
 end-model-doc
Returns:
the value of the '*Partition*' reference list.
See Also:
[`UMLPackage.getActivity_Partition()`](../../metadata/UMLPackage.html#getActivity_Partition())
[`ActivityPartition.get_activityOfPartition()`](../mdintermediateactivities/ActivityPartition.html#get_activityOfPartition())
Model:
opposite="_activityOfPartition" ordered="false"
Generated:
getVariable
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Variable](../mdstructuredactivities/Variable.html)> getVariable()
Returns the value of the '***Variable***' containment reference list.
 The list contents are of type [`Variable`](../mdstructuredactivities/Variable.html).
 It is bidirectional and its opposite is
 '[`*Activity Scope*`](../mdstructuredactivities/Variable.html#getActivityScope())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Top-level Variables defined by the Activity.
 end-model-doc
Returns:
the value of the '*Variable*' containment reference list.
See Also:
[`UMLPackage.getActivity_Variable()`](../../metadata/UMLPackage.html#getActivity_Variable())
[`Variable.getActivityScope()`](../mdstructuredactivities/Variable.html#getActivityScope())
Model:
opposite="activityScope" containment="true" resolveProxies="true" ordered="false"
Generated:
getStructuredNode
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html)> getStructuredNode()
Returns the value of the '***Structured Node***' reference list.
 The list contents are of type [`StructuredActivityNode`](../mdstructuredactivities/StructuredActivityNode.html).
 It is bidirectional and its opposite is
 '[`*Activity*`](../mdstructuredactivities/StructuredActivityNode.html#getActivity())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Top-level StructuredActivityNodes in the Activity.
 end-model-doc
Returns:
the value of the '*Structured Node*' reference list.
See Also:
[`UMLPackage.getActivity_StructuredNode()`](../../metadata/UMLPackage.html#getActivity_StructuredNode())
[`StructuredActivityNode.getActivity()`](../mdstructuredactivities/StructuredActivityNode.html#getActivity())
Model:
opposite="activity" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getNode
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ActivityNode](ActivityNode.html)> getNode()
Returns the value of the '***Node***' containment reference list.
 The list contents are of type [`ActivityNode`](ActivityNode.html).
 It is bidirectional and its opposite is '[`*Activity*`](ActivityNode.html#getActivity())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityNodes coordinated by the Activity.
 end-model-doc
Returns:
the value of the '*Node*' containment reference list.
See Also:
[`UMLPackage.getActivity_Node()`](../../metadata/UMLPackage.html#getActivity_Node())
[`ActivityNode.getActivity()`](ActivityNode.html#getActivity())
Model:
opposite="activity" containment="true" resolveProxies="true" ordered="false"
Generated:
hasEdge
boolean hasEdge()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasGroup
boolean hasGroup()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPartition
boolean hasPartition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasVariable
boolean hasVariable()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasStructuredNode
boolean hasStructuredNode()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasNode
boolean hasNode()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities</a></div>
<h1 class="title" title="Interface Activity">Interface Activity</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code>, <code><a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Activity</span><span class="extends-implements">
extends <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Activity</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An Activity is the specification of parameterized Behavior as the coordinated sequencing of subordinate units.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getEdge()"><code><em>Edge</em></code></a></li>
<li><a href="#getGroup()"><code><em>Group</em></code></a></li>
<li><a href="#getPartition()"><code><em>Partition</em></code></a></li>
<li><a href="#getStructuredNode()"><code><em>Structured Node</em></code></a></li>
<li><a href="#isReadOnly()"><code><em>Read Only</em></code></a></li>
<li><a href="#isSingleExecution()"><code><em>Single Execution</em></code></a></li>
<li><a href="#getVariable()"><code><em>Variable</em></code></a></li>
<li><a href="#getNode()"><code><em>Node</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getActivity()"><code>UMLPackage.getActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='activities.mdfundamentalactivities'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEdge()">getEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Edge</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGroup()">getGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Group</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNode()">getNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Node</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPartition()">getPartition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Partition</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStructuredNode()">getStructuredNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Structured Node</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariable()">getVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Variable</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasEdge()">hasEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasGroup()">hasGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasNode()">hasNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPartition()">hasPartition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasStructuredNode()">hasStructuredNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasVariable()">hasVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReadOnly()">isReadOnly</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Read Only</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSingleExecution()">isSingleExecution</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Single Execution</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReadOnly(boolean)">setReadOnly</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isReadOnly()"><code><em>Read Only</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSingleExecution(boolean)">setSingleExecution</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isSingleExecution()"><code><em>Single Execution</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></h3>
<code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behavioredClassifierOfClassifierBehavior()">get_behavioredClassifierOfClassifierBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behavioredClassifierOfOwnedBehavior()">get_behavioredClassifierOfOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behaviorExecutionSpecificationOfBehavior()">get_behaviorExecutionSpecificationOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_behaviorOfRedefinedBehavior()">get_behaviorOfRedefinedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_callBehaviorActionOfBehavior()">get_callBehaviorActionOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_connectorOfContract()">get_connectorOfContract</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_decisionNodeOfDecisionInput()">get_decisionNodeOfDecisionInput</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectFlowOfSelection()">get_objectFlowOfSelection</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectFlowOfTransformation()">get_objectFlowOfTransformation</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection()">get_objectNodeOfSelection</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_opaqueExpressionOfBehavior()">get_opaqueExpressionOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_reduceActionOfReducer()">get_reduceActionOfReducer</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity()">get_stateOfDoActivity</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry()">get_stateOfEntry</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit()">get_stateOfExit</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect()">get_transitionOfEffect</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getContext()">getContext</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getEvent()">getEvent</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getObservation()">getObservation</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameter()">getOwnedParameter</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getOwnedParameterSet()">getOwnedParameterSet</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition()">getPostcondition</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition()">getPrecondition</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getRedefinedBehavior()">getRedefinedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getSpecification()">getSpecification</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_behaviorExecutionSpecificationOfBehavior()">has_behaviorExecutionSpecificationOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_behaviorOfRedefinedBehavior()">has_behaviorOfRedefinedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_callBehaviorActionOfBehavior()">has_callBehaviorActionOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_connectorOfContract()">has_connectorOfContract</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_decisionNodeOfDecisionInput()">has_decisionNodeOfDecisionInput</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectFlowOfSelection()">has_objectFlowOfSelection</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectFlowOfTransformation()">has_objectFlowOfTransformation</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_objectNodeOfSelection()">has_objectNodeOfSelection</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_opaqueExpressionOfBehavior()">has_opaqueExpressionOfBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#has_reduceActionOfReducer()">has_reduceActionOfReducer</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasEvent()">hasEvent</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasObservation()">hasObservation</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasOwnedParameter()">hasOwnedParameter</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasOwnedParameterSet()">hasOwnedParameterSet</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasPostcondition()">hasPostcondition</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasPrecondition()">hasPrecondition</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#hasRedefinedBehavior()">hasRedefinedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#isReentrant()">isReentrant</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_behavioredClassifierOfClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">set_behavioredClassifierOfClassifierBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_behavioredClassifierOfOwnedBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier)">set_behavioredClassifierOfOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfDoActivity(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfDoActivity</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfEntry(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfEntry</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_stateOfExit(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfExit</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#set_transitionOfEffect(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">set_transitionOfEffect</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#setReentrant(boolean)">setReentrant</a>, <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature)">setSpecification</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.BehavioredClassifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.<a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></h3>
<code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getClassifierBehavior()">getClassifierBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getInterfaceRealization()">getInterfaceRealization</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#getOwnedBehavior()">getOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasInterfaceRealization()">hasInterfaceRealization</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#hasOwnedBehavior()">hasOwnedBehavior</a>, <a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html#setClassifierBehavior(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setClassifierBehavior</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></h3>
<code><a href="../../classes/mdkernel/Class.html#getExtension()">getExtension</a>, <a href="../../classes/mdkernel/Class.html#getNestedClassifier()">getNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#getOwnedAttribute()">getOwnedAttribute</a>, <a href="../../classes/mdkernel/Class.html#getOwnedOperation()">getOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#getOwnedReception()">getOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#getSuperClass()">getSuperClass</a>, <a href="../../classes/mdkernel/Class.html#hasExtension()">hasExtension</a>, <a href="../../classes/mdkernel/Class.html#hasNestedClassifier()">hasNestedClassifier</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedOperation()">hasOwnedOperation</a>, <a href="../../classes/mdkernel/Class.html#hasOwnedReception()">hasOwnedReception</a>, <a href="../../classes/mdkernel/Class.html#hasSuperClass()">hasSuperClass</a>, <a href="../../classes/mdkernel/Class.html#isAbstract()">isAbstract</a>, <a href="../../classes/mdkernel/Class.html#isActive()">isActive</a>, <a href="../../classes/mdkernel/Class.html#setAbstract(boolean)">setAbstract</a>, <a href="../../classes/mdkernel/Class.html#setActive(boolean)">setActive</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></h3>
<code><a href="../../classes/mdkernel/Classifier.html#get_classifierOfRedefinedClassifier()">get_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_classifierTemplateParameterOfConstrainingClassifier()">get_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_componentRealizationOfRealizingClassifier()">get_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_createObjectActionOfClassifier()">get_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_exceptionHandlerOfExceptionType()">get_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#get_generalizationOfGeneral()">get_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationFlowOfConveyed()">get_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#get_informationItemOfRepresented()">get_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#get_instanceSpecificationOfClassifier()">get_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_interfaceOfNestedClassifier()">get_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()">get_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_readIsClassifiedObjectActionOfClassifier()">get_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfNewClassifier()">get_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_reclassifyObjectActionOfOldClassifier()">get_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#get_redefinableElementOfRedefinitionContext()">get_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#get_substitutionOfContract()">get_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#get_unmarshallActionOfUnmarshallType()">get_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#getAttribute()">getAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#getCollaborationUse()">getCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#getFeature()">getFeature</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneral()">getGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#getGeneralization()">getGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#getInheritedMember()">getInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#getOwnedUseCase()">getOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#getPowertypeExtent()">getPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#getRedefinedClassifier()">getRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#getRepresentation()">getRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#getSubstitution()">getSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#getUMLClass()">getUMLClass</a>, <a href="../../classes/mdkernel/Classifier.html#getUseCase()">getUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierOfRedefinedClassifier()">has_classifierOfRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_classifierTemplateParameterOfConstrainingClassifier()">has_classifierTemplateParameterOfConstrainingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_componentRealizationOfRealizingClassifier()">has_componentRealizationOfRealizingClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_createObjectActionOfClassifier()">has_createObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_exceptionHandlerOfExceptionType()">has_exceptionHandlerOfExceptionType</a>, <a href="../../classes/mdkernel/Classifier.html#has_generalizationOfGeneral()">has_generalizationOfGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationFlowOfConveyed()">has_informationFlowOfConveyed</a>, <a href="../../classes/mdkernel/Classifier.html#has_informationItemOfRepresented()">has_informationItemOfRepresented</a>, <a href="../../classes/mdkernel/Classifier.html#has_instanceSpecificationOfClassifier()">has_instanceSpecificationOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readExtentActionOfClassifier()">has_readExtentActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_readIsClassifiedObjectActionOfClassifier()">has_readIsClassifiedObjectActionOfClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfNewClassifier()">has_reclassifyObjectActionOfNewClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_reclassifyObjectActionOfOldClassifier()">has_reclassifyObjectActionOfOldClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#has_redefinableElementOfRedefinitionContext()">has_redefinableElementOfRedefinitionContext</a>, <a href="../../classes/mdkernel/Classifier.html#has_substitutionOfContract()">has_substitutionOfContract</a>, <a href="../../classes/mdkernel/Classifier.html#has_unmarshallActionOfUnmarshallType()">has_unmarshallActionOfUnmarshallType</a>, <a href="../../classes/mdkernel/Classifier.html#hasAttribute()">hasAttribute</a>, <a href="../../classes/mdkernel/Classifier.html#hasCollaborationUse()">hasCollaborationUse</a>, <a href="../../classes/mdkernel/Classifier.html#hasFeature()">hasFeature</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneral()">hasGeneral</a>, <a href="../../classes/mdkernel/Classifier.html#hasGeneralization()">hasGeneralization</a>, <a href="../../classes/mdkernel/Classifier.html#hasInheritedMember()">hasInheritedMember</a>, <a href="../../classes/mdkernel/Classifier.html#hasOwnedUseCase()">hasOwnedUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#hasPowertypeExtent()">hasPowertypeExtent</a>, <a href="../../classes/mdkernel/Classifier.html#hasRedefinedClassifier()">hasRedefinedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#hasSubstitution()">hasSubstitution</a>, <a href="../../classes/mdkernel/Classifier.html#hasUseCase()">hasUseCase</a>, <a href="../../classes/mdkernel/Classifier.html#isFinalSpecialization()">isFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#set_interfaceOfNestedClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">set_interfaceOfNestedClassifier</a>, <a href="../../classes/mdkernel/Classifier.html#setFinalSpecialization(boolean)">setFinalSpecialization</a>, <a href="../../classes/mdkernel/Classifier.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.RedefinableTemplateSignature)">setOwnedTemplateSignature</a>, <a href="../../classes/mdkernel/Classifier.html#setRepresentation(com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations.CollaborationUse)">setRepresentation</a>, <a href="../../classes/mdkernel/Classifier.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ClassifierTemplateParameter)">setTemplateParameter</a>, <a href="../../classes/mdkernel/Classifier.html#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<section class="detail" id="getEdge()">
<h3>getEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</span> <span class="element-name">getEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>Edge</b></em>' containment reference list.
 The list contents are of type <a href="../mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.
 It is bidirectional and its opposite is '<a href="../mdbasicactivities/ActivityEdge.html#getActivity()"><code><em>Activity</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityEdges expressing flow between the nodes of the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Edge</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getActivity_Edge()"><code>UMLPackage.getActivity_Edge()</code></a></li>
<li><a href="../mdbasicactivities/ActivityEdge.html#getActivity()"><code>ActivityEdge.getActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="activity" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroup()">
<h3>getGroup</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a>&gt;</span> <span class="element-name">getGroup</span>()</div>
<div class="block">Returns the value of the '<em><b>Group</b></em>' containment reference list.
 The list contents are of type <a href="ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.
 It is bidirectional and its opposite is
 '<a href="ActivityGroup.html#getInActivity()"><code><em>In Activity</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Top-level ActivityGroups in the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Group</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getActivity_Group()"><code>UMLPackage.getActivity_Group()</code></a></li>
<li><a href="ActivityGroup.html#getInActivity()"><code>ActivityGroup.getInActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inActivity" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReadOnly()">
<h3>isReadOnly</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReadOnly</span>()</div>
<div class="block">Returns the value of the '<em><b>Read Only</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, this Activity must not make any changes to objects. The default is false (an Activity may make nonlocal changes). (This is an assertion, not an
 executable property. It may be used by an execution engine to optimize model execution. If the assertion is violated by the Activity, then the model is
 ill-formed.)
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Read Only</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setReadOnly(boolean)"><code>setReadOnly(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivity_ReadOnly()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReadOnly(boolean)">
<h3>setReadOnly</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReadOnly</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isReadOnly()"><code><em>Read Only</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Read Only</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isReadOnly()"><code>isReadOnly()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSingleExecution()">
<h3>isSingleExecution</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSingleExecution</span>()</div>
<div class="block">Returns the value of the '<em><b>Single Execution</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, all invocations of the Activity are handled by the same execution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Single Execution</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setSingleExecution(boolean)"><code>setSingleExecution(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getActivity_SingleExecution()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSingleExecution(boolean)">
<h3>setSingleExecution</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSingleExecution</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isSingleExecution()"><code><em>Single Execution</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Single Execution</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isSingleExecution()"><code>isSingleExecution()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPartition()">
<h3>getPartition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</span> <span class="element-name">getPartition</span>()</div>
<div class="block">Returns the value of the '<em><b>Partition</b></em>' reference list.
 The list contents are of type <a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactivities/ActivityPartition.html#get_activityOfPartition()"><code><em>activity Of Partition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Top-level ActivityPartitions in the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Partition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivity_Partition()"><code>UMLPackage.getActivity_Partition()</code></a></li>
<li><a href="../mdintermediateactivities/ActivityPartition.html#get_activityOfPartition()"><code>ActivityPartition.get_activityOfPartition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_activityOfPartition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariable()">
<h3>getVariable</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a>&gt;</span> <span class="element-name">getVariable</span>()</div>
<div class="block">Returns the value of the '<em><b>Variable</b></em>' containment reference list.
 The list contents are of type <a href="../mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Variable</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdstructuredactivities/Variable.html#getActivityScope()"><code><em>Activity Scope</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Top-level Variables defined by the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Variable</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivity_Variable()"><code>UMLPackage.getActivity_Variable()</code></a></li>
<li><a href="../mdstructuredactivities/Variable.html#getActivityScope()"><code>Variable.getActivityScope()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="activityScope" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStructuredNode()">
<h3>getStructuredNode</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a>&gt;</span> <span class="element-name">getStructuredNode</span>()</div>
<div class="block">Returns the value of the '<em><b>Structured Node</b></em>' reference list.
 The list contents are of type <a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>StructuredActivityNode</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdstructuredactivities/StructuredActivityNode.html#getActivity()"><code><em>Activity</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Top-level StructuredActivityNodes in the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Structured Node</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivity_StructuredNode()"><code>UMLPackage.getActivity_StructuredNode()</code></a></li>
<li><a href="../mdstructuredactivities/StructuredActivityNode.html#getActivity()"><code>StructuredActivityNode.getActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="activity" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNode()">
<h3>getNode</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>&gt;</span> <span class="element-name">getNode</span>()</div>
<div class="block">Returns the value of the '<em><b>Node</b></em>' containment reference list.
 The list contents are of type <a href="ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityNode</code></a>.
 It is bidirectional and its opposite is '<a href="ActivityNode.html#getActivity()"><code><em>Activity</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityNodes coordinated by the Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Node</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getActivity_Node()"><code>UMLPackage.getActivity_Node()</code></a></li>
<li><a href="ActivityNode.html#getActivity()"><code>ActivityNode.getActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="activity" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasEdge()">
<h3>hasEdge</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasEdge</span>()
         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasGroup()">
<h3>hasGroup</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasGroup</span>()
          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPartition()">
<h3>hasPartition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPartition</span>()
              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasVariable()">
<h3>hasVariable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasVariable</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStructuredNode()">
<h3>hasStructuredNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasStructuredNode</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNode()">
<h3>hasNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasNode</span>()
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
