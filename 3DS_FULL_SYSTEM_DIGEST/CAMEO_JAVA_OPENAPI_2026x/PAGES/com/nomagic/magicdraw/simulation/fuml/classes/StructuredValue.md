# JAVA OPENAPI: StructuredValue (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/fuml/classes/StructuredValue.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/classes/StructuredValue.html`
- source_sha256: `98993aa7602365f2e0d4f0505aaa4e2f1069d49056bb063077c7a97caeb243f4`
- captured_utc: `2026-07-14T16:58:02.687588+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml.classes](package-summary.html)

## Class StructuredValue

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
[com.nomagic.magicdraw.simulation.fuml.classes.Value](Value.html)
com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.listener.SimulationListenerable`

Direct Known Subclasses:
`[CompoundValue](CompoundValue.html)`

@OpenApipublic abstract classStructuredValue
extends [Value](Value.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`listenerInfoSupport`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`abstract [FeatureValue](FeatureValue.html)`
`[getFeatureValue](#getFeatureValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature))([StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature)`
Gets the feature value.
`abstract com.nomagic.magicdraw.simulation.fuml.classes.FeatureValueList`
`[getFeatureValues](#getFeatureValues())()`
Gets the feature values.
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.classes.[Value](Value.html)
`[getTypes](Value.html#getTypes())`
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`_beginIsolation, _endIsolation, firePropertyChange, getListeners, register, register, unregister`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getFeatureValue
@OpenApi
@CheckForNullpublic abstract [FeatureValue](FeatureValue.html) getFeatureValue([StructuralFeature](../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html) feature)
Gets the feature value.
Parameters:
`feature` - the feature
Returns:
the feature value
getFeatureValues
@OpenApipublic abstract com.nomagic.magicdraw.simulation.fuml.classes.FeatureValueList getFeatureValues()
Gets the feature values.
Returns:
the feature values

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml.classes</a></div>
<h1 class="title" title="Class StructuredValue">Class StructuredValue</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
<div class="inheritance"><a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.Value</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.simulation.listener.SimulationListenerable</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="CompoundValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">CompoundValue</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">StructuredValue</span>
<span class="extends-implements">extends <a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor">Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor</h3>
<code>listenerInfoSupport</code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="FeatureValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">FeatureValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">getFeatureValue</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the feature value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract com.nomagic.magicdraw.simulation.fuml.classes.FeatureValueList</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureValues()">getFeatureValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the feature values.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.classes.Value">Methods inherited from class com.nomagic.magicdraw.simulation.fuml.classes.<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a></h3>
<code><a href="Value.html#getTypes()">getTypes</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor">Methods inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor</h3>
<code>_beginIsolation, _endIsolation, firePropertyChange, getListeners, register, register, unregister</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getFeatureValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.StructuralFeature)">
<h3>getFeatureValue</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="FeatureValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">FeatureValue</a></span> <span class="element-name">getFeatureValue</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/StructuralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">StructuralFeature</a> feature)</span></div>
<div class="block">Gets the feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>the feature value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureValues()">
<h3>getFeatureValues</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">com.nomagic.magicdraw.simulation.fuml.classes.FeatureValueList</span> <span class="element-name">getFeatureValues</span>()</div>
<div class="block">Gets the feature values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the feature values</dd>
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
