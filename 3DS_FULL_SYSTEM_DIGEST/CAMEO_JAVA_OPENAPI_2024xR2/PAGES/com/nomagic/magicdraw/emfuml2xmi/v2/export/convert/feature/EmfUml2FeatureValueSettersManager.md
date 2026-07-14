# JAVA OPENAPI: EmfUml2FeatureValueSettersManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/emfuml2xmi/v2/export/convert/feature/EmfUml2FeatureValueSettersManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/export/convert/feature/EmfUml2FeatureValueSettersManager.html`
- source_sha256: `36a476a530643b2bf0fd92b41010cb11675ac579ae007690ba21d84813026613`
- captured_utc: `2026-07-14T16:55:17.596033+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature](package-summary.html)

## Class EmfUml2FeatureValueSettersManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature.EmfUml2FeatureValueSettersManager

@OpenApipublic final classEmfUml2FeatureValueSettersManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Registers FeatureValueSetter for Eclipse UML2 model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addSetter](#addSetter(org.eclipse.emf_2_2_3.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature.EmfFeatureValueSetter))(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 [EmfFeatureValueSetter](EmfFeatureValueSetter.html) valueSetter)`
Registers feature value setter for given Eclipse UML2 metamodel class.
`static [EmfUml2FeatureValueSettersManager](EmfUml2FeatureValueSettersManager.html)`
`[getInstance](#getInstance())()`

`void`
`[removeSetter](#removeSetter(org.eclipse.emf_2_2_3.ecore.EClass,org.eclipse.emf_2_2_3.ecore.EStructuralFeature))(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 org.eclipse.emf_2_2_3.ecore.EStructuralFeature eStructuralFeature)`
Removes feature value setter.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [EmfUml2FeatureValueSettersManager](EmfUml2FeatureValueSettersManager.html) getInstance()
Returns:
manager instance.
addSetter
@OpenApipublic void addSetter(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 [EmfFeatureValueSetter](EmfFeatureValueSetter.html) valueSetter)
Registers feature value setter for given Eclipse UML2 metamodel class.
Parameters:
`eClass` - Eclipse UML2 metamodel class
`valueSetter` - feature converter
removeSetter
@OpenApipublic void removeSetter(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 org.eclipse.emf_2_2_3.ecore.EStructuralFeature eStructuralFeature)
Removes feature value setter.
Parameters:
`eClass` - Eclipse UML2 metamodel class
`eStructuralFeature` - feature

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature</a></div>
<h1 class="title" title="Class EmfUml2FeatureValueSettersManager">Class EmfUml2FeatureValueSettersManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature.EmfUml2FeatureValueSettersManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EmfUml2FeatureValueSettersManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Registers FeatureValueSetter for Eclipse UML2 model metaclasses</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSetter(org.eclipse.emf_2_2_3.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature.EmfFeatureValueSetter)">addSetter</a><wbr/>(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 <a href="EmfFeatureValueSetter.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature">EmfFeatureValueSetter</a> valueSetter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers feature value setter for given Eclipse UML2 metamodel class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature">EmfUml2FeatureValueSettersManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSetter(org.eclipse.emf_2_2_3.ecore.EClass,org.eclipse.emf_2_2_3.ecore.EStructuralFeature)">removeSetter</a><wbr/>(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 org.eclipse.emf_2_2_3.ecore.EStructuralFeature eStructuralFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes feature value setter.</div>
</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="EmfUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature">EmfUml2FeatureValueSettersManager</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSetter(org.eclipse.emf_2_2_3.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature.EmfFeatureValueSetter)">
<h3>addSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSetter</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 <a href="EmfFeatureValueSetter.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export.convert.feature">EmfFeatureValueSetter</a> valueSetter)</span></div>
<div class="block">Registers feature value setter for given Eclipse UML2 metamodel class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - Eclipse UML2 metamodel class</dd>
<dd><code>valueSetter</code> - feature converter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSetter(org.eclipse.emf_2_2_3.ecore.EClass,org.eclipse.emf_2_2_3.ecore.EStructuralFeature)">
<h3>removeSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSetter</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.ecore.EClass eClass,
 org.eclipse.emf_2_2_3.ecore.EStructuralFeature eStructuralFeature)</span></div>
<div class="block">Removes feature value setter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - Eclipse UML2 metamodel class</dd>
<dd><code>eStructuralFeature</code> - feature</dd>
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
