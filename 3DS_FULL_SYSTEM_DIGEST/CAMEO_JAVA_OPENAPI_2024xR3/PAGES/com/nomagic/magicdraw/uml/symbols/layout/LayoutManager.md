# JAVA OPENAPI: LayoutManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/LayoutManager.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/LayoutManager.html`
- source_sha256: `23b37e09d133c21b4c30152205d50edccc3d02166728c9d238db9a9052417e65`
- captured_utc: `2026-07-14T16:55:57.855484+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class LayoutManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.layout.LayoutManager

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApiAllpublic final classLayoutManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Deprecated.
Manager that binds layouters to diagrams.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[DiagramLayouter](DiagramLayouter.html)`
`[getDefaultLayouter](#getDefaultLayouter(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram)`
Deprecated.
Get default diagram layouter.
`[DiagramLayouter](DiagramLayouter.html)`
`[getDefaultLayouter](#getDefaultLayouter(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Deprecated.
Get default diagram layouter.
`static [LayoutManager](LayoutManager.html)`
`[getInstance](#getInstance())()`
Deprecated.
`static boolean`
`[isSupported](#isSupported())()`
Deprecated.
Check the layouter is supported.
`void`
`[registerDefaultLayouter](#registerDefaultLayouter(java.lang.String,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramLayouter](DiagramLayouter.html) layouter)`
Deprecated.
Register the given DiagramLayouter to be default layouter.
`void`
`[registerDefaultLayouter](#registerDefaultLayouter(java.util.function.Predicate,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html)> filter,
 [DiagramLayouter](DiagramLayouter.html) layouter)`
Deprecated.
Register the given DiagramLayouter to be default layouter.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [LayoutManager](LayoutManager.html) getInstance()
Deprecated.
getDefaultLayouter
public [DiagramLayouter](DiagramLayouter.html) getDefaultLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Deprecated.
Get default diagram layouter.
Parameters:
`diagramType` - The specify diagram type.
Returns:
DiagramLayouter.
getDefaultLayouter
public [DiagramLayouter](DiagramLayouter.html) getDefaultLayouter([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram)
Deprecated.
Get default diagram layouter.
Parameters:
`diagram` - diagram the layouter will be used in.
Returns:
DiagramLayouter.
registerDefaultLayouter
public void registerDefaultLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [DiagramLayouter](DiagramLayouter.html) layouter)
Deprecated.
Register the given DiagramLayouter to be default layouter.
Parameters:
`diagramType` - diagram type
`layouter` - layouter
registerDefaultLayouter
public void registerDefaultLayouter([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html)> filter,
 [DiagramLayouter](DiagramLayouter.html) layouter)
Deprecated.
Register the given DiagramLayouter to be default layouter.
Parameters:
`filter` - diagram filter
`layouter` - layouter
isSupported
public static boolean isSupported()
Deprecated.
Check the layouter is supported.
Returns:
true if supported

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class LayoutManager">Class LayoutManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.LayoutManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">LayoutManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Manager that binds layouters to diagrams.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDefaultLayouter(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getDefaultLayouter</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get default diagram layouter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDefaultLayouter(java.lang.String)">getDefaultLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get default diagram layouter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="LayoutManager.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">LayoutManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSupported()">isSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check the layouter is supported.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#registerDefaultLayouter(java.lang.String,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">registerDefaultLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Register the given DiagramLayouter to be default layouter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#registerDefaultLayouter(java.util.function.Predicate,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">registerDefaultLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; filter,
 <a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Register the given DiagramLayouter to be default layouter.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="LayoutManager.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">LayoutManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getDefaultLayouter(java.lang.String)">
<h3>getDefaultLayouter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></span> <span class="element-name">getDefaultLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get default diagram layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - The specify diagram type.</dd>
<dt>Returns:</dt>
<dd>DiagramLayouter.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultLayouter(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getDefaultLayouter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></span> <span class="element-name">getDefaultLayouter</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get default diagram layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram the layouter will be used in.</dd>
<dt>Returns:</dt>
<dd>DiagramLayouter.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerDefaultLayouter(java.lang.String,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">
<h3>registerDefaultLayouter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerDefaultLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Register the given DiagramLayouter to be default layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>layouter</code> - layouter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerDefaultLayouter(java.util.function.Predicate,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">
<h3>registerDefaultLayouter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerDefaultLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; filter,
 <a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Register the given DiagramLayouter to be default layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - diagram filter</dd>
<dd><code>layouter</code> - layouter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupported()">
<h3>isSupported</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSupported</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check the layouter is supported.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if supported</dd>
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
