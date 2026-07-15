# JAVA OPENAPI: SortTool.HumanDescendingSort (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/tools/SortTool.HumanDescendingSort.html
- source_path: `com/nomagic/magicreport/engine/tools/SortTool.HumanDescendingSort.html`
- source_sha256: `a3243f23741905b9ad2e879ab25776216465b1054b2ede65e830b23c4872aa41`
- captured_utc: `2026-07-14T16:58:37.361284+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class SortTool.HumanDescendingSort

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)
com.nomagic.magicreport.engine.tools.SortTool.HumanDescendingSort

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`

Enclosing class:
`[SortTool](SortTool.html)`

@OpenApiAllprotected static classSortTool.HumanDescendingSort
extends [SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)

sort Collection in descending.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.HumanDescendingSort)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HumanDescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`

`[HumanDescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)`

`[HumanDescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean))([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected int`
`[compareByDouble](#compareByDouble(double,double))(double dv1,
 double dv2)`

`protected int`
`[compareByLength](#compareByLength(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s2)`

`protected int`
`[compareByNull](#compareByNull(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v2)`

`protected int`
`[compareByString](#compareByString(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)`

`protected int`
`[compareByStringIgnoreCase](#compareByStringIgnoreCase(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)`
Methods inherited from class com.nomagic.magicreport.engine.tools.[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)
`[compare](SortTool.HumanAscendingSort.html#compare(java.lang.Object,java.lang.Object)), [getFieldNames](SortTool.HumanAscendingSort.html#getFieldNames()), [getSortTool](SortTool.HumanAscendingSort.html#getSortTool()), [isCaseInsensitive](SortTool.HumanAscendingSort.html#isCaseInsensitive()), [setCaseInsensitive](SortTool.HumanAscendingSort.html#setCaseInsensitive(boolean)), [setFieldNames](SortTool.HumanAscendingSort.html#setFieldNames(java.util.List)), [setSortTool](SortTool.HumanAscendingSort.html#setSortTool(com.nomagic.magicreport.engine.tools.SortTool))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#reversed()), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)), [thenComparingDouble](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)), [thenComparingInt](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)), [thenComparingLong](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HumanDescendingSort
public HumanDescendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
HumanDescendingSort
public HumanDescendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)
HumanDescendingSort
public HumanDescendingSort([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)
 ============ METHOD DETAIL ========== 
Method Details
compareByNull
protected int compareByNull([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v2)
Overrides:
`[compareByNull](SortTool.HumanAscendingSort.html#compareByNull(java.lang.Object,java.lang.Object))` in class `[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`
compareByDouble
protected int compareByDouble(double dv1,
 double dv2)
Overrides:
`[compareByDouble](SortTool.HumanAscendingSort.html#compareByDouble(double,double))` in class `[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`
compareByString
protected int compareByString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)
Overrides:
`[compareByString](SortTool.HumanAscendingSort.html#compareByString(java.lang.String,java.lang.String))` in class `[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`
compareByStringIgnoreCase
protected int compareByStringIgnoreCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)
Overrides:
`[compareByStringIgnoreCase](SortTool.HumanAscendingSort.html#compareByStringIgnoreCase(java.lang.String,java.lang.String))` in class `[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`
compareByLength
protected int compareByLength([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s2)
Overrides:
`[compareByLength](SortTool.HumanAscendingSort.html#compareByLength(java.lang.String,java.lang.String))` in class `[SortTool.HumanAscendingSort](SortTool.HumanAscendingSort.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class SortTool.HumanDescendingSort">Class SortTool.HumanDescendingSort</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.SortTool.HumanDescendingSort</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">protected static class </span><span class="element-name type-name-label">SortTool.HumanDescendingSort</span>
<span class="extends-implements">extends <a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></span></div>
<div class="block">sort Collection in descending.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.HumanDescendingSort">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String)">HumanDescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">HumanDescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">HumanDescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames,
 boolean isCaseInsensitive)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByDouble(double,double)">compareByDouble</a><wbr/>(double dv1,
 double dv2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByLength(java.lang.String,java.lang.String)">compareByLength</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByNull(java.lang.Object,java.lang.Object)">compareByNull</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByString(java.lang.String,java.lang.String)">compareByString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByStringIgnoreCase(java.lang.String,java.lang.String)">compareByStringIgnoreCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort">Methods inherited from class com.nomagic.magicreport.engine.tools.<a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></h3>
<code><a href="SortTool.HumanAscendingSort.html#compare(java.lang.Object,java.lang.Object)">compare</a>, <a href="SortTool.HumanAscendingSort.html#getFieldNames()">getFieldNames</a>, <a href="SortTool.HumanAscendingSort.html#getSortTool()">getSortTool</a>, <a href="SortTool.HumanAscendingSort.html#isCaseInsensitive()">isCaseInsensitive</a>, <a href="SortTool.HumanAscendingSort.html#setCaseInsensitive(boolean)">setCaseInsensitive</a>, <a href="SortTool.HumanAscendingSort.html#setFieldNames(java.util.List)">setFieldNames</a>, <a href="SortTool.HumanAscendingSort.html#setSortTool(com.nomagic.magicreport.engine.tools.SortTool)">setSortTool</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Comparator">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)" title="class or interface in java.util">thenComparing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)" title="class or interface in java.util">thenComparingDouble</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)" title="class or interface in java.util">thenComparingInt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction)" title="class or interface in java.util">thenComparingLong</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String)">
<h3>HumanDescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanDescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">
<h3>HumanDescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanDescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">
<h3>HumanDescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanDescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames,
 boolean isCaseInsensitive)</span></div>
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
<section class="detail" id="compareByNull(java.lang.Object,java.lang.Object)">
<h3>compareByNull</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByNull</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.HumanAscendingSort.html#compareByNull(java.lang.Object,java.lang.Object)">compareByNull</a></code> in class <code><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByDouble(double,double)">
<h3>compareByDouble</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByDouble</span><wbr/><span class="parameters">(double dv1,
 double dv2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.HumanAscendingSort.html#compareByDouble(double,double)">compareByDouble</a></code> in class <code><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByString(java.lang.String,java.lang.String)">
<h3>compareByString</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.HumanAscendingSort.html#compareByString(java.lang.String,java.lang.String)">compareByString</a></code> in class <code><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByStringIgnoreCase(java.lang.String,java.lang.String)">
<h3>compareByStringIgnoreCase</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByStringIgnoreCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.HumanAscendingSort.html#compareByStringIgnoreCase(java.lang.String,java.lang.String)">compareByStringIgnoreCase</a></code> in class <code><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByLength(java.lang.String,java.lang.String)">
<h3>compareByLength</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByLength</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.HumanAscendingSort.html#compareByLength(java.lang.String,java.lang.String)">compareByLength</a></code> in class <code><a href="SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a></code></dd>
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
