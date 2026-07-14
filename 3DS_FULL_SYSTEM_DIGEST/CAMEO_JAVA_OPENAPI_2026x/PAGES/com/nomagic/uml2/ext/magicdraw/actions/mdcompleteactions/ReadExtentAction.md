# JAVA OPENAPI: ReadExtentAction (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdcompleteactions/ReadExtentAction.html`
- source_sha256: `72f6099652b2232b47defe8bab80b2c253d5f15034346ee7300540007749e39c`
- captured_utc: `2026-07-14T16:58:47.970403+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions](package-summary.html)

## Interface ReadExtentAction

All Superinterfaces:
`[Action](../mdbasicactions/Action.html)`, `[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ExecutableNode](../../activities/mdstructuredactivities/ExecutableNode.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceReadExtentActionextends [Action](../mdbasicactions/Action.html)

begin-user-doc 
 A representation of the model object '***Read Extent Action***'.
 end-user-doc 
begin-model-doc 
 A ReadExtentAction is an Action that retrieves the current instances of a Classifier.
 end-model-doc 
The following features are supported:
 [`*Classifier*`](#getClassifier())
[`*Result*`](#getResult())

See Also:
[`UMLPackage.getReadExtentAction()`](../../metadata/UMLPackage.html#getReadExtentAction())
Model:
annotation="MOF package='actions.mdcompleteactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Classifier](../../classes/mdkernel/Classifier.html)`
`[getClassifier](#getClassifier())()`
Returns the value of the '***Classifier***' reference.
`[OutputPin](../mdbasicactions/OutputPin.html)`
`[getResult](#getResult())()`
Returns the value of the '***Result***' containment reference.
`void`
`[setClassifier](#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../classes/mdkernel/Classifier.html) value)`
Sets the value of the '[`*Classifier*`](#getClassifier())' reference.
`void`
`[setResult](#setResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin))([OutputPin](../mdbasicactions/OutputPin.html) value)`
Sets the value of the '[`*Result*`](#getResult())' containment reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.[Action](../mdbasicactions/Action.html)
`[get_actionExecutionSpecificationOfAction](../mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()), [get_actionInputPinOfFromAction](../mdbasicactions/Action.html#get_actionInputPinOfFromAction()), [get_interactionOfAction](../mdbasicactions/Action.html#get_interactionOfAction()), [getContext](../mdbasicactions/Action.html#getContext()), [getInput](../mdbasicactions/Action.html#getInput()), [getLocalPostcondition](../mdbasicactions/Action.html#getLocalPostcondition()), [getLocalPrecondition](../mdbasicactions/Action.html#getLocalPrecondition()), [getOutput](../mdbasicactions/Action.html#getOutput()), [has_actionExecutionSpecificationOfAction](../mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()), [hasInput](../mdbasicactions/Action.html#hasInput()), [hasLocalPostcondition](../mdbasicactions/Action.html#hasLocalPostcondition()), [hasLocalPrecondition](../mdbasicactions/Action.html#hasLocalPrecondition()), [hasOutput](../mdbasicactions/Action.html#hasOutput()), [isLocallyReentrant](../mdbasicactions/Action.html#isLocallyReentrant()), [set_actionInputPinOfFromAction](../mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)), [set_interactionOfAction](../mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)), [setLocallyReentrant](../mdbasicactions/Action.html#setLocallyReentrant(boolean))`
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
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
getResult
@CheckForNull[OutputPin](../mdbasicactions/OutputPin.html) getResult()
Returns the value of the '***Result***' containment reference.
 It is bidirectional and its opposite is
 '[`*read Extent Action Of Result*`](../mdbasicactions/OutputPin.html#get_readExtentActionOfResult())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The OutputPin on which the Classifier instances are placed.
 end-model-doc
Returns:
the value of the '*Result*' containment reference.
See Also:
[`setResult(OutputPin)`](#setResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin))
[`UMLPackage.getReadExtentAction_Result()`](../../metadata/UMLPackage.html#getReadExtentAction_Result())
[`OutputPin.get_readExtentActionOfResult()`](../mdbasicactions/OutputPin.html#get_readExtentActionOfResult())
Model:
opposite="_readExtentActionOfResult" containment="true" resolveProxies="true" required="true" ordered="false"
Generated:
setResult
void setResult(@CheckForNull
 [OutputPin](../mdbasicactions/OutputPin.html) value)
Sets the value of the '[`*Result*`](#getResult())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Result*' containment reference.
See Also:
[`getResult()`](#getResult())
Generated:
getClassifier
@CheckForNull[Classifier](../../classes/mdkernel/Classifier.html) getClassifier()
Returns the value of the '***Classifier***' reference.
 It is bidirectional and its opposite is
 '[`*read Extent Action Of Classifier*`](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Classifier whose instances are to be retrieved.
 end-model-doc
Returns:
the value of the '*Classifier*' reference.
See Also:
[`setClassifier(Classifier)`](#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
[`UMLPackage.getReadExtentAction_Classifier()`](../../metadata/UMLPackage.html#getReadExtentAction_Classifier())
[`Classifier.get_readExtentActionOfClassifier()`](../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier())
Model:
opposite="_readExtentActionOfClassifier" required="true" ordered="false"
Generated:
setClassifier
void setClassifier(@CheckForNull
 [Classifier](../../classes/mdkernel/Classifier.html) value)
Sets the value of the '[`*Classifier*`](#getClassifier())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Classifier*' reference.
See Also:
[`getClassifier()`](#getClassifier())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions</a></div>
<h1 class="title" title="Interface ReadExtentAction">Interface ReadExtentAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code>, <code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../activities/mdstructuredactivities/ExecutableNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ExecutableNode</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ReadExtentAction</span><span class="extends-implements">
extends <a href="../mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Read Extent Action</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A ReadExtentAction is an Action that retrieves the current instances of a Classifier.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getClassifier()"><code><em>Classifier</em></code></a></li>
<li><a href="#getResult()"><code><em>Result</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getReadExtentAction()"><code>UMLPackage.getReadExtentAction()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='actions.mdcompleteactions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClassifier()">getClassifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Classifier</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResult()">getResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Result</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setClassifier</a><wbr/>(<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getClassifier()"><code><em>Classifier</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">setResult</a><wbr/>(<a href="../mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getResult()"><code><em>Result</em></code></a>' containment reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.<a href="../mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></h3>
<code><a href="../mdbasicactions/Action.html#get_actionExecutionSpecificationOfAction()">get_actionExecutionSpecificationOfAction</a>, <a href="../mdbasicactions/Action.html#get_actionInputPinOfFromAction()">get_actionInputPinOfFromAction</a>, <a href="../mdbasicactions/Action.html#get_interactionOfAction()">get_interactionOfAction</a>, <a href="../mdbasicactions/Action.html#getContext()">getContext</a>, <a href="../mdbasicactions/Action.html#getInput()">getInput</a>, <a href="../mdbasicactions/Action.html#getLocalPostcondition()">getLocalPostcondition</a>, <a href="../mdbasicactions/Action.html#getLocalPrecondition()">getLocalPrecondition</a>, <a href="../mdbasicactions/Action.html#getOutput()">getOutput</a>, <a href="../mdbasicactions/Action.html#has_actionExecutionSpecificationOfAction()">has_actionExecutionSpecificationOfAction</a>, <a href="../mdbasicactions/Action.html#hasInput()">hasInput</a>, <a href="../mdbasicactions/Action.html#hasLocalPostcondition()">hasLocalPostcondition</a>, <a href="../mdbasicactions/Action.html#hasLocalPrecondition()">hasLocalPrecondition</a>, <a href="../mdbasicactions/Action.html#hasOutput()">hasOutput</a>, <a href="../mdbasicactions/Action.html#isLocallyReentrant()">isLocallyReentrant</a>, <a href="../mdbasicactions/Action.html#set_actionInputPinOfFromAction(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ActionInputPin)">set_actionInputPinOfFromAction</a>, <a href="../mdbasicactions/Action.html#set_interactionOfAction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">set_interactionOfAction</a>, <a href="../mdbasicactions/Action.html#setLocallyReentrant(boolean)">setLocallyReentrant</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<section class="detail" id="getResult()">
<h3>getResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></span> <span class="element-name">getResult</span>()</div>
<div class="block">Returns the value of the '<em><b>Result</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../mdbasicactions/OutputPin.html#get_readExtentActionOfResult()"><code><em>read Extent Action Of Result</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The OutputPin on which the Classifier instances are placed.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Result</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)"><code>setResult(OutputPin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getReadExtentAction_Result()"><code>UMLPackage.getReadExtentAction_Result()</code></a></li>
<li><a href="../mdbasicactions/OutputPin.html#get_readExtentActionOfResult()"><code>OutputPin.get_readExtentActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_readExtentActionOfResult" containment="true" resolveProxies="true" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OutputPin)">
<h3>setResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getResult()"><code><em>Result</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Result</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getResult()"><code>getResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifier()">
<h3>getClassifier</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getClassifier</span>()</div>
<div class="block">Returns the value of the '<em><b>Classifier</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()"><code><em>read Extent Action Of Classifier</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Classifier whose instances are to be retrieved.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Classifier</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>setClassifier(Classifier)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getReadExtentAction_Classifier()"><code>UMLPackage.getReadExtentAction_Classifier()</code></a></li>
<li><a href="../../classes/mdkernel/Classifier.html#get_readExtentActionOfClassifier()"><code>Classifier.get_readExtentActionOfClassifier()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_readExtentActionOfClassifier" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>setClassifier</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setClassifier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getClassifier()"><code><em>Classifier</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Classifier</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getClassifier()"><code>getClassifier()</code></a></li>
</ul>
</dd>
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
