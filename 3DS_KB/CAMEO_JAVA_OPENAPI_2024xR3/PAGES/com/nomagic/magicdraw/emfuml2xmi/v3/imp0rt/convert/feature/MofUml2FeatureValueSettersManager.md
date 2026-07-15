# JAVA OPENAPI: MofUml2FeatureValueSettersManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v3/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v3/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html`
- source_sha256: `641d57af771eb3df2a7b4a4ba3b0668d7ec427aae257737afe6c6470a544e7de`
- captured_utc: `2026-07-14T16:55:19.128052+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature](package-summary.html)

## Class MofUml2FeatureValueSettersManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl
com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature.MofUml2FeatureValueSettersManager

All Implemented Interfaces:
`[MofUml2FeatureValueSettersManager](../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html)`

@OpenApipublic final classMofUml2FeatureValueSettersManager
extends com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl
implements [MofUml2FeatureValueSettersManager](../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html)

Registers FeatureValueSetter for MagicDraw UML model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MofUml2FeatureValueSettersManager](MofUml2FeatureValueSettersManager.html)`
`[getInstance](#getInstance())()`

`protected void`
`[initialize](#initialize())()`
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl
`addSetter, getFeaturesSetters, removeSetter`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.[MofUml2FeatureValueSettersManager](../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html)
`[addSetter](../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html#addSetter(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofFeatureValueSetter)), [removeSetter](../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html#removeSetter(java.lang.Class,java.lang.String))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [MofUml2FeatureValueSettersManager](MofUml2FeatureValueSettersManager.html) getInstance()
Returns:
manager instance.
initialize
protected void initialize()
Overrides:
`initialize` in class `com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature</a></div>
<h1 class="title" title="Class MofUml2FeatureValueSettersManager">Class MofUml2FeatureValueSettersManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature.MofUml2FeatureValueSettersManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">MofUml2FeatureValueSettersManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl
implements <a href="../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></span></div>
<div class="block">Registers FeatureValueSetter for MagicDraw UML model metaclasses</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MofUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl</h3>
<code>addSetter, getFeaturesSetters, removeSetter</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManager">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.<a href="../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></h3>
<code><a href="../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html#addSetter(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofFeatureValueSetter)">addSetter</a>, <a href="../../../../imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html#removeSetter(java.lang.Class,java.lang.String)">removeSetter</a></code></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="MofUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>initialize</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl</code></dd>
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
