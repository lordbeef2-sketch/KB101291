# JAVA OPENAPI: Annotation (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Annotation.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Annotation.html`
- source_sha256: `31fdf534f8ead0278e1310c01e74189056dd9202f0c4c17e7bb6b47738b90468`
- captured_utc: `2026-07-14T16:44:48.506847+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Annotation

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`

@OpenApiAllpublic interfaceAnnotationextends [Relationship](Relationship.html)

An `Annotation` is a Relationship between an `AnnotatingElement` and the `Element` that is annotated by that `AnnotatingElement`.
 
 (owningAnnotatedElement <> null) = (ownedAnnotatingElement <> null)
 ownedAnnotatingElement <> null xor owningAnnotatingElement <> null
 ownedAnnotatingElement =
 let ownedAnnotatingElements : Sequence(AnnotatingElement) = 
 ownedRelatedElement->selectByKind(AnnotatingElement) in
 if ownedAnnotatingElements->isEmpty() then null
 else ownedAnnotatingElements->first()
 endif
 annotatingElement =
 if ownedAnnotatingElement <> null then ownedAnnotatingElement
 else owningAnnotatingElement
 endif

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](Element.html)`
`[getAnnotatedElement](#getAnnotatedElement())()`
The `Element` that is annotated by the `annotatingElement` of this Annotation.
`[AnnotatingElement](AnnotatingElement.html)`
`[getAnnotatingElement](#getAnnotatingElement())()`
The `AnnotatingElement` that annotates the `annotatedElement` of this `Annotation`.
`[AnnotatingElement](AnnotatingElement.html)`
`[getOwnedAnnotatingElement](#getOwnedAnnotatingElement())()`
The `annotatingElement` of this `Annotation`, when it is an `ownedRelatedElement`.
`[Element](Element.html)`
`[getOwningAnnotatedElement](#getOwningAnnotatedElement())()`
The `annotatedElement` of this `Annotation`, when it is also the `owningRelatedElement`.
`[AnnotatingElement](AnnotatingElement.html)`
`[getOwningAnnotatingElement](#getOwningAnnotatingElement())()`
The `annotatingElement` of this `Annotation`, when it is the `owningRelatedElement`.
`void`
`[setAnnotatedElement](#setAnnotatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](Element.html) value)`
The `Element` that is annotated by the `annotatingElement` of this Annotation.
`void`
`[setAnnotatingElement](#setAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement))([AnnotatingElement](AnnotatingElement.html) value)`
The `AnnotatingElement` that annotates the `annotatedElement` of this `Annotation`.
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
getAnnotatingElement
@CheckForNull[AnnotatingElement](AnnotatingElement.html) getAnnotatingElement()
The `AnnotatingElement` that annotates the `annotatedElement` of this `Annotation`. This is always either the `ownedAnnotatingElement` or the `owningAnnotatingElement`.
Returns:
the annotatingElement value
Model:
derived="true"
 transient="true"
 opposite=[`AnnotatingElement.getAnnotation()`](AnnotatingElement.html#getAnnotation())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
setAnnotatingElement
void setAnnotatingElement(@CheckForNull
 [AnnotatingElement](AnnotatingElement.html) value)
The `AnnotatingElement` that annotates the `annotatedElement` of this `Annotation`. This is always either the `ownedAnnotatingElement` or the `owningAnnotatingElement`.
Parameters:
`value` - the annotatingElement value
Model:
derived="true"
 transient="true"
 opposite=[`AnnotatingElement.getAnnotation()`](AnnotatingElement.html#getAnnotation())
 redefines=[`Relationship.getSource()`](Relationship.html#getSource())
getAnnotatedElement
@CheckForNull[Element](Element.html) getAnnotatedElement()
The `Element` that is annotated by the `annotatingElement` of this Annotation.
Returns:
the annotatedElement value
Model:
derived="false"
 transient="false"
 oppositeRoleName="annotation"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
setAnnotatedElement
void setAnnotatedElement(@CheckForNull
 [Element](Element.html) value)
The `Element` that is annotated by the `annotatingElement` of this Annotation.
Parameters:
`value` - the annotatedElement value
Model:
derived="false"
 transient="false"
 oppositeRoleName="annotation"
 redefines=[`Relationship.getTarget()`](Relationship.html#getTarget())
getOwningAnnotatedElement
@CheckForNull[Element](Element.html) getOwningAnnotatedElement()
The `annotatedElement` of this `Annotation`, when it is also the `owningRelatedElement`.
Returns:
the owningAnnotatedElement value
Model:
derived="true"
 transient="true"
 opposite=[`Element.getOwnedAnnotation()`](Element.html#getOwnedAnnotation())
 subsets=[`getAnnotatedElement()`](#getAnnotatedElement()), [`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
getOwningAnnotatingElement
@CheckForNull[AnnotatingElement](AnnotatingElement.html) getOwningAnnotatingElement()
The `annotatingElement` of this `Annotation`, when it is the `owningRelatedElement`.
Returns:
the owningAnnotatingElement value
Model:
derived="true"
 transient="true"
 opposite=[`AnnotatingElement.getOwnedAnnotatingRelationship()`](AnnotatingElement.html#getOwnedAnnotatingRelationship())
 subsets=[`getAnnotatingElement()`](#getAnnotatingElement()), [`Relationship.getOwningRelatedElement()`](Relationship.html#getOwningRelatedElement())
getOwnedAnnotatingElement
@CheckForNull[AnnotatingElement](AnnotatingElement.html) getOwnedAnnotatingElement()
The `annotatingElement` of this `Annotation`, when it is an `ownedRelatedElement`.
Returns:
the ownedAnnotatingElement value
Model:
derived="true"
 transient="true"
 opposite=[`AnnotatingElement.getOwningAnnotatingRelationship()`](AnnotatingElement.html#getOwningAnnotatingRelationship())
 subsets=[`getAnnotatingElement()`](#getAnnotatingElement()), [`Relationship.getOwnedRelatedElement()`](Relationship.html#getOwnedRelatedElement())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Annotation">Interface Annotation</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Annotation</span><span class="extends-implements">
extends <a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></span></div>
<div class="block"><p>An <code>Annotation</code> is a Relationship between an <code>AnnotatingElement</code> and the <code>Element</code> that is annotated by that <code>AnnotatingElement</code>.</p>
 
 (owningAnnotatedElement &lt;&gt; null) = (ownedAnnotatingElement &lt;&gt; null)
 ownedAnnotatingElement &lt;&gt; null xor owningAnnotatingElement &lt;&gt; null
 ownedAnnotatingElement =
     let ownedAnnotatingElements : Sequence(AnnotatingElement) = 
         ownedRelatedElement-&gt;selectByKind(AnnotatingElement) in
     if ownedAnnotatingElements-&gt;isEmpty() then null
     else ownedAnnotatingElements-&gt;first()
     endif
 annotatingElement =
     if ownedAnnotatingElement &lt;&gt; null then ownedAnnotatingElement
     else owningAnnotatingElement
     endif</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAnnotatedElement()">getAnnotatedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Element</code> that is annotated by the <code>annotatingElement</code> of this Annotation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAnnotatingElement()">getAnnotatingElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AnnotatingElement</code> that annotates the <code>annotatedElement</code> of this <code>Annotation</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedAnnotatingElement()">getOwnedAnnotatingElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>annotatingElement</code> of this <code>Annotation</code>, when it is an <code>ownedRelatedElement</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningAnnotatedElement()">getOwningAnnotatedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>annotatedElement</code> of this <code>Annotation</code>, when it is also the <code>owningRelatedElement</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningAnnotatingElement()">getOwningAnnotatingElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>annotatingElement</code> of this <code>Annotation</code>, when it is the <code>owningRelatedElement</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAnnotatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setAnnotatedElement</a><wbr/>(<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Element</code> that is annotated by the <code>annotatingElement</code> of this Annotation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">setAnnotatingElement</a><wbr/>(<a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>AnnotatingElement</code> that annotates the <code>annotatedElement</code> of this <code>Annotation</code>.</div>
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
<section class="detail" id="getAnnotatingElement()">
<h3>getAnnotatingElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></span> <span class="element-name">getAnnotatingElement</span>()</div>
<div class="block"><p>The <code>AnnotatingElement</code> that annotates the <code>annotatedElement</code> of this <code>Annotation</code>. This is always either the <code>ownedAnnotatingElement</code> or the <code>owningAnnotatingElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the annotatingElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="AnnotatingElement.html#getAnnotation()"><code>AnnotatingElement.getAnnotation()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnnotatingElement(com.dassault_systemes.modeler.kerml.model.kerml.AnnotatingElement)">
<h3>setAnnotatingElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAnnotatingElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a> value)</span></div>
<div class="block"><p>The <code>AnnotatingElement</code> that annotates the <code>annotatedElement</code> of this <code>Annotation</code>. This is always either the <code>ownedAnnotatingElement</code> or the <code>owningAnnotatingElement</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the annotatingElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="AnnotatingElement.html#getAnnotation()"><code>AnnotatingElement.getAnnotation()</code></a>
        redefines=<a href="Relationship.html#getSource()"><code>Relationship.getSource()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatedElement()">
<h3>getAnnotatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getAnnotatedElement</span>()</div>
<div class="block"><p>The <code>Element</code> that is annotated by the <code>annotatingElement</code> of this Annotation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the annotatedElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="annotation"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnnotatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setAnnotatedElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAnnotatedElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> value)</span></div>
<div class="block"><p>The <code>Element</code> that is annotated by the <code>annotatingElement</code> of this Annotation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the annotatedElement value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="annotation"
        redefines=<a href="Relationship.html#getTarget()"><code>Relationship.getTarget()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningAnnotatedElement()">
<h3>getOwningAnnotatedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getOwningAnnotatedElement</span>()</div>
<div class="block"><p>The <code>annotatedElement</code> of this <code>Annotation</code>, when it is also the <code>owningRelatedElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningAnnotatedElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="Element.html#getOwnedAnnotation()"><code>Element.getOwnedAnnotation()</code></a>
        subsets=<a href="#getAnnotatedElement()"><code>getAnnotatedElement()</code></a>, <a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningAnnotatingElement()">
<h3>getOwningAnnotatingElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></span> <span class="element-name">getOwningAnnotatingElement</span>()</div>
<div class="block"><p>The <code>annotatingElement</code> of this <code>Annotation</code>, when it is the <code>owningRelatedElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the owningAnnotatingElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="AnnotatingElement.html#getOwnedAnnotatingRelationship()"><code>AnnotatingElement.getOwnedAnnotatingRelationship()</code></a>
        subsets=<a href="#getAnnotatingElement()"><code>getAnnotatingElement()</code></a>, <a href="Relationship.html#getOwningRelatedElement()"><code>Relationship.getOwningRelatedElement()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedAnnotatingElement()">
<h3>getOwnedAnnotatingElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="AnnotatingElement.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">AnnotatingElement</a></span> <span class="element-name">getOwnedAnnotatingElement</span>()</div>
<div class="block"><p>The <code>annotatingElement</code> of this <code>Annotation</code>, when it is an <code>ownedRelatedElement</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the ownedAnnotatingElement value</dd>
<dt>Model:</dt>
<dd>derived="true"
        transient="true"
        opposite=<a href="AnnotatingElement.html#getOwningAnnotatingRelationship()"><code>AnnotatingElement.getOwningAnnotatingRelationship()</code></a>
        subsets=<a href="#getAnnotatingElement()"><code>getAnnotatingElement()</code></a>, <a href="Relationship.html#getOwnedRelatedElement()"><code>Relationship.getOwnedRelatedElement()</code></a></dd>
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
