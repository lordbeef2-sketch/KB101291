# JAVA OPENAPI: PostProjectOpenConverterManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/persistence/convert/PostProjectOpenConverterManager.html
- source_path: `com/nomagic/magicdraw/persistence/convert/PostProjectOpenConverterManager.html`
- source_sha256: `fe05b2496cdce85993e63af17fafe639cd2e6f0227dc514547c6129a67cd50f4`
- captured_utc: `2026-07-14T16:45:39.052522+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.persistence.convert](package-summary.html)

## Class PostProjectOpenConverterManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.persistence.convert.PostProjectOpenConverterManager

@OpenApipublic final classPostProjectOpenConverterManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Manager used for storing and getting `ProjectPostProjectLoadConverter`.

See Also:
`ProjectPostProjectLoadConverter`

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [PostProjectOpenConverterManager](PostProjectOpenConverterManager.html)`
`[getInstance](#getInstance())()`
Method used for getting instance of [`PostProjectOpenConverterManager`](PostProjectOpenConverterManager.html).
`void`
`[register](#register(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter))(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter esiConverter)`
Method used for registering new `ProjectPostProjectLoadConverter`.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [PostProjectOpenConverterManager](PostProjectOpenConverterManager.html) getInstance()
Method used for getting instance of [`PostProjectOpenConverterManager`](PostProjectOpenConverterManager.html).
Returns:
Instance of [`PostProjectOpenConverterManager`](PostProjectOpenConverterManager.html).
register
@OpenApipublic void register(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter esiConverter)
Method used for registering new `ProjectPostProjectLoadConverter`. Registered converters are not unregistered
 automatically.
Parameters:
`esiConverter` - Converter which you want to register.
See Also:
`ProjectPostProjectLoadConverter`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.persistence.convert</a></div>
<h1 class="title" title="Class PostProjectOpenConverterManager">Class PostProjectOpenConverterManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.persistence.convert.PostProjectOpenConverterManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">PostProjectOpenConverterManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Manager used for storing and getting <code>ProjectPostProjectLoadConverter</code>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>ProjectPostProjectLoadConverter</code></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PostProjectOpenConverterManager.html" title="class in com.nomagic.magicdraw.persistence.convert">PostProjectOpenConverterManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method used for getting instance of <a href="PostProjectOpenConverterManager.html" title="class in com.nomagic.magicdraw.persistence.convert"><code>PostProjectOpenConverterManager</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#register(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter)">register</a><wbr/>(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter esiConverter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method used for registering new <code>ProjectPostProjectLoadConverter</code>.</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PostProjectOpenConverterManager.html" title="class in com.nomagic.magicdraw.persistence.convert">PostProjectOpenConverterManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Method used for getting instance of <a href="PostProjectOpenConverterManager.html" title="class in com.nomagic.magicdraw.persistence.convert"><code>PostProjectOpenConverterManager</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Instance of <a href="PostProjectOpenConverterManager.html" title="class in com.nomagic.magicdraw.persistence.convert"><code>PostProjectOpenConverterManager</code></a>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="register(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter)">
<h3>register</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(com.nomagic.magicdraw.persistence.convert.ProjectPostProjectLoadConverter esiConverter)</span></div>
<div class="block">Method used for registering new <code>ProjectPostProjectLoadConverter</code>. Registered converters are not unregistered
 automatically.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>esiConverter</code> - Converter which you want to register.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>ProjectPostProjectLoadConverter</code></li>
</ul>
</dd>
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
