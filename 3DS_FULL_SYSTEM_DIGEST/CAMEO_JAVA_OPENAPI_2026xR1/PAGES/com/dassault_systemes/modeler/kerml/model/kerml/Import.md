# JAVA OPENAPI: Import (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Import.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Import.html`
- source_sha256: `017ba1996148828f16b64f4f9f678ea119935ecf073d0f0f3d8c37ae3720f2ac`
- captured_utc: `2026-07-14T16:44:49.164859+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Import

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`

All Known Subinterfaces:
`[Expose](../../../sysml/model/sysml/Expose.html)`, `[MembershipExpose](../../../sysml/model/sysml/MembershipExpose.html)`, `[MembershipImport](MembershipImport.html)`, `[NamespaceExpose](../../../sysml/model/sysml/NamespaceExpose.html)`, `[NamespaceImport](NamespaceImport.html)`

@OpenApiAllpublic interfaceImportextends [Relationship](Relationship.html)

An `Import` is an `Relationship` between its `importOwningNamespace` and either a `Membership` (for a `MembershipImport`) or another `Namespace` (for a `NamespaceImport`), which determines a set of `Memberships` that become `importedMemberships` of the `importOwningNamespace`. If `isImportAll = false` (the default), then only public `Memberships` are considered "visible". If `isImportAll = true`, then all `Memberships` are considered "visible", regardless of their declared `visibility`. If `isRecursive = true`, then visible `Memberships` are also recursively imported from owned sub-`Namespaces`.
 
 
 importOwningNamespace.owner = null implies 
 visibility = VisibilityKind::private

Model:
abstract=true

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](Element.html)`
`[getImportedElement](#getImportedElement())()`
The effectively imported `Element` for this Import.
`[Namespace](Namespace.html)`
`[getImportOwningNamespace](#getImportOwningNamespace())()`
The Namespace into which Memberships are imported by this Import, which must be the `owningRelatedElement` of the Import.
`[VisibilityKind](VisibilityKind.html)`
`[getVisibility](#getVisibility())()`
The visibility level of the imported `members` from this Import relative to the `importOwningNamespace`.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)>`
`[importedMemberships](#importedMemberships(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)`
Returns Memberships that are to become `importedMemberships` of the `importOwningNamespace`.
`boolean`
`[isImportAll](#isImportAll())()`
Whether to import memberships without regard to declared visibility.
`boolean`
`[isRecursive](#isRecursive())()`
Whether to recursively import Memberships from visible, owned sub-Namespaces.
`void`
`[setImportOwningNamespace](#setImportOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](Namespace.html) value)`
The Namespace into which Memberships are imported by this Import, which must be the `owningRelatedElement` of the Import.
`void`
`[setIsImportAll](#setIsImportAll(boolean))(boolean value)`
Whether to import memberships without regard to declared visibility.
`void`
`[setIsRecursive](#setIsRecursive(boolean))(boolean value)`
Whether to recursively import Memberships from visible, owned sub-Namespaces.
`void`
`[setVisibility](#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind))([VisibilityKind](VisibilityKind.html) value)`
The visibility level of the imported `members` from this Import relative to the `importOwningNamespace`.
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
getImportOwningNamespace
@CheckForNull[Namespace](Namespace.html) getImportOwningNamespace()
The Namespace into which Memberships are imported by this Import, which must be the `owningRelatedElement` of the Import.
Returns:
the importOwningNamespace value
Model:
derived="true"
 transient="true"
 opposite=[`Namespace.getOwnedImport()`](Namespace.html#getOwnedImport())
 subsets=[`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
setImportOwningNamespace
void setImportOwningNamespace(@CheckForNull
 [Namespace](Namespace.html) value)
The Namespace into which Memberships are imported by this Import, which must be the `owningRelatedElement` of the Import.
Parameters:
`value` - the importOwningNamespace value
Model:
derived="true"
 transient="true"
 opposite=[`Namespace.getOwnedImport()`](Namespace.html#getOwnedImport())
 subsets=[`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getVisibility
@CheckForNull[VisibilityKind](VisibilityKind.html) getVisibility()
The visibility level of the imported `members` from this Import relative to the `importOwningNamespace`. The default is `private`.
Returns:
the visibility value
Model:
derived="false"
 transient="false"
setVisibility
void setVisibility(@CheckForNull
 [VisibilityKind](VisibilityKind.html) value)
The visibility level of the imported `members` from this Import relative to the `importOwningNamespace`. The default is `private`.
Parameters:
`value` - the visibility value
Model:
derived="false"
 transient="false"
isRecursive
boolean isRecursive()
Whether to recursively import Memberships from visible, owned sub-Namespaces.
Returns:
the isRecursive value
Model:
derived="false"
 transient="false"
setIsRecursive
void setIsRecursive(boolean value)
Whether to recursively import Memberships from visible, owned sub-Namespaces.
Parameters:
`value` - the isRecursive value
Model:
derived="false"
 transient="false"
isImportAll
boolean isImportAll()
Whether to import memberships without regard to declared visibility.
Returns:
the isImportAll value
Model:
derived="false"
 transient="false"
setIsImportAll
void setIsImportAll(boolean value)
Whether to import memberships without regard to declared visibility.
Parameters:
`value` - the isImportAll value
Model:
derived="false"
 transient="false"
getImportedElement
@CheckForNull[Element](Element.html) getImportedElement()
The effectively imported `Element` for this Import. For a `MembershipImport`, this is the `memberElement` of the `importedMembership`. For a `NamespaceImport`, it is the `importedNamespace`.
Returns:
the importedElement value
Model:
derived="true"
 transient="true"
 oppositeRoleName="membershipImport"
importedMemberships
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Membership](Membership.html)> importedMemberships([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Namespace](Namespace.html)> excluded)
Returns Memberships that are to become `importedMemberships` of the `importOwningNamespace`. (The `excluded` parameter is used to handle the possibility of circular Import Relationships.)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Import">Interface Import</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../sysml/model/sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a></code>, <code><a href="../../../sysml/model/sysml/MembershipExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">MembershipExpose</a></code>, <code><a href="MembershipImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MembershipImport</a></code>, <code><a href="../../../sysml/model/sysml/NamespaceExpose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">NamespaceExpose</a></code>, <code><a href="NamespaceImport.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">NamespaceImport</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Import</span><span class="extends-implements">
extends <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>An <code>Import</code> is an <code>Relationship</code> between its <code>importOwningNamespace</code> and either a <code>Membership</code> (for a <code>MembershipImport</code>) or another <code>Namespace</code> (for a <code>NamespaceImport</code>), which determines a set of <code>Memberships</code> that become <code>importedMemberships</code> of the <code>importOwningNamespace</code>. If <code>isImportAll = false</code> (the default), then only public <code>Memberships</code> are considered "visible". If <code>isImportAll = true</code>, then all <code>Memberships</code> are considered "visible", regardless of their declared <code>visibility</code>. If <code>isRecursive = true</code>, then visible <code>Memberships</code> are also recursively imported from owned sub-<code>Namespaces</code>.</p>
 
 
 importOwningNamespace.owner = null implies 
     visibility = VisibilityKind::private</div>
<dl class="notes">
<dt>Model:</dt>
<dd>abstract=true</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedElement()">getImportedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The effectively imported <code>Element</code> for this Import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportOwningNamespace()">getImportOwningNamespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Namespace into which Memberships are imported by this Import, which must be the <code>owningRelatedElement</code> of the Import.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The visibility level of the imported <code>members</code> from this Import relative to the <code>importOwningNamespace</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importedMemberships(java.util.List)">importedMemberships</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Memberships that are to become <code>importedMemberships</code> of the <code>importOwningNamespace</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isImportAll()">isImportAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether to import memberships without regard to declared visibility.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isRecursive()">isRecursive</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether to recursively import Memberships from visible, owned sub-Namespaces.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setImportOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">setImportOwningNamespace</a><wbr/>(<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Namespace into which Memberships are imported by this Import, which must be the <code>owningRelatedElement</code> of the Import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsImportAll(boolean)">setIsImportAll</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether to import memberships without regard to declared visibility.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsRecursive(boolean)">setIsRecursive</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether to recursively import Memberships from visible, owned sub-Namespaces.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind)">setVisibility</a><wbr/>(<a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The visibility level of the imported <code>members</code> from this Import relative to the <code>importOwningNamespace</code>.</div>
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
<section class="detail" id="getImportOwningNamespace()">
<h3>getImportOwningNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">getImportOwningNamespace</span>()</div>
<div class="block"><p>The Namespace into which Memberships are imported by this Import, which must be the <code>owningRelatedElement</code> of the Import.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the importOwningNamespace value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Namespace.html#getOwnedImport()"><code>Namespace.getOwnedImport()</code></a>
        subsets=<a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImportOwningNamespace(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>setImportOwningNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setImportOwningNamespace</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> value)</span></div>
<div class="block"><p>The Namespace into which Memberships are imported by this Import, which must be the <code>owningRelatedElement</code> of the Import.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the importOwningNamespace value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Namespace.html#getOwnedImport()"><code>Namespace.getOwnedImport()</code></a>
        subsets=<a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibility()">
<h3>getVisibility</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="VisibilityKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">VisibilityKind</a></span> <span class="element-name">getVisibility</span>()</div>
<div class="block"><p>The visibility level of the imported <code>members</code> from this Import relative to the <code>importOwningNamespace</code>. The default is <code>private</code>.</p></div>
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
<div class="block"><p>The visibility level of the imported <code>members</code> from this Import relative to the <code>importOwningNamespace</code>. The default is <code>private</code>.</p></div>
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
<section class="detail" id="isRecursive()">
<h3>isRecursive</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isRecursive</span>()</div>
<div class="block"><p>Whether to recursively import Memberships from visible, owned sub-Namespaces.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isRecursive value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsRecursive(boolean)">
<h3>setIsRecursive</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsRecursive</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether to recursively import Memberships from visible, owned sub-Namespaces.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isRecursive value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImportAll()">
<h3>isImportAll</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isImportAll</span>()</div>
<div class="block"><p>Whether to import memberships without regard to declared visibility.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isImportAll value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsImportAll(boolean)">
<h3>setIsImportAll</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsImportAll</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether to import memberships without regard to declared visibility.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isImportAll value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportedElement()">
<h3>getImportedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getImportedElement</span>()</div>
<div class="block"><p>The effectively imported <code>Element</code> for this Import. For a <code>MembershipImport</code>, this is the <code>memberElement</code> of the <code>importedMembership</code>. For a <code>NamespaceImport</code>, it is the <code>importedNamespace</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the importedElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="membershipImport"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importedMemberships(java.util.List)">
<h3>importedMemberships</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a>&gt;</span> <span class="element-name">importedMemberships</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a>&gt; excluded)</span></div>
<div class="block"><p>Returns Memberships that are to become <code>importedMemberships</code> of the <code>importOwningNamespace</code>. (The <code>excluded</code> parameter is used to handle the possibility of circular Import Relationships.)</p></div>
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
