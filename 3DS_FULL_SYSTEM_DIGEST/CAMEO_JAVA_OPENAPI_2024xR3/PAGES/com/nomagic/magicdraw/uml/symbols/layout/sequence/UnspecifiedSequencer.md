# JAVA OPENAPI: UnspecifiedSequencer (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/sequence/UnspecifiedSequencer.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/sequence/UnspecifiedSequencer.html`
- source_sha256: `31a0206c784f036f4361e427074f1d2564f112f32888aba0c198bdc3dba45249`
- captured_utc: `2026-07-14T16:55:58.945498+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout.sequence](package-summary.html)

## Class UnspecifiedSequencer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.layout.sequence.UnspecifiedSequencer

All Implemented Interfaces:
`[Sequencer](Sequencer.html)`, `[Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[ShapeElement](../../shapes/ShapeElement.html)>`

@OpenApiAllpublic classUnspecifiedSequencer
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Sequencer](Sequencer.html)

An empty sequencer. It does not say anything for the layouter, so the layouter will determine the
 ordering by path crossing etc.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NAME](#NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UnspecifiedSequencer](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[compare](#compare(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../../shapes/ShapeElement.html) o1,
 [ShapeElement](../../shapes/ShapeElement.html) o2)`
Compares objects.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
The name of the sequencer
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)), [reversed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#reversed()), [thenComparing](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)), [thenComparing](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)), [thenComparing](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)), [thenComparingDouble](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)), [thenComparingInt](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)), [thenComparingLong](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction))`

============ FIELD DETAIL =========== 
Field Details
NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NAME
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UnspecifiedSequencer
public UnspecifiedSequencer()
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Description copied from interface: `[Sequencer](Sequencer.html#getName())`
The name of the sequencer
Specified by:
`[getName](Sequencer.html#getName())` in interface `[Sequencer](Sequencer.html)`
Returns:
sequencer name
compare
public int compare([ShapeElement](../../shapes/ShapeElement.html) o1,
 [ShapeElement](../../shapes/ShapeElement.html) o2)
Compares objects.
Specified by:
`[compare](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#compare(T,T))` in interface `[Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[ShapeElement](../../shapes/ShapeElement.html)>`
Specified by:
`[compare](Sequencer.html#compare(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))` in interface `[Sequencer](Sequencer.html)`
Parameters:
`o1` - first object
`o2` - second object
Returns:
compare value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout.sequence</a></div>
<h1 class="title" title="Class UnspecifiedSequencer">Class UnspecifiedSequencer</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.sequence.UnspecifiedSequencer</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="Sequencer.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout.sequence">Sequencer</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">UnspecifiedSequencer</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="Sequencer.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout.sequence">Sequencer</a></span></div>
<div class="block">An empty sequencer. It does not say anything for the layouter, so the layouter will determine the
 ordering by path crossing etc.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NAME">NAME</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UnspecifiedSequencer</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compare(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">compare</a><wbr/>(<a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o1,
 <a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The name of the sequencer</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Comparator">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)" title="class or interface in java.util">thenComparingDouble</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)" title="class or interface in java.util">thenComparingInt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction)" title="class or interface in java.util">thenComparingLong</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="NAME">
<h3>NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NAME</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>UnspecifiedSequencer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UnspecifiedSequencer</span>()</div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Sequencer.html#getName()">Sequencer</a></code></span></div>
<div class="block">The name of the sequencer</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Sequencer.html#getName()">getName</a></code> in interface <code><a href="Sequencer.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout.sequence">Sequencer</a></code></dd>
<dt>Returns:</dt>
<dd>sequencer name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compare(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>compare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compare</span><wbr/><span class="parameters">(<a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o1,
 <a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o2)</span></div>
<div class="block">Compares objects.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html#compare(T,T)" title="class or interface in java.util">compare</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="../../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a href="Sequencer.html#compare(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">compare</a></code> in interface <code><a href="Sequencer.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout.sequence">Sequencer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o1</code> - first object</dd>
<dd><code>o2</code> - second object</dd>
<dt>Returns:</dt>
<dd>compare value</dd>
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
