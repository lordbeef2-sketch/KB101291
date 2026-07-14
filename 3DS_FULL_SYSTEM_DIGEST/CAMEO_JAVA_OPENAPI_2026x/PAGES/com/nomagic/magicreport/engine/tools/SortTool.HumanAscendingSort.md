# JAVA OPENAPI: SortTool.HumanAscendingSort (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/tools/SortTool.HumanAscendingSort.html
- source_path: `com/nomagic/magicreport/engine/tools/SortTool.HumanAscendingSort.html`
- source_sha256: `7f3abec6fcaa9c64d9cdcc4022d84e19f1c87412d7c649ad0cff2c02a2340744`
- captured_utc: `2026-07-14T16:58:37.443286+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class SortTool.HumanAscendingSort

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`

Direct Known Subclasses:
`[SortTool.HumanDescendingSort](SortTool.HumanDescendingSort.html)`

Enclosing class:
`[SortTool](SortTool.html)`

@OpenApiAllprotected static classSortTool.HumanAscendingSort
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>, [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

Sort Collection in ascending.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HumanAscendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)`
Create ascending sort.
`[HumanAscendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean))([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)`
Create ascending sort.
`[HumanAscendingSort](#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean))([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)`
Create ascending sort.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[compare](#compare(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2)`
Compares its two arguments for order.
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

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getFieldNames](#getFieldNames())()`

`[SortTool](SortTool.html)`
`[getSortTool](#getSortTool())()`

`boolean`
`[isCaseInsensitive](#isCaseInsensitive())()`

`void`
`[setCaseInsensitive](#setCaseInsensitive(boolean))(boolean isCaseInsensitive)`

`void`
`[setFieldNames](#setFieldNames(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames)`

`void`
`[setSortTool](#setSortTool(com.nomagic.magicreport.engine.tools.SortTool))([SortTool](SortTool.html) sortTool)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#equals(java.lang.Object)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#reversed()), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.Comparator)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function)), [thenComparing](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparing(java.util.function.Function,java.util.Comparator)), [thenComparingDouble](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingDouble(java.util.function.ToDoubleFunction)), [thenComparingInt](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingInt(java.util.function.ToIntFunction)), [thenComparingLong](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#thenComparingLong(java.util.function.ToLongFunction))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HumanAscendingSort
public HumanAscendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName)
Create ascending sort.
Parameters:
`sortTool` - the sort tool
`fieldName` - field being sorted
HumanAscendingSort
public HumanAscendingSort([SortTool](SortTool.html) sortTool,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fieldName,
 boolean isCaseInsensitive)
Create ascending sort.
Parameters:
`sortTool` - the sort tool
`fieldName` - field being sorted
`isCaseInsensitive` - true to sort case-insensitive
HumanAscendingSort
public HumanAscendingSort([SortTool](SortTool.html) sortTool,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames,
 boolean isCaseInsensitive)
Create ascending sort.
Parameters:
`sortTool` - the sort tool
`fieldNames` - collection of field being sorted
`isCaseInsensitive` - true to sort case-insensitive
 ============ METHOD DETAIL ========== 
Method Details
compare
public int compare([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2)
Compares its two arguments for order.
Specified by:
`[compare](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#compare(T,T))` in interface `[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
Parameters:
`o1` - the first object to be compared.
`o2` - the second object to be compared.
Returns:
a negative integer, zero, or a positive integer as the first argument is less than, equal to, or
 greater than the second.
See Also:
[`Comparator.compare(java.lang.Object, java.lang.Object)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#compare(T,T))
compareByNull
protected int compareByNull([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) v2)
compareByDouble
protected int compareByDouble(double dv1,
 double dv2)
compareByString
protected int compareByString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)
compareByStringIgnoreCase
protected int compareByStringIgnoreCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token2)
compareByLength
protected int compareByLength([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s1,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s2)
getSortTool
public [SortTool](SortTool.html) getSortTool()
setSortTool
public void setSortTool([SortTool](SortTool.html) sortTool)
getFieldNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getFieldNames()
setFieldNames
public void setFieldNames([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fieldNames)
isCaseInsensitive
public boolean isCaseInsensitive()
setCaseInsensitive
public void setCaseInsensitive(boolean isCaseInsensitive)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class SortTool.HumanAscendingSort">Class SortTool.HumanAscendingSort</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="SortTool.HumanDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanDescendingSort</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">protected static class </span><span class="element-name type-name-label">SortTool.HumanAscendingSort</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Sort Collection in ascending.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.SortTool.HumanAscendingSort">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String)">HumanAscendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</code></div>
<div class="col-last even-row-color">
<div class="block">Create ascending sort.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">HumanAscendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create ascending sort.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">HumanAscendingSort</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames,
 boolean isCaseInsensitive)</code></div>
<div class="col-last even-row-color">
<div class="block">Create ascending sort.</div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compare(java.lang.Object,java.lang.Object)">compare</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares its two arguments for order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByDouble(double,double)">compareByDouble</a><wbr/>(double dv1,
 double dv2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByLength(java.lang.String,java.lang.String)">compareByLength</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByNull(java.lang.Object,java.lang.Object)">compareByNull</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByString(java.lang.String,java.lang.String)">compareByString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareByStringIgnoreCase(java.lang.String,java.lang.String)">compareByStringIgnoreCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFieldNames()">getFieldNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortTool()">getSortTool</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCaseInsensitive()">isCaseInsensitive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCaseInsensitive(boolean)">setCaseInsensitive</a><wbr/>(boolean isCaseInsensitive)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFieldNames(java.util.List)">setFieldNames</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSortTool(com.nomagic.magicreport.engine.tools.SortTool)">setSortTool</a><wbr/>(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
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
<h3>HumanAscendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanAscendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName)</span></div>
<div class="block">Create ascending sort.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortTool</code> - the sort tool</dd>
<dd><code>fieldName</code> - field being sorted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.lang.String,boolean)">
<h3>HumanAscendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanAscendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fieldName,
 boolean isCaseInsensitive)</span></div>
<div class="block">Create ascending sort.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortTool</code> - the sort tool</dd>
<dd><code>fieldName</code> - field being sorted</dd>
<dd><code>isCaseInsensitive</code> - true to sort case-insensitive</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.tools.SortTool,java.util.Collection,boolean)">
<h3>HumanAscendingSort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HumanAscendingSort</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames,
 boolean isCaseInsensitive)</span></div>
<div class="block">Create ascending sort.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortTool</code> - the sort tool</dd>
<dd><code>fieldNames</code> - collection of field being sorted</dd>
<dd><code>isCaseInsensitive</code> - true to sort case-insensitive</dd>
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
<section class="detail" id="compare(java.lang.Object,java.lang.Object)">
<h3>compare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compare</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2)</span></div>
<div class="block">Compares its two arguments for order.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#compare(T,T)" title="class or interface in java.util">compare</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>o1</code> - the first object to be compared.</dd>
<dd><code>o2</code> - the second object to be compared.</dd>
<dt>Returns:</dt>
<dd>a negative integer, zero, or a positive integer as the first argument is less than, equal to, or
         greater than the second.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html#compare(T,T)" title="class or interface in java.util"><code>Comparator.compare(java.lang.Object, java.lang.Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareByNull(java.lang.Object,java.lang.Object)">
<h3>compareByNull</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByNull</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> v2)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareByDouble(double,double)">
<h3>compareByDouble</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByDouble</span><wbr/><span class="parameters">(double dv1,
 double dv2)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareByString(java.lang.String,java.lang.String)">
<h3>compareByString</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareByStringIgnoreCase(java.lang.String,java.lang.String)">
<h3>compareByStringIgnoreCase</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByStringIgnoreCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token2)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareByLength(java.lang.String,java.lang.String)">
<h3>compareByLength</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">compareByLength</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s2)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSortTool()">
<h3>getSortTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></span> <span class="element-name">getSortTool</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSortTool(com.nomagic.magicreport.engine.tools.SortTool)">
<h3>setSortTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSortTool</span><wbr/><span class="parameters">(<a href="SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a> sortTool)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFieldNames()">
<h3>getFieldNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getFieldNames</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFieldNames(java.util.List)">
<h3>setFieldNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFieldNames</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fieldNames)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCaseInsensitive()">
<h3>isCaseInsensitive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCaseInsensitive</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCaseInsensitive(boolean)">
<h3>setCaseInsensitive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCaseInsensitive</span><wbr/><span class="parameters">(boolean isCaseInsensitive)</span></div>
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
