# JAVA OPENAPI: FeatureMembership (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureMembership.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/FeatureMembership.html`
- source_sha256: `fcac21dd45350221cc827a6cd98c6b39bfea3edbfef62f0a1014318cf33f159f`
- captured_utc: `2026-07-14T16:44:48.920856+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface FeatureMembership

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Membership](Membership.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[OwningMembership](OwningMembership.html)`, `[Relationship](Relationship.html)`

All Known Subinterfaces:
`[ActorMembership](../../../sysml/model/sysml/ActorMembership.html)`, `[EndFeatureMembership](EndFeatureMembership.html)`, `[FramedConcernMembership](../../../sysml/model/sysml/FramedConcernMembership.html)`, `[ObjectiveMembership](../../../sysml/model/sysml/ObjectiveMembership.html)`, `[ParameterMembership](ParameterMembership.html)`, `[RequirementConstraintMembership](../../../sysml/model/sysml/RequirementConstraintMembership.html)`, `[RequirementVerificationMembership](../../../sysml/model/sysml/RequirementVerificationMembership.html)`, `[ResultExpressionMembership](ResultExpressionMembership.html)`, `[ReturnParameterMembership](ReturnParameterMembership.html)`, `[StakeholderMembership](../../../sysml/model/sysml/StakeholderMembership.html)`, `[StateSubactionMembership](../../../sysml/model/sysml/StateSubactionMembership.html)`, `[SubjectMembership](../../../sysml/model/sysml/SubjectMembership.html)`, `[TransitionFeatureMembership](../../../sysml/model/sysml/TransitionFeatureMembership.html)`, `[ViewRenderingMembership](../../../sysml/model/sysml/ViewRenderingMembership.html)`

@OpenApiAllpublic interfaceFeatureMembershipextends [OwningMembership](OwningMembership.html)

A `FeatureMembership` is an `OwningMembership` between an `ownedMemberFeature` and an `owningType`. If the `ownedMemberFeature` has `isVariable = false`, then the `FeatureMembership` implies that the `owningType` is also a `featuringType` of the `ownedMemberFeature`. If the `ownedMemberFeature` has `isVariable = true`, then the `FeatureMembership` implies that the `ownedMemberFeature` is featured by the *`snapshots`* of the `owningType`, which must specialize the Kernel Semantic Library base class *`Occurrence`*.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Feature](Feature.html)`
`[getOwnedMemberFeature](#getOwnedMemberFeature())()`
The `Feature` that this `FeatureMembership` relates to its `owningType`, making it an `ownedFeature` of the `owningType`.
`[Type](Type.html)`
`[getOwningType](#getOwningType())()`
The `Type` that owns this `FeatureMembership`.
`void`
`[setOwnedMemberFeature](#setOwnedMemberFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) value)`
The `Feature` that this `FeatureMembership` relates to its `owningType`, making it an `ownedFeature` of the `owningType`.
`void`
`[setOwningType](#setOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](Type.html) value)`
The `Type` that owns this `FeatureMembership`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Membership](Membership.html)
`[getMemberElement](Membership.html#getMemberElement()), [getMemberElementId](Membership.html#getMemberElementId()), [getMemberName](Membership.html#getMemberName()), [getMembershipOwningNamespace](Membership.html#getMembershipOwningNamespace()), [getMemberShortName](Membership.html#getMemberShortName()), [getVisibility](Membership.html#getVisibility()), [isDistinguishableFrom](Membership.html#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [setMemberElement](Membership.html#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setMemberName](Membership.html#setMemberName(java.lang.String)), [setMembershipOwningNamespace](Membership.html#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)), [setMemberShortName](Membership.html#setMemberShortName(java.lang.String)), [setVisibility](Membership.html#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[OwningMembership](OwningMembership.html)
`[getOwnedMemberElement](OwningMembership.html#getOwnedMemberElement()), [getOwnedMemberElementId](OwningMembership.html#getOwnedMemberElementId()), [getOwnedMemberName](OwningMembership.html#getOwnedMemberName()), [getOwnedMemberShortName](OwningMembership.html#getOwnedMemberShortName()), [path](OwningMembership.html#path()), [setOwnedMemberElement](OwningMembership.html#setOwnedMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](Relationship.html)
`[getOwnedRelatedElement](Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](Relationship.html#getOwningRelatedElement()), [getRelatedElement](Relationship.html#getRelatedElement()), [getSource](Relationship.html#getSource()), [getTarget](Relationship.html#getTarget()), [isImplied](Relationship.html#isImplied()), [libraryNamespace](Relationship.html#libraryNamespace()), [setIsImplied](Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`

============ METHOD DETAIL ========== 
Method Details
getOwningType
@CheckForNull[Type](Type.html) getOwningType()
The `Type` that owns this `FeatureMembership`.
Returns:
the owningType value
Model:
derived="true"
 transient="true"
 opposite=[`Type.getOwnedFeatureMembership()`](Type.html#getOwnedFeatureMembership())
 redefines=[`Membership.getMembershipOwningNamespace()`](Membership.html#getMembershipOwningNamespace())
setOwningType
void setOwningType(@CheckForNull
 [Type](Type.html) value)
The `Type` that owns this `FeatureMembership`.
Parameters:
`value` - the owningType value
Model:
derived="true"
 transient="true"
 opposite=[`Type.getOwnedFeatureMembership()`](Type.html#getOwnedFeatureMembership())
 redefines=[`Membership.getMembershipOwningNamespace()`](Membership.html#getMembershipOwningNamespace())
getOwnedMemberFeature
@CheckForNull[Feature](Feature.html) getOwnedMemberFeature()
The `Feature` that this `FeatureMembership` relates to its `owningType`, making it an `ownedFeature` of the `owningType`.
Returns:
the ownedMemberFeature value
Model:
derived="true"
 transient="true"
 opposite=[`Feature.getOwningFeatureMembership()`](Feature.html#getOwningFeatureMembership())
 redefines=[`OwningMembership.getOwnedMemberElement()`](OwningMembership.html#getOwnedMemberElement())
setOwnedMemberFeature
void setOwnedMemberFeature(@CheckForNull
 [Feature](Feature.html) value)
The `Feature` that this `FeatureMembership` relates to its `owningType`, making it an `ownedFeature` of the `owningType`.
Parameters:
`value` - the ownedMemberFeature value
Model:
derived="true"
 transient="true"
 opposite=[`Feature.getOwningFeatureMembership()`](Feature.html#getOwningFeatureMembership())
 redefines=[`OwningMembership.getOwnedMemberElement()`](OwningMembership.html#getOwnedMemberElement())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface FeatureMembership">Interface FeatureMembership</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></code>, <code><a href="EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></code>, <code><a href="../../../sysml/model/sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></code>, <code><a href="ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></code>, <code><a href="ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></code>, <code><a href="ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></code>, <code><a href="../../../sysml/model/sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></code>, <code><a href="../../../sysml/model/sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></code>, <code><a href="../../../sysml/model/sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">FeatureMembership</span><span class="extends-implements">
extends <a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></span></div>
<div class="block"><p>A <code>FeatureMembership</code> is an <code>OwningMembership</code> between an <code>ownedMemberFeature</code> and an <code>owningType</code>. If the <code>ownedMemberFeature</code> has <code>isVariable = false</code>, then the <code>FeatureMembership</code> implies that the <code>owningType</code> is also a <code>featuringType</code> of the <code>ownedMemberFeature</code>. If the <code>ownedMemberFeature</code> has <code>isVariable = true</code>, then the <code>FeatureMembership</code> implies that the <code>ownedMemberFeature</code> is featured by the <em><code>snapshots</code></em> of the <code>owningType</code>, which must specialize the Kernel Semantic Library base class <em><code>Occurrence</code></em>.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedMemberFeature()">getOwnedMemberFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that this <code>FeatureMembership</code> relates to its <code>owningType</code>, making it an <code>ownedFeature</code> of the <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningType()">getOwningType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Type</code> that owns this <code>FeatureMembership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedMemberFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setOwnedMemberFeature</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that this <code>FeatureMembership</code> relates to its <code>owningType</code>, making it an <code>ownedFeature</code> of the <code>owningType</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setOwningType</a><wbr/>(<a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Type</code> that owns this <code>FeatureMembership</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Membership">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></h3>
<code><a href="Membership.html#getMemberElement()">getMemberElement</a>, <a href="Membership.html#getMemberElementId()">getMemberElementId</a>, <a href="Membership.html#getMemberName()">getMemberName</a>, <a href="Membership.html#getMembershipOwningNamespace()">getMembershipOwningNamespace</a>, <a href="Membership.html#getMemberShortName()">getMemberShortName</a>, <a href="Membership.html#getVisibility()">getVisibility</a>, <a href="Membership.html#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">isDistinguishableFrom</a>, <a href="Membership.html#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setMemberElement</a>, <a href="Membership.html#setMemberName(java.lang.String)">setMemberName</a>, <a href="Membership.html#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">setMembershipOwningNamespace</a>, <a href="Membership.html#setMemberShortName(java.lang.String)">setMemberShortName</a>, <a href="Membership.html#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></h3>
<code><a href="OwningMembership.html#getOwnedMemberElement()">getOwnedMemberElement</a>, <a href="OwningMembership.html#getOwnedMemberElementId()">getOwnedMemberElementId</a>, <a href="OwningMembership.html#getOwnedMemberName()">getOwnedMemberName</a>, <a href="OwningMembership.html#getOwnedMemberShortName()">getOwnedMemberShortName</a>, <a href="OwningMembership.html#path()">path</a>, <a href="OwningMembership.html#setOwnedMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwnedMemberElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#getSource()">getSource</a>, <a href="Relationship.html#getTarget()">getTarget</a>, <a href="Relationship.html#isImplied()">isImplied</a>, <a href="Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
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
<section class="detail" id="getOwningType()">
<h3>getOwningType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getOwningType</span>()</div>
<div class="block"><p>The <code>Type</code> that owns this <code>FeatureMembership</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Type.html#getOwnedFeatureMembership()"><code>Type.getOwnedFeatureMembership()</code></a>
        redefines=<a href="Membership.html#getMembershipOwningNamespace()"><code>Membership.getMembershipOwningNamespace()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>setOwningType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> value)</span></div>
<div class="block"><p>The <code>Type</code> that owns this <code>FeatureMembership</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the owningType value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Type.html#getOwnedFeatureMembership()"><code>Type.getOwnedFeatureMembership()</code></a>
        redefines=<a href="Membership.html#getMembershipOwningNamespace()"><code>Membership.getMembershipOwningNamespace()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMemberFeature()">
<h3>getOwnedMemberFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedMemberFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that this <code>FeatureMembership</code> relates to its <code>owningType</code>, making it an <code>ownedFeature</code> of the <code>owningType</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedMemberFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Feature.html#getOwningFeatureMembership()"><code>Feature.getOwningFeatureMembership()</code></a>
        redefines=<a href="OwningMembership.html#getOwnedMemberElement()"><code>OwningMembership.getOwnedMemberElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedMemberFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setOwnedMemberFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedMemberFeature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</span></div>
<div class="block"><p>The <code>Feature</code> that this <code>FeatureMembership</code> relates to its <code>owningType</code>, making it an <code>ownedFeature</code> of the <code>owningType</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the ownedMemberFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Feature.html#getOwningFeatureMembership()"><code>Feature.getOwningFeatureMembership()</code></a>
        redefines=<a href="OwningMembership.html#getOwnedMemberElement()"><code>OwningMembership.getOwnedMemberElement()</code></a></dd>
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
