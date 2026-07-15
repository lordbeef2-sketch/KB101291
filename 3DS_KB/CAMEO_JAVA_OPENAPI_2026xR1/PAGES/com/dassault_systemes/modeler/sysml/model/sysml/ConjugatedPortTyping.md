# JAVA OPENAPI: ConjugatedPortTyping (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/ConjugatedPortTyping.html
- source_path: `com/dassault_systemes/modeler/sysml/model/sysml/ConjugatedPortTyping.html`
- source_sha256: `a353ca62901a6c1ce2e1c089c4a0524b44d14bbda450250ef13514c91e5fef1b`
- captured_utc: `2026-07-14T16:45:03.429048+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model.sysml](package-summary.html)

## Interface ConjugatedPortTyping

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../../kerml/model/kerml/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[FeatureTyping](../../../kerml/model/kerml/FeatureTyping.html)`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](../../../kerml/model/kerml/Relationship.html)`, `[Specialization](../../../kerml/model/kerml/Specialization.html)`

@OpenApiAllpublic interfaceConjugatedPortTypingextends [FeatureTyping](../../../kerml/model/kerml/FeatureTyping.html)

A `ConjugatedPortTyping` is a `FeatureTyping` whose `type` is a `ConjugatedPortDefinition`. (This relationship is intended to be an abstract-syntax marker for a special surface notation for conjugated typing of ports.)
 portDefinition = conjugatedPortDefinition.originalPortDefinition

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ConjugatedPortDefinition](ConjugatedPortDefinition.html)`
`[getConjugatedPortDefinition](#getConjugatedPortDefinition())()`
The `type` of this `ConjugatedPortTyping` considered as a `FeatureTyping`, which must be a `ConjugatedPortDefinition`.
`[PortDefinition](PortDefinition.html)`
`[getPortDefinition](#getPortDefinition())()`
The `originalPortDefinition` of the `conjugatedPortDefinition` of this `ConjugatedPortTyping`.
`void`
`[setConjugatedPortDefinition](#setConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition))([ConjugatedPortDefinition](ConjugatedPortDefinition.html) value)`
The `type` of this `ConjugatedPortTyping` considered as a `FeatureTyping`, which must be a `ConjugatedPortDefinition`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](../../../kerml/model/kerml/Element.html)
`[effectiveName](../../../kerml/model/kerml/Element.html#effectiveName()), [effectiveShortName](../../../kerml/model/kerml/Element.html#effectiveShortName()), [escapedName](../../../kerml/model/kerml/Element.html#escapedName()), [getAliasIds](../../../kerml/model/kerml/Element.html#getAliasIds()), [getDeclaredName](../../../kerml/model/kerml/Element.html#getDeclaredName()), [getDeclaredShortName](../../../kerml/model/kerml/Element.html#getDeclaredShortName()), [getDocumentation](../../../kerml/model/kerml/Element.html#getDocumentation()), [getElementId](../../../kerml/model/kerml/Element.html#getElementId()), [getName](../../../kerml/model/kerml/Element.html#getName()), [getOwnedAnnotation](../../../kerml/model/kerml/Element.html#getOwnedAnnotation()), [getOwnedElement](../../../kerml/model/kerml/Element.html#getOwnedElement()), [getOwnedRelationship](../../../kerml/model/kerml/Element.html#getOwnedRelationship()), [getOwner](../../../kerml/model/kerml/Element.html#getOwner()), [getOwningMembership](../../../kerml/model/kerml/Element.html#getOwningMembership()), [getOwningNamespace](../../../kerml/model/kerml/Element.html#getOwningNamespace()), [getOwningRelationship](../../../kerml/model/kerml/Element.html#getOwningRelationship()), [getQualifiedName](../../../kerml/model/kerml/Element.html#getQualifiedName()), [getShortName](../../../kerml/model/kerml/Element.html#getShortName()), [getTextualRepresentation](../../../kerml/model/kerml/Element.html#getTextualRepresentation()), [isImpliedIncluded](../../../kerml/model/kerml/Element.html#isImpliedIncluded()), [isLibraryElement](../../../kerml/model/kerml/Element.html#isLibraryElement()), [setDeclaredName](../../../kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](../../../kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)), [setElementId](../../../kerml/model/kerml/Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](../../../kerml/model/kerml/Element.html#setIsImpliedIncluded(boolean)), [setOwner](../../../kerml/model/kerml/Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](../../../kerml/model/kerml/Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](../../../kerml/model/kerml/Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[FeatureTyping](../../../kerml/model/kerml/FeatureTyping.html)
`[getOwningFeature](../../../kerml/model/kerml/FeatureTyping.html#getOwningFeature()), [getType](../../../kerml/model/kerml/FeatureTyping.html#getType()), [getTypedFeature](../../../kerml/model/kerml/FeatureTyping.html#getTypedFeature()), [setType](../../../kerml/model/kerml/FeatureTyping.html#setType(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [setTypedFeature](../../../kerml/model/kerml/FeatureTyping.html#setTypedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](../../../kerml/model/kerml/Relationship.html)
`[getOwnedRelatedElement](../../../kerml/model/kerml/Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](../../../kerml/model/kerml/Relationship.html#getOwningRelatedElement()), [getRelatedElement](../../../kerml/model/kerml/Relationship.html#getRelatedElement()), [getSource](../../../kerml/model/kerml/Relationship.html#getSource()), [getTarget](../../../kerml/model/kerml/Relationship.html#getTarget()), [isImplied](../../../kerml/model/kerml/Relationship.html#isImplied()), [libraryNamespace](../../../kerml/model/kerml/Relationship.html#libraryNamespace()), [path](../../../kerml/model/kerml/Relationship.html#path()), [setIsImplied](../../../kerml/model/kerml/Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](../../../kerml/model/kerml/Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Specialization](../../../kerml/model/kerml/Specialization.html)
`[getGeneral](../../../kerml/model/kerml/Specialization.html#getGeneral()), [getOwningType](../../../kerml/model/kerml/Specialization.html#getOwningType()), [getSpecific](../../../kerml/model/kerml/Specialization.html#getSpecific()), [setGeneral](../../../kerml/model/kerml/Specialization.html#setGeneral(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [setSpecific](../../../kerml/model/kerml/Specialization.html#setSpecific(com.dassault_systemes.modeler.kerml.model.kerml.Type))`

============ METHOD DETAIL ========== 
Method Details
getPortDefinition
@CheckForNull[PortDefinition](PortDefinition.html) getPortDefinition()
The `originalPortDefinition` of the `conjugatedPortDefinition` of this `ConjugatedPortTyping`.
Returns:
the portDefinition value
Model:
derived="true"
 transient="true"
 oppositeRoleName="conjugatedPortTyping"
getConjugatedPortDefinition
@CheckForNull[ConjugatedPortDefinition](ConjugatedPortDefinition.html) getConjugatedPortDefinition()
The `type` of this `ConjugatedPortTyping` considered as a `FeatureTyping`, which must be a `ConjugatedPortDefinition`.
Returns:
the conjugatedPortDefinition value
Model:
derived="false"
 transient="false"
 oppositeRoleName="typingByConjugatedPort"
setConjugatedPortDefinition
void setConjugatedPortDefinition(@CheckForNull
 [ConjugatedPortDefinition](ConjugatedPortDefinition.html) value)
The `type` of this `ConjugatedPortTyping` considered as a `FeatureTyping`, which must be a `ConjugatedPortDefinition`.
Parameters:
`value` - the conjugatedPortDefinition value
Model:
derived="false"
 transient="false"
 oppositeRoleName="typingByConjugatedPort"

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model.sysml</a></div>
<h1 class="title" title="Interface ConjugatedPortTyping">Interface ConjugatedPortTyping</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../kerml/model/kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../../kerml/model/kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="../../../kerml/model/kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ConjugatedPortTyping</span><span class="extends-implements">
extends <a href="../../../kerml/model/kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></span></div>
<div class="block"><p>A <code>ConjugatedPortTyping</code> is a <code>FeatureTyping</code> whose <code>type</code> is a <code>ConjugatedPortDefinition</code>. (This relationship is intended to be an abstract-syntax marker for a special surface notation for conjugated typing of ports.)</p>
 portDefinition = conjugatedPortDefinition.originalPortDefinition</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConjugatedPortDefinition()">getConjugatedPortDefinition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>type</code> of this <code>ConjugatedPortTyping</code> considered as a <code>FeatureTyping</code>, which must be a <code>ConjugatedPortDefinition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPortDefinition()">getPortDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>originalPortDefinition</code> of the <code>conjugatedPortDefinition</code> of this <code>ConjugatedPortTyping</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition)">setConjugatedPortDefinition</a><wbr/>(<a href="ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>type</code> of this <code>ConjugatedPortTyping</code> considered as a <code>FeatureTyping</code>, which must be a <code>ConjugatedPortDefinition</code>.</div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.FeatureTyping">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/FeatureTyping.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureTyping</a></h3>
<code><a href="../../../kerml/model/kerml/FeatureTyping.html#getOwningFeature()">getOwningFeature</a>, <a href="../../../kerml/model/kerml/FeatureTyping.html#getType()">getType</a>, <a href="../../../kerml/model/kerml/FeatureTyping.html#getTypedFeature()">getTypedFeature</a>, <a href="../../../kerml/model/kerml/FeatureTyping.html#setType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setType</a>, <a href="../../../kerml/model/kerml/FeatureTyping.html#setTypedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setTypedFeature</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="../../../kerml/model/kerml/Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="../../../kerml/model/kerml/Relationship.html#getSource()">getSource</a>, <a href="../../../kerml/model/kerml/Relationship.html#getTarget()">getTarget</a>, <a href="../../../kerml/model/kerml/Relationship.html#isImplied()">isImplied</a>, <a href="../../../kerml/model/kerml/Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="../../../kerml/model/kerml/Relationship.html#path()">path</a>, <a href="../../../kerml/model/kerml/Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="../../../kerml/model/kerml/Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Specialization">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="../../../kerml/model/kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></h3>
<code><a href="../../../kerml/model/kerml/Specialization.html#getGeneral()">getGeneral</a>, <a href="../../../kerml/model/kerml/Specialization.html#getOwningType()">getOwningType</a>, <a href="../../../kerml/model/kerml/Specialization.html#getSpecific()">getSpecific</a>, <a href="../../../kerml/model/kerml/Specialization.html#setGeneral(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setGeneral</a>, <a href="../../../kerml/model/kerml/Specialization.html#setSpecific(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setSpecific</a></code></div>
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
<section class="detail" id="getPortDefinition()">
<h3>getPortDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></span> <span class="element-name">getPortDefinition</span>()</div>
<div class="block"><p>The <code>originalPortDefinition</code> of the <code>conjugatedPortDefinition</code> of this <code>ConjugatedPortTyping</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the portDefinition value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        oppositeRoleName="conjugatedPortTyping"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConjugatedPortDefinition()">
<h3>getConjugatedPortDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a></span> <span class="element-name">getConjugatedPortDefinition</span>()</div>
<div class="block"><p>The <code>type</code> of this <code>ConjugatedPortTyping</code> considered as a <code>FeatureTyping</code>, which must be a <code>ConjugatedPortDefinition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the conjugatedPortDefinition value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="typingByConjugatedPort"</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.ConjugatedPortDefinition)">
<h3>setConjugatedPortDefinition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setConjugatedPortDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a> value)</span></div>
<div class="block"><p>The <code>type</code> of this <code>ConjugatedPortTyping</code> considered as a <code>FeatureTyping</code>, which must be a <code>ConjugatedPortDefinition</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the conjugatedPortDefinition value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="typingByConjugatedPort"</dd>
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
