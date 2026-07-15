# JAVA OPENAPI: MofUml2ElementsCreatorManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v3/imp0rt/convert/element/MofUml2ElementsCreatorManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v3/imp0rt/convert/element/MofUml2ElementsCreatorManager.html`
- source_sha256: `510a35dd61a1020c7fb368d2b74f7be5045330f61aa1ce0519a12c7f76f77fdd`
- captured_utc: `2026-07-14T16:55:19.103052+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element](package-summary.html)

## Class MofUml2ElementsCreatorManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element.MofUml2ElementsCreatorManager

All Implemented Interfaces:
`[MofUml2ElementsCreatorManager](../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html)`

@OpenApipublic final classMofUml2ElementsCreatorManager
extends com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
implements [MofUml2ElementsCreatorManager](../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html)

Registers MofElementCreators for Eclipse UML2 model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MofUml2ElementsCreatorManager](MofUml2ElementsCreatorManager.html)`
`[getInstance](#getInstance())()`

`protected void`
`[initialize](#initialize())()`
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
`addCreator, getCreator, removeConverter`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.[MofUml2ElementsCreatorManager](../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html)
`[addCreator](../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html#addCreator(org.eclipse.emf.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofElementCreator)), [removeConverter](../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html#removeConverter(org.eclipse.emf.ecore.EClass))`

============ METHOD DETAIL ========== 
Method Details
initialize
protected void initialize()
Overrides:
`initialize` in class `com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl`
getInstance
@OpenApipublic static [MofUml2ElementsCreatorManager](MofUml2ElementsCreatorManager.html) getInstance()
Returns:
manager instance.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element</a></div>
<h1 class="title" title="Class MofUml2ElementsCreatorManager">Class MofUml2ElementsCreatorManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element.MofUml2ElementsCreatorManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">MofUml2ElementsCreatorManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
implements <a href="../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></span></div>
<div class="block">Registers MofElementCreators for Eclipse UML2 model metaclasses</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MofUml2ElementsCreatorManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</h3>
<code>addCreator, getCreator, removeConverter</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManager">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.<a href="../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></h3>
<code><a href="../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html#addCreator(org.eclipse.emf.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofElementCreator)">addCreator</a>, <a href="../../../../imp0rt/convert/element/MofUml2ElementsCreatorManager.html#removeConverter(org.eclipse.emf.ecore.EClass)">removeConverter</a></code></div>
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
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>initialize</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="MofUml2ElementsCreatorManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager instance.</dd>
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
