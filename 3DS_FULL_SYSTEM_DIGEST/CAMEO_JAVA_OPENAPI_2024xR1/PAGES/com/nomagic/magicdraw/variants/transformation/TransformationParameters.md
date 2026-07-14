# JAVA OPENAPI: TransformationParameters (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/variants/transformation/TransformationParameters.html
- source_path: `com/nomagic/magicdraw/variants/transformation/TransformationParameters.html`
- source_sha256: `df1d37c0f3f68e288bad69ea08a9cd0b92cdc7ae89fddcc61d7afec4dec14795`
- captured_utc: `2026-07-14T16:52:20.306990+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.transformation](package-summary.html)

## Class TransformationParameters

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.transformation.TransformationParameters

@OpenApiAllpublic classTransformationParameters
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Transformation parameters passed to each [`ElementTransformation`](ElementTransformation.html) when model transformation is executed.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TransformationParameters](#%3Cinit%3E(boolean))(boolean shouldIgnoreLocks)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Notifier](../ui/Notifier.html)`
`[getNotifier](#getNotifier())()`

`void`
`[setNotifier](#setNotifier(com.nomagic.magicdraw.variants.ui.Notifier))([Notifier](../ui/Notifier.html) notifier)`

`void`
`[setShouldIgnoreLocks](#setShouldIgnoreLocks(boolean))(boolean shouldIgnoreLocks)`

`boolean`
`[shouldIgnoreLocks](#shouldIgnoreLocks())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TransformationParameters
public TransformationParameters(boolean shouldIgnoreLocks)
 ============ METHOD DETAIL ========== 
Method Details
shouldIgnoreLocks
public boolean shouldIgnoreLocks()
Returns:
should transformation ignore another user locked elements.
setShouldIgnoreLocks
public void setShouldIgnoreLocks(boolean shouldIgnoreLocks)
Parameters:
`shouldIgnoreLocks` - should transformation ignore another user locked elements.
setNotifier
public void setNotifier([Notifier](../ui/Notifier.html) notifier)
Parameters:
`notifier` - used to notify user.
getNotifier
public [Notifier](../ui/Notifier.html) getNotifier()
Returns:
notifier used to notify user.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.transformation</a></div>
<h1 class="title" title="Class TransformationParameters">Class TransformationParameters</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.transformation.TransformationParameters</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TransformationParameters</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Transformation parameters passed to each <a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation"><code>ElementTransformation</code></a> when model transformation is executed.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">TransformationParameters</a><wbr/>(boolean shouldIgnoreLocks)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotifier()">getNotifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNotifier(com.nomagic.magicdraw.variants.ui.Notifier)">setNotifier</a><wbr/>(<a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShouldIgnoreLocks(boolean)">setShouldIgnoreLocks</a><wbr/>(boolean shouldIgnoreLocks)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shouldIgnoreLocks()">shouldIgnoreLocks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>TransformationParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TransformationParameters</span><wbr/><span class="parameters">(boolean shouldIgnoreLocks)</span></div>
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
<section class="detail" id="shouldIgnoreLocks()">
<h3>shouldIgnoreLocks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldIgnoreLocks</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>should transformation ignore another user locked elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShouldIgnoreLocks(boolean)">
<h3>setShouldIgnoreLocks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShouldIgnoreLocks</span><wbr/><span class="parameters">(boolean shouldIgnoreLocks)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shouldIgnoreLocks</code> - should transformation ignore another user locked elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNotifier(com.nomagic.magicdraw.variants.ui.Notifier)">
<h3>setNotifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNotifier</span><wbr/><span class="parameters">(<a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notifier</code> - used to notify user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotifier()">
<h3>getNotifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a></span> <span class="element-name">getNotifier</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notifier used to notify user.</dd>
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
