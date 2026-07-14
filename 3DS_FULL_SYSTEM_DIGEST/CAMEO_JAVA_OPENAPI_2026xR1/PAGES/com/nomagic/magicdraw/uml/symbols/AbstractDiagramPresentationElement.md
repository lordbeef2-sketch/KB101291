# JAVA OPENAPI: AbstractDiagramPresentationElement (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html`
- source_sha256: `7c7d256ffd1f1fffa62a072c61c4ed9384783a71dc18deb4acdd610c173c4c32`
- captured_utc: `2026-07-14T16:46:05.850877+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class AbstractDiagramPresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](PresentationElement.html)
com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer`, `[BaseElement](../BaseElement.html)`, `[MDElement](../core/MDElement.html)`, `[ModelElementProvider](../core/ModelElementProvider.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[DiagramPresentationElement](DiagramPresentationElement.html)`

@OpenApipublic abstract classAbstractDiagramPresentationElement
extends [PresentationElement](PresentationElement.html)
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[DASHED_STROKE](PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](PresentationElement.html#SOLID_STROKE)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor))([BasePresentationElementVisitor](BasePresentationElementVisitor.html) visitor)`

`boolean`
`[addContentPropertyChangeListener](#addContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener for changes in all symbols contained in the diagram.
`final void`
`[close](#close())()`
Closes diagram window.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectPresentationElementsRecursively](#collectPresentationElementsRecursively())()`
Collects all elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingManipulatedElementsRecursively](#collectShowingManipulatedElementsRecursively())()`
Collects all visible manipulated elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingPresentationElementsRecursively](#collectShowingPresentationElementsRecursively())()`
Collects all visible elements in this diagram recursively.
`void`
`[ensureLoaded](#ensureLoaded())()`
Ensures that the diagram is loaded.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class))([ModelElement](../../../../dassault_systemes/modeler/foundation/model/ModelElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element for a given model element of the given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element for a given model element of a given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElementForPathConnecting](#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class))([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
`final [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)>`
`[findPresentationElementsForPathConnecting](#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
`boolean`
`[isLoaded](#isLoaded())()`
Check if the diagram is loaded.
`boolean`
`[isSymbolDiagram](#isSymbolDiagram())()`
Checks if diagram displays symbols as its contents.
`void`
`[open](#open())()`
Open the diagram
`void`
`[open](#open(boolean))(boolean showProgress)`
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
`void`
`[openInActiveTab](#openInActiveTab(boolean))(boolean showProgress)`
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
`boolean`
`[removeContentPropertyChangeListener](#removeContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregister the given listener from the diagram.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[collectSubManipulatedElements](PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getElement](PresentationElement.html#getElement()), [getManipulatedParent](PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](PresentationElement.html#getManipulatedPresentationElements()), [getMiddlePoint](PresentationElement.html#getMiddlePoint()), [getObjectParent](PresentationElement.html#getObjectParent()), [getParent](PresentationElement.html#getParent()), [getPreferredDimension](PresentationElement.html#getPreferredDimension()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke(int)), [getSelected](PresentationElement.html#getSelected()), [getStroke](PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](PresentationElement.html#getStroke(int)), [getStroke](PresentationElement.html#getStroke(int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int,int)), [getStroke](PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](PresentationElement.html#isSelected()), [onFind](PresentationElement.html#onFind()), [onFind](PresentationElement.html#onFind(boolean)), [setAllSelected](PresentationElement.html#setAllSelected(boolean)), [setSelected](PresentationElement.html#setSelected(boolean)), [setSelected](PresentationElement.html#setSelected(java.util.List))`
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../utils/NameOwner.html)
`[getName](../../utils/NameOwner.html#getName())`

============ METHOD DETAIL ========== 
Method Details
collectShowingManipulatedElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingManipulatedElementsRecursively()
Collects all visible manipulated elements in this diagram recursively.
Returns:
manipulated elements in this diagram
collectShowingPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingPresentationElementsRecursively()
Collects all visible elements in this diagram recursively.
Returns:
visible elements in this diagram
collectPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectPresentationElementsRecursively()
Collects all elements in this diagram recursively.
Returns:
elements in this diagram
addContentPropertyChangeListener
@OpenApipublic boolean addContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Registers the listener for changes in all symbols contained in the diagram.
Parameters:
`listener` - the `PropertyChangeListener` to be added
Returns:
true if listener was added - it wasn't there yet, otherwise false
removeContentPropertyChangeListener
@OpenApipublic boolean removeContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Unregister the given listener from the diagram.
Parameters:
`listener` - the PropertyChangeListener to be removed
Returns:
true if listener was removed
isSymbolDiagram
@OpenApipublic boolean isSymbolDiagram()
Checks if diagram displays symbols as its contents. Another type of diagrams may be tables, matrices.
Returns:
true if diagram displays symbols
accept
@OpenApipublic void accept([BasePresentationElementVisitor](BasePresentationElementVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
isLoaded
@OpenApipublic boolean isLoaded()
Check if the diagram is loaded.
Returns:
true if diagram contents is loaded
ensureLoaded
@OpenApipublic void ensureLoaded()
Ensures that the diagram is loaded.
 If the diagram is not loaded, load it.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element for a given model element of a given symbol type in this diagram.
 Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 [ModelElement](../../../../dassault_systemes/modeler/foundation/model/ModelElement.html) element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element for a given model element of the given symbol type in this diagram. Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElementForPathConnecting
@CheckForNull
@OpenApipublic final [PresentationElement](PresentationElement.html) findPresentationElementForPathConnecting([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
 Does recursive search.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have a presentation element in this diagram.
findPresentationElementsForPathConnecting
@OpenApipublic final [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)> findPresentationElementsForPathConnecting([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
 Does recursive search.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
a stream of presentation elements
open
@OpenApipublic void open()
Open the diagram
open
@OpenApipublic void open(boolean showProgress)
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
Parameters:
`showProgress` - show progress dialog
openInActiveTab
@OpenApipublic void openInActiveTab(boolean showProgress)
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
Parameters:
`showProgress` - show progress dialog
close
@OpenApipublic final void close()
Closes diagram window.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class AbstractDiagramPresentationElement">Class AbstractDiagramPresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
<div class="inheritance"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code>com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractDiagramPresentationElement</span>
<span class="extends-implements">extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor)">accept</a><wbr/>(<a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContentPropertyChangeListener(java.beans.PropertyChangeListener)">addContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes diagram window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectPresentationElementsRecursively()">collectPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingManipulatedElementsRecursively()">collectShowingManipulatedElementsRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingPresentationElementsRecursively()">collectShowingPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureLoaded()">ensureLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Ensures that the diagram is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">findPresentationElement</a><wbr/>(<a href="../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element for a given model element of the given symbol type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element for a given model element of a given symbol type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">findPresentationElementForPathConnecting</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElementsForPathConnecting</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if the diagram is loaded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSymbolDiagram()">isSymbolDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram displays symbols as its contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open()">open</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(boolean)">open</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openInActiveTab(boolean)">openInActiveTab</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">removeContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given listener from the diagram.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="PresentationElement.html#getElement()">getElement</a>, <a href="PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="PresentationElement.html#getParent()">getParent</a>, <a href="PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="PresentationElement.html#getSelected()">getSelected</a>, <a href="PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="PresentationElement.html#getStroke(int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="PresentationElement.html#isSelected()">isSelected</a>, <a href="PresentationElement.html#onFind()">onFind</a>, <a href="PresentationElement.html#onFind(boolean)">onFind</a>, <a href="PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="PresentationElement.html#setSelected(java.util.List)">setSelected</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../utils/NameOwner.html#getName()">getName</a></code></div>
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
<section class="detail" id="collectShowingManipulatedElementsRecursively()">
<h3>collectShowingManipulatedElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingManipulatedElementsRecursively</span>()</div>
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manipulated elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectShowingPresentationElementsRecursively()">
<h3>collectShowingPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingPresentationElementsRecursively</span>()</div>
<div class="block">Collects all visible elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectPresentationElementsRecursively()">
<h3>collectPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectPresentationElementsRecursively</span>()</div>
<div class="block">Collects all elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added</dd>
<dt>Returns:</dt>
<dd>true if listener was added - it wasn't there yet, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removeContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Unregister the given listener from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed</dd>
<dt>Returns:</dt>
<dd>true if listener was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSymbolDiagram()">
<h3>isSymbolDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSymbolDiagram</span>()</div>
<div class="block">Checks if diagram displays symbols as its contents. Another type of diagrams may be tables, matrices.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram displays symbols</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Check if the diagram is loaded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram contents is loaded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureLoaded()">
<h3>ensureLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureLoaded</span>()</div>
<div class="block">Ensures that the diagram is loaded.
 If the diagram is not loaded, load it.
 Make sure the project is active before invoking this method.
 Otherwise, the diagram may not be loaded.</div>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element for a given model element of a given symbol type in this diagram.
 Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element for a given model element of the given symbol type in this diagram. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">
<h3>findPresentationElementForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElementForPathConnecting</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds a presentation element to connect some PathElement for given model element of the given type in this diagram.
 Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have a presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElementsForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">findPresentationElementsForPathConnecting</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds all symbols to connect some PathElement for a given model element of a given type in this diagram.
 Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>a stream of presentation elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open()">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span>()</div>
<div class="block">Open the diagram</div>
</section>
</li>
<li>
<section class="detail" id="open(boolean)">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openInActiveTab(boolean)">
<h3>openInActiveTab</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openInActiveTab</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">close</span>()</div>
<div class="block">Closes diagram window.</div>
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
