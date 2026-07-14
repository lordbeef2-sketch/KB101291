# JAVA OPENAPI: FeatureValue (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/fuml/classes/FeatureValue.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/classes/FeatureValue.html`
- source_sha256: `da53f131177c627aaff0824397add1bf65f1c0025d0fc9bef7a0d8c1093a1ae3`
- captured_utc: `2026-07-14T16:58:02.718588+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml.classes](package-summary.html)

## Class FeatureValue

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider<[StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)>
com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.listener.SimulationListenerable`

@OpenApipublic classFeatureValue
extends com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider<[StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)>
implements com.nomagic.magicdraw.simulation.listener.SimulationListenerable

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider
`values`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ValueList](ValueList.html)`
`[getValues](#getValues())()`
Gets values.
`boolean`
`[hasValues](#hasValues())()`

`void`
`[setValues](#setValues(com.nomagic.magicdraw.simulation.fuml.classes.ValueList))([ValueList](ValueList.html) newValues)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
setValues
@OpenApipublic void setValues([ValueList](ValueList.html) newValues)
Overrides:
`setValues` in class `com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider<[StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)>`
getValues
@OpenApipublic [ValueList](ValueList.html) getValues()
Description copied from class: `com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider`
Gets values.
Overrides:
`getValues` in class `com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider<[StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html)>`
Returns:
ValueList.
hasValues
@OpenApipublic boolean hasValues()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml.classes</a></div>
<h1 class="title" title="Class FeatureValue">Class FeatureValue</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.simulation.listener.SimulationListenerable</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureValue</span>
<span class="extends-implements">extends com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a>&gt;
implements com.nomagic.magicdraw.simulation.listener.SimulationListenerable</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider">Fields inherited from class com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider</h3>
<code>values</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValueList.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">ValueList</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValues()">getValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasValues()">hasValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValues(com.nomagic.magicdraw.simulation.fuml.classes.ValueList)">setValues</a><wbr/>(<a href="ValueList.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">ValueList</a> newValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="setValues(com.nomagic.magicdraw.simulation.fuml.classes.ValueList)">
<h3>setValues</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValues</span><wbr/><span class="parameters">(<a href="ValueList.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">ValueList</a> newValues)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>setValues</code> in class <code>com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValues()">
<h3>getValues</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ValueList.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">ValueList</a></span> <span class="element-name">getValues</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code>com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider</code></span></div>
<div class="block">Gets values.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getValues</code> in class <code>com.nomagic.magicdraw.simulation.fuml.data.ValueListProvider&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>ValueList.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasValues()">
<h3>hasValues</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasValues</span>()</div>
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
