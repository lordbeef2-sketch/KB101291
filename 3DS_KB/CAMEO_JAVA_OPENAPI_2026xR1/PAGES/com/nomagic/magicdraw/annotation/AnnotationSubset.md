# JAVA OPENAPI: AnnotationSubset (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/annotation/AnnotationSubset.html
- source_path: `com/nomagic/magicdraw/annotation/AnnotationSubset.html`
- source_sha256: `90a83b3384ff29cc29c77e08327ebb0c914ceef1034edde3523985ac8353be55`
- captured_utc: `2026-07-14T16:45:08.113110+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Class AnnotationSubset

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.annotation.AnnotationSubset

@OpenApiAllpublic final classAnnotationSubset
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Defines a subset of registered annotations.
 Used to filter annotations when retrieving them from the [`AnnotationManager`](AnnotationManager.html)
`AnnotationSubset.ALL` means any registered annotation.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [AnnotationSubset](AnnotationSubset.html)`
`[ALL](#ALL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AnnotationSubset](#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Comparator))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> included,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> excluded,
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [AnnotationSubset](AnnotationSubset.html)`
`[allExcluding](#allExcluding(java.util.Collection,java.util.Comparator))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> excludedCategories,
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)`

`boolean`
`[containsCategory](#containsCategory(com.nomagic.magicdraw.annotation.AnnotationCategory))([AnnotationCategory](AnnotationCategory.html) category)`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`[Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)>`
`[getComparator](#getComparator())()`

`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)>`
`[getExcludedCategories](#getExcludedCategories())()`
Excluded categories, that are strictly not contained by this subset
 If category is both included and excluded, it is still not contained by this subset
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)>`
`[getIncludedCategories](#getIncludedCategories())()`
If included categories are empty, then every possible category is contained by this subset, except the excluded ones.
`int`
`[hashCode](#hashCode())()`

`static [AnnotationSubset](AnnotationSubset.html)`
`[includingOnly](#includingOnly(java.util.Collection,java.util.Comparator))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> includedCategories,
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ALL
public static final [AnnotationSubset](AnnotationSubset.html) ALL
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AnnotationSubset
public AnnotationSubset([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> included,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> excluded,
 @CheckForNull
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)
 ============ METHOD DETAIL ========== 
Method Details
allExcluding
public static [AnnotationSubset](AnnotationSubset.html) allExcluding([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> excludedCategories,
 @CheckForNull
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)
includingOnly
public static [AnnotationSubset](AnnotationSubset.html) includingOnly([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> includedCategories,
 @CheckForNull
 [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> comparator)
Returns:
AnnotationSubset for any annotation group with the given scope
containsCategory
public boolean containsCategory([AnnotationCategory](AnnotationCategory.html) category)
Returns:
true if the given annotation category belongs to this subset
getIncludedCategories
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> getIncludedCategories()
If included categories are empty, then every possible category is contained by this subset, except the excluded ones.
getExcludedCategories
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[AnnotationCategory](AnnotationCategory.html)> getExcludedCategories()
Excluded categories, that are strictly not contained by this subset
 If category is both included and excluded, it is still not contained by this subset
getComparator
@CheckForNullpublic [Comparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)<[Annotation](Annotation.html)> getComparator()
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Class AnnotationSubset">Class AnnotationSubset</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.annotation.AnnotationSubset</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">AnnotationSubset</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Defines a subset of registered annotations.
 Used to filter annotations when retrieving them from the <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationManager</code></a>
<code>AnnotationSubset.ALL</code> means any registered annotation.</div>
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
<div class="col-first even-row-color"><code>static final <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALL">ALL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,java.util.Comparator)">AnnotationSubset</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; included,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; excluded,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#allExcluding(java.util.Collection,java.util.Comparator)">allExcluding</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; excludedCategories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#containsCategory(com.nomagic.magicdraw.annotation.AnnotationCategory)">containsCategory</a><wbr/>(<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a><wbr/>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComparator()">getComparator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExcludedCategories()">getExcludedCategories</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Excluded categories, that are strictly not contained by this subset
 If category is both included and excluded, it is still not contained by this subset</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncludedCategories()">getIncludedCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If included categories are empty, then every possible category is contained by this subset, except the excluded ones.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#includingOnly(java.util.Collection,java.util.Comparator)">includingOnly</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; includedCategories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ALL">
<h3>ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">ALL</span></div>
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
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,java.util.Comparator)">
<h3>AnnotationSubset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnnotationSubset</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; included,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; excluded,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</span></div>
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
<section class="detail" id="allExcluding(java.util.Collection,java.util.Comparator)">
<h3>allExcluding</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">allExcluding</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; excludedCategories,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</span></div>
</section>
</li>
<li>
<section class="detail" id="includingOnly(java.util.Collection,java.util.Comparator)">
<h3>includingOnly</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">includingOnly</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt; includedCategories,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; comparator)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AnnotationSubset for any annotation group with the given scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsCategory(com.nomagic.magicdraw.annotation.AnnotationCategory)">
<h3>containsCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">containsCategory</span><wbr/><span class="parameters">(<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the given annotation category belongs to this subset</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludedCategories()">
<h3>getIncludedCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt;</span> <span class="element-name">getIncludedCategories</span>()</div>
<div class="block">If included categories are empty, then every possible category is contained by this subset, except the excluded ones.</div>
</section>
</li>
<li>
<section class="detail" id="getExcludedCategories()">
<h3>getExcludedCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>&gt;</span> <span class="element-name">getExcludedCategories</span>()</div>
<div class="block">Excluded categories, that are strictly not contained by this subset
 If category is both included and excluded, it is still not contained by this subset</div>
</section>
</li>
<li>
<section class="detail" id="getComparator()">
<h3>getComparator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getComparator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
