# JAVA OPENAPI: CopyPasting (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/copypaste/CopyPasting.html
- source_path: `com/nomagic/magicdraw/copypaste/CopyPasting.html`
- source_sha256: `39b898079b37b3ca658c1c1783eb7d2410df2237d2d87c17f00d557e1a786113`
- captured_utc: `2026-07-14T16:51:13.353100+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.copypaste](package-summary.html)

## Class CopyPasting

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.copypaste.CopyPasting

@OpenApiAllpublic classCopyPasting
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Provides API for copy-pasting elements in the model and symbol styles in diagrams.
 You can copy model elements and symbols either to another location in the same project or to another project.
 This must be done in the same session.
 There are two modes of making copies of model elements:
 Deep copying (with new data)
Shallow copying (with reused data)
Example 1: Copying an element
Element element = ...; // Element to copy/paste.
 Element parent = ...; // Parent to which the element has to be pasted: either the same project or another project.

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone");

 // 3rd parameter indicates whether element name uniqueness should be preserved in the parent.
 CopyPasting.copyPasteElement(element, parent, true);

 sessionManager.closeSession();
Example 2: Copying multiple elements and symbols
List elements = ...; // Elements to copy/paste.
 List views = ...; // Symbols to copy/paste.
 Element parent = ...; // Parent to which elements should be pasted: either the same project or another project.

 BaseElement symbolParent = ...; // Parent to which symbols should be pasted.

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone");

 // 4th parameter indicates whether deep or shallow copy is applied.
 // 5th parameter indicates whether element name uniqueness should be preserved in the parent.
 List baseElements = CopyPasting.copyPasteElements(views, parent, symbolParent, true, true);

 sessionManager.closeSession();
Example 3: Copying style from one symbol to another
PresentationElement source = ...; // Symbol with symbol properties (style) to copy
 PresentationElement target = ...; // Symbol to paste style on

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone Symbol Style");

 CopyPasting.copyPasteSymbolsStyle(source, target)

 sessionManager.closeSession();
Example 4: Copying style from symbol to multiple symbols
PresentationElement source = ...; // Symbol with symbol properties (style) to copy
 Collectiontargets = ...; // Symbols to paste style on

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone Symbol Style");

 CopyPasting.copyPasteSymbolsStyle(source, targets)

 sessionManager.closeSession();

See Also:
[`BaseElement`](../uml/BaseElement.html)
[`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
[`PresentationElement`](../uml/symbols/PresentationElement.html)
[`SessionManager`](../openapi/uml/SessionManager.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CopyPasting](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[copyPasteElement](#copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)`
Makes a copy of the specified element and places it under the parent (namespace).
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[copyPasteElement](#copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 boolean increaseElementNames)`
Makes a copy of the specified element and places it under the parent (namespace).
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)>`
`[copyPasteElements](#copyPasteElements(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement,boolean,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> objectsToCopy,
 [BaseElement](../uml/BaseElement.html) dataParent,
 [BaseElement](../uml/BaseElement.html) viewParent,
 boolean withNewData,
 boolean increaseElementNames)`
Clones given objects (model elements or symbols) and establishes correct relationships.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[copyPasteElements](#copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)`
Makes a copy of specified elements and places them under the given parent (namespace).
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[copyPasteElements](#copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 boolean increaseElementNames)`
Makes a copy of specified elements and places them under the given parent (namespace).
`static void`
`[copyPasteSymbolsStyle](#copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../uml/symbols/PresentationElement.html) sourceSymbol,
 [PresentationElement](../uml/symbols/PresentationElement.html) targetSymbol)`
Copies symbol style from provided source symbol and pastes on target symbol.
`static void`
`[copyPasteSymbolsStyle](#copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Collection))([PresentationElement](../uml/symbols/PresentationElement.html) sourceSymbol,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> targetSymbols)`
Copies symbol style from provided source symbol and pastes it on each target symbol.
`static void`
`[copyPasteSymbolsStyle](#copyPasteSymbolsStyle(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> sourceSymbols,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> targetSymbols)`
Copies symbol style from one of the source symbols to target symbols.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CopyPasting
public CopyPasting()
 ============ METHOD DETAIL ========== 
Method Details
copyPasteElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) copyPasteElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)
Makes a copy of the specified element and places it under the parent (namespace).
 Does not increase element names in the given namespace.
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`elementToCopy` - element to copy.
`parent` - owner to which to add copied element.
Returns:
cloned element.
copyPasteElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) copyPasteElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 boolean increaseElementNames)
Makes a copy of the specified element and places it under the parent (namespace).
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`elementToCopy` - element to copy.
`parent` - owner to which to add copied element.
`increaseElementNames` - indicates if element names should be increased in given namespace to avoid duplication.
Returns:
cloned element.
copyPasteElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) copyPasteElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)
Makes a copy of specified elements and places them under the given parent (namespace).
 Does not increase element names in the given namespace.
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`elementsToCopy` - collection of Element} objects to be copied.
`parent` - parent where objects should be placed.
Returns:
list of copies.
copyPasteElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) copyPasteElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToCopy,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent,
 boolean increaseElementNames)
Makes a copy of specified elements and places them under the given parent (namespace).
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`elementsToCopy` - collection of Element} objects to be copied.
`parent` - parent where objects should be placed.
`increaseElementNames` - indicates if element names should be increased in given namespace to avoid duplication.
Returns:
list of copies.
copyPasteElements
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)> copyPasteElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> objectsToCopy,
 @CheckForNull
 [BaseElement](../uml/BaseElement.html) dataParent,
 [BaseElement](../uml/BaseElement.html) viewParent,
 boolean withNewData,
 boolean increaseElementNames)
Clones given objects (model elements or symbols) and establishes correct relationships.
 Returns correct copies. These copies can contain views and model elements (mixed).
Parameters:
`objectsToCopy` - objects to copy.
`dataParent` - data parent.
`viewParent` - parent of symbols.
`withNewData` - indicates whether pasting should be done with new data (deep or shallow copy).
`increaseElementNames` - indicates whether elements names should be increased.
Returns:
cloned elements.
copyPasteSymbolsStyle
public static void copyPasteSymbolsStyle([PresentationElement](../uml/symbols/PresentationElement.html) sourceSymbol,
 [PresentationElement](../uml/symbols/PresentationElement.html) targetSymbol)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Copies symbol style from provided source symbol and pastes on target symbol.
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`sourceSymbol` - symbol to copy style from
`targetSymbol` - symbol to paste style on
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - when target symbol is read only or symbol's owner is read only.
copyPasteSymbolsStyle
public static void copyPasteSymbolsStyle([PresentationElement](../uml/symbols/PresentationElement.html) sourceSymbol,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> targetSymbols)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Copies symbol style from provided source symbol and pastes it on each target symbol.
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`sourceSymbol` - symbol to copy style from
`targetSymbols` - symbols to paste style on
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - when any of the target symbols is read only or symbol's owner is read only.
copyPasteSymbolsStyle
public static void copyPasteSymbolsStyle([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> sourceSymbols,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../uml/symbols/PresentationElement.html)> targetSymbols)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Copies symbol style from one of the source symbols to target symbols.
 For each target symbol first found appropriate source symbol is selected. Symbols of the same element type are preferred.
 
 Assumes that session is started by [`SessionManager`](../openapi/uml/SessionManager.html).
Parameters:
`sourceSymbols` - symbols to copy style from
`targetSymbols` - symbols to paste style on
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - when any of the target symbols is read only or symbol's owner is read only.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.copypaste</a></div>
<h1 class="title" title="Class CopyPasting">Class CopyPasting</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.copypaste.CopyPasting</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CopyPasting</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Provides API for copy-pasting elements in the model and symbol styles in diagrams.
 </p>
 You can copy model elements and symbols either to another location in the same project or to another project.
 This must be done in the same session.
 There are two modes of making copies of model elements:
 <ul>
<li> Deep copying (with new data) </li>
<li> Shallow copying (with reused data) </li>
</ul>
<p>
<h4> Example 1: Copying an element </h4>
<pre>
 Element element = ...; // Element to copy/paste.
 Element parent = ...;  // Parent to which the element has to be pasted: either the same project or another project.

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone");

 // 3rd parameter indicates whether element name uniqueness should be preserved in the parent.
 CopyPasting.copyPasteElement(element, parent, true);

 sessionManager.closeSession();
 </pre>
<p>
<h4> Example 2: Copying multiple elements and symbols </h4>
<pre>
 List elements = ...; // Elements to copy/paste.
 List views = ...; // Symbols to copy/paste.
 Element parent = ...;  // Parent to which elements should be pasted: either the same project or another project.

 BaseElement symbolParent = ...; // Parent to which symbols should be pasted.

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone");

 // 4th parameter indicates whether deep or shallow copy is applied.
 // 5th parameter indicates whether element name uniqueness should be preserved in the parent.
 List baseElements = CopyPasting.copyPasteElements(views, parent, symbolParent, true, true);

 sessionManager.closeSession();
 </pre>
<p>
<h4> Example 3: Copying style from one symbol to another </h4>
<pre>
 PresentationElement source = ...; // Symbol with symbol properties (style) to copy
 PresentationElement target = ...; // Symbol to paste style on

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone Symbol Style");

 CopyPasting.copyPasteSymbolsStyle(source, target)

 sessionManager.closeSession();
 </pre>
<p>
<h4> Example 4: Copying style from symbol to multiple symbols </h4>
<pre>
 PresentationElement source = ...; // Symbol with symbol properties (style) to copy
 Collection<presentationelement> targets = ...; // Symbols to paste style on

 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Clone Symbol Style");

 CopyPasting.copyPasteSymbolsStyle(source, targets)

 sessionManager.closeSession();
 </presentationelement></pre></p></p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml"><code>BaseElement</code></a></li>
<li><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></li>
<li><a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a></li>
<li><a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CopyPasting</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">copyPasteElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a copy of the specified element and places it under the parent (namespace).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">copyPasteElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 boolean increaseElementNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a copy of the specified element and places it under the parent (namespace).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteElements(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">copyPasteElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; objectsToCopy,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> dataParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> viewParent,
 boolean withNewData,
 boolean increaseElementNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clones given objects (model elements or symbols) and establishes correct relationships.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">copyPasteElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a copy of specified elements and places them under the given parent (namespace).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">copyPasteElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 boolean increaseElementNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a copy of specified elements and places them under the given parent (namespace).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">copyPasteSymbolsStyle</a><wbr/>(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourceSymbol,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> targetSymbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies symbol style from provided source symbol and pastes on target symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Collection)">copyPasteSymbolsStyle</a><wbr/>(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourceSymbol,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targetSymbols)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies symbol style from provided source symbol and pastes it on each target symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyPasteSymbolsStyle(java.util.Collection,java.util.Collection)">copyPasteSymbolsStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; sourceSymbols,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targetSymbols)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies symbol style from one of the source symbols to target symbols.</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>CopyPasting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CopyPasting</span>()</div>
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
<section class="detail" id="copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>copyPasteElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">copyPasteElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</span></div>
<div class="block">Makes a copy of the specified element and places it under the parent (namespace).
 Does not increase element names in the given namespace.
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementToCopy</code> - element to copy.</dd>
<dd><code>parent</code> - owner to which to add copied element.</dd>
<dt>Returns:</dt>
<dd>cloned element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>copyPasteElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">copyPasteElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 boolean increaseElementNames)</span></div>
<div class="block">Makes a copy of the specified element and places it under the parent (namespace).
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementToCopy</code> - element to copy.</dd>
<dd><code>parent</code> - owner to which to add copied element.</dd>
<dd><code>increaseElementNames</code> - indicates if element names should be increased in given namespace to avoid duplication.</dd>
<dt>Returns:</dt>
<dd>cloned element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>copyPasteElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">copyPasteElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</span></div>
<div class="block">Makes a copy of specified elements and places them under the given parent (namespace).
 Does not increase element names in the given namespace.
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementsToCopy</code> - collection of  Element} objects to be copied.</dd>
<dd><code>parent</code> - parent where objects should be placed.</dd>
<dt>Returns:</dt>
<dd>list of copies.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteElements(java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>copyPasteElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">copyPasteElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToCopy,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent,
 boolean increaseElementNames)</span></div>
<div class="block">Makes a copy of specified elements and places them under the given parent (namespace).
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementsToCopy</code> - collection of  Element} objects to be copied.</dd>
<dd><code>parent</code> - parent where objects should be placed.</dd>
<dd><code>increaseElementNames</code> - indicates if element names should be increased in given namespace to avoid duplication.</dd>
<dt>Returns:</dt>
<dd>list of copies.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteElements(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement,boolean,boolean)">
<h3>copyPasteElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">copyPasteElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; objectsToCopy,
 @CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> dataParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> viewParent,
 boolean withNewData,
 boolean increaseElementNames)</span></div>
<div class="block">Clones given objects (model elements or symbols) and establishes correct relationships.
 Returns correct copies. These copies can contain views and model elements (mixed).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objectsToCopy</code> - objects to copy.</dd>
<dd><code>dataParent</code> - data parent.</dd>
<dd><code>viewParent</code> - parent of symbols.</dd>
<dd><code>withNewData</code> - indicates whether pasting should be done with new data (deep or shallow copy).</dd>
<dd><code>increaseElementNames</code> - indicates whether elements names should be increased.</dd>
<dt>Returns:</dt>
<dd>cloned elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>copyPasteSymbolsStyle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copyPasteSymbolsStyle</span><wbr/><span class="parameters">(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourceSymbol,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> targetSymbol)</span>
                                  throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Copies symbol style from provided source symbol and pastes on target symbol.
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceSymbol</code> - symbol to copy style from</dd>
<dd><code>targetSymbol</code> - symbol to paste style on</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - when target symbol is read only or symbol's owner is read only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteSymbolsStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Collection)">
<h3>copyPasteSymbolsStyle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copyPasteSymbolsStyle</span><wbr/><span class="parameters">(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sourceSymbol,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targetSymbols)</span>
                                  throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Copies symbol style from provided source symbol and pastes it on each target symbol.
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceSymbol</code> - symbol to copy style from</dd>
<dd><code>targetSymbols</code> - symbols to paste style on</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - when any of the target symbols is read only or symbol's owner is read only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyPasteSymbolsStyle(java.util.Collection,java.util.Collection)">
<h3>copyPasteSymbolsStyle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copyPasteSymbolsStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; sourceSymbols,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targetSymbols)</span>
                                  throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Copies symbol style from one of the source symbols to target symbols.
 For each target symbol first found appropriate source symbol is selected. Symbols of the same element type are preferred.
 <p></p>
 Assumes that session is started by <a href="../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceSymbols</code> - symbols to copy style from</dd>
<dd><code>targetSymbols</code> - symbols to paste style on</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - when any of the target symbols is read only or symbol's owner is read only.</dd>
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
