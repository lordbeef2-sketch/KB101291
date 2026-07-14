# JAVA OPENAPI: Gate (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/interactions/mdfragments/Gate.html
- source_path: `com/nomagic/uml2/ext/magicdraw/interactions/mdfragments/Gate.html`
- source_sha256: `cb411973d13e471b042a434281e02ad6cf92bb555ac9313eac5c2663ef88c00b`
- captured_utc: `2026-07-14T16:53:01.165507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.interactions.mdfragments](package-summary.html)

## Interface Gate

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[MessageEnd](../mdbasicinteractions/MessageEnd.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceGateextends [MessageEnd](../mdbasicinteractions/MessageEnd.html)

begin-user-doc 
 A representation of the model object '***Gate***'.
 end-user-doc 
begin-model-doc 
 A Gate is a MessageEnd which serves as a connection point for relating a Message which has a MessageEnd (sendEvent / receiveEvent) outside an InteractionFragment
 with another Message which has a MessageEnd (receiveEvent / sendEvent) inside that InteractionFragment.
 end-model-doc 
The following features are supported:
 [`*Formal Gate*`](#getFormalGate())
[`*gate Of Formal Gate*`](#get_gateOfFormalGate())
[`*combined Fragment Of Cfragment Gate*`](#get_combinedFragmentOfCfragmentGate())
[`*interaction Of Formal Gate*`](#get_interactionOfFormalGate())
[`*interaction Use Of Actual Gate*`](#get_interactionUseOfActualGate())

See Also:
[`UMLPackage.getGate()`](../../metadata/UMLPackage.html#getGate())
Model:
annotation="MOF package='interactions.mdfragments'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[CombinedFragment](CombinedFragment.html)`
`[get_combinedFragmentOfCfragmentGate](#get_combinedFragmentOfCfragmentGate())()`
Returns the value of the '***combined Fragment Of Cfragment Gate***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Gate](Gate.html)>`
`[get_gateOfFormalGate](#get_gateOfFormalGate())()`
Returns the value of the '***gate Of Formal Gate***' reference list.
`[Interaction](../mdbasicinteractions/Interaction.html)`
`[get_interactionOfFormalGate](#get_interactionOfFormalGate())()`
Returns the value of the '***interaction Of Formal Gate***' container reference.
`[InteractionUse](InteractionUse.html)`
`[get_interactionUseOfActualGate](#get_interactionUseOfActualGate())()`
Returns the value of the '***interaction Use Of Actual Gate***' container reference.
`[Gate](Gate.html)`
`[getFormalGate](#getFormalGate())()`
Returns the value of the '***Formal Gate***' reference.
`boolean`
`[has_gateOfFormalGate](#has_gateOfFormalGate())()`

`void`
`[set_combinedFragmentOfCfragmentGate](#set_combinedFragmentOfCfragmentGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))([CombinedFragment](CombinedFragment.html) value)`
Sets the value of the
 '[`*combined Fragment Of Cfragment Gate*`](#get_combinedFragmentOfCfragmentGate())' container
 reference.
`void`
`[set_interactionOfFormalGate](#set_interactionOfFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([Interaction](../mdbasicinteractions/Interaction.html) value)`
Sets the value of the '[`*interaction Of Formal Gate*`](#get_interactionOfFormalGate())'
 container reference.
`void`
`[set_interactionUseOfActualGate](#set_interactionUseOfActualGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))([InteractionUse](InteractionUse.html) value)`
Sets the value of the
 '[`*interaction Use Of Actual Gate*`](#get_interactionUseOfActualGate())' container reference.
`void`
`[setFormalGate](#setFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate))([Gate](Gate.html) value)`
Sets the value of the '[`*Formal Gate*`](#getFormalGate())' reference.
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.[MessageEnd](../mdbasicinteractions/MessageEnd.html)
`[get_messageOfReceiveEvent](../mdbasicinteractions/MessageEnd.html#get_messageOfReceiveEvent()), [get_messageOfSendEvent](../mdbasicinteractions/MessageEnd.html#get_messageOfSendEvent()), [getMessage](../mdbasicinteractions/MessageEnd.html#getMessage()), [set_messageOfReceiveEvent](../mdbasicinteractions/MessageEnd.html#set_messageOfReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [set_messageOfSendEvent](../mdbasicinteractions/MessageEnd.html#set_messageOfSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [setMessage](../mdbasicinteractions/MessageEnd.html#setMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
getFormalGate
@CheckForNull[Gate](Gate.html) getFormalGate()
Returns the value of the '***Formal Gate***' reference.
 It is bidirectional and its opposite is '[`*gate Of Formal Gate*`](#get_gateOfFormalGate())'.
 begin-user-doc 
If the meaning of the '*Formal Gate*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Formal Gate*' reference.
See Also:
[`setFormalGate(Gate)`](#setFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate))
[`UMLPackage.getGate_FormalGate()`](../../metadata/UMLPackage.html#getGate_FormalGate())
[`get_gateOfFormalGate()`](#get_gateOfFormalGate())
Model:
opposite="_gateOfFormalGate" ordered="false"
Generated:
setFormalGate
void setFormalGate(@CheckForNull
 [Gate](Gate.html) value)
Sets the value of the '[`*Formal Gate*`](#getFormalGate())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Formal Gate*' reference.
See Also:
[`getFormalGate()`](#getFormalGate())
Generated:
get_gateOfFormalGate
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Gate](Gate.html)> get_gateOfFormalGate()
Returns the value of the '***gate Of Formal Gate***' reference list.
 The list contents are of type [`Gate`](Gate.html).
 It is bidirectional and its opposite is '[`*Formal Gate*`](#getFormalGate())'.
 begin-user-doc 
If the meaning of the '*gate Of Formal Gate*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*gate Of Formal Gate*' reference list.
See Also:
[`UMLPackage.getGate__gateOfFormalGate()`](../../metadata/UMLPackage.html#getGate__gateOfFormalGate())
[`getFormalGate()`](#getFormalGate())
Model:
opposite="formalGate" ordered="false"
Generated:
get_combinedFragmentOfCfragmentGate
@CheckForNull[CombinedFragment](CombinedFragment.html) get_combinedFragmentOfCfragmentGate()
Returns the value of the '***combined Fragment Of Cfragment Gate***' container reference.
 It is bidirectional and its opposite is
 '[`*Cfragment Gate*`](CombinedFragment.html#getCfragmentGate())'.
 begin-user-doc 
If the meaning of the '*combined Fragment Of Cfragment Gate*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*combined Fragment Of Cfragment Gate*' container reference.
See Also:
[`set_combinedFragmentOfCfragmentGate(CombinedFragment)`](#set_combinedFragmentOfCfragmentGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))
[`UMLPackage.getGate__combinedFragmentOfCfragmentGate()`](../../metadata/UMLPackage.html#getGate__combinedFragmentOfCfragmentGate())
[`CombinedFragment.getCfragmentGate()`](CombinedFragment.html#getCfragmentGate())
Model:
opposite="cfragmentGate" transient="false" ordered="false"
Generated:
set_combinedFragmentOfCfragmentGate
void set_combinedFragmentOfCfragmentGate(@CheckForNull
 [CombinedFragment](CombinedFragment.html) value)
Sets the value of the
 '[`*combined Fragment Of Cfragment Gate*`](#get_combinedFragmentOfCfragmentGate())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*combined Fragment Of Cfragment Gate*' container reference.
See Also:
[`get_combinedFragmentOfCfragmentGate()`](#get_combinedFragmentOfCfragmentGate())
Generated:
get_interactionUseOfActualGate
@CheckForNull[InteractionUse](InteractionUse.html) get_interactionUseOfActualGate()
Returns the value of the '***interaction Use Of Actual Gate***' container reference.
 It is bidirectional and its opposite is '[`*Actual Gate*`](InteractionUse.html#getActualGate())'.
 begin-user-doc 
If the meaning of the '*interaction Use Of Actual Gate*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Use Of Actual Gate*' container reference.
See Also:
[`set_interactionUseOfActualGate(InteractionUse)`](#set_interactionUseOfActualGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))
[`UMLPackage.getGate__interactionUseOfActualGate()`](../../metadata/UMLPackage.html#getGate__interactionUseOfActualGate())
[`InteractionUse.getActualGate()`](InteractionUse.html#getActualGate())
Model:
opposite="actualGate" transient="false" ordered="false"
Generated:
set_interactionUseOfActualGate
void set_interactionUseOfActualGate(@CheckForNull
 [InteractionUse](InteractionUse.html) value)
Sets the value of the
 '[`*interaction Use Of Actual Gate*`](#get_interactionUseOfActualGate())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Use Of Actual Gate*' container reference.
See Also:
[`get_interactionUseOfActualGate()`](#get_interactionUseOfActualGate())
Generated:
has_gateOfFormalGate
boolean has_gateOfFormalGate()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
get_interactionOfFormalGate
@CheckForNull[Interaction](../mdbasicinteractions/Interaction.html) get_interactionOfFormalGate()
Returns the value of the '***interaction Of Formal Gate***' container reference.
 It is bidirectional and its opposite is '[`*Formal Gate*`](../mdbasicinteractions/Interaction.html#getFormalGate())'.
 begin-user-doc 
If the meaning of the '*interaction Of Formal Gate*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Of Formal Gate*' container reference.
See Also:
[`set_interactionOfFormalGate(Interaction)`](#set_interactionOfFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))
[`UMLPackage.getGate__interactionOfFormalGate()`](../../metadata/UMLPackage.html#getGate__interactionOfFormalGate())
[`Interaction.getFormalGate()`](../mdbasicinteractions/Interaction.html#getFormalGate())
Model:
opposite="formalGate" transient="false" ordered="false"
Generated:
set_interactionOfFormalGate
void set_interactionOfFormalGate(@CheckForNull
 [Interaction](../mdbasicinteractions/Interaction.html) value)
Sets the value of the '[`*interaction Of Formal Gate*`](#get_interactionOfFormalGate())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Of Formal Gate*' container reference.
See Also:
[`get_interactionOfFormalGate()`](#get_interactionOfFormalGate())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.interactions.mdfragments</a></div>
<h1 class="title" title="Interface Gate">Interface Gate</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Gate</span><span class="extends-implements">
extends <a href="../mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Gate</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Gate is a MessageEnd which serves as a connection point for relating a Message which has a MessageEnd (sendEvent / receiveEvent) outside an InteractionFragment
 with another Message which has a MessageEnd (receiveEvent / sendEvent)  inside that InteractionFragment.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getFormalGate()"><code><em>Formal Gate</em></code></a></li>
<li><a href="#get_gateOfFormalGate()"><code><em>gate Of Formal Gate</em></code></a></li>
<li><a href="#get_combinedFragmentOfCfragmentGate()"><code><em>combined Fragment Of Cfragment Gate</em></code></a></li>
<li><a href="#get_interactionOfFormalGate()"><code><em>interaction Of Formal Gate</em></code></a></li>
<li><a href="#get_interactionUseOfActualGate()"><code><em>interaction Use Of Actual Gate</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getGate()"><code>UMLPackage.getGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='interactions.mdfragments'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_combinedFragmentOfCfragmentGate()">get_combinedFragmentOfCfragmentGate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>combined Fragment Of Cfragment Gate</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_gateOfFormalGate()">get_gateOfFormalGate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>gate Of Formal Gate</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionOfFormalGate()">get_interactionOfFormalGate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Of Formal Gate</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionUseOfActualGate()">get_interactionUseOfActualGate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Use Of Actual Gate</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFormalGate()">getFormalGate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Formal Gate</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_gateOfFormalGate()">has_gateOfFormalGate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_combinedFragmentOfCfragmentGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">set_combinedFragmentOfCfragmentGate</a><wbr/>(<a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_combinedFragmentOfCfragmentGate()"><code><em>combined Fragment Of Cfragment Gate</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionOfFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">set_interactionOfFormalGate</a><wbr/>(<a href="../mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_interactionOfFormalGate()"><code><em>interaction Of Formal Gate</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionUseOfActualGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfActualGate</a><wbr/>(<a href="InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfActualGate()"><code><em>interaction Use Of Actual Gate</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">setFormalGate</a><wbr/>(<a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getFormalGate()"><code><em>Formal Gate</em></code></a>' reference.</div>
</div>
</div>
</div>
</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.<a href="../mdbasicinteractions/MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></h3>
<code><a href="../mdbasicinteractions/MessageEnd.html#get_messageOfReceiveEvent()">get_messageOfReceiveEvent</a>, <a href="../mdbasicinteractions/MessageEnd.html#get_messageOfSendEvent()">get_messageOfSendEvent</a>, <a href="../mdbasicinteractions/MessageEnd.html#getMessage()">getMessage</a>, <a href="../mdbasicinteractions/MessageEnd.html#set_messageOfReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfReceiveEvent</a>, <a href="../mdbasicinteractions/MessageEnd.html#set_messageOfSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfSendEvent</a>, <a href="../mdbasicinteractions/MessageEnd.html#setMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">setMessage</a></code></div>
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
<section class="detail" id="getFormalGate()">
<h3>getFormalGate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a></span> <span class="element-name">getFormalGate</span>()</div>
<div class="block">Returns the value of the '<em><b>Formal Gate</b></em>' reference.
 It is bidirectional and its opposite is '<a href="#get_gateOfFormalGate()"><code><em>gate Of Formal Gate</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Formal Gate</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Formal Gate</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)"><code>setFormalGate(Gate)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getGate_FormalGate()"><code>UMLPackage.getGate_FormalGate()</code></a></li>
<li><a href="#get_gateOfFormalGate()"><code>get_gateOfFormalGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_gateOfFormalGate" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.Gate)">
<h3>setFormalGate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFormalGate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getFormalGate()"><code><em>Formal Gate</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Formal Gate</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getFormalGate()"><code>getFormalGate()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_gateOfFormalGate()">
<h3>get_gateOfFormalGate</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">Gate</a>&gt;</span> <span class="element-name">get_gateOfFormalGate</span>()</div>
<div class="block">Returns the value of the '<em><b>gate Of Formal Gate</b></em>' reference list.
 The list contents are of type <a href="Gate.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments"><code>Gate</code></a>.
 It is bidirectional and its opposite is '<a href="#getFormalGate()"><code><em>Formal Gate</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>gate Of Formal Gate</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>gate Of Formal Gate</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getGate__gateOfFormalGate()"><code>UMLPackage.getGate__gateOfFormalGate()</code></a></li>
<li><a href="#getFormalGate()"><code>getFormalGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="formalGate" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_combinedFragmentOfCfragmentGate()">
<h3>get_combinedFragmentOfCfragmentGate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></span> <span class="element-name">get_combinedFragmentOfCfragmentGate</span>()</div>
<div class="block">Returns the value of the '<em><b>combined Fragment Of Cfragment Gate</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="CombinedFragment.html#getCfragmentGate()"><code><em>Cfragment Gate</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>combined Fragment Of Cfragment Gate</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>combined Fragment Of Cfragment Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_combinedFragmentOfCfragmentGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)"><code>set_combinedFragmentOfCfragmentGate(CombinedFragment)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getGate__combinedFragmentOfCfragmentGate()"><code>UMLPackage.getGate__combinedFragmentOfCfragmentGate()</code></a></li>
<li><a href="CombinedFragment.html#getCfragmentGate()"><code>CombinedFragment.getCfragmentGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="cfragmentGate" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_combinedFragmentOfCfragmentGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">
<h3>set_combinedFragmentOfCfragmentGate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_combinedFragmentOfCfragmentGate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_combinedFragmentOfCfragmentGate()"><code><em>combined Fragment Of Cfragment Gate</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>combined Fragment Of Cfragment Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_combinedFragmentOfCfragmentGate()"><code>get_combinedFragmentOfCfragmentGate()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionUseOfActualGate()">
<h3>get_interactionUseOfActualGate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></span> <span class="element-name">get_interactionUseOfActualGate</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Use Of Actual Gate</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="InteractionUse.html#getActualGate()"><code><em>Actual Gate</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Use Of Actual Gate</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Use Of Actual Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionUseOfActualGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)"><code>set_interactionUseOfActualGate(InteractionUse)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getGate__interactionUseOfActualGate()"><code>UMLPackage.getGate__interactionUseOfActualGate()</code></a></li>
<li><a href="InteractionUse.html#getActualGate()"><code>InteractionUse.getActualGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="actualGate" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionUseOfActualGate(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">
<h3>set_interactionUseOfActualGate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionUseOfActualGate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfActualGate()"><code><em>interaction Use Of Actual Gate</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Use Of Actual Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_interactionUseOfActualGate()"><code>get_interactionUseOfActualGate()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_gateOfFormalGate()">
<h3>has_gateOfFormalGate</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_gateOfFormalGate</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionOfFormalGate()">
<h3>get_interactionOfFormalGate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">get_interactionOfFormalGate</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Of Formal Gate</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdbasicinteractions/Interaction.html#getFormalGate()"><code><em>Formal Gate</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Of Formal Gate</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Of Formal Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionOfFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)"><code>set_interactionOfFormalGate(Interaction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getGate__interactionOfFormalGate()"><code>UMLPackage.getGate__interactionOfFormalGate()</code></a></li>
<li><a href="../mdbasicinteractions/Interaction.html#getFormalGate()"><code>Interaction.getFormalGate()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="formalGate" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionOfFormalGate(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>set_interactionOfFormalGate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionOfFormalGate</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_interactionOfFormalGate()"><code><em>interaction Of Formal Gate</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Of Formal Gate</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_interactionOfFormalGate()"><code>get_interactionOfFormalGate()</code></a></li>
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
