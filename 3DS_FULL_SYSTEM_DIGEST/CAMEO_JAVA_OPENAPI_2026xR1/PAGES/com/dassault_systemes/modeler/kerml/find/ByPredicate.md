# JAVA OPENAPI: ByPredicate (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/find/ByPredicate.html
- source_path: `com/dassault_systemes/modeler/kerml/find/ByPredicate.html`
- source_sha256: `6f6f5dc2eccd6fc4990cb9838b77879b606af312b12be72388f1a650972fd702`
- captured_utc: `2026-07-14T16:44:44.620798+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.find](package-summary.html)

## Class ByPredicate

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.find.AbstractFinder
com.dassault_systemes.modeler.kerml.find.ByPredicate

@OpenApiAllpublic classByPredicate
extends com.dassault_systemes.modeler.kerml.find.AbstractFinder
Finder implementation that locates [`elements`](../model/kerml/Element.html) using a
 custom predicate among directly owned elements.

 This finder performs a non-recursive search and evaluates the provided
 predicate against elements owned by the given `context`.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ByPredicate](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`<T extends [Element](../model/kerml/Element.html)> 
T`
`[find](#find(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class))([Element](../model/kerml/Element.html) context,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> test,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> metaclass)`
Finds a single element matching the given predicate and type.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[streamOf](#streamOf(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class))([Element](../model/kerml/Element.html) context,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> test,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> metaclass)`
Returns a stream of elements matching the given predicate and type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ByPredicate
public ByPredicate()
 ============ METHOD DETAIL ========== 
Method Details
find
public <T extends [Element](../model/kerml/Element.html)> T find([Element](../model/kerml/Element.html) context,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> test,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> metaclass)
Finds a single element matching the given predicate and type.
Overrides:
`find` in class `com.dassault_systemes.modeler.kerml.find.AbstractFinder`
Type Parameters:
`T` - element type
Parameters:
`context` - the element whose direct owned elements are searched
`test` - predicate used to filter elements
`metaclass` - expected type of the result
Returns:
the first matching element, or `null` if none found
streamOf
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> streamOf([Element](../model/kerml/Element.html) context,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<T> test,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> metaclass)
Returns a stream of elements matching the given predicate and type.
Overrides:
`streamOf` in class `com.dassault_systemes.modeler.kerml.find.AbstractFinder`
Type Parameters:
`T` - element type
Parameters:
`context` - the element whose direct owned elements are searched
`test` - predicate used to filter elements
`metaclass` - expected element type
Returns:
stream of matching elements (may be empty)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.find</a></div>
<h1 class="title" title="Class ByPredicate">Class ByPredicate</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.find.AbstractFinder
<div class="inheritance">com.dassault_systemes.modeler.kerml.find.ByPredicate</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ByPredicate</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.kerml.find.AbstractFinder</span></div>
<div class="block">Finder implementation that locates <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>elements</code></a> using a
 custom predicate among directly owned elements.

 <p>
 This finder performs a non-recursive search and evaluates the provided
 predicate against elements owned by the given <code>context</code>.
 </p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ByPredicate</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class)">find</a><wbr/>(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; test,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds a single element matching the given predicate and type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOf(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class)">streamOf</a><wbr/>(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; test,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; metaclass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a stream of elements matching the given predicate and type.</div>
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
<h3>ByPredicate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ByPredicate</span>()</div>
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
<section class="detail" id="find(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; test,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; metaclass)</span></div>
<div class="block">Finds a single element matching the given predicate and type.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>find</code> in class <code>com.dassault_systemes.modeler.kerml.find.AbstractFinder</code></dd>
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>context</code> - the element whose direct owned elements are searched</dd>
<dd><code>test</code> - predicate used to filter elements</dd>
<dd><code>metaclass</code> - expected type of the result</dd>
<dt>Returns:</dt>
<dd>the first matching element, or <code>null</code> if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOf(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate,java.lang.Class)">
<h3>streamOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">streamOf</span><wbr/><span class="parameters">(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;T&gt; test,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; metaclass)</span></div>
<div class="block">Returns a stream of elements matching the given predicate and type.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>streamOf</code> in class <code>com.dassault_systemes.modeler.kerml.find.AbstractFinder</code></dd>
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>context</code> - the element whose direct owned elements are searched</dd>
<dd><code>test</code> - predicate used to filter elements</dd>
<dd><code>metaclass</code> - expected element type</dd>
<dt>Returns:</dt>
<dd>stream of matching elements (may be empty)</dd>
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
