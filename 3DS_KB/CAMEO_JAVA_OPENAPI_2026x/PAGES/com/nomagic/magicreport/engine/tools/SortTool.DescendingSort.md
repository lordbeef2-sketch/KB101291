# JAVA OPENAPI: SortTool.DescendingSort (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/tools/SortTool.DescendingSort.html
- source_path: `com/nomagic/magicreport/engine/tools/SortTool.DescendingSort.html`
- source_sha256: `9613ebad3c62e5b103050d9c0ec795cc8c5331a5b9dfd66cc79d95c7a4420664`
- captured_utc: `2026-07-14T16:58:37.347285+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class SortTool.DescendingSort

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.engine.tools.SortTool.AscendingSort](SortTool.AscendingSort.html)
com.nomagic.magicreport.engine.tools.SortTool.DescendingSort

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`

Enclosing class:
`[SortTool](SortTool.html)`

protected static classSortTool.DescendingSort
extends [SortTool.AscendingSort](SortTool.AscendingSort.html)

sort Collection in descending

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.DescendingSort)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`

`[DescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)`

`[DescendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean))([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected int`
`[compareByComparable](#compareByComparable(java.lang.Comparable,java.lang.Comparable))([Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> v1,
 [Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> v2)`

`protected int`
`[compareByNull](#compareByNull(java.lang.Object,java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2,
 boolean isUseComparable)`

`protected int`
`[compareByString](#compareByString(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v2)`

`protected int`
`[compareByStringIgnoreCase](#compareByStringIgnoreCase(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v2)`
Methods inherited from class com.nomagic.magicreport.engine.tools.[SortTool.AscendingSort](SortTool.AscendingSort.html)
`[compare](SortTool.AscendingSort.html#compare(java.lang.Object,java.lang.Object)), [getCompareResult](SortTool.AscendingSort.html#getCompareResult(java.lang.Object,java.lang.Object,java.lang.String)), [getFieldNames](SortTool.AscendingSort.html#getFieldNames()), [getSortTool](SortTool.AscendingSort.html#getSortTool()), [isCaseInsensitive](SortTool.AscendingSort.html#isCaseInsensitive()), [setCaseInsensitive](SortTool.AscendingSort.html#setCaseInsensitive(boolean)), [setFieldNames](SortTool.AscendingSort.html#setFieldNames(java.util.List)), [setSortTool](SortTool.AscendingSort.html#setSortTool(com.nomagic.magicreport.engine.tools.SortTool))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#reversed()), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)), [thenComparingDouble](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)), [thenComparingInt](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)), [thenComparingLong](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DescendingSort
public DescendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
DescendingSort
public DescendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)
DescendingSort
public DescendingSort([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)
 ============ METHOD DETAIL ========== 
Method Details
compareByNull
protected int compareByNull([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2,
 boolean isUseComparable)
Overrides:
`[compareByNull](SortTool.AscendingSort.html#compareByNull(java.lang.Object,java.lang.Object,boolean))` in class `[SortTool.AscendingSort](SortTool.AscendingSort.html)`
compareByString
protected int compareByString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v2)
Overrides:
`[compareByString](SortTool.AscendingSort.html#compareByString(java.lang.String,java.lang.String))` in class `[SortTool.AscendingSort](SortTool.AscendingSort.html)`
compareByStringIgnoreCase
protected int compareByStringIgnoreCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) v2)
Overrides:
`[compareByStringIgnoreCase](SortTool.AscendingSort.html#compareByStringIgnoreCase(java.lang.String,java.lang.String))` in class `[SortTool.AscendingSort](SortTool.AscendingSort.html)`
compareByComparable
protected int compareByComparable([Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> v1,
 [Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> v2)
Overrides:
`[compareByComparable](SortTool.AscendingSort.html#compareByComparable(java.lang.Comparable,java.lang.Comparable))` in class `[SortTool.AscendingSort](SortTool.AscendingSort.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class SortTool.DescendingSort">Class SortTool.DescendingSort</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">com.nomagic.magicreport.engine.tools.SortTool.AscendingSort</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.SortTool.DescendingSort</div>
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
<div class="type-signature"><span class="modifiers">protected static class </span><span class="element-name type-name-label">SortTool.DescendingSort</span>
<span class="extends-implements">extends <a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></span></div>
<div class="block">sort Collection in descending</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.DescendingSort">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String)">DescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">DescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">DescendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByComparable(java.lang.Comparable,java.lang.Comparable)">compareByComparable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; v2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByNull(java.lang.Object,java.lang.Object,boolean)">compareByNull</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2,
 boolean isUseComparable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByString(java.lang.String,java.lang.String)">compareByString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByStringIgnoreCase(java.lang.String,java.lang.String)">compareByStringIgnoreCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool.AscendingSort">Methods inherited from class com.nomagic.magicreport.engine.tools.<a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></h3>
<code><a href="SortTool.AscendingSort.html#compare(java.lang.Object,java.lang.Object)">compare</a>, <a href="SortTool.AscendingSort.html#getCompareResult(java.lang.Object,java.lang.Object,java.lang.String)">getCompareResult</a>, <a href="SortTool.AscendingSort.html#getFieldNames()">getFieldNames</a>, <a href="SortTool.AscendingSort.html#getSortTool()">getSortTool</a>, <a href="SortTool.AscendingSort.html#isCaseInsensitive()">isCaseInsensitive</a>, <a href="SortTool.AscendingSort.html#setCaseInsensitive(boolean)">setCaseInsensitive</a>, <a href="SortTool.AscendingSort.html#setFieldNames(java.util.List)">setFieldNames</a>, <a href="SortTool.AscendingSort.html#setSortTool(com.nomagic.magicreport.engine.tools.SortTool)">setSortTool</a></code></div>
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
<h3>DescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">
<h3>DescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">
<h3>DescendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DescendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
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
<section class="detail" id="compareByNull(java.lang.Object,java.lang.Object,boolean)">
<h3>compareByNull</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByNull</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2,
 boolean isUseComparable)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.AscendingSort.html#compareByNull(java.lang.Object,java.lang.Object,boolean)">compareByNull</a></code> in class <code><a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByString(java.lang.String,java.lang.String)">
<h3>compareByString</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.AscendingSort.html#compareByString(java.lang.String,java.lang.String)">compareByString</a></code> in class <code><a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByStringIgnoreCase(java.lang.String,java.lang.String)">
<h3>compareByStringIgnoreCase</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByStringIgnoreCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> v2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.AscendingSort.html#compareByStringIgnoreCase(java.lang.String,java.lang.String)">compareByStringIgnoreCase</a></code> in class <code><a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByComparable(java.lang.Comparable,java.lang.Comparable)">
<h3>compareByComparable</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByComparable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; v2)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SortTool.AscendingSort.html#compareByComparable(java.lang.Comparable,java.lang.Comparable)">compareByComparable</a></code> in class <code><a href="SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a></code></dd>
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
