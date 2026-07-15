# JAVA OPENAPI: CustomDropDiagramHandlerFactory (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/dnd/CustomDropDiagramHandlerFactory.html
- source_path: `com/nomagic/magicdraw/ui/dnd/CustomDropDiagramHandlerFactory.html`
- source_sha256: `81c742622ac0ae7a32cad45fd1b0f29ffc55a852562e117ce2955b1d77092243`
- captured_utc: `2026-07-14T16:46:02.813838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class CustomDropDiagramHandlerFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.CustomDropDiagramHandlerFactory

@OpenApiAllpublic classCustomDropDiagramHandlerFactory
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Custom Drag and Drop handler factory, used to created and register Custom Drag and Drop handlers for diagram drop.
 To register a Custom Drag and Drop handler you must create a factory [`CustomDragAndDropHandlerFactory`](CustomDragAndDropHandlerFactory.html) which creates
 [`CustomDragAndDropHandler`](CustomDragAndDropHandler.html) which you need to implement.

See Also:
[`CustomDragAndDropHandler`](CustomDragAndDropHandler.html)
[`CustomDragAndDropHandlerFactory`](CustomDragAndDropHandlerFactory.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CustomDropDiagramHandlerFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[register](#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandler))([CustomDragAndDropHandler](CustomDragAndDropHandler.html) handler)`
Deprecated.
use a factory to register handler [`register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)`](#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory))
`static void`
`[register](#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory))([CustomDragAndDropHandlerFactory](CustomDragAndDropHandlerFactory.html) factory)`
Registers a factory which creates [`CustomDragAndDropHandler`](CustomDragAndDropHandler.html)
`static void`
`[unregister](#unregister(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory))([CustomDragAndDropHandlerFactory](CustomDragAndDropHandlerFactory.html) factory)`
Unregister a registered drop handler factory
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CustomDropDiagramHandlerFactory
public CustomDropDiagramHandlerFactory()
 ============ METHOD DETAIL ========== 
Method Details
register
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static void register([CustomDragAndDropHandler](CustomDragAndDropHandler.html) handler)
Deprecated.
use a factory to register handler [`register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)`](#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory))
register
public static void register([CustomDragAndDropHandlerFactory](CustomDragAndDropHandlerFactory.html) factory)
Registers a factory which creates [`CustomDragAndDropHandler`](CustomDragAndDropHandler.html)
Parameters:
`factory` - to register [`CustomDragAndDropHandler`](CustomDragAndDropHandler.html)
unregister
public static void unregister([CustomDragAndDropHandlerFactory](CustomDragAndDropHandlerFactory.html) factory)
Unregister a registered drop handler factory
Parameters:
`factory` - to unregister

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class CustomDropDiagramHandlerFactory">Class CustomDropDiagramHandlerFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.CustomDropDiagramHandlerFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CustomDropDiagramHandlerFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Custom Drag and Drop handler factory, used to created and register Custom Drag and Drop handlers for diagram drop.
 To register a Custom Drag and Drop handler you must create a factory <a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandlerFactory</code></a> which creates
 <a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandler</code></a> which you need to implement.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandler</code></a></li>
<li><a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandlerFactory</code></a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CustomDropDiagramHandlerFactory</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandler)">register</a><wbr/>(<a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use a factory to register handler <a href="#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)"><code>register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)">register</a><wbr/>(<a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandlerFactory</a> factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers a factory which creates <a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandler</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregister(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)">unregister</a><wbr/>(<a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandlerFactory</a> factory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregister a registered drop handler factory</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>CustomDropDiagramHandlerFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CustomDropDiagramHandlerFactory</span>()</div>
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
<section class="detail" id="register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandler)">
<h3>register</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandler</a> handler)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use a factory to register handler <a href="#register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)"><code>register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="register(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)">
<h3>register</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandlerFactory</a> factory)</span></div>
<div class="block">Registers a factory which creates <a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandler</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - to register <a href="CustomDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDragAndDropHandler</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregister(com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandlerFactory)">
<h3>unregister</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregister</span><wbr/><span class="parameters">(<a href="CustomDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd">CustomDragAndDropHandlerFactory</a> factory)</span></div>
<div class="block">Unregister a registered drop handler factory</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - to unregister</dd>
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
