# JAVA OPENAPI: ActivityEdge (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdbasicactivities/ActivityEdge.html`
- source_sha256: `845200a9016e121d3a3035d9623b3ceb47530e825eee4d773b573fab4a27cfe4`
- captured_utc: `2026-07-14T16:58:50.924438+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities](package-summary.html)

## Interface ActivityEdge

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[ControlFlow](ControlFlow.html)`, `[ObjectFlow](ObjectFlow.html)`

public interfaceActivityEdgeextends [RedefinableElement](../../classes/mdkernel/RedefinableElement.html)

begin-user-doc 
 A representation of the model object '***Activity Edge***'.
 end-user-doc 
begin-model-doc 
 An ActivityEdge is an abstract class for directed connections between two ActivityNodes.
 end-model-doc 
The following features are supported:
 [`*Guard*`](#getGuard())
[`*In Group*`](#getInGroup())
[`*In Partition*`](#getInPartition())
[`*In Structured Node*`](#getInStructuredNode())
[`*Interrupts*`](#getInterrupts())
[`*Redefined Edge*`](#getRedefinedEdge())
[`*activity Edge Of Redefined Edge*`](#get_activityEdgeOfRedefinedEdge())
[`*Source*`](#getSource())
[`*Target*`](#getTarget())
[`*Weight*`](#getWeight())
[`*information Flow Of Realizing Activity Edge*`](#get_informationFlowOfRealizingActivityEdge())
[`*Activity*`](#getActivity())

See Also:
[`UMLPackage.getActivityEdge()`](../../metadata/UMLPackage.html#getActivityEdge())
Model:
abstract="true"
 annotation="MOF package='activities.mdbasicactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](ActivityEdge.html)>`
`[get_activityEdgeOfRedefinedEdge](#get_activityEdgeOfRedefinedEdge())()`
Returns the value of the '***activity Edge Of Redefined Edge***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfRealizingActivityEdge](#get_informationFlowOfRealizingActivityEdge())()`
Returns the value of the '***information Flow Of Realizing Activity Edge***' reference list.
`[Activity](../mdfundamentalactivities/Activity.html)`
`[getActivity](#getActivity())()`
Returns the value of the '***Activity***' container reference.
`[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`
`[getGuard](#getGuard())()`
Returns the value of the '***Guard***' containment reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)>`
`[getInGroup](#getInGroup())()`
Returns the value of the '***In Group***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../mdintermediateactivities/ActivityPartition.html)>`
`[getInPartition](#getInPartition())()`
Returns the value of the '***In Partition***' reference list.
`[StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html)`
`[getInStructuredNode](#getInStructuredNode())()`
Returns the value of the '***In Structured Node***' container reference.
`[InterruptibleActivityRegion](../mdcompleteactivities/InterruptibleActivityRegion.html)`
`[getInterrupts](#getInterrupts())()`
Returns the value of the '***Interrupts***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](ActivityEdge.html)>`
`[getRedefinedEdge](#getRedefinedEdge())()`
Returns the value of the '***Redefined Edge***' reference list.
`[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`
`[getSource](#getSource())()`
Returns the value of the '***Source***' reference.
`[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`
`[getTarget](#getTarget())()`
Returns the value of the '***Target***' reference.
`[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`
`[getWeight](#getWeight())()`
Returns the value of the '***Weight***' containment reference.
`boolean`
`[has_activityEdgeOfRedefinedEdge](#has_activityEdgeOfRedefinedEdge())()`

`boolean`
`[has_informationFlowOfRealizingActivityEdge](#has_informationFlowOfRealizingActivityEdge())()`

`boolean`
`[hasInGroup](#hasInGroup())()`

`boolean`
`[hasInPartition](#hasInPartition())()`

`boolean`
`[hasRedefinedEdge](#hasRedefinedEdge())()`

`void`
`[setActivity](#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))([Activity](../mdfundamentalactivities/Activity.html) value)`
Sets the value of the '[`*Activity*`](#getActivity())' container reference.
`void`
`[setGuard](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)`
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
`void`
`[setInStructuredNode](#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))([StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html) value)`
Sets the value of the '[`*In Structured Node*`](#getInStructuredNode())'
 container reference.
`void`
`[setInterrupts](#setInterrupts(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion))([InterruptibleActivityRegion](../mdcompleteactivities/InterruptibleActivityRegion.html) value)`
Sets the value of the '[`*Interrupts*`](#getInterrupts())' reference.
`void`
`[setSource](#setSource(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode))([ActivityNode](../mdfundamentalactivities/ActivityNode.html) value)`
Sets the value of the '[`*Source*`](#getSource())' reference.
`void`
`[setTarget](#setTarget(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode))([ActivityNode](../mdfundamentalactivities/ActivityNode.html) value)`
Sets the value of the '[`*Target*`](#getTarget())' reference.
`void`
`[setWeight](#setWeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)`
Sets the value of the '[`*Weight*`](#getWeight())' containment reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
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
getActivity
@CheckForNull[Activity](../mdfundamentalactivities/Activity.html) getActivity()
Returns the value of the '***Activity***' container reference.
 It is bidirectional and its opposite is '[`*Edge*`](../mdfundamentalactivities/Activity.html#getEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Activity containing the ActivityEdge, if it is directly owned by an Activity.
 end-model-doc
Returns:
the value of the '*Activity*' container reference.
See Also:
[`setActivity(Activity)`](#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity))
[`UMLPackage.getActivityEdge_Activity()`](../../metadata/UMLPackage.html#getActivityEdge_Activity())
[`Activity.getEdge()`](../mdfundamentalactivities/Activity.html#getEdge())
Model:
opposite="edge" transient="false" ordered="false"
Generated:
setActivity
void setActivity(@CheckForNull
 [Activity](../mdfundamentalactivities/Activity.html) value)
Sets the value of the '[`*Activity*`](#getActivity())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Activity*' container reference.
See Also:
[`getActivity()`](#getActivity())
Generated:
getSource
@CheckForNull[ActivityNode](../mdfundamentalactivities/ActivityNode.html) getSource()
Returns the value of the '***Source***' reference.
 It is bidirectional and its opposite is '[`*Outgoing*`](../mdfundamentalactivities/ActivityNode.html#getOutgoing())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ActivityNode from which tokens are taken when they traverse the ActivityEdge.
 end-model-doc
Returns:
the value of the '*Source*' reference.
See Also:
[`setSource(ActivityNode)`](#setSource(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode))
[`UMLPackage.getActivityEdge_Source()`](../../metadata/UMLPackage.html#getActivityEdge_Source())
[`ActivityNode.getOutgoing()`](../mdfundamentalactivities/ActivityNode.html#getOutgoing())
Model:
opposite="outgoing" required="true" ordered="false"
Generated:
setSource
void setSource(@CheckForNull
 [ActivityNode](../mdfundamentalactivities/ActivityNode.html) value)
Sets the value of the '[`*Source*`](#getSource())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Source*' reference.
See Also:
[`getSource()`](#getSource())
Generated:
getTarget
@CheckForNull[ActivityNode](../mdfundamentalactivities/ActivityNode.html) getTarget()
Returns the value of the '***Target***' reference.
 It is bidirectional and its opposite is '[`*Incoming*`](../mdfundamentalactivities/ActivityNode.html#getIncoming())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ActivityNode to which tokens are put when they traverse the ActivityEdge.
 end-model-doc
Returns:
the value of the '*Target*' reference.
See Also:
[`setTarget(ActivityNode)`](#setTarget(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode))
[`UMLPackage.getActivityEdge_Target()`](../../metadata/UMLPackage.html#getActivityEdge_Target())
[`ActivityNode.getIncoming()`](../mdfundamentalactivities/ActivityNode.html#getIncoming())
Model:
opposite="incoming" required="true" ordered="false"
Generated:
setTarget
void setTarget(@CheckForNull
 [ActivityNode](../mdfundamentalactivities/ActivityNode.html) value)
Sets the value of the '[`*Target*`](#getTarget())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Target*' reference.
See Also:
[`getTarget()`](#getTarget())
Generated:
getInGroup
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityGroup](../mdfundamentalactivities/ActivityGroup.html)> getInGroup()
Returns the value of the '***In Group***' reference list.
 The list contents are of type [`ActivityGroup`](../mdfundamentalactivities/ActivityGroup.html).
 It is bidirectional and its opposite is
 '[`*Contained Edge*`](../mdfundamentalactivities/ActivityGroup.html#getContainedEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityGroups containing the ActivityEdge.
 end-model-doc
Returns:
the value of the '*In Group*' reference list.
See Also:
[`UMLPackage.getActivityEdge_InGroup()`](../../metadata/UMLPackage.html#getActivityEdge_InGroup())
[`ActivityGroup.getContainedEdge()`](../mdfundamentalactivities/ActivityGroup.html#getContainedEdge())
Model:
opposite="containedEdge" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getRedefinedEdge
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](ActivityEdge.html)> getRedefinedEdge()
Returns the value of the '***Redefined Edge***' reference list.
 The list contents are of type [`ActivityEdge`](ActivityEdge.html).
 It is bidirectional and its opposite is
 '[`*activity Edge Of Redefined Edge*`](#get_activityEdgeOfRedefinedEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityEdges from a generalization of the Activity containing this ActivityEdge that are redefined by this ActivityEdge.
 end-model-doc
Returns:
the value of the '*Redefined Edge*' reference list.
See Also:
[`UMLPackage.getActivityEdge_RedefinedEdge()`](../../metadata/UMLPackage.html#getActivityEdge_RedefinedEdge())
[`get_activityEdgeOfRedefinedEdge()`](#get_activityEdgeOfRedefinedEdge())
Model:
opposite="_activityEdgeOfRedefinedEdge" ordered="false"
Generated:
get_activityEdgeOfRedefinedEdge
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityEdge](ActivityEdge.html)> get_activityEdgeOfRedefinedEdge()
Returns the value of the '***activity Edge Of Redefined Edge***' reference list.
 The list contents are of type [`ActivityEdge`](ActivityEdge.html).
 It is bidirectional and its opposite is
 '[`*Redefined Edge*`](#getRedefinedEdge())'.
 begin-user-doc 
If the meaning of the '*activity Edge Of Redefined Edge*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Edge Of Redefined Edge*' reference list.
See Also:
[`UMLPackage.getActivityEdge__activityEdgeOfRedefinedEdge()`](../../metadata/UMLPackage.html#getActivityEdge__activityEdgeOfRedefinedEdge())
[`getRedefinedEdge()`](#getRedefinedEdge())
Model:
opposite="redefinedEdge" ordered="false"
Generated:
getInPartition
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ActivityPartition](../mdintermediateactivities/ActivityPartition.html)> getInPartition()
Returns the value of the '***In Partition***' reference list.
 The list contents are of type [`ActivityPartition`](../mdintermediateactivities/ActivityPartition.html).
 It is bidirectional and its opposite is '[`*Edge*`](../mdintermediateactivities/ActivityPartition.html#getEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 ActivityPartitions containing the ActivityEdge.
 end-model-doc
Returns:
the value of the '*In Partition*' reference list.
See Also:
[`UMLPackage.getActivityEdge_InPartition()`](../../metadata/UMLPackage.html#getActivityEdge_InPartition())
[`ActivityPartition.getEdge()`](../mdintermediateactivities/ActivityPartition.html#getEdge())
Model:
opposite="edge" ordered="false"
Generated:
getGuard
@CheckForNull[ValueSpecification](../../classes/mdkernel/ValueSpecification.html) getGuard()
Returns the value of the '***Guard***' containment reference.
 It is bidirectional and its opposite is
 '[`*activity Edge Of Guard*`](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A ValueSpecification that is evaluated to determine if a token can traverse the ActivityEdge. If an ActivityEdge has no guard, then there is no restriction on
 tokens traversing the edge.
 end-model-doc
Returns:
the value of the '*Guard*' containment reference.
See Also:
[`setGuard(ValueSpecification)`](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getActivityEdge_Guard()`](../../metadata/UMLPackage.html#getActivityEdge_Guard())
[`ValueSpecification.get_activityEdgeOfGuard()`](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard())
Model:
opposite="_activityEdgeOfGuard" containment="true" resolveProxies="true" ordered="false"
Generated:
setGuard
void setGuard(@CheckForNull
 [ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Guard*' containment reference.
See Also:
[`getGuard()`](#getGuard())
Generated:
getWeight
@CheckForNull[ValueSpecification](../../classes/mdkernel/ValueSpecification.html) getWeight()
Returns the value of the '***Weight***' containment reference.
 It is bidirectional and its opposite is
 '[`*activity Edge Of Weight*`](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The minimum number of tokens that must traverse the ActivityEdge at the same time. If no weight is specified, this is equivalent to specifying a constant value
 of 1.
 end-model-doc
Returns:
the value of the '*Weight*' containment reference.
See Also:
[`setWeight(ValueSpecification)`](#setWeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getActivityEdge_Weight()`](../../metadata/UMLPackage.html#getActivityEdge_Weight())
[`ValueSpecification.get_activityEdgeOfWeight()`](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight())
Model:
opposite="_activityEdgeOfWeight" containment="true" resolveProxies="true" ordered="false"
Generated:
setWeight
void setWeight(@CheckForNull
 [ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)
Sets the value of the '[`*Weight*`](#getWeight())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Weight*' containment reference.
See Also:
[`getWeight()`](#getWeight())
Generated:
getInterrupts
@CheckForNull[InterruptibleActivityRegion](../mdcompleteactivities/InterruptibleActivityRegion.html) getInterrupts()
Returns the value of the '***Interrupts***' reference.
 It is bidirectional and its opposite is
 '[`*Interrupting Edge*`](../mdcompleteactivities/InterruptibleActivityRegion.html#getInterruptingEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The InterruptibleActivityRegion for which this ActivityEdge is an interruptingEdge.
 end-model-doc
Returns:
the value of the '*Interrupts*' reference.
See Also:
[`setInterrupts(InterruptibleActivityRegion)`](#setInterrupts(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion))
[`UMLPackage.getActivityEdge_Interrupts()`](../../metadata/UMLPackage.html#getActivityEdge_Interrupts())
[`InterruptibleActivityRegion.getInterruptingEdge()`](../mdcompleteactivities/InterruptibleActivityRegion.html#getInterruptingEdge())
Model:
opposite="interruptingEdge" ordered="false"
Generated:
setInterrupts
void setInterrupts(@CheckForNull
 [InterruptibleActivityRegion](../mdcompleteactivities/InterruptibleActivityRegion.html) value)
Sets the value of the '[`*Interrupts*`](#getInterrupts())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Interrupts*' reference.
See Also:
[`getInterrupts()`](#getInterrupts())
Generated:
getInStructuredNode
@CheckForNull[StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html) getInStructuredNode()
Returns the value of the '***In Structured Node***' container reference.
 It is bidirectional and its opposite is '[`*Edge*`](../mdstructuredactivities/StructuredActivityNode.html#getEdge())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The StructuredActivityNode containing the ActivityEdge, if it is owned by a StructuredActivityNode.
 end-model-doc
Returns:
the value of the '*In Structured Node*' container reference.
See Also:
[`setInStructuredNode(StructuredActivityNode)`](#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))
[`UMLPackage.getActivityEdge_InStructuredNode()`](../../metadata/UMLPackage.html#getActivityEdge_InStructuredNode())
[`StructuredActivityNode.getEdge()`](../mdstructuredactivities/StructuredActivityNode.html#getEdge())
Model:
opposite="edge" transient="false" ordered="false"
Generated:
setInStructuredNode
void setInStructuredNode(@CheckForNull
 [StructuredActivityNode](../mdstructuredactivities/StructuredActivityNode.html) value)
Sets the value of the '[`*In Structured Node*`](#getInStructuredNode())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*In Structured Node*' container reference.
See Also:
[`getInStructuredNode()`](#getInStructuredNode())
Generated:
get_informationFlowOfRealizingActivityEdge
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfRealizingActivityEdge()
Returns the value of the '***information Flow Of Realizing Activity Edge***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Realizing Activity Edge*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingActivityEdge())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Realizing Activity Edge*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Realizing Activity Edge*' reference list.
See Also:
[`UMLPackage.getActivityEdge__informationFlowOfRealizingActivityEdge()`](../../metadata/UMLPackage.html#getActivityEdge__informationFlowOfRealizingActivityEdge())
[`InformationFlow.getRealizingActivityEdge()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingActivityEdge())
Model:
opposite="realizingActivityEdge" ordered="false"
Generated:
hasInGroup
boolean hasInGroup()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedEdge
boolean hasRedefinedEdge()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_activityEdgeOfRedefinedEdge
boolean has_activityEdgeOfRedefinedEdge()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasInPartition
boolean hasInPartition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfRealizingActivityEdge
boolean has_informationFlowOfRealizingActivityEdge()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities</a></div>
<h1 class="title" title="Interface ActivityEdge">Interface ActivityEdge</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code>, <code><a href="ObjectFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectFlow</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ActivityEdge</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Activity Edge</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ActivityEdge is an abstract class for directed connections between two ActivityNodes.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getGuard()"><code><em>Guard</em></code></a></li>
<li><a href="#getInGroup()"><code><em>In Group</em></code></a></li>
<li><a href="#getInPartition()"><code><em>In Partition</em></code></a></li>
<li><a href="#getInStructuredNode()"><code><em>In Structured Node</em></code></a></li>
<li><a href="#getInterrupts()"><code><em>Interrupts</em></code></a></li>
<li><a href="#getRedefinedEdge()"><code><em>Redefined Edge</em></code></a></li>
<li><a href="#get_activityEdgeOfRedefinedEdge()"><code><em>activity Edge Of Redefined Edge</em></code></a></li>
<li><a href="#getSource()"><code><em>Source</em></code></a></li>
<li><a href="#getTarget()"><code><em>Target</em></code></a></li>
<li><a href="#getWeight()"><code><em>Weight</em></code></a></li>
<li><a href="#get_informationFlowOfRealizingActivityEdge()"><code><em>information Flow Of Realizing Activity Edge</em></code></a></li>
<li><a href="#getActivity()"><code><em>Activity</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge()"><code>UMLPackage.getActivityEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='activities.mdbasicactivities'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityEdgeOfRedefinedEdge()">get_activityEdgeOfRedefinedEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Edge Of Redefined Edge</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfRealizingActivityEdge()">get_informationFlowOfRealizingActivityEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Activity Edge</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActivity()">getActivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Activity</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGuard()">getGuard</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInGroup()">getInGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>In Group</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInPartition()">getInPartition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>In Partition</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInStructuredNode()">getInStructuredNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>In Structured Node</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInterrupts()">getInterrupts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Interrupts</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedEdge()">getRedefinedEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Edge</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Source</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Target</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWeight()">getWeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Weight</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_activityEdgeOfRedefinedEdge()">has_activityEdgeOfRedefinedEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfRealizingActivityEdge()">has_informationFlowOfRealizingActivityEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasInGroup()">hasInGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasInPartition()">hasInPartition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedEdge()">hasRedefinedEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a><wbr/>(<a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getActivity()"><code><em>Activity</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setGuard</a><wbr/>(<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a><wbr/>(<a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInStructuredNode()"><code><em>In Structured Node</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInterrupts(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion)">setInterrupts</a><wbr/>(<a href="../mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInterrupts()"><code><em>Interrupts</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSource(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">setSource</a><wbr/>(<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTarget(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">setTarget</a><wbr/>(<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setWeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setWeight</a><wbr/>(<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getWeight()"><code><em>Weight</em></code></a>' containment reference.</div>
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
<section class="detail" id="getActivity()">
<h3>getActivity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getActivity</span>()</div>
<div class="block">Returns the value of the '<em><b>Activity</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdfundamentalactivities/Activity.html#getEdge()"><code><em>Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Activity containing the ActivityEdge, if it is directly owned by an Activity.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Activity</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)"><code>setActivity(Activity)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Activity()"><code>UMLPackage.getActivityEdge_Activity()</code></a></li>
<li><a href="../mdfundamentalactivities/Activity.html#getEdge()"><code>Activity.getEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="edge" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">
<h3>setActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setActivity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getActivity()"><code><em>Activity</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Activity</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getActivity()"><code>getActivity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></span> <span class="element-name">getSource</span>()</div>
<div class="block">Returns the value of the '<em><b>Source</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()"><code><em>Outgoing</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ActivityNode from which tokens are taken when they traverse the ActivityEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Source</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSource(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)"><code>setSource(ActivityNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Source()"><code>UMLPackage.getActivityEdge_Source()</code></a></li>
<li><a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()"><code>ActivityNode.getOutgoing()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="outgoing" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSource(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">
<h3>setSource</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSource</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Source</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSource()"><code>getSource()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></span> <span class="element-name">getTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>Target</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()"><code><em>Incoming</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ActivityNode to which tokens are put when they traverse the ActivityEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Target</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setTarget(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)"><code>setTarget(ActivityNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Target()"><code>UMLPackage.getActivityEdge_Target()</code></a></li>
<li><a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()"><code>ActivityNode.getIncoming()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="incoming" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode)">
<h3>setTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Target</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getTarget()"><code>getTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInGroup()">
<h3>getInGroup</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityGroup</a>&gt;</span> <span class="element-name">getInGroup</span>()</div>
<div class="block">Returns the value of the '<em><b>In Group</b></em>' reference list.
 The list contents are of type <a href="../mdfundamentalactivities/ActivityGroup.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities"><code>ActivityGroup</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()"><code><em>Contained Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityGroups containing the ActivityEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>In Group</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_InGroup()"><code>UMLPackage.getActivityEdge_InGroup()</code></a></li>
<li><a href="../mdfundamentalactivities/ActivityGroup.html#getContainedEdge()"><code>ActivityGroup.getContainedEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="containedEdge" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedEdge()">
<h3>getRedefinedEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</span> <span class="element-name">getRedefinedEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Edge</b></em>' reference list.
 The list contents are of type <a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_activityEdgeOfRedefinedEdge()"><code><em>activity Edge Of Redefined Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityEdges from a generalization of the Activity containing this ActivityEdge that are redefined by this ActivityEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Edge</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_RedefinedEdge()"><code>UMLPackage.getActivityEdge_RedefinedEdge()</code></a></li>
<li><a href="#get_activityEdgeOfRedefinedEdge()"><code>get_activityEdgeOfRedefinedEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_activityEdgeOfRedefinedEdge" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityEdgeOfRedefinedEdge()">
<h3>get_activityEdgeOfRedefinedEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a>&gt;</span> <span class="element-name">get_activityEdgeOfRedefinedEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Edge Of Redefined Edge</b></em>' reference list.
 The list contents are of type <a href="ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ActivityEdge</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedEdge()"><code><em>Redefined Edge</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Edge Of Redefined Edge</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Edge Of Redefined Edge</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge__activityEdgeOfRedefinedEdge()"><code>UMLPackage.getActivityEdge__activityEdgeOfRedefinedEdge()</code></a></li>
<li><a href="#getRedefinedEdge()"><code>getRedefinedEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedEdge" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInPartition()">
<h3>getInPartition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>&gt;</span> <span class="element-name">getInPartition</span>()</div>
<div class="block">Returns the value of the '<em><b>In Partition</b></em>' reference list.
 The list contents are of type <a href="../mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities"><code>ActivityPartition</code></a>.
 It is bidirectional and its opposite is '<a href="../mdintermediateactivities/ActivityPartition.html#getEdge()"><code><em>Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 ActivityPartitions containing the ActivityEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>In Partition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_InPartition()"><code>UMLPackage.getActivityEdge_InPartition()</code></a></li>
<li><a href="../mdintermediateactivities/ActivityPartition.html#getEdge()"><code>ActivityPartition.getEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="edge" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGuard()">
<h3>getGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard()"><code><em>activity Edge Of Guard</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A ValueSpecification that is evaluated to determine if a token can traverse the ActivityEdge. If an ActivityEdge has no guard, then there is no restriction on
 tokens traversing the edge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Guard</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setGuard(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Guard()"><code>UMLPackage.getActivityEdge_Guard()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard()"><code>ValueSpecification.get_activityEdgeOfGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_activityEdgeOfGuard" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Guard</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getGuard()"><code>getGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWeight()">
<h3>getWeight</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getWeight</span>()</div>
<div class="block">Returns the value of the '<em><b>Weight</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight()"><code><em>activity Edge Of Weight</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The minimum number of tokens that must traverse the ActivityEdge at the same time. If no weight is specified, this is equivalent to specifying a constant value
 of 1.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Weight</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setWeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setWeight(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Weight()"><code>UMLPackage.getActivityEdge_Weight()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight()"><code>ValueSpecification.get_activityEdgeOfWeight()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_activityEdgeOfWeight" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWeight(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setWeight</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setWeight</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getWeight()"><code><em>Weight</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Weight</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getWeight()"><code>getWeight()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterrupts()">
<h3>getInterrupts</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a></span> <span class="element-name">getInterrupts</span>()</div>
<div class="block">Returns the value of the '<em><b>Interrupts</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactivities/InterruptibleActivityRegion.html#getInterruptingEdge()"><code><em>Interrupting Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The InterruptibleActivityRegion for which this ActivityEdge is an interruptingEdge.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Interrupts</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setInterrupts(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion)"><code>setInterrupts(InterruptibleActivityRegion)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_Interrupts()"><code>UMLPackage.getActivityEdge_Interrupts()</code></a></li>
<li><a href="../mdcompleteactivities/InterruptibleActivityRegion.html#getInterruptingEdge()"><code>InterruptibleActivityRegion.getInterruptingEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="interruptingEdge" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInterrupts(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.InterruptibleActivityRegion)">
<h3>setInterrupts</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInterrupts</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactivities/InterruptibleActivityRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">InterruptibleActivityRegion</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInterrupts()"><code><em>Interrupts</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Interrupts</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getInterrupts()"><code>getInterrupts()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInStructuredNode()">
<h3>getInStructuredNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">getInStructuredNode</span>()</div>
<div class="block">Returns the value of the '<em><b>In Structured Node</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdstructuredactivities/StructuredActivityNode.html#getEdge()"><code><em>Edge</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The StructuredActivityNode containing the ActivityEdge, if it is owned by a StructuredActivityNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>In Structured Node</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)"><code>setInStructuredNode(StructuredActivityNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getActivityEdge_InStructuredNode()"><code>UMLPackage.getActivityEdge_InStructuredNode()</code></a></li>
<li><a href="../mdstructuredactivities/StructuredActivityNode.html#getEdge()"><code>StructuredActivityNode.getEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="edge" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">
<h3>setInStructuredNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInStructuredNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInStructuredNode()"><code><em>In Structured Node</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>In Structured Node</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getInStructuredNode()"><code>getInStructuredNode()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfRealizingActivityEdge()">
<h3>get_informationFlowOfRealizingActivityEdge</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfRealizingActivityEdge</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Activity Edge</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingActivityEdge()"><code><em>Realizing Activity Edge</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Realizing Activity Edge</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Realizing Activity Edge</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getActivityEdge__informationFlowOfRealizingActivityEdge()"><code>UMLPackage.getActivityEdge__informationFlowOfRealizingActivityEdge()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingActivityEdge()"><code>InformationFlow.getRealizingActivityEdge()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="realizingActivityEdge" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInGroup()">
<h3>hasInGroup</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasInGroup</span>()
            throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedEdge()">
<h3>hasRedefinedEdge</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedEdge</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_activityEdgeOfRedefinedEdge()">
<h3>has_activityEdgeOfRedefinedEdge</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_activityEdgeOfRedefinedEdge</span>()
                                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInPartition()">
<h3>hasInPartition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasInPartition</span>()
                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfRealizingActivityEdge()">
<h3>has_informationFlowOfRealizingActivityEdge</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfRealizingActivityEdge</span>()
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
