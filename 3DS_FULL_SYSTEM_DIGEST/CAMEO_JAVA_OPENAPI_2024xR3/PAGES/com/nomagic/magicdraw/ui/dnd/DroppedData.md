# JAVA OPENAPI: DroppedData (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dnd/DroppedData.html
- source_path: `com/nomagic/magicdraw/ui/dnd/DroppedData.html`
- source_sha256: `af897d33b673e62dea554777adca023bc2e1af17e1be24f0ce5926c8a85b6a54`
- captured_utc: `2026-07-14T16:55:52.746430+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class DroppedData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.DroppedData

@OpenApiAllpublic classDroppedData
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Wraps essential info from [`TransferHandler.TransferSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html) to make it accessible after drop is complete

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DroppedData](#%3Cinit%3E(java.lang.Object,int,java.awt.Point))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) transferredData,
 int dropAction,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) dropPoint)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getDropAction](#getDropAction())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getDropPoint](#getDropPoint())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getTransferredData](#getTransferredData())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DroppedData
public DroppedData([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) transferredData,
 int dropAction,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) dropPoint)
Parameters:
`transferredData` - data extracted from [`TransferHandler.TransferSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html)
`dropAction` - one of transfer handler actions
`dropPoint` - point on screen where the drag finished and was dropped
 ============ METHOD DETAIL ========== 
Method Details
getTransferredData
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getTransferredData()
Returns:
data extracted from [`TransferHandler.TransferSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html)
getDropPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getDropPoint()
Returns:
point on screen where the drag finished and was dropped
getDropAction
public int getDropAction()
Returns:
one of transfer handler actions
 [`TransferHandler.NONE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#NONE)
[`TransferHandler.LINK`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#LINK)
[`TransferHandler.MOVE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#MOVE)
[`TransferHandler.COPY`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#COPY)
[`TransferHandler.COPY_OR_MOVE`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#COPY_OR_MOVE)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class DroppedData">Class DroppedData</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.DroppedData</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DroppedData</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Wraps essential info from <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing"><code>TransferHandler.TransferSupport</code></a> to make it accessible after drop is complete</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Object,int,java.awt.Point)">DroppedData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> transferredData,
 int dropAction,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> dropPoint)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDropAction()">getDropAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDropPoint()">getDropPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransferredData()">getTransferredData</a>()</code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Object,int,java.awt.Point)">
<h3>DroppedData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DroppedData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> transferredData,
 int dropAction,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> dropPoint)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transferredData</code> - data extracted from <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing"><code>TransferHandler.TransferSupport</code></a></dd>
<dd><code>dropAction</code> - one of transfer handler actions</dd>
<dd><code>dropPoint</code> - point on screen where the drag finished and was dropped</dd>
</dl>
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
<section class="detail" id="getTransferredData()">
<h3>getTransferredData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTransferredData</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>data extracted from <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing"><code>TransferHandler.TransferSupport</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDropPoint()">
<h3>getDropPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getDropPoint</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>point on screen where the drag finished and was dropped</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDropAction()">
<h3>getDropAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDropAction</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>one of transfer handler actions
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#NONE" title="class or interface in javax.swing"><code>TransferHandler.NONE</code></a>
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#LINK" title="class or interface in javax.swing"><code>TransferHandler.LINK</code></a>
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#MOVE" title="class or interface in javax.swing"><code>TransferHandler.MOVE</code></a>
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#COPY" title="class or interface in javax.swing"><code>TransferHandler.COPY</code></a>
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.html#COPY_OR_MOVE" title="class or interface in javax.swing"><code>TransferHandler.COPY_OR_MOVE</code></a></dd>
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
