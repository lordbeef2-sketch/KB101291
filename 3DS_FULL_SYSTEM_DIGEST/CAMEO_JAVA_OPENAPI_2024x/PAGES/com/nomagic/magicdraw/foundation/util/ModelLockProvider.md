# JAVA OPENAPI: ModelLockProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/foundation/util/ModelLockProvider.html
- source_path: `com/nomagic/magicdraw/foundation/util/ModelLockProvider.html`
- source_sha256: `fcb4b8c272f3bec077ef2b7aa999b5dff4f6b76ea8a5468aa7cea2d27417968c`
- captured_utc: `2026-07-14T16:51:22.456219+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.util](package-summary.html)

## Class ModelLockProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.foundation.util.ModelLockProvider

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.util.ModelLockProvider`

public abstract classModelLockProvider
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.dassault_systemes.modeler.foundation.util.ModelLockProvider

The class implementation provides a bridge between model's implementation and the application.
 Model will use single instance of the class in order to get a lock and the locking configuration by an object.
 Application will be able to provide a lock and the locking configuration via configuring single instance.

Version:
1.0

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModelLockProvider](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ModelLockProvider](ModelLockProvider.html)`
`[getInstance](#getInstance())()`
Returns configured instance of `ModelLockProvider`.
`static void`
`[setInstance](#setInstance(com.nomagic.magicdraw.foundation.util.ModelLockProvider))([ModelLockProvider](ModelLockProvider.html) instance)`
Configures single instance of `ModelLockProvider`.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.util.ModelLockProvider
`getLock, getTimeUnit, getTryLockTime`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModelLockProvider
public ModelLockProvider()
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [ModelLockProvider](ModelLockProvider.html) getInstance()
Returns configured instance of `ModelLockProvider`.
Returns:
single instance.
setInstance
public static void setInstance([ModelLockProvider](ModelLockProvider.html) instance)
Configures single instance of `ModelLockProvider`.
Parameters:
`instance` - new instance.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.util</a></div>
<h1 class="title" title="Class ModelLockProvider">Class ModelLockProvider</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.foundation.util.ModelLockProvider</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.util.ModelLockProvider</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ModelLockProvider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.dassault_systemes.modeler.foundation.util.ModelLockProvider</span></div>
<div class="block">The class implementation provides a bridge between model's implementation and the application.
 Model will use single instance of the class in order to get a lock and the locking configuration by an object.
 Application will be able to provide a lock and the locking configuration via configuring single instance.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ModelLockProvider</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ModelLockProvider.html" title="class in com.nomagic.magicdraw.foundation.util">ModelLockProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns configured instance of <code>ModelLockProvider</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setInstance(com.nomagic.magicdraw.foundation.util.ModelLockProvider)">setInstance</a><wbr/>(<a href="ModelLockProvider.html" title="class in com.nomagic.magicdraw.foundation.util">ModelLockProvider</a> instance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Configures single instance of <code>ModelLockProvider</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.util.ModelLockProvider">Methods inherited from interface com.dassault_systemes.modeler.foundation.util.ModelLockProvider</h3>
<code>getLock, getTimeUnit, getTryLockTime</code></div>
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
<h3>ModelLockProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelLockProvider</span>()</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ModelLockProvider.html" title="class in com.nomagic.magicdraw.foundation.util">ModelLockProvider</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns configured instance of <code>ModelLockProvider</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>single instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInstance(com.nomagic.magicdraw.foundation.util.ModelLockProvider)">
<h3>setInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setInstance</span><wbr/><span class="parameters">(<a href="ModelLockProvider.html" title="class in com.nomagic.magicdraw.foundation.util">ModelLockProvider</a> instance)</span></div>
<div class="block">Configures single instance of <code>ModelLockProvider</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - new instance.</dd>
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
