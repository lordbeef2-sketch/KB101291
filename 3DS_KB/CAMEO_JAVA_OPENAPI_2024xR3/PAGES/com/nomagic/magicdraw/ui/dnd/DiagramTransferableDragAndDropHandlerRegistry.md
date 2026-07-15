# JAVA OPENAPI: DiagramTransferableDragAndDropHandlerRegistry (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dnd/DiagramTransferableDragAndDropHandlerRegistry.html
- source_path: `com/nomagic/magicdraw/ui/dnd/DiagramTransferableDragAndDropHandlerRegistry.html`
- source_sha256: `bd73322b48fe285c4697ba67f33a5ede49c1e987e964c20e62ed2520e9dab6e3`
- captured_utc: `2026-07-14T16:55:52.623425+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class DiagramTransferableDragAndDropHandlerRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerRegistry

@OpenApiAllpublic classDiagramTransferableDragAndDropHandlerRegistry
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Registry of [`DiagramTransferableDragAndDropHandlerFactory`](DiagramTransferableDragAndDropHandlerFactory.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramTransferableDragAndDropHandlerRegistry](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html)>`
`[getFactories](#getFactories())()`

`static void`
`[register](#register(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory))([DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html) factory)`
Registers a factory which creates a diagram transferable drag and drop handler
`static void`
`[unregister](#unregister(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory))([DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html) factory)`
Unregister a factory from registered transferable factories
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramTransferableDragAndDropHandlerRegistry
public DiagramTransferableDragAndDropHandlerRegistry()
 ============ METHOD DETAIL ========== 
Method Details
register
public static void register([DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html) factory)
Registers a factory which creates a diagram transferable drag and drop handler
Parameters:
`factory` - to register diagram transferable drag and drop handler
unregister
public static void unregister([DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html) factory)
Unregister a factory from registered transferable factories
Parameters:
`factory` - to unregister
getFactories
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[DiagramTransferableDragAndDropHandlerFactory](DiagramTransferableDragAndDropHandlerFactory.html)> getFactories()
Returns:
diagram transferable drag and drop handler factories

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class DiagramTransferableDragAndDropHandlerRegistry">Class DiagramTransferableDragAndDropHandlerRegistry</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerRegistry</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramTransferableDragAndDropHandlerRegistry</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Registry of <a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd"><code>DiagramTransferableDragAndDropHandlerFactory</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramTransferableDragAndDropHandlerRegistry</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFactories()">getFactories</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#register(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory)">register</a><wbr/>(<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a> factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers a factory which creates a diagram transferable drag and drop handler</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregister(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory)">unregister</a><wbr/>(<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a> factory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregister a factory from registered transferable factories</div>
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
<h3>DiagramTransferableDragAndDropHandlerRegistry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramTransferableDragAndDropHandlerRegistry</span>()</div>
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
<section class="detail" id="register(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory)">
<h3>register</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a> factory)</span></div>
<div class="block">Registers a factory which creates a diagram transferable drag and drop handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - to register diagram transferable drag and drop handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregister(com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandlerFactory)">
<h3>unregister</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregister</span><wbr/><span class="parameters">(<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a> factory)</span></div>
<div class="block">Unregister a factory from registered transferable factories</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - to unregister</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFactories()">
<h3>getFactories</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="DiagramTransferableDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandlerFactory</a>&gt;</span> <span class="element-name">getFactories</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram transferable drag and drop handler factories</dd>
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
