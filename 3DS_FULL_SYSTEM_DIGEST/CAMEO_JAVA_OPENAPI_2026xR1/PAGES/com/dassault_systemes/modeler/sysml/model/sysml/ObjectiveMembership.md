# JAVA OPENAPI: ObjectiveMembership (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/ObjectiveMembership.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/ObjectiveMembership.html`
- source_sha256: `966165f6d42778bfb6b62f7e0c706daf2c3b2744d860040fc5600105ce00c6dd`
- captured_utc: `2026-07-14T16:45:04.265060+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Interface ObjectiveMembership

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../../kerml/model/kerml/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[FeatureMembership](../../../kerml/model/kerml/FeatureMembership.html)`, `[Membership](../../../kerml/model/kerml/Membership.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[OwningMembership](../../../kerml/model/kerml/OwningMembership.html)`, `[Relationship](../../../kerml/model/kerml/Relationship.html)`

@OpenApiAllpublic interfaceObjectiveMembershipextends [FeatureMembership](../../../kerml/model/kerml/FeatureMembership.html)

An `ObjectiveMembership` is a `FeatureMembership` that indicates that its `ownedObjectiveRequirement` is the objective `RequirementUsage` for its `owningType`, which must be a `CaseDefinition` or `CaseUsage`.
 owningType.oclIsType(CaseDefinition) or
 owningType.oclIsType(CaseUsage)
 
 ownedObjectiveRequirement.isComposite

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[RequirementUsage](RequirementUsage.html)`
`[getOwnedObjectiveRequirement](#getOwnedObjectiveRequirement())()`
The RequirementUsage that is the `ownedMemberFeature` of this RequirementUsage.
`void`
`[setOwnedObjectiveRequirement](#setOwnedObjectiveRequirement(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage))([RequirementUsage](RequirementUsage.html) value)`
The RequirementUsage that is the `ownedMemberFeature` of this RequirementUsage.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](../../../kerml/model/kerml/Element.html)
`[effectiveName](../../../kerml/model/kerml/Element.html#effectiveName()), [effectiveShortName](../../../kerml/model/kerml/Element.html#effectiveShortName()), [escapedName](../../../kerml/model/kerml/Element.html#escapedName()), [getAliasIds](../../../kerml/model/kerml/Element.html#getAliasIds()), [getDeclaredName](../../../kerml/model/kerml/Element.html#getDeclaredName()), [getDeclaredShortName](../../../kerml/model/kerml/Element.html#getDeclaredShortName()), [getDocumentation](../../../kerml/model/kerml/Element.html#getDocumentation()), [getElementId](../../../kerml/model/kerml/Element.html#getElementId()), [getName](../../../kerml/model/kerml/Element.html#getName()), [getOwnedAnnotation](../../../kerml/model/kerml/Element.html#getOwnedAnnotation()), [getOwnedElement](../../../kerml/model/kerml/Element.html#getOwnedElement()), [getOwnedRelationship](../../../kerml/model/kerml/Element.html#getOwnedRelationship()), [getOwner](../../../kerml/model/kerml/Element.html#getOwner()), [getOwningMembership](../../../kerml/model/kerml/Element.html#getOwningMembership()), [getOwningNamespace](../../../kerml/model/kerml/Element.html#getOwningNamespace()), [getOwningRelationship](../../../kerml/model/kerml/Element.html#getOwningRelationship()), [getQualifiedName](../../../kerml/model/kerml/Element.html#getQualifiedName()), [getShortName](../../../kerml/model/kerml/Element.html#getShortName()), [getTextualRepresentation](../../../kerml/model/kerml/Element.html#getTextualRepresentation()), [isImpliedIncluded](../../../kerml/model/kerml/Element.html#isImpliedIncluded()), [isLibraryElement](../../../kerml/model/kerml/Element.html#isLibraryElement()), [setDeclaredName](../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)), [setElementId](../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)), [setOwner](../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[FeatureMembership](../../../kerml/model/kerml/FeatureMembership.html)
`[getOwnedMemberFeature](../../../kerml/model/kerml/FeatureMembership.html#getOwnedMemberFeature()), [getOwningType](../../../kerml/model/kerml/FeatureMembership.html#getOwningType()), [setOwnedMemberFeature](../../../kerml/model/kerml/FeatureMembership.html#setOwnedMemberFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [setOwningType](../../../kerml/model/kerml/FeatureMembership.html#setOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Type))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Membership](../../../kerml/model/kerml/Membership.html)
`[getMemberElement](../../../kerml/model/kerml/Membership.html#getMemberElement()), [getMemberElementId](../../../kerml/model/kerml/Membership.html#getMemberElementId()), [getMemberName](../../../kerml/model/kerml/Membership.html#getMemberName()), [getMembershipOwningNamespace](../../../kerml/model/kerml/Membership.html#getMembershipOwningNamespace()), [getMemberShortName](../../../kerml/model/kerml/Membership.html#getMemberShortName()), [getVisibility](../../../kerml/model/kerml/Membership.html#getVisibility()), [isDistinguishableFrom](../../../kerml/model/kerml/Membership.html#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [setMemberElement](../../../kerml/model/kerml/Membership.html#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setMemberName](../../../kerml/model/kerml/Membership.html#setMemberName(java.lang.String)), [setMembershipOwningNamespace](../../../kerml/model/kerml/Membership.html#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)), [setMemberShortName](../../../kerml/model/kerml/Membership.html#setMemberShortName(java.lang.String)), [setVisibility](../../../kerml/model/kerml/Membership.html#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[OwningMembership](../../../kerml/model/kerml/OwningMembership.html)
`[getOwnedMemberElement](../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberElement()), [getOwnedMemberElementId](../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberElementId()), [getOwnedMemberName](../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberName()), [getOwnedMemberShortName](../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberShortName()), [path](../../../kerml/model/kerml/OwningMembership.html#path()), [setOwnedMemberElement](../../../kerml/model/kerml/OwningMembership.html#setOwnedMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](../../../kerml/model/kerml/Relationship.html)
`[getOwnedRelatedElement](../../../kerml/model/kerml/Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](../../../kerml/model/kerml/Relationship.html#getOwningRelatedElement()), [getRelatedElement](../../../kerml/model/kerml/Relationship.html#getRelatedElement()), [getSource](../../../kerml/model/kerml/Relationship.html#getSource()), [getTarget](../../../kerml/model/kerml/Relationship.html#getTarget()), [isImplied](../../../kerml/model/kerml/Relationship.html#isImplied()), [libraryNamespace](../../../kerml/model/kerml/Relationship.html#libraryNamespace()), [setIsImplied](../../../kerml/model/kerml/Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](../../../kerml/model/kerml/Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`

============ METHOD DETAIL ========== 
Method Details
getOwnedObjectiveRequirement
@CheckForNull[RequirementUsage](RequirementUsage.html) getOwnedObjectiveRequirement()
The RequirementUsage that is the `ownedMemberFeature` of this RequirementUsage.
Returns:
the ownedObjectiveRequirement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningObjectiveMembership"
setOwnedObjectiveRequirement
void setOwnedObjectiveRequirement(@CheckForNull
 [RequirementUsage](RequirementUsage.html) value)
The RequirementUsage that is the `ownedMemberFeature` of this RequirementUsage.
Parameters:
`value` - the ownedObjectiveRequirement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="owningObjectiveMembership"

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Interface ObjectiveMembership">Interface ObjectiveMembership</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></code>, <code><a href="../../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../../kerml/model/kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></code>, <code><a href="../../../kerml/model/kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ObjectiveMembership</span><span class="extends-implements">
extends <a href="../../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></span></div>
<div class="block"><p>An <code>ObjectiveMembership</code> is a <code>FeatureMembership</code> that indicates that its <code>ownedObjectiveRequirement</code> is the objective <code>RequirementUsage</code> for its <code>owningType</code>, which must be a <code>CaseDefinition</code> or <code>CaseUsage</code>.</p>
 owningType.oclIsType(CaseDefinition) or
 owningType.oclIsType(CaseUsage)
 
 ownedObjectiveRequirement.isComposite</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedObjectiveRequirement()">getOwnedObjectiveRequirement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The RequirementUsage that is the <code>ownedMemberFeature</code> of this RequirementUsage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedObjectiveRequirement(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage)">setOwnedObjectiveRequirement</a><wbr/>(<a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The RequirementUsage that is the <code>ownedMemberFeature</code> of this RequirementUsage.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="../../../kerml/model/kerml/Element.html#effectiveName()">effectiveName</a>, <a href="../../../kerml/model/kerml/Element.html#effectiveShortName()">effectiveShortName</a>, <a href="../../../kerml/model/kerml/Element.html#escapedName()">escapedName</a>, <a href="../../../kerml/model/kerml/Element.html#getAliasIds()">getAliasIds</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredName()">getDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getDocumentation()">getDocumentation</a>, <a href="../../../kerml/model/kerml/Element.html#getElementId()">getElementId</a>, <a href="../../../kerml/model/kerml/Element.html#getName()">getName</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../../kerml/model/kerml/Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getOwner()">getOwner</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningMembership()">getOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="../../../kerml/model/kerml/Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="../../../kerml/model/kerml/Element.html#getQualifiedName()">getQualifiedName</a>, <a href="../../../kerml/model/kerml/Element.html#getShortName()">getShortName</a>, <a href="../../../kerml/model/kerml/Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="../../../kerml/model/kerml/Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#isLibraryElement()">isLibraryElement</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a></h3>
<code><a href="../../../kerml/model/kerml/FeatureMembership.html#getOwnedMemberFeature()">getOwnedMemberFeature</a>, <a href="../../../kerml/model/kerml/FeatureMembership.html#getOwningType()">getOwningType</a>, <a href="../../../kerml/model/kerml/FeatureMembership.html#setOwnedMemberFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setOwnedMemberFeature</a>, <a href="../../../kerml/model/kerml/FeatureMembership.html#setOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setOwningType</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Membership">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></h3>
<code><a href="../../../kerml/model/kerml/Membership.html#getMemberElement()">getMemberElement</a>, <a href="../../../kerml/model/kerml/Membership.html#getMemberElementId()">getMemberElementId</a>, <a href="../../../kerml/model/kerml/Membership.html#getMemberName()">getMemberName</a>, <a href="../../../kerml/model/kerml/Membership.html#getMembershipOwningNamespace()">getMembershipOwningNamespace</a>, <a href="../../../kerml/model/kerml/Membership.html#getMemberShortName()">getMemberShortName</a>, <a href="../../../kerml/model/kerml/Membership.html#getVisibility()">getVisibility</a>, <a href="../../../kerml/model/kerml/Membership.html#isDistinguishableFrom(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">isDistinguishableFrom</a>, <a href="../../../kerml/model/kerml/Membership.html#setMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setMemberElement</a>, <a href="../../../kerml/model/kerml/Membership.html#setMemberName(java.lang.String)">setMemberName</a>, <a href="../../../kerml/model/kerml/Membership.html#setMembershipOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">setMembershipOwningNamespace</a>, <a href="../../../kerml/model/kerml/Membership.html#setMemberShortName(java.lang.String)">setMemberShortName</a>, <a href="../../../kerml/model/kerml/Membership.html#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)">setVisibility</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a></h3>
<code><a href="../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberElement()">getOwnedMemberElement</a>, <a href="../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberElementId()">getOwnedMemberElementId</a>, <a href="../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberName()">getOwnedMemberName</a>, <a href="../../../kerml/model/kerml/OwningMembership.html#getOwnedMemberShortName()">getOwnedMemberShortName</a>, <a href="../../../kerml/model/kerml/OwningMembership.html#path()">path</a>, <a href="../../../kerml/model/kerml/OwningMembership.html#setOwnedMemberElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwnedMemberElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="../../../kerml/model/kerml/Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getSource()">getSource</a>, <a href="../../../kerml/model/kerml/Relationship.html#getTarget()">getTarget</a>, <a href="../../../kerml/model/kerml/Relationship.html#isImplied()">isImplied</a>, <a href="../../../kerml/model/kerml/Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="../../../kerml/model/kerml/Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="../../../kerml/model/kerml/Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
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
<section class="detail" id="getOwnedObjectiveRequirement()">
<h3>getOwnedObjectiveRequirement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">getOwnedObjectiveRequirement</span>()</div>
<div class="block"><p>The RequirementUsage that is the <code>ownedMemberFeature</code> of this RequirementUsage.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedObjectiveRequirement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningObjectiveMembership"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedObjectiveRequirement(com.dassault_systemes.modeler.sysml.model.sysml.RequirementUsage)">
<h3>setOwnedObjectiveRequirement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedObjectiveRequirement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a> value)</span></div>
<div class="block"><p>The RequirementUsage that is the <code>ownedMemberFeature</code> of this RequirementUsage.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the ownedObjectiveRequirement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="owningObjectiveMembership"</dd>
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
