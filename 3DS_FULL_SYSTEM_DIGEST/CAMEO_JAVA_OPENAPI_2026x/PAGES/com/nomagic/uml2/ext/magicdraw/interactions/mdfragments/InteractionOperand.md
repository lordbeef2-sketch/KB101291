# JAVA OPENAPI: InteractionOperand (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html
- source_path: `com/nomagic/uml2/ext/magicdraw/interactions/mdfragments/InteractionOperand.html`
- source_sha256: `4d168c8b8304af967cd8bf79b11c08e68bb114102e8ff4ab4a8892968c9d3509`
- captured_utc: `2026-07-14T16:58:56.982507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.interactions.mdfragments](package-summary.html)

## Interface InteractionOperand

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[InteractionFragment](../mdbasicinteractions/InteractionFragment.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceInteractionOperandextends [Namespace](../../classes/mdkernel/Namespace.html), [InteractionFragment](../mdbasicinteractions/InteractionFragment.html)

begin-user-doc 
 A representation of the model object '***Interaction Operand***'.
 end-user-doc 
begin-model-doc 
 An InteractionOperand is contained in a CombinedFragment. An InteractionOperand represents one operand of the expression given by the enclosing CombinedFragment.
 end-model-doc 
The following features are supported:
 [`*Fragment*`](#getFragment())
[`*Guard*`](#getGuard())
[`*combined Fragment Of Operand*`](#get_combinedFragmentOfOperand())

See Also:
[`UMLPackage.getInteractionOperand()`](../../metadata/UMLPackage.html#getInteractionOperand())
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
`[get_combinedFragmentOfOperand](#get_combinedFragmentOfOperand())()`
Returns the value of the '***combined Fragment Of Operand***' container reference.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InteractionFragment](../mdbasicinteractions/InteractionFragment.html)>`
`[getFragment](#getFragment())()`
Returns the value of the '***Fragment***' containment reference list.
`[InteractionConstraint](InteractionConstraint.html)`
`[getGuard](#getGuard())()`
Returns the value of the '***Guard***' containment reference.
`boolean`
`[hasFragment](#hasFragment())()`

`void`
`[set_combinedFragmentOfOperand](#set_combinedFragmentOfOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))([CombinedFragment](CombinedFragment.html) value)`
Sets the value of the
 '[`*combined Fragment Of Operand*`](#get_combinedFragmentOfOperand())'
 container reference.
`void`
`[setGuard](#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))([InteractionConstraint](InteractionConstraint.html) value)`
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.[InteractionFragment](../mdbasicinteractions/InteractionFragment.html)
`[getCovered](../mdbasicinteractions/InteractionFragment.html#getCovered()), [getEnclosingInteraction](../mdbasicinteractions/InteractionFragment.html#getEnclosingInteraction()), [getEnclosingOperand](../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand()), [getGeneralOrdering](../mdbasicinteractions/InteractionFragment.html#getGeneralOrdering()), [hasCovered](../mdbasicinteractions/InteractionFragment.html#hasCovered()), [hasGeneralOrdering](../mdbasicinteractions/InteractionFragment.html#hasGeneralOrdering()), [setEnclosingInteraction](../mdbasicinteractions/InteractionFragment.html#setEnclosingInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)), [setEnclosingOperand](../mdbasicinteractions/InteractionFragment.html#setEnclosingOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
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
getGuard
@CheckForNull[InteractionConstraint](InteractionConstraint.html) getGuard()
Returns the value of the '***Guard***' containment reference.
 It is bidirectional and its opposite is
 '[`*interaction Operand Of Guard*`](InteractionConstraint.html#get_interactionOperandOfGuard())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Constraint of the operand.
 end-model-doc
Returns:
the value of the '*Guard*' containment reference.
See Also:
[`setGuard(InteractionConstraint)`](#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))
[`UMLPackage.getInteractionOperand_Guard()`](../../metadata/UMLPackage.html#getInteractionOperand_Guard())
[`InteractionConstraint.get_interactionOperandOfGuard()`](InteractionConstraint.html#get_interactionOperandOfGuard())
Model:
opposite="_interactionOperandOfGuard" containment="true" resolveProxies="true" ordered="false"
Generated:
setGuard
void setGuard(@CheckForNull
 [InteractionConstraint](InteractionConstraint.html) value)
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Guard*' containment reference.
See Also:
[`getGuard()`](#getGuard())
Generated:
get_combinedFragmentOfOperand
@CheckForNull[CombinedFragment](CombinedFragment.html) get_combinedFragmentOfOperand()
Returns the value of the '***combined Fragment Of Operand***' container reference.
 It is bidirectional and its opposite is '[`*Operand*`](CombinedFragment.html#getOperand())'.
 begin-user-doc 
If the meaning of the '*combined Fragment Of Operand*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*combined Fragment Of Operand*' container reference.
See Also:
[`set_combinedFragmentOfOperand(CombinedFragment)`](#set_combinedFragmentOfOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment))
[`UMLPackage.getInteractionOperand__combinedFragmentOfOperand()`](../../metadata/UMLPackage.html#getInteractionOperand__combinedFragmentOfOperand())
[`CombinedFragment.getOperand()`](CombinedFragment.html#getOperand())
Model:
opposite="operand" transient="false" ordered="false"
Generated:
set_combinedFragmentOfOperand
void set_combinedFragmentOfOperand(@CheckForNull
 [CombinedFragment](CombinedFragment.html) value)
Sets the value of the
 '[`*combined Fragment Of Operand*`](#get_combinedFragmentOfOperand())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*combined Fragment Of Operand*' container reference.
See Also:
[`get_combinedFragmentOfOperand()`](#get_combinedFragmentOfOperand())
Generated:
getFragment
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[InteractionFragment](../mdbasicinteractions/InteractionFragment.html)> getFragment()
Returns the value of the '***Fragment***' containment reference list.
 The list contents are of type [`InteractionFragment`](../mdbasicinteractions/InteractionFragment.html).
 It is bidirectional and its opposite is
 '[`*Enclosing Operand*`](../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The fragments of the operand.
 end-model-doc
Returns:
the value of the '*Fragment*' containment reference list.
See Also:
[`UMLPackage.getInteractionOperand_Fragment()`](../../metadata/UMLPackage.html#getInteractionOperand_Fragment())
[`InteractionFragment.getEnclosingOperand()`](../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand())
Model:
opposite="enclosingOperand" containment="true" resolveProxies="true"
Generated:
hasFragment
boolean hasFragment()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.interactions.mdfragments</a></div>
<h1 class="title" title="Interface InteractionOperand">Interface InteractionOperand</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">InteractionOperand</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Interaction Operand</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An InteractionOperand is contained in a CombinedFragment. An InteractionOperand represents one operand of the expression given by the enclosing CombinedFragment.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getFragment()"><code><em>Fragment</em></code></a></li>
<li><a href="#getGuard()"><code><em>Guard</em></code></a></li>
<li><a href="#get_combinedFragmentOfOperand()"><code><em>combined Fragment Of Operand</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getInteractionOperand()"><code>UMLPackage.getInteractionOperand()</code></a></li>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_combinedFragmentOfOperand()">get_combinedFragmentOfOperand</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>combined Fragment Of Operand</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFragment()">getFragment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Fragment</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGuard()">getGuard</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasFragment()">hasFragment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_combinedFragmentOfOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">set_combinedFragmentOfOperand</a><wbr/>(<a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_combinedFragmentOfOperand()"><code><em>combined Fragment Of Operand</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">setGuard</a><wbr/>(<a href="InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' containment reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.InteractionFragment">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.<a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a></h3>
<code><a href="../mdbasicinteractions/InteractionFragment.html#getCovered()">getCovered</a>, <a href="../mdbasicinteractions/InteractionFragment.html#getEnclosingInteraction()">getEnclosingInteraction</a>, <a href="../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand()">getEnclosingOperand</a>, <a href="../mdbasicinteractions/InteractionFragment.html#getGeneralOrdering()">getGeneralOrdering</a>, <a href="../mdbasicinteractions/InteractionFragment.html#hasCovered()">hasCovered</a>, <a href="../mdbasicinteractions/InteractionFragment.html#hasGeneralOrdering()">hasGeneralOrdering</a>, <a href="../mdbasicinteractions/InteractionFragment.html#setEnclosingInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">setEnclosingInteraction</a>, <a href="../mdbasicinteractions/InteractionFragment.html#setEnclosingOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionOperand)">setEnclosingOperand</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
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
<section class="detail" id="getGuard()">
<h3>getGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></span> <span class="element-name">getGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="InteractionConstraint.html#get_interactionOperandOfGuard()"><code><em>interaction Operand Of Guard</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Constraint of the operand.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Guard</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)"><code>setGuard(InteractionConstraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInteractionOperand_Guard()"><code>UMLPackage.getInteractionOperand_Guard()</code></a></li>
<li><a href="InteractionConstraint.html#get_interactionOperandOfGuard()"><code>InteractionConstraint.get_interactionOperandOfGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_interactionOperandOfGuard" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">
<h3>setGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</span></div>
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
<section class="detail" id="get_combinedFragmentOfOperand()">
<h3>get_combinedFragmentOfOperand</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a></span> <span class="element-name">get_combinedFragmentOfOperand</span>()</div>
<div class="block">Returns the value of the '<em><b>combined Fragment Of Operand</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="CombinedFragment.html#getOperand()"><code><em>Operand</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>combined Fragment Of Operand</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>combined Fragment Of Operand</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_combinedFragmentOfOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)"><code>set_combinedFragmentOfOperand(CombinedFragment)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInteractionOperand__combinedFragmentOfOperand()"><code>UMLPackage.getInteractionOperand__combinedFragmentOfOperand()</code></a></li>
<li><a href="CombinedFragment.html#getOperand()"><code>CombinedFragment.getOperand()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="operand" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_combinedFragmentOfOperand(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.CombinedFragment)">
<h3>set_combinedFragmentOfOperand</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_combinedFragmentOfOperand</span><wbr/><span class="parameters">(@CheckForNull
 <a href="CombinedFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">CombinedFragment</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_combinedFragmentOfOperand()"><code><em>combined Fragment Of Operand</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>combined Fragment Of Operand</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_combinedFragmentOfOperand()"><code>get_combinedFragmentOfOperand()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFragment()">
<h3>getFragment</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">InteractionFragment</a>&gt;</span> <span class="element-name">getFragment</span>()</div>
<div class="block">Returns the value of the '<em><b>Fragment</b></em>' containment reference list.
 The list contents are of type <a href="../mdbasicinteractions/InteractionFragment.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>InteractionFragment</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand()"><code><em>Enclosing Operand</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The fragments of the operand.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Fragment</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getInteractionOperand_Fragment()"><code>UMLPackage.getInteractionOperand_Fragment()</code></a></li>
<li><a href="../mdbasicinteractions/InteractionFragment.html#getEnclosingOperand()"><code>InteractionFragment.getEnclosingOperand()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="enclosingOperand" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasFragment()">
<h3>hasFragment</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasFragment</span>()
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
