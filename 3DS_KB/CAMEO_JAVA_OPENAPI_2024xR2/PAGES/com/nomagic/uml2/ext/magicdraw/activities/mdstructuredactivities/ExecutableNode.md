# JAVA OPENAPI: ExecutableNode (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/ExecutableNode.html`
- source_sha256: `304f5fa7569a4de377e78f0805cd61c836b6f1103f5f2eb02cc2da4dd947a302`
- captured_utc: `2026-07-14T16:56:14.551675+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities](package-summary.html)

## Interface ExecutableNode

All Superinterfaces:
`[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[AcceptCallAction](../../actions/mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html)`, `[Action](../../actions/mdbasicactions/Action.html)`, `[AddStructuralFeatureValueAction](../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../../actions/mdstructuredactions/AddVariableValueAction.html)`, `[BroadcastSignalAction](../../actions/mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](../../actions/mdbasicactions/CallAction.html)`, `[CallBehaviorAction](../../actions/mdbasicactions/CallBehaviorAction.html)`, `[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)`, `[ClearAssociationAction](../../actions/mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../../actions/mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../../actions/mdstructuredactions/ClearVariableAction.html)`, `[ConditionalNode](ConditionalNode.html)`, `[CreateLinkAction](../../actions/mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../../actions/mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../../actions/mdintermediateactions/CreateObjectAction.html)`, `[DestroyLinkAction](../../actions/mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../../actions/mdintermediateactions/DestroyObjectAction.html)`, `[ExpansionRegion](../mdextrastructuredactivities/ExpansionRegion.html)`, `[InvocationAction](../../actions/mdbasicactions/InvocationAction.html)`, `[LinkAction](../../actions/mdintermediateactions/LinkAction.html)`, `[LoopNode](LoopNode.html)`, `[OpaqueAction](../../actions/mdbasicactions/OpaqueAction.html)`, `[RaiseExceptionAction](../../actions/mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../../actions/mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../../actions/mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../../actions/mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../../actions/mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../../actions/mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../../actions/mdstructuredactions/ReadVariableAction.html)`, `[ReclassifyObjectAction](../../actions/mdcompleteactions/ReclassifyObjectAction.html)`, `[ReduceAction](../../actions/mdcompleteactions/ReduceAction.html)`, `[RemoveStructuralFeatureValueAction](../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../../actions/mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../../actions/mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](../../actions/mdbasicactions/SendSignalAction.html)`, `[SequenceNode](SequenceNode.html)`, `[StartClassifierBehaviorAction](../../actions/mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../../actions/mdcompleteactions/StartObjectBehaviorAction.html)`, `[StructuralFeatureAction](../../actions/mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](StructuredActivityNode.html)`, `[TestIdentityAction](../../actions/mdintermediateactions/TestIdentityAction.html)`, `[UnmarshallAction](../../actions/mdcompleteactions/UnmarshallAction.html)`, `[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html)`, `[VariableAction](../../actions/mdstructuredactions/VariableAction.html)`, `[WriteLinkAction](../../actions/mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../../actions/mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../../actions/mdstructuredactions/WriteVariableAction.html)`

public interfaceExecutableNodeextends [ActivityNode](../mdfundamentalactivities/ActivityNode.html)

begin-user-doc 
 A representation of the model object '***Executable Node***'.
 end-user-doc 
begin-model-doc 
 An ExecutableNode is an abstract class for ActivityNodes whose execution may be controlled using ControlFlows and to which ExceptionHandlers may be attached.
 end-model-doc 
The following features are supported:
 [`*clause Of Body*`](#get_clauseOfBody())
[`*clause Of Test*`](#get_clauseOfTest())
[`*loop Node Of Body Part*`](#get_loopNodeOfBodyPart())
[`*loop Node Of Setup Part*`](#get_loopNodeOfSetupPart())
[`*loop Node Of Test*`](#get_loopNodeOfTest())
[`*exception Handler Of Handler Body*`](#get_exceptionHandlerOfHandlerBody())
[`*Handler*`](#getHandler())
[`*sequence Node Of Executable Node*`](#get_sequenceNodeOfExecutableNode())

See Also:
[`UMLPackage.getExecutableNode()`](../../metadata/UMLPackage.html#getExecutableNode())
Model:
abstract="true"
 annotation="MOF package='activities.mdstructuredactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Clause](Clause.html)`
`[get_clauseOfBody](#get_clauseOfBody())()`
Returns the value of the '***clause Of Body***' reference.
`[Clause](Clause.html)`
`[get_clauseOfTest](#get_clauseOfTest())()`
Returns the value of the '***clause Of Test***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)>`
`[get_exceptionHandlerOfHandlerBody](#get_exceptionHandlerOfHandlerBody())()`
Returns the value of the '***exception Handler Of Handler Body***' reference list.
`[LoopNode](LoopNode.html)`
`[get_loopNodeOfBodyPart](#get_loopNodeOfBodyPart())()`
Returns the value of the '***loop Node Of Body Part***' reference.
`[LoopNode](LoopNode.html)`
`[get_loopNodeOfSetupPart](#get_loopNodeOfSetupPart())()`
Returns the value of the '***loop Node Of Setup Part***' reference.
`[LoopNode](LoopNode.html)`
`[get_loopNodeOfTest](#get_loopNodeOfTest())()`
Returns the value of the '***loop Node Of Test***' reference.
`[SequenceNode](SequenceNode.html)`
`[get_sequenceNodeOfExecutableNode](#get_sequenceNodeOfExecutableNode())()`
Returns the value of the '***sequence Node Of Executable Node***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)>`
`[getHandler](#getHandler())()`
Returns the value of the '***Handler***' containment reference list.
`boolean`
`[has_exceptionHandlerOfHandlerBody](#has_exceptionHandlerOfHandlerBody())()`

`boolean`
`[hasHandler](#hasHandler())()`

`void`
`[set_clauseOfBody](#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))([Clause](Clause.html) value)`
Sets the value of the '[`*clause Of Body*`](#get_clauseOfBody())'
 reference.
`void`
`[set_clauseOfTest](#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))([Clause](Clause.html) value)`
Sets the value of the '[`*clause Of Test*`](#get_clauseOfTest())'
 reference.
`void`
`[set_loopNodeOfBodyPart](#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](LoopNode.html) value)`
Sets the value of the
 '[`*loop Node Of Body Part*`](#get_loopNodeOfBodyPart())' reference.
`void`
`[set_loopNodeOfSetupPart](#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](LoopNode.html) value)`
Sets the value of the
 '[`*loop Node Of Setup Part*`](#get_loopNodeOfSetupPart())' reference.
`void`
`[set_loopNodeOfTest](#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](LoopNode.html) value)`
Sets the value of the '[`*loop Node Of Test*`](#get_loopNodeOfTest())'
 reference.
`void`
`[set_sequenceNodeOfExecutableNode](#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))([SequenceNode](SequenceNode.html) value)`
Sets the value of the '[`*sequence Node
 Of Executable Node*`](#get_sequenceNodeOfExecutableNode())' container reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getActivity](../mdfundamentalactivities/ActivityNode.html#getActivity()), [getIncoming](../mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setActivity](../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setInStructuredNode](../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getHandler
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)> getHandler()
Returns the value of the '***Handler***' containment reference list.
 The list contents are of type [`ExceptionHandler`](../mdextrastructuredactivities/ExceptionHandler.html).
 It is bidirectional and its opposite is
 '[`*Protected Node*`](../mdextrastructuredactivities/ExceptionHandler.html#getProtectedNode())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A set of ExceptionHandlers that are examined if an exception propagates out of the ExceptionNode.
 end-model-doc
Returns:
the value of the '*Handler*' containment reference list.
See Also:
[`UMLPackage.getExecutableNode_Handler()`](../../metadata/UMLPackage.html#getExecutableNode_Handler())
[`ExceptionHandler.getProtectedNode()`](../mdextrastructuredactivities/ExceptionHandler.html#getProtectedNode())
Model:
opposite="protectedNode" containment="true" resolveProxies="true" ordered="false"
Generated:
get_exceptionHandlerOfHandlerBody
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)> get_exceptionHandlerOfHandlerBody()
Returns the value of the '***exception Handler Of Handler Body***' reference list.
 The list contents are of type [`ExceptionHandler`](../mdextrastructuredactivities/ExceptionHandler.html).
 It is bidirectional and its opposite is
 '[`*Handler Body*`](../mdextrastructuredactivities/ExceptionHandler.html#getHandlerBody())'.
 begin-user-doc 
If the meaning of the '*exception Handler Of Handler Body*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*exception Handler Of Handler Body*' reference list.
See Also:
[`UMLPackage.getExecutableNode__exceptionHandlerOfHandlerBody()`](../../metadata/UMLPackage.html#getExecutableNode__exceptionHandlerOfHandlerBody())
[`ExceptionHandler.getHandlerBody()`](../mdextrastructuredactivities/ExceptionHandler.html#getHandlerBody())
Model:
opposite="handlerBody" ordered="false"
Generated:
get_loopNodeOfSetupPart
@CheckForNull[LoopNode](LoopNode.html) get_loopNodeOfSetupPart()
Returns the value of the '***loop Node Of Setup Part***' reference.
 It is bidirectional and its opposite is '[`*Setup Part*`](LoopNode.html#getSetupPart())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Setup Part*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Setup Part*' reference.
See Also:
[`set_loopNodeOfSetupPart(LoopNode)`](#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getExecutableNode__loopNodeOfSetupPart()`](../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfSetupPart())
[`LoopNode.getSetupPart()`](LoopNode.html#getSetupPart())
Model:
opposite="setupPart" ordered="false"
Generated:
set_loopNodeOfSetupPart
void set_loopNodeOfSetupPart(@CheckForNull
 [LoopNode](LoopNode.html) value)
Sets the value of the
 '[`*loop Node Of Setup Part*`](#get_loopNodeOfSetupPart())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Setup Part*' reference.
See Also:
[`get_loopNodeOfSetupPart()`](#get_loopNodeOfSetupPart())
Generated:
get_loopNodeOfBodyPart
@CheckForNull[LoopNode](LoopNode.html) get_loopNodeOfBodyPart()
Returns the value of the '***loop Node Of Body Part***' reference.
 It is bidirectional and its opposite is '[`*Body Part*`](LoopNode.html#getBodyPart())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Body Part*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Body Part*' reference.
See Also:
[`set_loopNodeOfBodyPart(LoopNode)`](#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getExecutableNode__loopNodeOfBodyPart()`](../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfBodyPart())
[`LoopNode.getBodyPart()`](LoopNode.html#getBodyPart())
Model:
opposite="bodyPart" ordered="false"
Generated:
set_loopNodeOfBodyPart
void set_loopNodeOfBodyPart(@CheckForNull
 [LoopNode](LoopNode.html) value)
Sets the value of the
 '[`*loop Node Of Body Part*`](#get_loopNodeOfBodyPart())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Body Part*' reference.
See Also:
[`get_loopNodeOfBodyPart()`](#get_loopNodeOfBodyPart())
Generated:
get_clauseOfTest
@CheckForNull[Clause](Clause.html) get_clauseOfTest()
Returns the value of the '***clause Of Test***' reference.
 It is bidirectional and its opposite is '[`*Test*`](Clause.html#getTest())'.
 begin-user-doc 
If the meaning of the '*clause Of Test*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clause Of Test*' reference.
See Also:
[`set_clauseOfTest(Clause)`](#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))
[`UMLPackage.getExecutableNode__clauseOfTest()`](../../metadata/UMLPackage.html#getExecutableNode__clauseOfTest())
[`Clause.getTest()`](Clause.html#getTest())
Model:
opposite="test" ordered="false"
Generated:
set_clauseOfTest
void set_clauseOfTest(@CheckForNull
 [Clause](Clause.html) value)
Sets the value of the '[`*clause Of Test*`](#get_clauseOfTest())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*clause Of Test*' reference.
See Also:
[`get_clauseOfTest()`](#get_clauseOfTest())
Generated:
get_clauseOfBody
@CheckForNull[Clause](Clause.html) get_clauseOfBody()
Returns the value of the '***clause Of Body***' reference.
 It is bidirectional and its opposite is '[`*Body*`](Clause.html#getBody())'.
 begin-user-doc 
If the meaning of the '*clause Of Body*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clause Of Body*' reference.
See Also:
[`set_clauseOfBody(Clause)`](#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))
[`UMLPackage.getExecutableNode__clauseOfBody()`](../../metadata/UMLPackage.html#getExecutableNode__clauseOfBody())
[`Clause.getBody()`](Clause.html#getBody())
Model:
opposite="body" ordered="false"
Generated:
set_clauseOfBody
void set_clauseOfBody(@CheckForNull
 [Clause](Clause.html) value)
Sets the value of the '[`*clause Of Body*`](#get_clauseOfBody())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*clause Of Body*' reference.
See Also:
[`get_clauseOfBody()`](#get_clauseOfBody())
Generated:
get_loopNodeOfTest
@CheckForNull[LoopNode](LoopNode.html) get_loopNodeOfTest()
Returns the value of the '***loop Node Of Test***' reference.
 It is bidirectional and its opposite is '[`*Test*`](LoopNode.html#getTest())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Test*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Test*' reference.
See Also:
[`set_loopNodeOfTest(LoopNode)`](#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getExecutableNode__loopNodeOfTest()`](../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfTest())
[`LoopNode.getTest()`](LoopNode.html#getTest())
Model:
opposite="test" ordered="false"
Generated:
set_loopNodeOfTest
void set_loopNodeOfTest(@CheckForNull
 [LoopNode](LoopNode.html) value)
Sets the value of the '[`*loop Node Of Test*`](#get_loopNodeOfTest())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Test*' reference.
See Also:
[`get_loopNodeOfTest()`](#get_loopNodeOfTest())
Generated:
get_sequenceNodeOfExecutableNode
@CheckForNull[SequenceNode](SequenceNode.html) get_sequenceNodeOfExecutableNode()
Returns the value of the '***sequence Node Of Executable Node***' container reference.
 It is bidirectional and its opposite is
 '[`*Executable Node*`](SequenceNode.html#getExecutableNode())'.
 begin-user-doc 
If the meaning of the '*sequence Node Of Executable Node*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*sequence Node Of Executable Node*' container reference.
See Also:
[`set_sequenceNodeOfExecutableNode(SequenceNode)`](#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))
[`UMLPackage.getExecutableNode__sequenceNodeOfExecutableNode()`](../../metadata/UMLPackage.html#getExecutableNode__sequenceNodeOfExecutableNode())
[`SequenceNode.getExecutableNode()`](SequenceNode.html#getExecutableNode())
Model:
opposite="executableNode" transient="false" ordered="false"
Generated:
set_sequenceNodeOfExecutableNode
void set_sequenceNodeOfExecutableNode(@CheckForNull
 [SequenceNode](SequenceNode.html) value)
Sets the value of the '[`*sequence Node
 Of Executable Node*`](#get_sequenceNodeOfExecutableNode())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*sequence Node Of Executable Node*' container reference.
See Also:
[`get_sequenceNodeOfExecutableNode()`](#get_sequenceNodeOfExecutableNode())
Generated:
hasHandler
boolean hasHandler()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_exceptionHandlerOfHandlerBody
boolean has_exceptionHandlerOfHandlerBody()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities</a></div>
<h1 class="title" title="Interface ExecutableNode">Interface ExecutableNode</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../actions/mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../../actions/mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="../../actions/mdbasicactions/CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="../../actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../../actions/mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../../actions/mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../../actions/mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="../../actions/mdbasicactions/InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../../actions/mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../actions/mdbasicactions/OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../../actions/mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../../actions/mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../../actions/mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../../actions/mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../../actions/mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="../../actions/mdbasicactions/SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../actions/mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../../actions/mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../../actions/mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../actions/mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../../actions/mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../../actions/mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../../actions/mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../../actions/mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../../actions/mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ExecutableNode</span><span class="extends-implements">
extends <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Executable Node</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ExecutableNode is an abstract class for ActivityNodes whose execution may be controlled using ControlFlows and to which ExceptionHandlers may be attached.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_clauseOfBody()"><code><em>clause Of Body</em></code></a></li>
<li><a href="#get_clauseOfTest()"><code><em>clause Of Test</em></code></a></li>
<li><a href="#get_loopNodeOfBodyPart()"><code><em>loop Node Of Body Part</em></code></a></li>
<li><a href="#get_loopNodeOfSetupPart()"><code><em>loop Node Of Setup Part</em></code></a></li>
<li><a href="#get_loopNodeOfTest()"><code><em>loop Node Of Test</em></code></a></li>
<li><a href="#get_exceptionHandlerOfHandlerBody()"><code><em>exception Handler Of Handler Body</em></code></a></li>
<li><a href="#getHandler()"><code><em>Handler</em></code></a></li>
<li><a href="#get_sequenceNodeOfExecutableNode()"><code><em>sequence Node Of Executable Node</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getExecutableNode()"><code>UMLPackage.getExecutableNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='activities.mdstructuredactivities'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clauseOfBody()">get_clauseOfBody</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clause Of Body</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clauseOfTest()">get_clauseOfTest</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clause Of Test</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_exceptionHandlerOfHandlerBody()">get_exceptionHandlerOfHandlerBody</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>exception Handler Of Handler Body</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfBodyPart()">get_loopNodeOfBodyPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Body Part</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfSetupPart()">get_loopNodeOfSetupPart</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Setup Part</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfTest()">get_loopNodeOfTest</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Test</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_sequenceNodeOfExecutableNode()">get_sequenceNodeOfExecutableNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>sequence Node Of Executable Node</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHandler()">getHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Handler</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_exceptionHandlerOfHandlerBody()">has_exceptionHandlerOfHandlerBody</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasHandler()">hasHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfBody</a><wbr/>(<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_clauseOfBody()"><code><em>clause Of Body</em></code></a>'
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfTest</a><wbr/>(<a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_clauseOfTest()"><code><em>clause Of Test</em></code></a>'
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfBodyPart</a><wbr/>(<a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfBodyPart()"><code><em>loop Node Of Body Part</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfSetupPart</a><wbr/>(<a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfSetupPart()"><code><em>loop Node Of Setup Part</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfTest</a><wbr/>(<a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_loopNodeOfTest()"><code><em>loop Node Of Test</em></code></a>'
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">set_sequenceNodeOfExecutableNode</a><wbr/>(<a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_sequenceNodeOfExecutableNode()"><code><em>sequence Node
 Of Executable Node</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getActivity()">getActivity</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
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
<section class="detail" id="getHandler()">
<h3>getHandler</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</span> <span class="element-name">getHandler</span>()</div>
<div class="block">Returns the value of the '<em><b>Handler</b></em>' containment reference list.
 The list contents are of type <a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdextrastructuredactivities/ExceptionHandler.html#getProtectedNode()"><code><em>Protected Node</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A set of ExceptionHandlers that are examined if an exception propagates out of the ExceptionNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Handler</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getExecutableNode_Handler()"><code>UMLPackage.getExecutableNode_Handler()</code></a></li>
<li><a href="../mdextrastructuredactivities/ExceptionHandler.html#getProtectedNode()"><code>ExceptionHandler.getProtectedNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="protectedNode" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_exceptionHandlerOfHandlerBody()">
<h3>get_exceptionHandlerOfHandlerBody</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</span> <span class="element-name">get_exceptionHandlerOfHandlerBody</span>()</div>
<div class="block">Returns the value of the '<em><b>exception Handler Of Handler Body</b></em>' reference list.
 The list contents are of type <a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdextrastructuredactivities/ExceptionHandler.html#getHandlerBody()"><code><em>Handler Body</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>exception Handler Of Handler Body</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>exception Handler Of Handler Body</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__exceptionHandlerOfHandlerBody()"><code>UMLPackage.getExecutableNode__exceptionHandlerOfHandlerBody()</code></a></li>
<li><a href="../mdextrastructuredactivities/ExceptionHandler.html#getHandlerBody()"><code>ExceptionHandler.getHandlerBody()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="handlerBody" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfSetupPart()">
<h3>get_loopNodeOfSetupPart</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfSetupPart</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Setup Part</b></em>' reference.
 It is bidirectional and its opposite is '<a href="LoopNode.html#getSetupPart()"><code><em>Setup Part</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Setup Part</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Setup Part</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfSetupPart(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfSetupPart()"><code>UMLPackage.getExecutableNode__loopNodeOfSetupPart()</code></a></li>
<li><a href="LoopNode.html#getSetupPart()"><code>LoopNode.getSetupPart()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="setupPart" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfSetupPart</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfSetupPart</span><wbr/><span class="parameters">(@CheckForNull
 <a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfSetupPart()"><code><em>loop Node Of Setup Part</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Setup Part</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfSetupPart()"><code>get_loopNodeOfSetupPart()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfBodyPart()">
<h3>get_loopNodeOfBodyPart</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfBodyPart</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Body Part</b></em>' reference.
 It is bidirectional and its opposite is '<a href="LoopNode.html#getBodyPart()"><code><em>Body Part</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Body Part</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Body Part</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfBodyPart(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfBodyPart()"><code>UMLPackage.getExecutableNode__loopNodeOfBodyPart()</code></a></li>
<li><a href="LoopNode.html#getBodyPart()"><code>LoopNode.getBodyPart()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="bodyPart" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfBodyPart</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfBodyPart</span><wbr/><span class="parameters">(@CheckForNull
 <a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfBodyPart()"><code><em>loop Node Of Body Part</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Body Part</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfBodyPart()"><code>get_loopNodeOfBodyPart()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clauseOfTest()">
<h3>get_clauseOfTest</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></span> <span class="element-name">get_clauseOfTest</span>()</div>
<div class="block">Returns the value of the '<em><b>clause Of Test</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Clause.html#getTest()"><code><em>Test</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clause Of Test</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clause Of Test</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)"><code>set_clauseOfTest(Clause)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__clauseOfTest()"><code>UMLPackage.getExecutableNode__clauseOfTest()</code></a></li>
<li><a href="Clause.html#getTest()"><code>Clause.getTest()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="test" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">
<h3>set_clauseOfTest</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_clauseOfTest</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_clauseOfTest()"><code><em>clause Of Test</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>clause Of Test</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_clauseOfTest()"><code>get_clauseOfTest()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clauseOfBody()">
<h3>get_clauseOfBody</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></span> <span class="element-name">get_clauseOfBody</span>()</div>
<div class="block">Returns the value of the '<em><b>clause Of Body</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Clause.html#getBody()"><code><em>Body</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clause Of Body</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clause Of Body</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)"><code>set_clauseOfBody(Clause)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__clauseOfBody()"><code>UMLPackage.getExecutableNode__clauseOfBody()</code></a></li>
<li><a href="Clause.html#getBody()"><code>Clause.getBody()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="body" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">
<h3>set_clauseOfBody</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_clauseOfBody</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_clauseOfBody()"><code><em>clause Of Body</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>clause Of Body</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_clauseOfBody()"><code>get_clauseOfBody()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfTest()">
<h3>get_loopNodeOfTest</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfTest</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Test</b></em>' reference.
 It is bidirectional and its opposite is '<a href="LoopNode.html#getTest()"><code><em>Test</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Test</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Test</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfTest(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__loopNodeOfTest()"><code>UMLPackage.getExecutableNode__loopNodeOfTest()</code></a></li>
<li><a href="LoopNode.html#getTest()"><code>LoopNode.getTest()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="test" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfTest</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfTest</span><wbr/><span class="parameters">(@CheckForNull
 <a href="LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_loopNodeOfTest()"><code><em>loop Node Of Test</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Test</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfTest()"><code>get_loopNodeOfTest()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_sequenceNodeOfExecutableNode()">
<h3>get_sequenceNodeOfExecutableNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></span> <span class="element-name">get_sequenceNodeOfExecutableNode</span>()</div>
<div class="block">Returns the value of the '<em><b>sequence Node Of Executable Node</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="SequenceNode.html#getExecutableNode()"><code><em>Executable Node</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>sequence Node Of Executable Node</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>sequence Node Of Executable Node</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)"><code>set_sequenceNodeOfExecutableNode(SequenceNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getExecutableNode__sequenceNodeOfExecutableNode()"><code>UMLPackage.getExecutableNode__sequenceNodeOfExecutableNode()</code></a></li>
<li><a href="SequenceNode.html#getExecutableNode()"><code>SequenceNode.getExecutableNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="executableNode" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">
<h3>set_sequenceNodeOfExecutableNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_sequenceNodeOfExecutableNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_sequenceNodeOfExecutableNode()"><code><em>sequence Node
 Of Executable Node</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>sequence Node Of Executable Node</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_sequenceNodeOfExecutableNode()"><code>get_sequenceNodeOfExecutableNode()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasHandler()">
<h3>hasHandler</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasHandler</span>()
            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_exceptionHandlerOfHandlerBody()">
<h3>has_exceptionHandlerOfHandlerBody</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_exceptionHandlerOfHandlerBody</span>()
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
