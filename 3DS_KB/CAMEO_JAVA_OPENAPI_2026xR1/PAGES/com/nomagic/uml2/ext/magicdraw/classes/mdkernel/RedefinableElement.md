# JAVA OPENAPI: RedefinableElement (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/RedefinableElement.html`
- source_sha256: `75c16434e49da90544bf1cf2464fff90458d4467737b1b9c9c47bc7b29322596`
- captured_utc: `2026-07-14T16:46:30.012201+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface RedefinableElement

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[AcceptCallAction](../../actions/mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html)`, `[Action](../../actions/mdbasicactions/Action.html)`, `[ActionInputPin](../../actions/mdstructuredactions/ActionInputPin.html)`, `[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html)`, `[ActivityFinalNode](../../activities/mdbasicactivities/ActivityFinalNode.html)`, `[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[ActivityParameterNode](../../activities/mdbasicactivities/ActivityParameterNode.html)`, `[Actor](../../mdusecases/Actor.html)`, `[AddStructuralFeatureValueAction](../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../../actions/mdstructuredactions/AddVariableValueAction.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](Association.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioralFeature](BehavioralFeature.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](../../actions/mdbasicactions/CallAction.html)`, `[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)`, `[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)`, `[CentralBufferNode](../../activities/mdintermediateactivities/CentralBufferNode.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../../actions/mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../../actions/mdstructuredactions/ClearVariableAction.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`, `[ConnectionPointReference](../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html)`, `[Connector](../../compositestructures/mdinternalstructures/Connector.html)`, `[ControlFlow](../../activities/mdbasicactivities/ControlFlow.html)`, `[ControlNode](../../activities/mdbasicactivities/ControlNode.html)`, `[CreateLinkAction](../../actions/mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../../actions/mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)`, `[DataStoreNode](../../activities/mdcompleteactivities/DataStoreNode.html)`, `[DataType](DataType.html)`, `[DecisionNode](../../activities/mdintermediateactivities/DecisionNode.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[DestroyLinkAction](../../actions/mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../../actions/mdintermediateactions/DestroyObjectAction.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](Enumeration.html)`, `[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[ExpansionNode](../../activities/mdextrastructuredactivities/ExpansionNode.html)`, `[ExpansionRegion](../../activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[ExtensionPoint](../../mdusecases/ExtensionPoint.html)`, `[Feature](Feature.html)`, `[FinalNode](../../activities/mdintermediateactivities/FinalNode.html)`, `[FinalState](../../statemachines/mdbehaviorstatemachines/FinalState.html)`, `[FlowFinalNode](../../activities/mdintermediateactivities/FlowFinalNode.html)`, `[ForkNode](../../activities/mdintermediateactivities/ForkNode.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[InitialNode](../../activities/mdbasicactivities/InitialNode.html)`, `[InputPin](../../actions/mdbasicactions/InputPin.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[Interface](../mdinterfaces/Interface.html)`, `[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)`, `[JoinNode](../../activities/mdintermediateactivities/JoinNode.html)`, `[LinkAction](../../actions/mdintermediateactions/LinkAction.html)`, `[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`, `[MergeNode](../../activities/mdintermediateactivities/MergeNode.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[ObjectFlow](../../activities/mdbasicactivities/ObjectFlow.html)`, `[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`, `[OpaqueAction](../../actions/mdbasicactions/OpaqueAction.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[Operation](Operation.html)`, `[OutputPin](../../actions/mdbasicactions/OutputPin.html)`, `[Pin](../../actions/mdbasicactions/Pin.html)`, `[Port](../../compositestructures/mdports/Port.html)`, `[PrimitiveType](PrimitiveType.html)`, `[Property](Property.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`, `[Pseudostate](../../statemachines/mdbehaviorstatemachines/Pseudostate.html)`, `[RaiseExceptionAction](../../actions/mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../../actions/mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../../actions/mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../../actions/mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../../actions/mdstructuredactions/ReadVariableAction.html)`, `[Reception](../../commonbehaviors/mdcommunications/Reception.html)`, `[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)`, `[RedefinableTemplateSignature](../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html)`, `[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)`, `[Region](../../statemachines/mdbehaviorstatemachines/Region.html)`, `[RemoveStructuralFeatureValueAction](../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../../actions/mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../../actions/mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)`, `[SequenceNode](../../activities/mdstructuredactivities/SequenceNode.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[StartClassifierBehaviorAction](../../actions/mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../../actions/mdcompleteactions/StartObjectBehaviorAction.html)`, `[State](../../statemachines/mdbehaviorstatemachines/State.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StructuralFeature](StructuralFeature.html)`, `[StructuralFeatureAction](../../actions/mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[TestIdentityAction](../../actions/mdintermediateactions/TestIdentityAction.html)`, `[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`, `[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)`, `[UseCase](../../mdusecases/UseCase.html)`, `[ValuePin](../../actions/mdbasicactions/ValuePin.html)`, `[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html)`, `[VariableAction](../../actions/mdstructuredactions/VariableAction.html)`, `[Vertex](../../statemachines/mdbehaviorstatemachines/Vertex.html)`, `[WriteLinkAction](../../actions/mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../../actions/mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../../actions/mdstructuredactions/WriteVariableAction.html)`

public interfaceRedefinableElementextends [NamedElement](NamedElement.html)

begin-user-doc 
 A representation of the model object '***Redefinable Element***'.
 end-user-doc 
begin-model-doc 
 A RedefinableElement is an element that, when defined in the context of a Classifier, can be redefined more specifically or differently in the context of another
 Classifier that specializes (directly or indirectly) the context Classifier.
 end-model-doc 
The following features are supported:
 [`*Leaf*`](#isLeaf())
[`*Redefined Element*`](#getRedefinedElement())
[`*redefinable Element Of Redefined Element*`](#get_redefinableElementOfRedefinedElement())
[`*Redefinition Context*`](#getRedefinitionContext())

See Also:
[`UMLPackage.getRedefinableElement()`](../../metadata/UMLPackage.html#getRedefinableElement())
Model:
abstract="true"
 annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)>`
`[get_redefinableElementOfRedefinedElement](#get_redefinableElementOfRedefinedElement())()`
Returns the value of the '***redefinable Element Of Redefined Element***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)>`
`[getRedefinedElement](#getRedefinedElement())()`
Returns the value of the '***Redefined Element***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)>`
`[getRedefinitionContext](#getRedefinitionContext())()`
Returns the value of the '***Redefinition Context***' reference list.
`boolean`
`[has_redefinableElementOfRedefinedElement](#has_redefinableElementOfRedefinedElement())()`

`boolean`
`[hasRedefinedElement](#hasRedefinedElement())()`

`boolean`
`[hasRedefinitionContext](#hasRedefinitionContext())()`

`boolean`
`[isLeaf](#isLeaf())()`
Returns the value of the '***Leaf***' attribute.
`void`
`[setLeaf](#setLeaf(boolean))(boolean value)`
Sets the value of the '[`*Leaf*`](#isLeaf())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [getVisibility](NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getRedefinedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)> getRedefinedElement()
Returns the value of the '***Redefined Element***' reference list.
 The list contents are of type [`RedefinableElement`](RedefinableElement.html).
 It is bidirectional and its opposite is '[`*redefinable Element Of Redefined Element*`](#get_redefinableElementOfRedefinedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The RedefinableElement that is being redefined by this element.
 end-model-doc
Returns:
the value of the '*Redefined Element*' reference list.
See Also:
[`UMLPackage.getRedefinableElement_RedefinedElement()`](../../metadata/UMLPackage.html#getRedefinableElement_RedefinedElement())
[`get_redefinableElementOfRedefinedElement()`](#get_redefinableElementOfRedefinedElement())
Model:
opposite="_redefinableElementOfRedefinedElement" transient="true" volatile="true" derived="true" ordered="false"
Generated:
get_redefinableElementOfRedefinedElement
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RedefinableElement](RedefinableElement.html)> get_redefinableElementOfRedefinedElement()
Returns the value of the '***redefinable Element Of Redefined Element***' reference list.
 The list contents are of type [`RedefinableElement`](RedefinableElement.html).
 It is bidirectional and its opposite is
 '[`*Redefined Element*`](#getRedefinedElement())'.
 begin-user-doc 
If the meaning of the '*redefinable Element Of Redefined Element*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*redefinable Element Of Redefined Element*' reference list.
See Also:
[`UMLPackage.getRedefinableElement__redefinableElementOfRedefinedElement()`](../../metadata/UMLPackage.html#getRedefinableElement__redefinableElementOfRedefinedElement())
[`getRedefinedElement()`](#getRedefinedElement())
Model:
opposite="redefinedElement" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getRedefinitionContext
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](Classifier.html)> getRedefinitionContext()
Returns the value of the '***Redefinition Context***' reference list.
 The list contents are of type [`Classifier`](Classifier.html).
 It is bidirectional and its opposite is '[`*redefinable Element Of Redefinition Context*`](Classifier.html#get_redefinableElementOfRedefinitionContext())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The contexts that this element may be redefined from.
 end-model-doc
Returns:
the value of the '*Redefinition Context*' reference list.
See Also:
[`UMLPackage.getRedefinableElement_RedefinitionContext()`](../../metadata/UMLPackage.html#getRedefinableElement_RedefinitionContext())
[`Classifier.get_redefinableElementOfRedefinitionContext()`](Classifier.html#get_redefinableElementOfRedefinitionContext())
Model:
opposite="_redefinableElementOfRedefinitionContext" transient="true" volatile="true" derived="true" ordered="false"
Generated:
isLeaf
boolean isLeaf()
Returns the value of the '***Leaf***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates whether it is possible to further redefine a RedefinableElement. If the value is true, then it is not possible to further redefine the
 RedefinableElement.
 end-model-doc
Returns:
the value of the '*Leaf*' attribute.
See Also:
[`setLeaf(boolean)`](#setLeaf(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getRedefinableElement_Leaf()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setLeaf
void setLeaf(boolean value)
Sets the value of the '[`*Leaf*`](#isLeaf())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Leaf*' attribute.
See Also:
[`isLeaf()`](#isLeaf())
Generated:
hasRedefinitionContext
boolean hasRedefinitionContext()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedElement
boolean hasRedefinedElement()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_redefinableElementOfRedefinedElement
boolean has_redefinableElementOfRedefinedElement()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface RedefinableElement">Interface RedefinableElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityFinalNode</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../activities/mdbasicactivities/ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="../../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code>, <code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a></code>, <code><a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code>, <code><a href="../../activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ControlNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlNode</a></code>, <code><a href="../../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../../activities/mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code>, <code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../mdusecases/ExtensionPoint.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">ExtensionPoint</a></code>, <code><a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../activities/mdintermediateactivities/FinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FinalNode</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code>, <code><a href="../../activities/mdintermediateactivities/FlowFinalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">FlowFinalNode</a></code>, <code><a href="../../activities/mdintermediateactivities/ForkNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ForkNode</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../activities/mdbasicactivities/InitialNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">InitialNode</a></code>, <code><a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code>, <code><a href="../../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code>, <code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="../../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="../../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a></code>, <code><a href="../../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code>, <code><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/RedefinableTemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">RedefinableTemplateSignature</a></code>, <code><a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code>, <code><a href="../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="../../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a></code>, <code><a href="../../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code>, <code><a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code>, <code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code>, <code><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code>, <code><a href="../../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RedefinableElement</span><span class="extends-implements">
extends <a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Redefinable Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A RedefinableElement is an element that, when defined in the context of a Classifier, can be redefined more specifically or differently in the context of another
 Classifier that specializes (directly or indirectly) the context Classifier.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#isLeaf()"><code><em>Leaf</em></code></a></li>
<li><a href="#getRedefinedElement()"><code><em>Redefined Element</em></code></a></li>
<li><a href="#get_redefinableElementOfRedefinedElement()"><code><em>redefinable Element Of Redefined Element</em></code></a></li>
<li><a href="#getRedefinitionContext()"><code><em>Redefinition Context</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getRedefinableElement()"><code>UMLPackage.getRedefinableElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='classes.mdkernel'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>redefinable Element Of Redefined Element</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedElement()">getRedefinedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Element</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinitionContext()">getRedefinitionContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedElement()">hasRedefinedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinitionContext()">hasRedefinitionContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLeaf()">isLeaf</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Leaf</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLeaf(boolean)">setLeaf</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isLeaf()"><code><em>Leaf</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#getVisibility()">getVisibility</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
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
<section class="detail" id="getRedefinedElement()">
<h3>getRedefinedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</span> <span class="element-name">getRedefinedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Element</b></em>' reference list.
 The list contents are of type <a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.
 It is bidirectional and its opposite is '<a href="#get_redefinableElementOfRedefinedElement()"><code><em>redefinable Element Of Redefined Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The RedefinableElement that is being redefined by this element.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getRedefinableElement_RedefinedElement()"><code>UMLPackage.getRedefinableElement_RedefinedElement()</code></a></li>
<li><a href="#get_redefinableElementOfRedefinedElement()"><code>get_redefinableElementOfRedefinedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_redefinableElementOfRedefinedElement" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_redefinableElementOfRedefinedElement()">
<h3>get_redefinableElementOfRedefinedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a>&gt;</span> <span class="element-name">get_redefinableElementOfRedefinedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>redefinable Element Of Redefined Element</b></em>' reference list.
 The list contents are of type <a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>RedefinableElement</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedElement()"><code><em>Redefined Element</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>redefinable Element Of Redefined Element</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>redefinable Element Of Redefined Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getRedefinableElement__redefinableElementOfRedefinedElement()"><code>UMLPackage.getRedefinableElement__redefinableElementOfRedefinedElement()</code></a></li>
<li><a href="#getRedefinedElement()"><code>getRedefinedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedElement" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinitionContext()">
<h3>getRedefinitionContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getRedefinitionContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.
 The list contents are of type <a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is '<a href="Classifier.html#get_redefinableElementOfRedefinitionContext()"><code><em>redefinable Element Of Redefinition Context</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The contexts that this element may be redefined from.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefinition Context</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getRedefinableElement_RedefinitionContext()"><code>UMLPackage.getRedefinableElement_RedefinitionContext()</code></a></li>
<li><a href="Classifier.html#get_redefinableElementOfRedefinitionContext()"><code>Classifier.get_redefinableElementOfRedefinitionContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_redefinableElementOfRedefinitionContext" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLeaf()">
<h3>isLeaf</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLeaf</span>()</div>
<div class="block">Returns the value of the '<em><b>Leaf</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates whether it is possible to further redefine a RedefinableElement. If the value is true, then it is not possible to further redefine the
 RedefinableElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Leaf</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setLeaf(boolean)"><code>setLeaf(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getRedefinableElement_Leaf()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLeaf(boolean)">
<h3>setLeaf</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLeaf</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isLeaf()"><code><em>Leaf</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Leaf</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isLeaf()"><code>isLeaf()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinitionContext()">
<h3>hasRedefinitionContext</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinitionContext</span>()
                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedElement()">
<h3>hasRedefinedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedElement</span>()
                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_redefinableElementOfRedefinedElement()">
<h3>has_redefinableElementOfRedefinedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_redefinableElementOfRedefinedElement</span>()
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
