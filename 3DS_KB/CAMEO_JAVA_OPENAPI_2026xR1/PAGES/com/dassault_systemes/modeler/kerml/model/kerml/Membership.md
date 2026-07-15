# JAVA OPENAPI: Membership (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Membership.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Membership.html`
- source_sha256: `c44d4b28602103a2e4ac2039e8c7d03faaf8846ab8706dcc2003e16c9f94978c`
- captured_utc: `2026-07-14T16:44:49.852867+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Membership

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`

All Known Subinterfaces:
`[ActorMembership](../../../sysml/model/sysml/ActorMembership.html)`, `[ElementFilterMembership](ElementFilterMembership.html)`, `[EndFeatureMembership](EndFeatureMembership.html)`, `[FeatureMembership](FeatureMembership.html)`, `[FeatureValue](FeatureValue.html)`, `[FramedConcernMembership](../../../sysml/model/sysml/FramedConcernMembership.html)`, `[ObjectiveMembership](../../../sysml/model/sysml/ObjectiveMembership.html)`, `[OwningMembership](OwningMembership.html)`, `[ParameterMembership](ParameterMembership.html)`, `[RequirementConstraintMembership](../../../sysml/model/sysml/RequirementConstraintMembership.html)`, `[RequirementVerificationMembership](../../../sysml/model/sysml/RequirementVerificationMembership.html)`, `[ResultExpressionMembership](ResultExpressionMembership.html)`, `[ReturnParameterMembership](ReturnParameterMembership.html)`, `[StakeholderMembership](../../../sysml/model/sysml/StakeholderMembership.html)`, `[StateSubactionMembership](../../../sysml/model/sysml/StateSubactionMembership.html)`, `[SubjectMembership](../../../sysml/model/sysml/SubjectMembership.html)`, `[TransitionFeatureMembership](../../../sysml/model/sysml/TransitionFeatureMembership.html)`, `[VariantMembership](../../../sysml/model/sysml/VariantMembership.html)`, `[ViewRenderingMembership](../../../sysml/model/sysml/ViewRenderingMembership.html)`

@OpenApiAllpublic interfaceMembershipextends [Relationship](Relationship.html)

A `Membership` is a `Relationship` between a `Namespace` and an `Element` that indicates the `Element` is a `member` of (i.e., is contained in) the Namespace. Any `memberNames` specify how the `memberElement` is identified in the `Namespace` and the `visibility` specifies whether or not the `memberElement` is publicly visible from outside the `Namespace`.
If a `Membership` is an `OwningMembership`, then it owns its `memberElement`, which becomes an `ownedMember` of the `membershipOwningNamespace`. Otherwise, the `memberNames` of a `Membership` are effectively aliases within the `membershipOwningNamespace` for an `Element` with a separate `OwningMembership` in the same or a different `Namespace`.

 
 memberElementId = memberElement.elementId

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](Element.html)`
`[getMemberElement](#getMemberElement())()`
The `Element` that becomes a `member` of the `membershipOwningNamespace` due to this `Membership`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMemberElementId](#getMemberElementId())()`
The `elementId` of the `memberElement`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMemberName](#getMemberName())()`
The name of the `memberElement` relative to the `membershipOwningNamespace`.
`[Namespace](Namespace.html)`
`[getMembershipOwningNamespace](#getMembershipOwningNamespace())()`
The `Namespace` of which the `memberElement` becomes a `member` due to this `Membership`.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMemberShortName](#getMemberShortName())()`
The short name of the `memberElement` relative to the `membershipOwningNamespace`.
`[VisibilityKind](VisibilityKind.html)`
`[getVisibility](#getVisibility())()`
Whether or not the `Membership` of the `memberElement` in the `membershipOwningNamespace` is publicly visible outside that `Namespace`.
`boolean`
`[isDistinguishableFrom](#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership))([Membership](Membership.html) other)`
Whether this `Membership` is distinguishable from a given `other` `Membership`.
`void`
`[setMemberElement](#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) value)`
The `Element` that becomes a `member` of the `membershipOwningNamespace` due to this `Membership`.
`void`
`[setMemberName](#setMemberName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
The name of the `memberElement` relative to the `membershipOwningNamespace`.
`void`
`[setMembershipOwningNamespace](#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](Namespace.html) value)`
The `Namespace` of which the `memberElement` becomes a `member` due to this `Membership`.
`void`
`[setMemberShortName](#setMemberShortName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
The short name of the `memberElement` relative to the `membershipOwningNamespace`.
`void`
`[setVisibility](#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind))([VisibilityKind](VisibilityKind.html) value)`
Whether or not the `Membership` of the `memberElement` in the `membershipOwningNamespace` is publicly visible outside that `Namespace`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](Relationship.html)
`[getOwnedRelatedElement](Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](Relationship.html#getOwningRelatedElement()), [getRelatedElement](Relationship.html#getRelatedElement()), [getSource](Relationship.html#getSource()), [getTarget](Relationship.html#getTarget()), [isImplied](Relationship.html#isImplied()), [libraryNamespace](Relationship.html#libraryNamespace()), [path](Relationship.html#path()), [setIsImplied](Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`

============ METHOD DETAIL ========== 
Method Details
getMemberElementId
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMemberElementId()
The `elementId` of the `memberElement`.
Returns:
the memberElementId value
Model:
derived="true"
 transient="true"
getMembershipOwningNamespace
@CheckForNull[Namespace](Namespace.html) getMembershipOwningNamespace()
The `Namespace` of which the `memberElement` becomes a `member` due to this `Membership`.
Returns:
the membershipOwningNamespace value
Model:
derived="true"
 transient="true"
 opposite=[`Namespace.getOwnedMembership()`](Namespace.html#getOwnedMembership())
 subsets=[`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
setMembershipOwningNamespace
void setMembershipOwningNamespace(@CheckForNull
 [Namespace](Namespace.html) value)
The `Namespace` of which the `memberElement` becomes a `member` due to this `Membership`.
Parameters:
`value` - the membershipOwningNamespace value
Model:
derived="true"
 transient="true"
 opposite=[`Namespace.getOwnedMembership()`](Namespace.html#getOwnedMembership())
 subsets=[`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getMemberShortName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMemberShortName()
The short name of the `memberElement` relative to the `membershipOwningNamespace`.
Returns:
the memberShortName value
Model:
derived="false"
 transient="false"
setMemberShortName
void setMemberShortName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
The short name of the `memberElement` relative to the `membershipOwningNamespace`.
Parameters:
`value` - the memberShortName value
Model:
derived="false"
 transient="false"
getMemberElement
@CheckForNull[Element](Element.html) getMemberElement()
The `Element` that becomes a `member` of the `membershipOwningNamespace` due to this `Membership`.
Returns:
the memberElement value
Model:
derived="false"
 transient="false"
 oppositeRoleName="membership"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
setMemberElement
void setMemberElement(@CheckForNull
 [Element](Element.html) value)
The `Element` that becomes a `member` of the `membershipOwningNamespace` due to this `Membership`.
Parameters:
`value` - the memberElement value
Model:
derived="false"
 transient="false"
 oppositeRoleName="membership"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
getMemberName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMemberName()
The name of the `memberElement` relative to the `membershipOwningNamespace`.
Returns:
the memberName value
Model:
derived="false"
 transient="false"
setMemberName
void setMemberName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
The name of the `memberElement` relative to the `membershipOwningNamespace`.
Parameters:
`value` - the memberName value
Model:
derived="false"
 transient="false"
getVisibility
@CheckForNull[VisibilityKind](VisibilityKind.html) getVisibility()
Whether or not the `Membership` of the `memberElement` in the `membershipOwningNamespace` is publicly visible outside that `Namespace`.
Returns:
the visibility value
Model:
derived="false"
 transient="false"
setVisibility
void setVisibility(@CheckForNull
 [VisibilityKind](VisibilityKind.html) value)
Whether or not the `Membership` of the `memberElement` in the `membershipOwningNamespace` is publicly visible outside that `Namespace`.
Parameters:
`value` - the visibility value
Model:
derived="false"
 transient="false"
isDistinguishableFrom
boolean isDistinguishableFrom([Membership](Membership.html) other)
Whether this `Membership` is distinguishable from a given `other` `Membership`. By default, this is true if this `Membership` has no `memberShortName` or `memberName`; or each of the `memberShortName` and `memberName` are different than both of those of the `other` `Membership`; or neither of the metaclasses of the `memberElement` of this `Membership` and the `memberElement` of the `other` `Membership` conform to the other. But this may be overridden in specializations of `Membership`.
 
 not (memberElement.oclKindOf(other.memberElement.oclType()) or
 other.memberElement.oclKindOf(memberElement.oclType())) or
 (shortMemberName = null or
 (shortMemberName <> other.shortMemberName and
 shortMemberName <> other.memberName)) and
 (memberName = null or
 (memberName <> other.shortMemberName and
 memberName <> other.memberName)))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Membership">Interface Membership</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActorMembership</a></code>, <code><a href="ElementFilterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ElementFilterMembership</a></code>, <code><a href="EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">EndFeatureMembership</a></code>, <code><a href="FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code>, <code><a href="FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code>, <code><a href="../../../sysml/model/sysml/FramedConcernMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">FramedConcernMembership</a></code>, <code><a href="../../../sysml/model/sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ObjectiveMembership</a></code>, <code><a href="OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code>, <code><a href="ParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementConstraintMembership</a></code>, <code><a href="../../../sysml/model/sysml/RequirementVerificationMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementVerificationMembership</a></code>, <code><a href="ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ResultExpressionMembership</a></code>, <code><a href="ReturnParameterMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">ReturnParameterMembership</a></code>, <code><a href="../../../sysml/model/sysml/StakeholderMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StakeholderMembership</a></code>, <code><a href="../../../sysml/model/sysml/StateSubactionMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">StateSubactionMembership</a></code>, <code><a href="../../../sysml/model/sysml/SubjectMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">SubjectMembership</a></code>, <code><a href="../../../sysml/model/sysml/TransitionFeatureMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">TransitionFeatureMembership</a></code>, <code><a href="../../../sysml/model/sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">VariantMembership</a></code>, <code><a href="../../../sysml/model/sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ViewRenderingMembership</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Membership</span><span class="extends-implements">
extends <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>A <code>Membership</code> is a <code>Relationship</code> between a <code>Namespace</code> and an <code>Element</code> that indicates the <code>Element</code> is a <code>member</code> of (i.e., is contained in) the Namespace. Any <code>memberNames</code> specify how the <code>memberElement</code> is identified in the <code>Namespace</code> and the <code>visibility</code> specifies whether or not the <code>memberElement</code> is publicly visible from outside the <code>Namespace</code>.</p>
<p>If a <code>Membership</code> is an <code>OwningMembership</code>, then it owns its <code>memberElement</code>, which becomes an <code>ownedMember</code> of the <code>membershipOwningNamespace</code>. Otherwise, the <code>memberNames</code> of a <code>Membership</code> are effectively aliases within the <code>membershipOwningNamespace</code> for an <code>Element</code> with a separate <code>OwningMembership</code> in the same or a different <code>Namespace</code>.</p>
<p> </p>
 
 memberElementId = memberElement.elementId</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMemberElement()">getMemberElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Element</code> that becomes a <code>member</code> of the <code>membershipOwningNamespace</code> due to this <code>Membership</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMemberElementId()">getMemberElementId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>elementId</code> of the <code>memberElement</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMemberName()">getMemberName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMembershipOwningNamespace()">getMembershipOwningNamespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Namespace</code> of which the <code>memberElement</code> becomes a <code>member</code> due to this <code>Membership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMemberShortName()">getMemberShortName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The short name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not the <code>Membership</code> of the <code>memberElement</code> in the <code>membershipOwningNamespace</code> is publicly visible outside that <code>Namespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">isDistinguishableFrom</a><wbr/>(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> other)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>Membership</code> is distinguishable from a given <code>other</code> <code>Membership</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setMemberElement</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Element</code> that becomes a <code>member</code> of the <code>membershipOwningNamespace</code> due to this <code>Membership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMemberName(java.lang.String)">setMemberName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">setMembershipOwningNamespace</a><wbr/>(<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Namespace</code> of which the <code>memberElement</code> becomes a <code>member</code> due to this <code>Membership</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMemberShortName(java.lang.String)">setMemberShortName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The short name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)">setVisibility</a><wbr/>(<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether or not the <code>Membership</code> of the <code>memberElement</code> in the <code>membershipOwningNamespace</code> is publicly visible outside that <code>Namespace</code>.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#getSource()">getSource</a>, <a href="Relationship.html#getTarget()">getTarget</a>, <a href="Relationship.html#isImplied()">isImplied</a>, <a href="Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="Relationship.html#path()">path</a>, <a href="Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
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
<section class="detail" id="getMemberElementId()">
<h3>getMemberElementId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMemberElementId</span>()</div>
<div class="block"><p>The <code>elementId</code> of the <code>memberElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the memberElementId value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMembershipOwningNamespace()">
<h3>getMembershipOwningNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">getMembershipOwningNamespace</span>()</div>
<div class="block"><p>The <code>Namespace</code> of which the <code>memberElement</code> becomes a <code>member</code> due to this <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the membershipOwningNamespace value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Namespace.html#getOwnedMembership()"><code>Namespace.getOwnedMembership()</code></a>
        subsets=<a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>setMembershipOwningNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMembershipOwningNamespace</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> value)</span></div>
<div class="block"><p>The <code>Namespace</code> of which the <code>memberElement</code> becomes a <code>member</code> due to this <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the membershipOwningNamespace value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Namespace.html#getOwnedMembership()"><code>Namespace.getOwnedMembership()</code></a>
        subsets=<a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMemberShortName()">
<h3>getMemberShortName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMemberShortName</span>()</div>
<div class="block"><p>The short name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the memberShortName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMemberShortName(java.lang.String)">
<h3>setMemberShortName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMemberShortName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>The short name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the memberShortName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMemberElement()">
<h3>getMemberElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getMemberElement</span>()</div>
<div class="block"><p>The <code>Element</code> that becomes a <code>member</code> of the <code>membershipOwningNamespace</code> due to this <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the memberElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="membership"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setMemberElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMemberElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</span></div>
<div class="block"><p>The <code>Element</code> that becomes a <code>member</code> of the <code>membershipOwningNamespace</code> due to this <code>Membership</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the memberElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="membership"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMemberName()">
<h3>getMemberName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMemberName</span>()</div>
<div class="block"><p>The name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the memberName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMemberName(java.lang.String)">
<h3>setMemberName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMemberName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>The name of the <code>memberElement</code> relative to the <code>membershipOwningNamespace</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the memberName value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibility()">
<h3>getVisibility</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">getVisibility</span>()</div>
<div class="block"><p>Whether or not the <code>Membership</code> of the <code>memberElement</code> in the <code>membershipOwningNamespace</code> is publicly visible outside that <code>Namespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the visibility value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)">
<h3>setVisibility</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setVisibility</span><wbr/><span class="parameters">(@CheckForNull
 <a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a> value)</span></div>
<div class="block"><p>Whether or not the <code>Membership</code> of the <code>memberElement</code> in the <code>membershipOwningNamespace</code> is publicly visible outside that <code>Namespace</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the visibility value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">
<h3>isDistinguishableFrom</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDistinguishableFrom</span><wbr/><span class="parameters">(<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a> other)</span></div>
<div class="block"><p>Whether this <code>Membership</code> is distinguishable from a given <code>other</code> <code>Membership</code>. By default, this is true if this <code>Membership</code> has no <code>memberShortName</code> or <code>memberName</code>; or each of the <code>memberShortName</code> and <code>memberName</code> are different than both of those of the <code>other</code> <code>Membership</code>; or neither of the metaclasses of the <code>memberElement</code> of this <code>Membership</code> and the <code>memberElement</code> of the <code>other</code> <code>Membership</code> conform to the other. But this may be overridden in specializations of <code>Membership</code>.</p>
 
 not (memberElement.oclKindOf(other.memberElement.oclType()) or
      other.memberElement.oclKindOf(memberElement.oclType())) or
 (shortMemberName = null or
     (shortMemberName &lt;&gt; other.shortMemberName and
      shortMemberName &lt;&gt; other.memberName)) and
 (memberName = null or
     (memberName &lt;&gt; other.shortMemberName and
      memberName &lt;&gt; other.memberName)))</div>
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
