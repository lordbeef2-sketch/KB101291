# JAVA OPENAPI: Action (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/Action.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/Action.html`
- source_sha256: `f8f041807afdb9b66bc925530f2536e1134e27a1dc643022efe5f7697cc5268f`
- captured_utc: `2026-07-14T16:46:23.443112+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions](package-summary.html)

## Interface Action

All Superinterfaces:
`[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[AcceptCallAction](../mdcompleteactions/AcceptCallAction.html)`, `[AcceptEventAction](../mdcompleteactions/AcceptEventAction.html)`, `[AddStructuralFeatureValueAction](../mdintermediateactions/AddStructuralFeatureValueAction.html)`, `[AddVariableValueAction](../mdstructuredactions/AddVariableValueAction.html)`, `[BroadcastSignalAction](../mdintermediateactions/BroadcastSignalAction.html)`, `[CallAction](CallAction.html)`, `[CallBehaviorAction](CallBehaviorAction.html)`, `[CallOperationAction](CallOperationAction.html)`, `[ClearAssociationAction](../mdintermediateactions/ClearAssociationAction.html)`, `[ClearStructuralFeatureAction](../mdintermediateactions/ClearStructuralFeatureAction.html)`, `[ClearVariableAction](../mdstructuredactions/ClearVariableAction.html)`, `[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`, `[CreateLinkAction](../mdintermediateactions/CreateLinkAction.html)`, `[CreateLinkObjectAction](../mdcompleteactions/CreateLinkObjectAction.html)`, `[CreateObjectAction](../mdintermediateactions/CreateObjectAction.html)`, `[DestroyLinkAction](../mdintermediateactions/DestroyLinkAction.html)`, `[DestroyObjectAction](../mdintermediateactions/DestroyObjectAction.html)`, `[ExpansionRegion](../../activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[InvocationAction](InvocationAction.html)`, `[LinkAction](../mdintermediateactions/LinkAction.html)`, `[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`, `[OpaqueAction](OpaqueAction.html)`, `[RaiseExceptionAction](../mdstructuredactions/RaiseExceptionAction.html)`, `[ReadExtentAction](../mdcompleteactions/ReadExtentAction.html)`, `[ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html)`, `[ReadLinkAction](../mdintermediateactions/ReadLinkAction.html)`, `[ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html)`, `[ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`, `[ReadSelfAction](../mdintermediateactions/ReadSelfAction.html)`, `[ReadStructuralFeatureAction](../mdintermediateactions/ReadStructuralFeatureAction.html)`, `[ReadVariableAction](../mdstructuredactions/ReadVariableAction.html)`, `[ReclassifyObjectAction](../mdcompleteactions/ReclassifyObjectAction.html)`, `[ReduceAction](../mdcompleteactions/ReduceAction.html)`, `[RemoveStructuralFeatureValueAction](../mdintermediateactions/RemoveStructuralFeatureValueAction.html)`, `[RemoveVariableValueAction](../mdstructuredactions/RemoveVariableValueAction.html)`, `[ReplyAction](../mdcompleteactions/ReplyAction.html)`, `[SendObjectAction](../mdintermediateactions/SendObjectAction.html)`, `[SendSignalAction](SendSignalAction.html)`, `[SequenceNode](../../activities/mdstructuredactivities/SequenceNode.html)`, `[StartClassifierBehaviorAction](../mdcompleteactions/StartClassifierBehaviorAction.html)`, `[StartObjectBehaviorAction](../mdcompleteactions/StartObjectBehaviorAction.html)`, `[StructuralFeatureAction](../mdintermediateactions/StructuralFeatureAction.html)`, `[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`, `[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html)`, `[UnmarshallAction](../mdcompleteactions/UnmarshallAction.html)`, `[ValueSpecificationAction](../mdintermediateactions/ValueSpecificationAction.html)`, `[VariableAction](../mdstructuredactions/VariableAction.html)`, `[WriteLinkAction](../mdintermediateactions/WriteLinkAction.html)`, `[WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html)`, `[WriteVariableAction](../mdstructuredactions/WriteVariableAction.html)`

public interfaceActionextends [ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)

begin-user-doc 
 A representation of the model object '***Action***'.
 end-user-doc 
begin-model-doc 
 An Action is the fundamental unit of executable functionality. The execution of an Action represents some transformation or processing in the modeled system.
 Actions provide the ExecutableNodes within Activities and may also be used within Interactions.
 end-model-doc 
The following features are supported:
 [`*Local Postcondition*`](#getLocalPostcondition())
[`*Output*`](#getOutput())
[`*Local Precondition*`](#getLocalPrecondition())
[`*Input*`](#getInput())
[`*Context*`](#getContext())
[`*Locally Reentrant*`](#isLocallyReentrant())
[`*action Input Pin Of From Action*`](#get_actionInputPinOfFromAction())
[`*action Execution Specification Of Action*`](#get_actionExecutionSpecificationOfAction())
[`*interaction Of Action*`](#get_interactionOfAction())

See Also:
[`UMLPackage.getAction()`](../../metadata/UMLPackage.html#getAction())
Model:
abstract="true"
 annotation="MOF package='actions.mdbasicactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActionExecutionSpecification](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html)>`
`[get_actionExecutionSpecificationOfAction](#get_actionExecutionSpecificationOfAction())()`
Returns the value of the '***action Execution Specification Of Action***' reference list.
`[ActionInputPin](../mdstructuredactions/ActionInputPin.html)`
`[get_actionInputPinOfFromAction](#get_actionInputPinOfFromAction())()`
Returns the value of the '***action Input Pin Of From Action***' container reference.
`[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`
`[get_interactionOfAction](#get_interactionOfAction())()`
Returns the value of the '***interaction Of Action***' container reference.
`[Classifier](../../classes/mdkernel/Classifier.html)`
`[getContext](#getContext())()`
Returns the value of the '***Context***' reference.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InputPin](InputPin.html)>`
`[getInput](#getInput())()`
Returns the value of the '***Input***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)>`
`[getLocalPostcondition](#getLocalPostcondition())()`
Returns the value of the '***Local Postcondition***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)>`
`[getLocalPrecondition](#getLocalPrecondition())()`
Returns the value of the '***Local Precondition***' containment reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OutputPin](OutputPin.html)>`
`[getOutput](#getOutput())()`
Returns the value of the '***Output***' reference list.
`boolean`
`[has_actionExecutionSpecificationOfAction](#has_actionExecutionSpecificationOfAction())()`

`boolean`
`[hasInput](#hasInput())()`

`boolean`
`[hasLocalPostcondition](#hasLocalPostcondition())()`

`boolean`
`[hasLocalPrecondition](#hasLocalPrecondition())()`

`boolean`
`[hasOutput](#hasOutput())()`

`boolean`
`[isLocallyReentrant](#isLocallyReentrant())()`
Returns the value of the '***Locally Reentrant***' attribute.
`void`
`[set_actionInputPinOfFromAction](#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin))([ActionInputPin](../mdstructuredactions/ActionInputPin.html) value)`
Sets the value of the
 '[`*action Input Pin Of From Action*`](#get_actionInputPinOfFromAction())' container
 reference.
`void`
`[set_interactionOfAction](#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([Interaction](../../interactions/mdbasicinteractions/Interaction.html) value)`
Sets the value of the '[`*interaction Of Action*`](#get_interactionOfAction())' container
 reference.
`void`
`[setLocallyReentrant](#setLocallyReentrant(boolean))(boolean value)`
Sets the value of the '[`*Locally Reentrant*`](#isLocallyReentrant())' attribute.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getActivity](../../activities/mdfundamentalactivities/ActivityNode.html#getActivity()), [getIncoming](../../activities/mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../../activities/mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../../activities/mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../../activities/mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../../activities/mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../../activities/mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../../activities/mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../../activities/mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../../activities/mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../../activities/mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../../activities/mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setActivity](../../activities/mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setInStructuredNode](../../activities/mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)
`[get_clauseOfBody](../../activities/mdstructuredactivities/ExecutableNode.html#get_clauseOfBody()), [get_clauseOfTest](../../activities/mdstructuredactivities/ExecutableNode.html#get_clauseOfTest()), [get_exceptionHandlerOfHandlerBody](../../activities/mdstructuredactivities/ExecutableNode.html#get_exceptionHandlerOfHandlerBody()), [get_loopNodeOfBodyPart](../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfBodyPart()), [get_loopNodeOfSetupPart](../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfSetupPart()), [get_loopNodeOfTest](../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfTest()), [get_sequenceNodeOfExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html#get_sequenceNodeOfExecutableNode()), [getHandler](../../activities/mdstructuredactivities/ExecutableNode.html#getHandler()), [has_exceptionHandlerOfHandlerBody](../../activities/mdstructuredactivities/ExecutableNode.html#has_exceptionHandlerOfHandlerBody()), [hasHandler](../../activities/mdstructuredactivities/ExecutableNode.html#hasHandler()), [set_clauseOfBody](../../activities/mdstructuredactivities/ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_clauseOfTest](../../activities/mdstructuredactivities/ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_loopNodeOfBodyPart](../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfSetupPart](../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfTest](../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_sequenceNodeOfExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
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
getOutput
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[OutputPin](OutputPin.html)> getOutput()
Returns the value of the '***Output***' reference list.
 The list contents are of type [`OutputPin`](OutputPin.html).
 It is bidirectional and its opposite is '[`*action Of Output*`](OutputPin.html#get_actionOfOutput())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ordered set of OutputPins representing outputs from the Action.
 end-model-doc
Returns:
the value of the '*Output*' reference list.
See Also:
[`UMLPackage.getAction_Output()`](../../metadata/UMLPackage.html#getAction_Output())
[`OutputPin.get_actionOfOutput()`](OutputPin.html#get_actionOfOutput())
Model:
opposite="_actionOfOutput" transient="true" volatile="true" derived="true"
Generated:
get_interactionOfAction
@CheckForNull[Interaction](../../interactions/mdbasicinteractions/Interaction.html) get_interactionOfAction()
Returns the value of the '***interaction Of Action***' container reference.
 It is bidirectional and its opposite is '[`*Action*`](../../interactions/mdbasicinteractions/Interaction.html#getAction())'.
 begin-user-doc 
If the meaning of the '*interaction Of Action*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Of Action*' container reference.
See Also:
[`set_interactionOfAction(Interaction)`](#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))
[`UMLPackage.getAction__interactionOfAction()`](../../metadata/UMLPackage.html#getAction__interactionOfAction())
[`Interaction.getAction()`](../../interactions/mdbasicinteractions/Interaction.html#getAction())
Model:
opposite="action" transient="false" ordered="false"
Generated:
set_interactionOfAction
void set_interactionOfAction(@CheckForNull
 [Interaction](../../interactions/mdbasicinteractions/Interaction.html) value)
Sets the value of the '[`*interaction Of Action*`](#get_interactionOfAction())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Of Action*' container reference.
See Also:
[`get_interactionOfAction()`](#get_interactionOfAction())
Generated:
get_actionExecutionSpecificationOfAction
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActionExecutionSpecification](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html)> get_actionExecutionSpecificationOfAction()
Returns the value of the '***action Execution Specification Of Action***' reference list.
 The list contents are of type [`ActionExecutionSpecification`](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html).
 It is bidirectional and its opposite is
 '[`*Action*`](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html#getAction())'.
 begin-user-doc 
If the meaning of the '*action Execution Specification Of Action*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Execution Specification Of Action*' reference list.
See Also:
[`UMLPackage.getAction__actionExecutionSpecificationOfAction()`](../../metadata/UMLPackage.html#getAction__actionExecutionSpecificationOfAction())
[`ActionExecutionSpecification.getAction()`](../../interactions/mdbasicinteractions/ActionExecutionSpecification.html#getAction())
Model:
opposite="action" ordered="false"
Generated:
getInput
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InputPin](InputPin.html)> getInput()
Returns the value of the '***Input***' reference list.
 The list contents are of type [`InputPin`](InputPin.html).
 It is bidirectional and its opposite is '[`*action Of Input*`](InputPin.html#get_actionOfInput())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ordered set of InputPins representing the inputs to the Action.
 end-model-doc
Returns:
the value of the '*Input*' reference list.
See Also:
[`UMLPackage.getAction_Input()`](../../metadata/UMLPackage.html#getAction_Input())
[`InputPin.get_actionOfInput()`](InputPin.html#get_actionOfInput())
Model:
opposite="_actionOfInput" transient="true" volatile="true" derived="true"
Generated:
getContext
@CheckForNull[Classifier](../../classes/mdkernel/Classifier.html) getContext()
Returns the value of the '***Context***' reference.
 It is bidirectional and its opposite is '
invalid reference
`*action Of Context*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The context Classifier of the Behavior that contains this Action, or the Behavior itself if it has no context.
 end-model-doc
Returns:
the value of the '*Context*' reference.
See Also:
[`UMLPackage.getAction_Context()`](../../metadata/UMLPackage.html#getAction_Context())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_actionOfContext`
Model:
opposite="_actionOfContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isLocallyReentrant
boolean isLocallyReentrant()
Returns the value of the '***Locally Reentrant***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 If true, the Action can begin a new, concurrent execution, even if there is already another execution of the Action ongoing. If false, the Action cannot begin a
 new execution until any previous execution has completed.
 end-model-doc
Returns:
the value of the '*Locally Reentrant*' attribute.
See Also:
[`setLocallyReentrant(boolean)`](#setLocallyReentrant(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAction_LocallyReentrant()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setLocallyReentrant
void setLocallyReentrant(boolean value)
Sets the value of the '[`*Locally Reentrant*`](#isLocallyReentrant())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Locally Reentrant*' attribute.
See Also:
[`isLocallyReentrant()`](#isLocallyReentrant())
Generated:
getLocalPrecondition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)> getLocalPrecondition()
Returns the value of the '***Local Precondition***' containment reference list.
 The list contents are of type [`Constraint`](../../classes/mdkernel/Constraint.html).
 It is bidirectional and its opposite is
 '[`*action Of Local Precondition*`](../../classes/mdkernel/Constraint.html#get_actionOfLocalPrecondition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Constraint that must be satisfied when execution of the Action is started.
 end-model-doc
Returns:
the value of the '*Local Precondition*' containment reference list.
See Also:
[`UMLPackage.getAction_LocalPrecondition()`](../../metadata/UMLPackage.html#getAction_LocalPrecondition())
[`Constraint.get_actionOfLocalPrecondition()`](../../classes/mdkernel/Constraint.html#get_actionOfLocalPrecondition())
Model:
opposite="_actionOfLocalPrecondition" containment="true" resolveProxies="true" ordered="false"
Generated:
getLocalPostcondition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](../../classes/mdkernel/Constraint.html)> getLocalPostcondition()
Returns the value of the '***Local Postcondition***' containment reference list.
 The list contents are of type [`Constraint`](../../classes/mdkernel/Constraint.html).
 It is bidirectional and its opposite is
 '[`*action Of Local Postcondition*`](../../classes/mdkernel/Constraint.html#get_actionOfLocalPostcondition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Constraint that must be satisfied when execution of the Action is completed.
 end-model-doc
Returns:
the value of the '*Local Postcondition*' containment reference list.
See Also:
[`UMLPackage.getAction_LocalPostcondition()`](../../metadata/UMLPackage.html#getAction_LocalPostcondition())
[`Constraint.get_actionOfLocalPostcondition()`](../../classes/mdkernel/Constraint.html#get_actionOfLocalPostcondition())
Model:
opposite="_actionOfLocalPostcondition" containment="true" resolveProxies="true" ordered="false"
Generated:
get_actionInputPinOfFromAction
@CheckForNull[ActionInputPin](../mdstructuredactions/ActionInputPin.html) get_actionInputPinOfFromAction()
Returns the value of the '***action Input Pin Of From Action***' container reference.
 It is bidirectional and its opposite is '[`*From Action*`](../mdstructuredactions/ActionInputPin.html#getFromAction())'.
 begin-user-doc 
If the meaning of the '*action Input Pin Of From Action*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Input Pin Of From Action*' container reference.
See Also:
[`set_actionInputPinOfFromAction(ActionInputPin)`](#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin))
[`UMLPackage.getAction__actionInputPinOfFromAction()`](../../metadata/UMLPackage.html#getAction__actionInputPinOfFromAction())
[`ActionInputPin.getFromAction()`](../mdstructuredactions/ActionInputPin.html#getFromAction())
Model:
opposite="fromAction" transient="false" ordered="false"
Generated:
set_actionInputPinOfFromAction
void set_actionInputPinOfFromAction(@CheckForNull
 [ActionInputPin](../mdstructuredactions/ActionInputPin.html) value)
Sets the value of the
 '[`*action Input Pin Of From Action*`](#get_actionInputPinOfFromAction())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*action Input Pin Of From Action*' container reference.
See Also:
[`get_actionInputPinOfFromAction()`](#get_actionInputPinOfFromAction())
Generated:
hasOutput
boolean hasOutput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_actionExecutionSpecificationOfAction
boolean has_actionExecutionSpecificationOfAction()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasInput
boolean hasInput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasLocalPrecondition
boolean hasLocalPrecondition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasLocalPostcondition
boolean hasLocalPostcondition()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions</a></div>
<h1 class="title" title="Interface Action">Interface Action</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code>, <code><a href="../mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code>, <code><a href="../mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code>, <code><a href="../mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code>, <code><a href="../mdintermediateactions/BroadcastSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">BroadcastSignalAction</a></code>, <code><a href="CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code>, <code><a href="CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code>, <code><a href="CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code>, <code><a href="../mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code>, <code><a href="../mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code>, <code><a href="../mdstructuredactions/ClearVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ClearVariableAction</a></code>, <code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="../mdintermediateactions/CreateLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateLinkAction</a></code>, <code><a href="../mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code>, <code><a href="../mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code>, <code><a href="../mdintermediateactions/DestroyLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyLinkAction</a></code>, <code><a href="../mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code>, <code><a href="../mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code>, <code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code>, <code><a href="../mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code>, <code><a href="../mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code>, <code><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code>, <code><a href="../mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code>, <code><a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code>, <code><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code>, <code><a href="../mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code>, <code><a href="../mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code>, <code><a href="../mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code>, <code><a href="../mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code>, <code><a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code>, <code><a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code>, <code><a href="../mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code>, <code><a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code>, <code><a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code>, <code><a href="SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code>, <code><a href="../../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code>, <code><a href="../mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code>, <code><a href="../mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code>, <code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code>, <code><a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code>, <code><a href="../mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code>, <code><a href="../mdstructuredactions/VariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">VariableAction</a></code>, <code><a href="../mdintermediateactions/WriteLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteLinkAction</a></code>, <code><a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code>, <code><a href="../mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Action</span><span class="extends-implements">
extends <a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Action</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An Action is the fundamental unit of executable functionality. The execution of an Action represents some transformation or processing in the modeled system.
 Actions provide the ExecutableNodes within Activities and may also be used within Interactions.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getLocalPostcondition()"><code><em>Local Postcondition</em></code></a></li>
<li><a href="#getOutput()"><code><em>Output</em></code></a></li>
<li><a href="#getLocalPrecondition()"><code><em>Local Precondition</em></code></a></li>
<li><a href="#getInput()"><code><em>Input</em></code></a></li>
<li><a href="#getContext()"><code><em>Context</em></code></a></li>
<li><a href="#isLocallyReentrant()"><code><em>Locally Reentrant</em></code></a></li>
<li><a href="#get_actionInputPinOfFromAction()"><code><em>action Input Pin Of From Action</em></code></a></li>
<li><a href="#get_actionExecutionSpecificationOfAction()"><code><em>action Execution Specification Of Action</em></code></a></li>
<li><a href="#get_interactionOfAction()"><code><em>interaction Of Action</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getAction()"><code>UMLPackage.getAction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='actions.mdbasicactions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionExecutionSpecificationOfAction()">get_actionExecutionSpecificationOfAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Execution Specification Of Action</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionInputPinOfFromAction()">get_actionInputPinOfFromAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Input Pin Of From Action</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionOfAction()">get_interactionOfAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Of Action</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Context</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInput()">getInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Input</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLocalPostcondition()">getLocalPostcondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Local Postcondition</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLocalPrecondition()">getLocalPrecondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Local Precondition</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOutput()">getOutput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Output</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_actionExecutionSpecificationOfAction()">has_actionExecutionSpecificationOfAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasInput()">hasInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasLocalPostcondition()">hasLocalPostcondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasLocalPrecondition()">hasLocalPrecondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOutput()">hasOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLocallyReentrant()">isLocallyReentrant</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Locally Reentrant</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">set_actionInputPinOfFromAction</a><wbr/>(<a href="../mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_actionInputPinOfFromAction()"><code><em>action Input Pin Of From Action</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">set_interactionOfAction</a><wbr/>(<a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_interactionOfAction()"><code><em>interaction Of Action</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLocallyReentrant(boolean)">setLocallyReentrant</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isLocallyReentrant()"><code><em>Locally Reentrant</em></code></a>' attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../../activities/mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getActivity()">getActivity</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.<a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></h3>
<code><a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_clauseOfBody()">get_clauseOfBody</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_clauseOfTest()">get_clauseOfTest</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_exceptionHandlerOfHandlerBody()">get_exceptionHandlerOfHandlerBody</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfBodyPart()">get_loopNodeOfBodyPart</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfSetupPart()">get_loopNodeOfSetupPart</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_loopNodeOfTest()">get_loopNodeOfTest</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#get_sequenceNodeOfExecutableNode()">get_sequenceNodeOfExecutableNode</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#getHandler()">getHandler</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#has_exceptionHandlerOfHandlerBody()">has_exceptionHandlerOfHandlerBody</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#hasHandler()">hasHandler</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfBody</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfTest</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfBodyPart</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfSetupPart</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfTest</a>, <a href="../../activities/mdstructuredactivities/ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">set_sequenceNodeOfExecutableNode</a></code></div>
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
<section class="detail" id="getOutput()">
<h3>getOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a>&gt;</span> <span class="element-name">getOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>Output</b></em>' reference list.
 The list contents are of type <a href="OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>OutputPin</code></a>.
 It is bidirectional and its opposite is '<a href="OutputPin.html#get_actionOfOutput()"><code><em>action Of Output</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ordered set of OutputPins representing outputs from the Action.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Output</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getAction_Output()"><code>UMLPackage.getAction_Output()</code></a></li>
<li><a href="OutputPin.html#get_actionOfOutput()"><code>OutputPin.get_actionOfOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_actionOfOutput" transient="true" volatile="true" derived="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionOfAction()">
<h3>get_interactionOfAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">get_interactionOfAction</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Of Action</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Interaction.html#getAction()"><code><em>Action</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Of Action</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Of Action</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)"><code>set_interactionOfAction(Interaction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getAction__interactionOfAction()"><code>UMLPackage.getAction__interactionOfAction()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Interaction.html#getAction()"><code>Interaction.getAction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="action" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>set_interactionOfAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionOfAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_interactionOfAction()"><code><em>interaction Of Action</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Of Action</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_interactionOfAction()"><code>get_interactionOfAction()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionExecutionSpecificationOfAction()">
<h3>get_actionExecutionSpecificationOfAction</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">ActionExecutionSpecification</a>&gt;</span> <span class="element-name">get_actionExecutionSpecificationOfAction</span>()</div>
<div class="block">Returns the value of the '<em><b>action Execution Specification Of Action</b></em>' reference list.
 The list contents are of type <a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>ActionExecutionSpecification</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html#getAction()"><code><em>Action</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Execution Specification Of Action</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Execution Specification Of Action</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAction__actionExecutionSpecificationOfAction()"><code>UMLPackage.getAction__actionExecutionSpecificationOfAction()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/ActionExecutionSpecification.html#getAction()"><code>ActionExecutionSpecification.getAction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="action" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInput()">
<h3>getInput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a>&gt;</span> <span class="element-name">getInput</span>()</div>
<div class="block">Returns the value of the '<em><b>Input</b></em>' reference list.
 The list contents are of type <a href="InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>InputPin</code></a>.
 It is bidirectional and its opposite is '<a href="InputPin.html#get_actionOfInput()"><code><em>action Of Input</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ordered set of InputPins representing the inputs to the Action.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Input</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getAction_Input()"><code>UMLPackage.getAction_Input()</code></a></li>
<li><a href="InputPin.html#get_actionOfInput()"><code>InputPin.get_actionOfInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_actionOfInput" transient="true" volatile="true" derived="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Context</b></em>' reference.
 It is bidirectional and its opposite is '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>action Of Context</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The context Classifier of the Behavior that contains this Action, or the Behavior itself if it has no context.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAction_Context()"><code>UMLPackage.getAction_Context()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_actionOfContext</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_actionOfContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocallyReentrant()">
<h3>isLocallyReentrant</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLocallyReentrant</span>()</div>
<div class="block">Returns the value of the '<em><b>Locally Reentrant</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 If true, the Action can begin a new, concurrent execution, even if there is already another execution of the Action ongoing. If false, the Action cannot begin a
 new execution until any previous execution has completed.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Locally Reentrant</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setLocallyReentrant(boolean)"><code>setLocallyReentrant(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getAction_LocallyReentrant()</code></pre>
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
<section class="detail" id="setLocallyReentrant(boolean)">
<h3>setLocallyReentrant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLocallyReentrant</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isLocallyReentrant()"><code><em>Locally Reentrant</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Locally Reentrant</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isLocallyReentrant()"><code>isLocallyReentrant()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalPrecondition()">
<h3>getLocalPrecondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getLocalPrecondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Local Precondition</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Constraint.html#get_actionOfLocalPrecondition()"><code><em>action Of Local Precondition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Constraint that must be satisfied when execution of the Action is started.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Local Precondition</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAction_LocalPrecondition()"><code>UMLPackage.getAction_LocalPrecondition()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_actionOfLocalPrecondition()"><code>Constraint.get_actionOfLocalPrecondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_actionOfLocalPrecondition" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalPostcondition()">
<h3>getLocalPostcondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getLocalPostcondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Local Postcondition</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Constraint.html#get_actionOfLocalPostcondition()"><code><em>action Of Local Postcondition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Constraint that must be satisfied when execution of the Action is completed.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Local Postcondition</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getAction_LocalPostcondition()"><code>UMLPackage.getAction_LocalPostcondition()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_actionOfLocalPostcondition()"><code>Constraint.get_actionOfLocalPostcondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_actionOfLocalPostcondition" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionInputPinOfFromAction()">
<h3>get_actionInputPinOfFromAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></span> <span class="element-name">get_actionInputPinOfFromAction</span>()</div>
<div class="block">Returns the value of the '<em><b>action Input Pin Of From Action</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdstructuredactions/ActionInputPin.html#getFromAction()"><code><em>From Action</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Input Pin Of From Action</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Input Pin Of From Action</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)"><code>set_actionInputPinOfFromAction(ActionInputPin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getAction__actionInputPinOfFromAction()"><code>UMLPackage.getAction__actionInputPinOfFromAction()</code></a></li>
<li><a href="../mdstructuredactions/ActionInputPin.html#getFromAction()"><code>ActionInputPin.getFromAction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="fromAction" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">
<h3>set_actionInputPinOfFromAction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_actionInputPinOfFromAction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_actionInputPinOfFromAction()"><code><em>action Input Pin Of From Action</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>action Input Pin Of From Action</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_actionInputPinOfFromAction()"><code>get_actionInputPinOfFromAction()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOutput()">
<h3>hasOutput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOutput</span>()
           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_actionExecutionSpecificationOfAction()">
<h3>has_actionExecutionSpecificationOfAction</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_actionExecutionSpecificationOfAction</span>()
                                          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInput()">
<h3>hasInput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasInput</span>()
          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasLocalPrecondition()">
<h3>hasLocalPrecondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasLocalPrecondition</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasLocalPostcondition()">
<h3>hasLocalPostcondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasLocalPostcondition</span>()
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
