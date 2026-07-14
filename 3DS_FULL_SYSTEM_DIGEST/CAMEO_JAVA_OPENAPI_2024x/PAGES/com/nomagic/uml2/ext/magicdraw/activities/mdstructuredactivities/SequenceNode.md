# JAVA OPENAPI: SequenceNode (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdstructuredactivities/SequenceNode.html`
- source_sha256: `a124263cbb05cbc999033407de4eee2f2893f56c2b7e94fba1d76819a3ddb113`
- captured_utc: `2026-07-14T16:52:55.460443+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities](package-summary.html)

## Interface SequenceNode

All Superinterfaces:
`[Action](../../actions/mdbasicactions/Action.html)`, `[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)`, `[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ExecutableNode](ExecutableNode.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[StructuredActivityNode](StructuredActivityNode.html)`

public interfaceSequenceNodeextends [StructuredActivityNode](StructuredActivityNode.html)

begin-user-doc 
 A representation of the model object '***Sequence Node***'.
 end-user-doc 
begin-model-doc 
 A SequenceNode is a StructuredActivityNode that executes a sequence of ExecutableNodes in order.
 end-model-doc 
The following features are supported:
 [`*Executable Node*`](#getExecutableNode())

See Also:
[`UMLPackage.getSequenceNode()`](../../metadata/UMLPackage.html#getSequenceNode())
Model:
annotation="MOF package='activities.mdstructuredactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExecutableNode](ExecutableNode.html)>`
`[getExecutableNode](#getExecutableNode())()`
Returns the value of the '***Executable Node***' containment reference list.
`boolean`
`[hasExecutableNode](#hasExecutableNode())()`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.[Action](../../actions/mdbasicactions/Action.html)
`[get_actionExecutionSpecificationOfAction](../../actions/mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()), [get_actionInputPinOfFromAction](../../actions/mdbasicactions/Action.html#get_actionInputPinOfFromAction()), [get_interactionOfAction](../../actions/mdbasicactions/Action.html#get_interactionOfAction()), [getContext](../../actions/mdbasicactions/Action.html#getContext()), [getInput](../../actions/mdbasicactions/Action.html#getInput()), [getLocalPostcondition](../../actions/mdbasicactions/Action.html#getLocalPostcondition()), [getLocalPrecondition](../../actions/mdbasicactions/Action.html#getLocalPrecondition()), [getOutput](../../actions/mdbasicactions/Action.html#getOutput()), [has_actionExecutionSpecificationOfAction](../../actions/mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()), [hasInput](../../actions/mdbasicactions/Action.html#hasInput()), [hasLocalPostcondition](../../actions/mdbasicactions/Action.html#hasLocalPostcondition()), [hasLocalPrecondition](../../actions/mdbasicactions/Action.html#hasLocalPrecondition()), [hasOutput](../../actions/mdbasicactions/Action.html#hasOutput()), [isLocallyReentrant](../../actions/mdbasicactions/Action.html#isLocallyReentrant()), [set_actionInputPinOfFromAction](../../actions/mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)), [set_interactionOfAction](../../actions/mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)), [setLocallyReentrant](../../actions/mdbasicactions/Action.html#setLocallyReentrant(boolean))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)
`[getContainedEdge](../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()), [getContainedNode](../mdfundamentalactivities/ActivityGroup.html#getContainedNode()), [getInActivity](../mdfundamentalactivities/ActivityGroup.html#getInActivity()), [getSubgroup](../mdfundamentalactivities/ActivityGroup.html#getSubgroup()), [getSuperGroup](../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()), [hasContainedEdge](../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()), [hasContainedNode](../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()), [hasSubgroup](../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()), [setInActivity](../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setSuperGroup](../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getIncoming](../mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setInStructuredNode](../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.[ExecutableNode](ExecutableNode.html)
`[get_clauseOfBody](ExecutableNode.html#get_clauseOfBody()), [get_clauseOfTest](ExecutableNode.html#get_clauseOfTest()), [get_exceptionHandlerOfHandlerBody](ExecutableNode.html#get_exceptionHandlerOfHandlerBody()), [get_loopNodeOfBodyPart](ExecutableNode.html#get_loopNodeOfBodyPart()), [get_loopNodeOfSetupPart](ExecutableNode.html#get_loopNodeOfSetupPart()), [get_loopNodeOfTest](ExecutableNode.html#get_loopNodeOfTest()), [get_sequenceNodeOfExecutableNode](ExecutableNode.html#get_sequenceNodeOfExecutableNode()), [getHandler](ExecutableNode.html#getHandler()), [has_exceptionHandlerOfHandlerBody](ExecutableNode.html#has_exceptionHandlerOfHandlerBody()), [hasHandler](ExecutableNode.html#hasHandler()), [set_clauseOfBody](ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_clauseOfTest](ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)), [set_loopNodeOfBodyPart](ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfSetupPart](ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_loopNodeOfTest](ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)), [set_sequenceNodeOfExecutableNode](ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.[StructuredActivityNode](StructuredActivityNode.html)
`[getActivity](StructuredActivityNode.html#getActivity()), [getEdge](StructuredActivityNode.html#getEdge()), [getNode](StructuredActivityNode.html#getNode()), [getStructuredNodeInput](StructuredActivityNode.html#getStructuredNodeInput()), [getStructuredNodeOutput](StructuredActivityNode.html#getStructuredNodeOutput()), [getVariable](StructuredActivityNode.html#getVariable()), [hasEdge](StructuredActivityNode.html#hasEdge()), [hasNode](StructuredActivityNode.html#hasNode()), [hasStructuredNodeInput](StructuredActivityNode.html#hasStructuredNodeInput()), [hasStructuredNodeOutput](StructuredActivityNode.html#hasStructuredNodeOutput()), [hasVariable](StructuredActivityNode.html#hasVariable()), [isMustIsolate](StructuredActivityNode.html#isMustIsolate()), [setActivity](StructuredActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setMustIsolate](StructuredActivityNode.html#setMustIsolate(boolean))`

============ METHOD DETAIL ========== 
Method Details
getExecutableNode
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExecutableNode](ExecutableNode.html)> getExecutableNode()
Returns the value of the '***Executable Node***' containment reference list.
 The list contents are of type [`ExecutableNode`](ExecutableNode.html).
 It is bidirectional and its opposite is '[`*sequence Node Of Executable Node*`](ExecutableNode.html#get_sequenceNodeOfExecutableNode())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ordered set of ExecutableNodes to be sequenced.
 end-model-doc
Returns:
the value of the '*Executable Node*' containment reference list.
See Also:
[`UMLPackage.getSequenceNode_ExecutableNode()`](../../metadata/UMLPackage.html#getSequenceNode_ExecutableNode())
[`ExecutableNode.get_sequenceNodeOfExecutableNode()`](ExecutableNode.html#get_sequenceNodeOfExecutableNode())
Model:
opposite="_sequenceNodeOfExecutableNode" containment="true" resolveProxies="true"
Generated:
hasExecutableNode
boolean hasExecutableNode()
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
<h1 class="title" title="Interface SequenceNode">Interface SequenceNode</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></code>, <code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">SequenceNode</span><span class="extends-implements">
extends <a href="StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Sequence Node</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A SequenceNode is a StructuredActivityNode that executes a sequence of ExecutableNodes in order.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getExecutableNode()"><code><em>Executable Node</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getSequenceNode()"><code>UMLPackage.getSequenceNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='activities.mdstructuredactivities'"</dd>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExecutableNode()">getExecutableNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Executable Node</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasExecutableNode()">hasExecutableNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.<a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></h3>
<code><a href="../../actions/mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()">get_actionExecutionSpecificationOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#get_actionInputPinOfFromAction()">get_actionInputPinOfFromAction</a>, <a href="../../actions/mdbasicactions/Action.html#get_interactionOfAction()">get_interactionOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#getContext()">getContext</a>, <a href="../../actions/mdbasicactions/Action.html#getInput()">getInput</a>, <a href="../../actions/mdbasicactions/Action.html#getLocalPostcondition()">getLocalPostcondition</a>, <a href="../../actions/mdbasicactions/Action.html#getLocalPrecondition()">getLocalPrecondition</a>, <a href="../../actions/mdbasicactions/Action.html#getOutput()">getOutput</a>, <a href="../../actions/mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()">has_actionExecutionSpecificationOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#hasInput()">hasInput</a>, <a href="../../actions/mdbasicactions/Action.html#hasLocalPostcondition()">hasLocalPostcondition</a>, <a href="../../actions/mdbasicactions/Action.html#hasLocalPrecondition()">hasLocalPrecondition</a>, <a href="../../actions/mdbasicactions/Action.html#hasOutput()">hasOutput</a>, <a href="../../actions/mdbasicactions/Action.html#isLocallyReentrant()">isLocallyReentrant</a>, <a href="../../actions/mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">set_actionInputPinOfFromAction</a>, <a href="../../actions/mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">set_interactionOfAction</a>, <a href="../../actions/mdbasicactions/Action.html#setLocallyReentrant(boolean)">setLocallyReentrant</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a></h3>
<code><a href="../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()">getContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getContainedNode()">getContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getInActivity()">getInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSubgroup()">getSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#getSuperGroup()">getSuperGroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedEdge()">hasContainedEdge</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasContainedNode()">hasContainedNode</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#hasSubgroup()">hasSubgroup</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setInActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setInActivity</a>, <a href="../mdfundamentalactivities/ActivityGroup.html#setSuperGroup(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityGroup)">setSuperGroup</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ExecutableNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></h3>
<code><a href="ExecutableNode.html#get_clauseOfBody()">get_clauseOfBody</a>, <a href="ExecutableNode.html#get_clauseOfTest()">get_clauseOfTest</a>, <a href="ExecutableNode.html#get_exceptionHandlerOfHandlerBody()">get_exceptionHandlerOfHandlerBody</a>, <a href="ExecutableNode.html#get_loopNodeOfBodyPart()">get_loopNodeOfBodyPart</a>, <a href="ExecutableNode.html#get_loopNodeOfSetupPart()">get_loopNodeOfSetupPart</a>, <a href="ExecutableNode.html#get_loopNodeOfTest()">get_loopNodeOfTest</a>, <a href="ExecutableNode.html#get_sequenceNodeOfExecutableNode()">get_sequenceNodeOfExecutableNode</a>, <a href="ExecutableNode.html#getHandler()">getHandler</a>, <a href="ExecutableNode.html#has_exceptionHandlerOfHandlerBody()">has_exceptionHandlerOfHandlerBody</a>, <a href="ExecutableNode.html#hasHandler()">hasHandler</a>, <a href="ExecutableNode.html#set_clauseOfBody(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfBody</a>, <a href="ExecutableNode.html#set_clauseOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfTest</a>, <a href="ExecutableNode.html#set_loopNodeOfBodyPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfBodyPart</a>, <a href="ExecutableNode.html#set_loopNodeOfSetupPart(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfSetupPart</a>, <a href="ExecutableNode.html#set_loopNodeOfTest(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfTest</a>, <a href="ExecutableNode.html#set_sequenceNodeOfExecutableNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.SequenceNode)">set_sequenceNodeOfExecutableNode</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.<a href="StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></h3>
<code><a href="StructuredActivityNode.html#getActivity()">getActivity</a>, <a href="StructuredActivityNode.html#getEdge()">getEdge</a>, <a href="StructuredActivityNode.html#getNode()">getNode</a>, <a href="StructuredActivityNode.html#getStructuredNodeInput()">getStructuredNodeInput</a>, <a href="StructuredActivityNode.html#getStructuredNodeOutput()">getStructuredNodeOutput</a>, <a href="StructuredActivityNode.html#getVariable()">getVariable</a>, <a href="StructuredActivityNode.html#hasEdge()">hasEdge</a>, <a href="StructuredActivityNode.html#hasNode()">hasNode</a>, <a href="StructuredActivityNode.html#hasStructuredNodeInput()">hasStructuredNodeInput</a>, <a href="StructuredActivityNode.html#hasStructuredNodeOutput()">hasStructuredNodeOutput</a>, <a href="StructuredActivityNode.html#hasVariable()">hasVariable</a>, <a href="StructuredActivityNode.html#isMustIsolate()">isMustIsolate</a>, <a href="StructuredActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a>, <a href="StructuredActivityNode.html#setMustIsolate(boolean)">setMustIsolate</a></code></div>
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
<section class="detail" id="getExecutableNode()">
<h3>getExecutableNode</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a>&gt;</span> <span class="element-name">getExecutableNode</span>()</div>
<div class="block">Returns the value of the '<em><b>Executable Node</b></em>' containment reference list.
 The list contents are of type <a href="ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>ExecutableNode</code></a>.
 It is bidirectional and its opposite is '<a href="ExecutableNode.html#get_sequenceNodeOfExecutableNode()"><code><em>sequence Node Of Executable Node</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ordered set of ExecutableNodes to be sequenced.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Executable Node</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getSequenceNode_ExecutableNode()"><code>UMLPackage.getSequenceNode_ExecutableNode()</code></a></li>
<li><a href="ExecutableNode.html#get_sequenceNodeOfExecutableNode()"><code>ExecutableNode.get_sequenceNodeOfExecutableNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_sequenceNodeOfExecutableNode" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasExecutableNode()">
<h3>hasExecutableNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasExecutableNode</span>()
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
