# JAVA OPENAPI: FeatureInverting (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureInverting.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/FeatureInverting.html`
- source_sha256: `3db4843f03fd801a81fb0289d758509e7ea3eb53c4f2e7b4fe9b99c77af3e894`
- captured_utc: `2026-07-14T16:44:48.907856+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface FeatureInverting

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`

@OpenApiAllpublic interfaceFeatureInvertingextends [Relationship](Relationship.html)

A `FeatureInverting` is a `Relationship` between `Features` asserting that their interpretations (sequences) are the reverse of each other, identified as `featureInverted` and `invertingFeature`. For example, a `Feature` identifying each person's parents is the inverse of a `Feature` identifying each person's children. A person identified as a parent of another will identify that other as one of their children.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Feature](Feature.html)`
`[getFeatureInverted](#getFeatureInverted())()`
The `Feature` that is an inverse of the `invertingFeature`.
`[Feature](Feature.html)`
`[getInvertingFeature](#getInvertingFeature())()`
The `Feature` that is an inverse of the `invertedFeature`.
`[Feature](Feature.html)`
`[getOwningFeature](#getOwningFeature())()`
A `featureInverted` that is also the `owningRelatedElement` of this `FeatureInverting`.
`void`
`[setFeatureInverted](#setFeatureInverted(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) value)`
The `Feature` that is an inverse of the `invertingFeature`.
`void`
`[setInvertingFeature](#setInvertingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) value)`
The `Feature` that is an inverse of the `invertedFeature`.
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
getFeatureInverted
@CheckForNull[Feature](Feature.html) getFeatureInverted()
The `Feature` that is an inverse of the `invertingFeature`.
Returns:
the featureInverted value
Model:
derived="false"
 transient="false"
 oppositeRoleName="invertingFeatureInverting"
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
setFeatureInverted
void setFeatureInverted(@CheckForNull
 [Feature](Feature.html) value)
The `Feature` that is an inverse of the `invertingFeature`.
Parameters:
`value` - the featureInverted value
Model:
derived="false"
 transient="false"
 oppositeRoleName="invertingFeatureInverting"
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getInvertingFeature
@CheckForNull[Feature](Feature.html) getInvertingFeature()
The `Feature` that is an inverse of the `invertedFeature`.
Returns:
the invertingFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="invertedFeatureInverting"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
setInvertingFeature
void setInvertingFeature(@CheckForNull
 [Feature](Feature.html) value)
The `Feature` that is an inverse of the `invertedFeature`.
Parameters:
`value` - the invertingFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="invertedFeatureInverting"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
getOwningFeature
@CheckForNull[Feature](Feature.html) getOwningFeature()
A `featureInverted` that is also the `owningRelatedElement` of this `FeatureInverting`.
Returns:
the owningFeature value
Model:
derived="true"
 transient="true"
 opposite=[`Feature.getOwnedFeatureInverting()`](Feature.html#getOwnedFeatureInverting())
 subsets=[`getFeatureInverted()`](#getFeatureInverted()), [`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface FeatureInverting">Interface FeatureInverting</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">FeatureInverting</span><span class="extends-implements">
extends <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>A <code>FeatureInverting</code> is a <code>Relationship</code> between <code>Features</code> asserting that their interpretations (sequences) are the reverse of each other, identified as <code>featureInverted</code> and <code>invertingFeature</code>. For example, a <code>Feature</code> identifying each person's parents is the inverse of a <code>Feature</code> identifying each person's children. A person identified as a parent of another will identify that other as one of their children.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureInverted()">getFeatureInverted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is an inverse of the <code>invertingFeature</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInvertingFeature()">getInvertingFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is an inverse of the <code>invertedFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningFeature()">getOwningFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A <code>featureInverted</code> that is also the <code>owningRelatedElement</code> of this <code>FeatureInverting</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFeatureInverted(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setFeatureInverted</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is an inverse of the <code>invertingFeature</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInvertingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setInvertingFeature</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is an inverse of the <code>invertedFeature</code>.</div>
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
<section class="detail" id="getFeatureInverted()">
<h3>getFeatureInverted</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFeatureInverted</span>()</div>
<div class="block"><p>The <code>Feature</code> that is an inverse of the <code>invertingFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the featureInverted value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="invertingFeatureInverting"
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFeatureInverted(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setFeatureInverted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFeatureInverted</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</span></div>
<div class="block"><p>The <code>Feature</code> that is an inverse of the <code>invertingFeature</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the featureInverted value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="invertingFeatureInverting"
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvertingFeature()">
<h3>getInvertingFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getInvertingFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that is an inverse of the <code>invertedFeature</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the invertingFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="invertedFeatureInverting"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvertingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setInvertingFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInvertingFeature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</span></div>
<div class="block"><p>The <code>Feature</code> that is an inverse of the <code>invertedFeature</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the invertingFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="invertedFeatureInverting"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningFeature()">
<h3>getOwningFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwningFeature</span>()</div>
<div class="block"><p>A <code>featureInverted</code> that is also the <code>owningRelatedElement</code> of this <code>FeatureInverting</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningFeature value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Feature.html#getOwnedFeatureInverting()"><code>Feature.getOwnedFeatureInverting()</code></a>
        subsets=<a href="#getFeatureInverted()"><code>getFeatureInverted()</code></a>, <a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a></dd>
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
