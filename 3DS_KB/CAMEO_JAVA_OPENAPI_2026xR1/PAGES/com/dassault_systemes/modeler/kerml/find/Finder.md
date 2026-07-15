# JAVA OPENAPI: Finder (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/find/Finder.html
- source_path: `com/dassault_systemes/modeler/kerml/find/Finder.html`
- source_sha256: `185deed10d6264ab78343af894bb954ad3a000e46c2f584b1ae30d728d6a8375`
- captured_utc: `2026-07-14T16:44:44.612799+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.find](package-summary.html)

## Class Finder

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.find.Finder

@OpenApiAllpublic final classFinder
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class for providing access to various finders.

 This utility class provides a set of preconfigured, stateless finder
 implementations used to locate `Element` instances within a model.
 Each finder encapsulates a specific lookup strategy (e.g., by name,
 declared name, qualified name, predicate, or by EClass recursively).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ByDeclaredName](ByDeclaredName.html)`
`[byDeclaredName](#byDeclaredName())()`
Returns a finder that locates elements by their declared name among
 the direct owned elements of a given context.
`static [ByEClassRecursively](ByEClassRecursively.html)`
`[byEClassRecursively](#byEClassRecursively())()`
Returns a finder that locates elements by their `EClass`
 recursively in a project or collection of roots.
`static [ByName](ByName.html)`
`[byName](#byName())()`
Returns a finder that locates elements by their name among
 the direct owned elements of a given context.
`static [ByPredicate](ByPredicate.html)`
`[byPredicate](#byPredicate())()`
Returns a generic finder that locates elements using an arbitrary
 predicate evaluated over the direct owned elements of a given context.
`static [ByQualifiedName](ByQualifiedName.html)`
`[byQualifiedName](#byQualifiedName())()`
Returns a finder that locates elements by their qualified name.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
byName
public static [ByName](ByName.html) byName()
Returns a finder that locates elements by their name among
 the direct owned elements of a given context.
Returns:
shared [`ByName`](ByName.html) finder instance
byDeclaredName
public static [ByDeclaredName](ByDeclaredName.html) byDeclaredName()
Returns a finder that locates elements by their declared name among
 the direct owned elements of a given context.
Returns:
shared [`ByDeclaredName`](ByDeclaredName.html) finder instance
byPredicate
public static [ByPredicate](ByPredicate.html) byPredicate()
Returns a generic finder that locates elements using an arbitrary
 predicate evaluated over the direct owned elements of a given context.
Returns:
shared [`ByPredicate`](ByPredicate.html) finder instance
byQualifiedName
public static [ByQualifiedName](ByQualifiedName.html) byQualifiedName()
Returns a finder that locates elements by their qualified name.
Returns:
shared [`ByQualifiedName`](ByQualifiedName.html) finder instance
byEClassRecursively
public static [ByEClassRecursively](ByEClassRecursively.html) byEClassRecursively()
Returns a finder that locates elements by their `EClass`
 recursively in a project or collection of roots.
Returns:
shared [`ByEClassRecursively`](ByEClassRecursively.html) finder instance

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.find</a></div>
<h1 class="title" title="Class Finder">Class Finder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.find.Finder</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">Finder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for providing access to various finders.

 <p>
 This utility class provides a set of preconfigured, stateless finder
 implementations used to locate <code>Element</code> instances within a model.
 Each finder encapsulates a specific lookup strategy (e.g., by name,
 declared name, qualified name, predicate, or by EClass recursively).
 </p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ByDeclaredName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByDeclaredName</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byDeclaredName()">byDeclaredName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a finder that locates elements by their declared name among
 the direct owned elements of a given context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ByEClassRecursively.html" title="class in com.dassault_systemes.modeler.kerml.find">ByEClassRecursively</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byEClassRecursively()">byEClassRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a finder that locates elements by their <code>EClass</code>
 recursively in a project or collection of roots.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ByName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByName</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byName()">byName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a finder that locates elements by their name among
 the direct owned elements of a given context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ByPredicate.html" title="class in com.dassault_systemes.modeler.kerml.find">ByPredicate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byPredicate()">byPredicate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a generic finder that locates elements using an arbitrary
 predicate evaluated over the direct owned elements of a given context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ByQualifiedName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByQualifiedName</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byQualifiedName()">byQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a finder that locates elements by their qualified name.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="byName()">
<h3>byName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ByName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByName</a></span> <span class="element-name">byName</span>()</div>
<div class="block">Returns a finder that locates elements by their name among
 the direct owned elements of a given context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shared <a href="ByName.html" title="class in com.dassault_systemes.modeler.kerml.find"><code>ByName</code></a> finder instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byDeclaredName()">
<h3>byDeclaredName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ByDeclaredName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByDeclaredName</a></span> <span class="element-name">byDeclaredName</span>()</div>
<div class="block">Returns a finder that locates elements by their declared name among
 the direct owned elements of a given context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shared <a href="ByDeclaredName.html" title="class in com.dassault_systemes.modeler.kerml.find"><code>ByDeclaredName</code></a> finder instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byPredicate()">
<h3>byPredicate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ByPredicate.html" title="class in com.dassault_systemes.modeler.kerml.find">ByPredicate</a></span> <span class="element-name">byPredicate</span>()</div>
<div class="block">Returns a generic finder that locates elements using an arbitrary
 predicate evaluated over the direct owned elements of a given context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shared <a href="ByPredicate.html" title="class in com.dassault_systemes.modeler.kerml.find"><code>ByPredicate</code></a> finder instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byQualifiedName()">
<h3>byQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ByQualifiedName.html" title="class in com.dassault_systemes.modeler.kerml.find">ByQualifiedName</a></span> <span class="element-name">byQualifiedName</span>()</div>
<div class="block">Returns a finder that locates elements by their qualified name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shared <a href="ByQualifiedName.html" title="class in com.dassault_systemes.modeler.kerml.find"><code>ByQualifiedName</code></a> finder instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byEClassRecursively()">
<h3>byEClassRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ByEClassRecursively.html" title="class in com.dassault_systemes.modeler.kerml.find">ByEClassRecursively</a></span> <span class="element-name">byEClassRecursively</span>()</div>
<div class="block">Returns a finder that locates elements by their <code>EClass</code>
 recursively in a project or collection of roots.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shared <a href="ByEClassRecursively.html" title="class in com.dassault_systemes.modeler.kerml.find"><code>ByEClassRecursively</code></a> finder instance</dd>
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
