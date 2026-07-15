# JAVA OPENAPI: SymbolElementMap (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/SymbolElementMap.html
- source_path: `com/nomagic/magicdraw/uml/symbols/SymbolElementMap.html`
- source_sha256: `2b5611156d6d16099710b332b492a298564d8e94a4575998a895fb2e22e5d99c`
- captured_utc: `2026-07-14T16:55:56.348469+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class SymbolElementMap

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.SymbolElementMap

@OpenApipublic classSymbolElementMap
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Maps model elements to presentation elements of **loaded** diagrams.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SymbolElementMap](#%3Cinit%3E(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService))(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService service)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addPresentationElement](#addPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [PresentationElement](PresentationElement.html) presentationElement)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Returns all presentation elements for a specified model element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagramView)`
Returns all presentation elements for specified model element in a given diagram.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,java.util.Collection))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)> diagrams)`
Returns all presentation elements for specified model element in a given diagram.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns all presentation elements for a specified model element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram)`
Returns all presentation elements for specified model element in a given diagram.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getAllPresentationElements](#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)> diagrams)`
Returns all presentation elements for specified model element in a given diagram.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElements](#getElements())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[getModelElements](#getModelElements())()`

`[PresentationElement](PresentationElement.html)`
`[getPresentationElement](#getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Returns presentation element for a specified model element.
`[PresentationElement](PresentationElement.html)`
`[getPresentationElement](#getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](PresentationElement.html)> clazz)`
Gets presentation element for a specified model element and
 presentation element class.
`[PresentationElement](PresentationElement.html)`
`[getPresentationElement](#getPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Returns presentation element for a specified model element.
`void`
`[removePresentationElement](#removePresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [PresentationElement](PresentationElement.html) presentationElement)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SymbolElementMap
public SymbolElementMap(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService service)
 ============ METHOD DETAIL ========== 
Method Details
addPresentationElement
public void addPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [PresentationElement](PresentationElement.html) presentationElement)
removePresentationElement
public void removePresentationElement(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [PresentationElement](PresentationElement.html) presentationElement)
getPresentationElement
@OpenApi
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns presentation element for a specified model element. Presentation element of loaded diagrams only is returned.
Parameters:
`element` - model element
Returns:
first presentation element for specified model element.
getPresentationElement
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Returns presentation element for a specified model element. Presentation element of loaded diagrams only is returned.
Parameters:
`element` - model element
Returns:
first presentation element for specified model element.
getPresentationElement
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](PresentationElement.html)> clazz)
Gets presentation element for a specified model element and
 presentation element class.
Parameters:
`element` - model element for which to get a presentation element.
`clazz` - presentation element class to get.
Returns:
presentation element of a given model element.
getAllPresentationElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Returns all presentation elements for a specified model element. Presentation elements of loaded diagrams only are returned.
Parameters:
`element` - model element.
Returns:
list of `PresentationElement` objects.
getAllPresentationElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)
Returns all presentation elements for a specified model element. Presentation elements of loaded diagrams only are returned.
Parameters:
`element` - model element.
Returns:
list of `PresentationElement` objects.
getAllPresentationElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagram)
Returns all presentation elements for specified model element in a given diagram.
Parameters:
`element` - model element
`diagram` - diagram in which returned symbols should be used
Returns:
list of `PresentationElement` objects
getAllPresentationElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) diagramView)
Returns all presentation elements for specified model element in a given diagram.
Parameters:
`element` - model element
`diagramView` - diagram in which returned symbols should be used
Returns:
list of `PresentationElement` objects
getAllPresentationElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)> diagrams)
Returns all presentation elements for specified model element in a given diagram.
Parameters:
`element` - model element
`diagrams` - diagram in which returned symbols should be used
Returns:
list of `PresentationElement` objects
getAllPresentationElements
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getAllPresentationElements(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)> diagrams)
Returns all presentation elements for specified model element in a given diagram.
Parameters:
`element` - model element
`diagrams` - diagram in which returned symbols should be used
Returns:
list of `PresentationElement` objects
getElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElements()
Returns:
model elements that have symbols
getModelElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.foundation.model.ModelElement> getModelElements()
Returns:
model elements that have symbols

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class SymbolElementMap">Class SymbolElementMap</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.SymbolElementMap</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SymbolElementMap</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Maps model elements to presentation elements of <strong>loaded</strong> diagrams.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService)">SymbolElementMap</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService service)</code></div>
<div class="col-last even-row-color"> </div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement)">getAllPresentationElements</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for a specified model element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getAllPresentationElements</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,java.util.Collection)">getAllPresentationElements</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAllPresentationElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for a specified model element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getAllPresentationElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getAllPresentationElements</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElements()">getElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElements()">getModelElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getPresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns presentation element for a specified model element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">getPresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; clazz)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets presentation element for a specified model element and
 presentation element class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns presentation element for a specified model element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService)">
<h3>SymbolElementMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SymbolElementMap</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.SymbolElementMapService service)</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="addPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="removePresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>removePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns presentation element for a specified model element. Presentation element of loaded diagrams only is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dt>Returns:</dt>
<dd>first presentation element for specified model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>getPresentationElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Returns presentation element for a specified model element. Presentation element of loaded diagrams only is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dt>Returns:</dt>
<dd>first presentation element for specified model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">
<h3>getPresentationElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; clazz)</span></div>
<div class="block">Gets presentation element for a specified model element and
 presentation element class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element for which to get a presentation element.</dd>
<dd><code>clazz</code> - presentation element class to get.</dd>
<dt>Returns:</dt>
<dd>presentation element of a given model element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Returns all presentation elements for a specified model element. Presentation elements of loaded diagrams only are returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element.</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Returns all presentation elements for a specified model element. Presentation elements of loaded diagrams only are returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element.</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dd><code>diagram</code> - diagram in which returned symbols should be used</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</span></div>
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dd><code>diagramView</code> - diagram in which returned symbols should be used</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams)</span></div>
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dd><code>diagrams</code> - diagram in which returned symbols should be used</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllPresentationElements(com.dassault_systemes.modeler.foundation.model.ModelElement,java.util.Collection)">
<h3>getAllPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAllPresentationElements</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams)</span></div>
<div class="block">Returns all presentation elements for specified model element in a given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dd><code>diagrams</code> - diagram in which returned symbols should be used</dd>
<dt>Returns:</dt>
<dd>list of <code>PresentationElement</code> objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElements()">
<h3>getElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model elements that have symbols</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElements()">
<h3>getModelElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">getModelElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model elements that have symbols</dd>
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
