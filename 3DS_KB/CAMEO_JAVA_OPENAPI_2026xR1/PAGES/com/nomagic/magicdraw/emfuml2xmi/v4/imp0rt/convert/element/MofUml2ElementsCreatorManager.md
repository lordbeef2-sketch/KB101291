# JAVA OPENAPI: MofUml2ElementsCreatorManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/emfuml2xmi/v4/imp0rt/convert/element/MofUml2ElementsCreatorManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v4/imp0rt/convert/element/MofUml2ElementsCreatorManager.html`
- source_sha256: `077d3d0b90d2a2ef6d1c6fbcbd7795cbd0231b35229de44ac851e554bef0f6b6`
- captured_utc: `2026-07-14T16:45:35.338472+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element](package-summary.html)

## Class MofUml2ElementsCreatorManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManager

@OpenApipublic final classMofUml2ElementsCreatorManager
extends com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
Registers MofElementCreators for Eclipse UML2 model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addCreator](#addCreator(org.eclipse.emf_2_8_1.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofElementCreator))(org.eclipse.emf_2_8_1.ecore.EClass eClass,
 [MofElementCreator](MofElementCreator.html) creator)`
Registers new creator.
`static [MofUml2ElementsCreatorManager](MofUml2ElementsCreatorManager.html)`
`[getInstance](#getInstance())()`

`void`
`[removeConverter](#removeConverter(org.eclipse.emf_2_8_1.ecore.EClass))(org.eclipse.emf_2_8_1.ecore.EClass eClass)`
Removes elements creator.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
`getCreator`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [MofUml2ElementsCreatorManager](MofUml2ElementsCreatorManager.html) getInstance()
Returns:
manager instance.
addCreator
@OpenApipublic void addCreator(org.eclipse.emf_2_8_1.ecore.EClass eClass,
 [MofElementCreator](MofElementCreator.html) creator)
Registers new creator.
Overrides:
`addCreator` in class `com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl`
Parameters:
`eClass` - Eclipse UML2 model metaclass
`creator` - element creator
removeConverter
@OpenApipublic void removeConverter(org.eclipse.emf_2_8_1.ecore.EClass eClass)
Removes elements creator.
Overrides:
`removeConverter` in class `com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl`
Parameters:
`eClass` - Eclipse UML2 model metaclass

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element</a></div>
<h1 class="title" title="Class MofUml2ElementsCreatorManager">Class MofUml2ElementsCreatorManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">MofUml2ElementsCreatorManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCreator(org.eclipse.emf_2_8_1.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofElementCreator)">addCreator</a><wbr/>(org.eclipse.emf_2_8_1.ecore.EClass eClass,
 <a href="MofElementCreator.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element">MofElementCreator</a> creator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers new creator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MofUml2ElementsCreatorManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConverter(org.eclipse.emf_2_8_1.ecore.EClass)">removeConverter</a><wbr/>(org.eclipse.emf_2_8_1.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes elements creator.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</h3>
<code>getCreator</code></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="MofUml2ElementsCreatorManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element">MofUml2ElementsCreatorManager</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCreator(org.eclipse.emf_2_8_1.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofElementCreator)">
<h3>addCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCreator</span><wbr/><span class="parameters">(org.eclipse.emf_2_8_1.ecore.EClass eClass,
 <a href="MofElementCreator.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element">MofElementCreator</a> creator)</span></div>
<div class="block">Registers new creator.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addCreator</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>eClass</code> - Eclipse UML2 model metaclass</dd>
<dd><code>creator</code> - element creator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConverter(org.eclipse.emf_2_8_1.ecore.EClass)">
<h3>removeConverter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeConverter</span><wbr/><span class="parameters">(org.eclipse.emf_2_8_1.ecore.EClass eClass)</span></div>
<div class="block">Removes elements creator.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removeConverter</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert.element.MofUml2ElementsCreatorManagerImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>eClass</code> - Eclipse UML2 model metaclass</dd>
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
