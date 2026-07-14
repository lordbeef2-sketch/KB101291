# JAVA OPENAPI: Trigger (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html
- source_path: `com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdcommunications/Trigger.html`
- source_sha256: `ba1a62a11c7e2fc7b59ec3e5d61172ba377b9e1cda47069fce1239eb2aec9bd8`
- captured_utc: `2026-07-14T16:46:31.044214+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications](package-summary.html)

## Interface Trigger

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceTriggerextends [NamedElement](../../classes/mdkernel/NamedElement.html)

begin-user-doc 
 A representation of the model object '***Trigger***'.
 end-user-doc 
begin-model-doc 
 A Trigger specifies a specific point at which an Event occurrence may trigger an effect in a Behavior. A Trigger may be qualified by the Port on which the Event
 occurred.
 end-model-doc 
The following features are supported:
 [`*Port*`](#getPort())
[`*state Of Deferrable Trigger*`](#get_stateOfDeferrableTrigger())
[`*transition Of Trigger*`](#get_transitionOfTrigger())
[`*accept Event Action Of Trigger*`](#get_acceptEventActionOfTrigger())
[`*reply Action Of Reply To Call*`](#get_replyActionOfReplyToCall())
[`*Event*`](#getEvent())

See Also:
[`UMLPackage.getTrigger()`](../../metadata/UMLPackage.html#getTrigger())
Model:
annotation="MOF package='commonbehaviors.mdcommunications'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html)`
`[get_acceptEventActionOfTrigger](#get_acceptEventActionOfTrigger())()`
Returns the value of the '***accept Event Action Of Trigger***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)>`
`[get_replyActionOfReplyToCall](#get_replyActionOfReplyToCall())()`
Returns the value of the '***reply Action Of Reply To Call***' reference list.
`[State](../../statemachines/mdbehaviorstatemachines/State.html)`
`[get_stateOfDeferrableTrigger](#get_stateOfDeferrableTrigger())()`
Returns the value of the '***state Of Deferrable Trigger***' container reference.
`[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`
`[get_transitionOfTrigger](#get_transitionOfTrigger())()`
Returns the value of the '***transition Of Trigger***' container reference.
`[Event](Event.html)`
`[getEvent](#getEvent())()`
Returns the value of the '***Event***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Port](../../compositestructures/mdports/Port.html)>`
`[getPort](#getPort())()`
Returns the value of the '***Port***' reference list.
`boolean`
`[has_replyActionOfReplyToCall](#has_replyActionOfReplyToCall())()`

`boolean`
`[hasPort](#hasPort())()`

`void`
`[set_acceptEventActionOfTrigger](#set_acceptEventActionOfTrigger(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html) value)`
Sets the value of the
 '[`*accept Event Action Of Trigger*`](#get_acceptEventActionOfTrigger())'
 container reference.
`void`
`[set_stateOfDeferrableTrigger](#set_stateOfDeferrableTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../statemachines/mdbehaviorstatemachines/State.html) value)`
Sets the value of the
 '[`*state Of Deferrable Trigger*`](#get_stateOfDeferrableTrigger())' container
 reference.
`void`
`[set_transitionOfTrigger](#set_transitionOfTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)`
Sets the value of the '[`*transition Of Trigger*`](#get_transitionOfTrigger())'
 container reference.
`void`
`[setEvent](#setEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))([Event](Event.html) value)`
Sets the value of the '[`*Event*`](#getEvent())' reference.
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
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
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
getPort
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Port](../../compositestructures/mdports/Port.html)> getPort()
Returns the value of the '***Port***' reference list.
 The list contents are of type [`Port`](../../compositestructures/mdports/Port.html).
 It is bidirectional and its opposite is '[`*trigger Of Port*`](../../compositestructures/mdports/Port.html#get_triggerOfPort())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A optional Port of through which the given effect is detected.
 end-model-doc
Returns:
the value of the '*Port*' reference list.
See Also:
[`UMLPackage.getTrigger_Port()`](../../metadata/UMLPackage.html#getTrigger_Port())
[`Port.get_triggerOfPort()`](../../compositestructures/mdports/Port.html#get_triggerOfPort())
Model:
opposite="_triggerOfPort" ordered="false"
Generated:
get_acceptEventActionOfTrigger
@CheckForNull[AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html) get_acceptEventActionOfTrigger()
Returns the value of the '***accept Event Action Of Trigger***' container reference.
 It is bidirectional and its opposite is '[`*Trigger*`](../../actions/mdcompleteactions/AcceptEventAction.html#getTrigger())'.
 begin-user-doc 
If the meaning of the '*accept Event Action Of Trigger*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*accept Event Action Of Trigger*' container reference.
See Also:
[`set_acceptEventActionOfTrigger(AcceptEventAction)`](#set_acceptEventActionOfTrigger(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))
[`UMLPackage.getTrigger__acceptEventActionOfTrigger()`](../../metadata/UMLPackage.html#getTrigger__acceptEventActionOfTrigger())
[`AcceptEventAction.getTrigger()`](../../actions/mdcompleteactions/AcceptEventAction.html#getTrigger())
Model:
opposite="trigger" transient="false" ordered="false"
Generated:
set_acceptEventActionOfTrigger
void set_acceptEventActionOfTrigger(@CheckForNull
 [AcceptEventAction](../../actions/mdcompleteactions/AcceptEventAction.html) value)
Sets the value of the
 '[`*accept Event Action Of Trigger*`](#get_acceptEventActionOfTrigger())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*accept Event Action Of Trigger*' container reference.
See Also:
[`get_acceptEventActionOfTrigger()`](#get_acceptEventActionOfTrigger())
Generated:
get_replyActionOfReplyToCall
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ReplyAction](../../actions/mdcompleteactions/ReplyAction.html)> get_replyActionOfReplyToCall()
Returns the value of the '***reply Action Of Reply To Call***' reference list.
 The list contents are of type [`ReplyAction`](../../actions/mdcompleteactions/ReplyAction.html).
 It is bidirectional and its opposite is '[`*Reply To Call*`](../../actions/mdcompleteactions/ReplyAction.html#getReplyToCall())'.
 begin-user-doc 
If the meaning of the '*reply Action Of Reply To Call*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reply Action Of Reply To Call*' reference list.
See Also:
[`UMLPackage.getTrigger__replyActionOfReplyToCall()`](../../metadata/UMLPackage.html#getTrigger__replyActionOfReplyToCall())
[`ReplyAction.getReplyToCall()`](../../actions/mdcompleteactions/ReplyAction.html#getReplyToCall())
Model:
opposite="replyToCall" ordered="false"
Generated:
get_transitionOfTrigger
@CheckForNull[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) get_transitionOfTrigger()
Returns the value of the '***transition Of Trigger***' container reference.
 It is bidirectional and its opposite is '[`*Trigger*`](../../statemachines/mdbehaviorstatemachines/Transition.html#getTrigger())'.
 begin-user-doc 
If the meaning of the '*transition Of Trigger*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*transition Of Trigger*' container reference.
See Also:
[`set_transitionOfTrigger(Transition)`](#set_transitionOfTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))
[`UMLPackage.getTrigger__transitionOfTrigger()`](../../metadata/UMLPackage.html#getTrigger__transitionOfTrigger())
[`Transition.getTrigger()`](../../statemachines/mdbehaviorstatemachines/Transition.html#getTrigger())
Model:
opposite="trigger" transient="false" ordered="false"
Generated:
set_transitionOfTrigger
void set_transitionOfTrigger(@CheckForNull
 [Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)
Sets the value of the '[`*transition Of Trigger*`](#get_transitionOfTrigger())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*transition Of Trigger*' container reference.
See Also:
[`get_transitionOfTrigger()`](#get_transitionOfTrigger())
Generated:
get_stateOfDeferrableTrigger
@CheckForNull[State](../../statemachines/mdbehaviorstatemachines/State.html) get_stateOfDeferrableTrigger()
Returns the value of the '***state Of Deferrable Trigger***' container reference.
 It is bidirectional and its opposite is
 '[`*Deferrable Trigger*`](../../statemachines/mdbehaviorstatemachines/State.html#getDeferrableTrigger())'.
 begin-user-doc 
If the meaning of the '*state Of Deferrable Trigger*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Of Deferrable Trigger*' container reference.
See Also:
[`set_stateOfDeferrableTrigger(State)`](#set_stateOfDeferrableTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getTrigger__stateOfDeferrableTrigger()`](../../metadata/UMLPackage.html#getTrigger__stateOfDeferrableTrigger())
[`State.getDeferrableTrigger()`](../../statemachines/mdbehaviorstatemachines/State.html#getDeferrableTrigger())
Model:
opposite="deferrableTrigger" transient="false" ordered="false"
Generated:
set_stateOfDeferrableTrigger
void set_stateOfDeferrableTrigger(@CheckForNull
 [State](../../statemachines/mdbehaviorstatemachines/State.html) value)
Sets the value of the
 '[`*state Of Deferrable Trigger*`](#get_stateOfDeferrableTrigger())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*state Of Deferrable Trigger*' container reference.
See Also:
[`get_stateOfDeferrableTrigger()`](#get_stateOfDeferrableTrigger())
Generated:
getEvent
@CheckForNull[Event](Event.html) getEvent()
Returns the value of the '***Event***' reference.
 It is bidirectional and its opposite is
 '[`*trigger Of Event*`](Event.html#get_triggerOfEvent())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Event that detected by the Trigger.
 end-model-doc
Returns:
the value of the '*Event*' reference.
See Also:
[`setEvent(Event)`](#setEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))
[`UMLPackage.getTrigger_Event()`](../../metadata/UMLPackage.html#getTrigger_Event())
[`Event.get_triggerOfEvent()`](Event.html#get_triggerOfEvent())
Model:
opposite="_triggerOfEvent" required="true" ordered="false"
Generated:
setEvent
void setEvent(@CheckForNull
 [Event](Event.html) value)
Sets the value of the '[`*Event*`](#getEvent())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Event*' reference.
See Also:
[`getEvent()`](#getEvent())
Generated:
hasPort
boolean hasPort()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_replyActionOfReplyToCall
boolean has_replyActionOfReplyToCall()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications</a></div>
<h1 class="title" title="Interface Trigger">Interface Trigger</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Trigger</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Trigger</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Trigger specifies a specific point  at which an Event occurrence may trigger an effect in a Behavior. A Trigger may be qualified by the Port on which the Event
 occurred.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getPort()"><code><em>Port</em></code></a></li>
<li><a href="#get_stateOfDeferrableTrigger()"><code><em>state Of Deferrable Trigger</em></code></a></li>
<li><a href="#get_transitionOfTrigger()"><code><em>transition Of Trigger</em></code></a></li>
<li><a href="#get_acceptEventActionOfTrigger()"><code><em>accept Event Action Of Trigger</em></code></a></li>
<li><a href="#get_replyActionOfReplyToCall()"><code><em>reply Action Of Reply To Call</em></code></a></li>
<li><a href="#getEvent()"><code><em>Event</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getTrigger()"><code>UMLPackage.getTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='commonbehaviors.mdcommunications'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_acceptEventActionOfTrigger()">get_acceptEventActionOfTrigger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>accept Event Action Of Trigger</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_replyActionOfReplyToCall()">get_replyActionOfReplyToCall</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reply Action Of Reply To Call</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateOfDeferrableTrigger()">get_stateOfDeferrableTrigger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Of Deferrable Trigger</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_transitionOfTrigger()">get_transitionOfTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>transition Of Trigger</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEvent()">getEvent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Event</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPort()">getPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Port</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_replyActionOfReplyToCall()">has_replyActionOfReplyToCall</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPort()">hasPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_acceptEventActionOfTrigger(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">set_acceptEventActionOfTrigger</a><wbr/>(<a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_acceptEventActionOfTrigger()"><code><em>accept Event Action Of Trigger</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stateOfDeferrableTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">set_stateOfDeferrableTrigger</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_stateOfDeferrableTrigger()"><code><em>state Of Deferrable Trigger</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_transitionOfTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">set_transitionOfTrigger</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_transitionOfTrigger()"><code><em>transition Of Trigger</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">setEvent</a><wbr/>(<a href="Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getEvent()"><code><em>Event</em></code></a>' reference.</div>
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
<section class="detail" id="getPort()">
<h3>getPort</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</span> <span class="element-name">getPort</span>()</div>
<div class="block">Returns the value of the '<em><b>Port</b></em>' reference list.
 The list contents are of type <a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports"><code>Port</code></a>.
 It is bidirectional and its opposite is '<a href="../../compositestructures/mdports/Port.html#get_triggerOfPort()"><code><em>trigger Of Port</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A optional Port of through which the given effect is detected.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Port</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getTrigger_Port()"><code>UMLPackage.getTrigger_Port()</code></a></li>
<li><a href="../../compositestructures/mdports/Port.html#get_triggerOfPort()"><code>Port.get_triggerOfPort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_triggerOfPort" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_acceptEventActionOfTrigger()">
<h3>get_acceptEventActionOfTrigger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></span> <span class="element-name">get_acceptEventActionOfTrigger</span>()</div>
<div class="block">Returns the value of the '<em><b>accept Event Action Of Trigger</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/AcceptEventAction.html#getTrigger()"><code><em>Trigger</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>accept Event Action Of Trigger</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>accept Event Action Of Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_acceptEventActionOfTrigger(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)"><code>set_acceptEventActionOfTrigger(AcceptEventAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTrigger__acceptEventActionOfTrigger()"><code>UMLPackage.getTrigger__acceptEventActionOfTrigger()</code></a></li>
<li><a href="../../actions/mdcompleteactions/AcceptEventAction.html#getTrigger()"><code>AcceptEventAction.getTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="trigger" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_acceptEventActionOfTrigger(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>set_acceptEventActionOfTrigger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_acceptEventActionOfTrigger</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_acceptEventActionOfTrigger()"><code><em>accept Event Action Of Trigger</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>accept Event Action Of Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_acceptEventActionOfTrigger()"><code>get_acceptEventActionOfTrigger()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_replyActionOfReplyToCall()">
<h3>get_replyActionOfReplyToCall</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a>&gt;</span> <span class="element-name">get_replyActionOfReplyToCall</span>()</div>
<div class="block">Returns the value of the '<em><b>reply Action Of Reply To Call</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions"><code>ReplyAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdcompleteactions/ReplyAction.html#getReplyToCall()"><code><em>Reply To Call</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reply Action Of Reply To Call</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reply Action Of Reply To Call</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getTrigger__replyActionOfReplyToCall()"><code>UMLPackage.getTrigger__replyActionOfReplyToCall()</code></a></li>
<li><a href="../../actions/mdcompleteactions/ReplyAction.html#getReplyToCall()"><code>ReplyAction.getReplyToCall()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="replyToCall" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_transitionOfTrigger()">
<h3>get_transitionOfTrigger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">get_transitionOfTrigger</span>()</div>
<div class="block">Returns the value of the '<em><b>transition Of Trigger</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getTrigger()"><code><em>Trigger</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>transition Of Trigger</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>transition Of Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_transitionOfTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)"><code>set_transitionOfTrigger(Transition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTrigger__transitionOfTrigger()"><code>UMLPackage.getTrigger__transitionOfTrigger()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getTrigger()"><code>Transition.getTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="trigger" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_transitionOfTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>set_transitionOfTrigger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_transitionOfTrigger</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_transitionOfTrigger()"><code><em>transition Of Trigger</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>transition Of Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_transitionOfTrigger()"><code>get_transitionOfTrigger()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateOfDeferrableTrigger()">
<h3>get_stateOfDeferrableTrigger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">get_stateOfDeferrableTrigger</span>()</div>
<div class="block">Returns the value of the '<em><b>state Of Deferrable Trigger</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdbehaviorstatemachines/State.html#getDeferrableTrigger()"><code><em>Deferrable Trigger</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Of Deferrable Trigger</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Of Deferrable Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_stateOfDeferrableTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>set_stateOfDeferrableTrigger(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTrigger__stateOfDeferrableTrigger()"><code>UMLPackage.getTrigger__stateOfDeferrableTrigger()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#getDeferrableTrigger()"><code>State.getDeferrableTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="deferrableTrigger" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stateOfDeferrableTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>set_stateOfDeferrableTrigger</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stateOfDeferrableTrigger</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_stateOfDeferrableTrigger()"><code><em>state Of Deferrable Trigger</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>state Of Deferrable Trigger</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#get_stateOfDeferrableTrigger()"><code>get_stateOfDeferrableTrigger()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEvent()">
<h3>getEvent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></span> <span class="element-name">getEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>Event</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="Event.html#get_triggerOfEvent()"><code><em>trigger Of Event</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Event that detected by the Trigger.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#setEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)"><code>setEvent(Event)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTrigger_Event()"><code>UMLPackage.getTrigger_Event()</code></a></li>
<li><a href="Event.html#get_triggerOfEvent()"><code>Event.get_triggerOfEvent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_triggerOfEvent" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">
<h3>setEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEvent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getEvent()"><code><em>Event</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getEvent()"><code>getEvent()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPort()">
<h3>hasPort</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPort</span>()
         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_replyActionOfReplyToCall()">
<h3>has_replyActionOfReplyToCall</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_replyActionOfReplyToCall</span>()
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
