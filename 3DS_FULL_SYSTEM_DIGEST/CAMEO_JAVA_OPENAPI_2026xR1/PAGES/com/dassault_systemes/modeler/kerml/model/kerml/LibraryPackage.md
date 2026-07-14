# JAVA OPENAPI: LibraryPackage (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/LibraryPackage.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/LibraryPackage.html`
- source_sha256: `84c91243a87f1abeb2285d4c6653304969f95996454724612f437044ac2d0913`
- captured_utc: `2026-07-14T16:44:49.315862+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface LibraryPackage

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[Package](Package.html)`

@OpenApiAllpublic interfaceLibraryPackageextends [Package](Package.html)

A `LibraryPackage` is a `Package` that is the container for a model library. A `LibraryPackage` is itself a library `Element` as are all `Elements` that are directly or indirectly contained in it.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[isStandard](#isStandard())()`
Whether this `LibraryPackage` contains a standard library model.
`[Namespace](Namespace.html)`
`[libraryNamespace](#libraryNamespace())()`
The `libraryNamespace` for a `LibraryPackage` is itself.
`void`
`[setIsStandard](#setIsStandard(boolean))(boolean value)`
Whether this `LibraryPackage` contains a standard library model.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [path](Element.html#path()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Namespace](Namespace.html)
`[getImportedMembership](Namespace.html#getImportedMembership()), [getMember](Namespace.html#getMember()), [getMembership](Namespace.html#getMembership()), [getOwnedImport](Namespace.html#getOwnedImport()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedMembership](Namespace.html#getOwnedMembership()), [membershipsOfVisibility](Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)), [namesOf](Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [qualificationOf](Namespace.html#qualificationOf(java.lang.String)), [resolve](Namespace.html#resolve(java.lang.String)), [resolveGlobal](Namespace.html#resolveGlobal(java.lang.String)), [resolveLocal](Namespace.html#resolveLocal(java.lang.String)), [resolveVisible](Namespace.html#resolveVisible(java.lang.String)), [unqualifiedNameOf](Namespace.html#unqualifiedNameOf(java.lang.String)), [visibilityOf](Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)), [visibleMemberships](Namespace.html#visibleMemberships(java.util.List,boolean,boolean))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Package](Package.html)
`[getFilterCondition](Package.html#getFilterCondition()), [importedMemberships](Package.html#importedMemberships(java.util.List)), [includeAsMember](Package.html#includeAsMember(com.dassault_systemes.modeler.kerml.model.kerml.Element))`

============ METHOD DETAIL ========== 
Method Details
isStandard
boolean isStandard()
Whether this `LibraryPackage` contains a standard library model. This should only be set to true for `LibraryPackages` in the standard Kernel Model Libraries or in normative model libraries for a language built on KerML.
Returns:
the isStandard value
Model:
derived="false"
 transient="false"
setIsStandard
void setIsStandard(boolean value)
Whether this `LibraryPackage` contains a standard library model. This should only be set to true for `LibraryPackages` in the standard Kernel Model Libraries or in normative model libraries for a language built on KerML.
Parameters:
`value` - the isStandard value
Model:
derived="false"
 transient="false"
libraryNamespace
[Namespace](Namespace.html) libraryNamespace()
The `libraryNamespace` for a `LibraryPackage` is itself.
 self
Specified by:
`[libraryNamespace](Element.html#libraryNamespace())` in interface `[Element](Element.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface LibraryPackage">Interface LibraryPackage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">LibraryPackage</span><span class="extends-implements">
extends <a href="Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></span></div>
<div class="block"><p>A <code>LibraryPackage</code> is a <code>Package</code> that is the container for a model library. A <code>LibraryPackage</code> is itself a library <code>Element</code> as are all <code>Elements</code> that are directly or indirectly contained in it.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isStandard()">isStandard</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>LibraryPackage</code> contains a standard library model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#libraryNamespace()">libraryNamespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>libraryNamespace</code> for a <code>LibraryPackage</code> is itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIsStandard(boolean)">setIsStandard</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Whether this <code>LibraryPackage</code> contains a standard library model.</div>
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
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#path()">path</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Namespace">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></h3>
<code><a href="Namespace.html#getImportedMembership()">getImportedMembership</a>, <a href="Namespace.html#getMember()">getMember</a>, <a href="Namespace.html#getMembership()">getMembership</a>, <a href="Namespace.html#getOwnedImport()">getOwnedImport</a>, <a href="Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="Namespace.html#getOwnedMembership()">getOwnedMembership</a>, <a href="Namespace.html#membershipsOfVisibility(com.dassault_systemes.modeler.kerml.model.kerml.VisibilityKind,java.util.List)">membershipsOfVisibility</a>, <a href="Namespace.html#namesOf(com.dassault_systemes.modeler.kerml.model.kerml.Element)">namesOf</a>, <a href="Namespace.html#qualificationOf(java.lang.String)">qualificationOf</a>, <a href="Namespace.html#resolve(java.lang.String)">resolve</a>, <a href="Namespace.html#resolveGlobal(java.lang.String)">resolveGlobal</a>, <a href="Namespace.html#resolveLocal(java.lang.String)">resolveLocal</a>, <a href="Namespace.html#resolveVisible(java.lang.String)">resolveVisible</a>, <a href="Namespace.html#unqualifiedNameOf(java.lang.String)">unqualifiedNameOf</a>, <a href="Namespace.html#visibilityOf(com.dassault_systemes.modeler.kerml.model.kerml.Membership)">visibilityOf</a>, <a href="Namespace.html#visibleMemberships(java.util.List,boolean,boolean)">visibleMemberships</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Package">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Package.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Package</a></h3>
<code><a href="Package.html#getFilterCondition()">getFilterCondition</a>, <a href="Package.html#importedMemberships(java.util.List)">importedMemberships</a>, <a href="Package.html#includeAsMember(com.dassault_systemes.modeler.kerml.model.kerml.Element)">includeAsMember</a></code></div>
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
<section class="detail" id="isStandard()">
<h3>isStandard</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isStandard</span>()</div>
<div class="block"><p>Whether this <code>LibraryPackage</code> contains a standard library model. This should only be set to true for <code>LibraryPackages</code> in the standard Kernel Model Libraries or in normative model libraries for a language built on KerML.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the isStandard value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIsStandard(boolean)">
<h3>setIsStandard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIsStandard</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Whether this <code>LibraryPackage</code> contains a standard library model. This should only be set to true for <code>LibraryPackages</code> in the standard Kernel Model Libraries or in normative model libraries for a language built on KerML.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the isStandard value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="libraryNamespace()">
<h3>libraryNamespace</h3>
<div class="member-signature"><span class="return-type"><a href="Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a></span> <span class="element-name">libraryNamespace</span>()</div>
<div class="block"><p>The <code>libraryNamespace</code> for a <code>LibraryPackage</code> is itself.</p>
 self</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Element.html#libraryNamespace()">libraryNamespace</a></code> in interface <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></dd>
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
