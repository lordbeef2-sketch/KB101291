# JAVA OPENAPI: MofUml2FeatureValueSettersManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html`
- source_sha256: `1d161a2343b6ceb05b15ac4c8d23f5ccbba0800187c8313f7f4b37b5bfc0e7b7`
- captured_utc: `2026-07-14T16:51:18.990173+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature](package-summary.html)

## Interface MofUml2FeatureValueSettersManager

All Known Implementing Classes:
`[MofUml2FeatureValueSettersManager](../../../v3/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html)`, `com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl`

@OpenApipublic interfaceMofUml2FeatureValueSettersManager

Registers FeatureValueSetter for MagicDraw UML model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addSetter](#addSetter(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofFeatureValueSetter))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [MofFeatureValueSetter](MofFeatureValueSetter.html) valueSetter)`
Registers feature value setter for given MagicDraw UML metamodel class.
`void`
`[removeSetter](#removeSetter(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)`
Removes feature value setter.

============ METHOD DETAIL ========== 
Method Details
addSetter
@OpenApivoid addSetter([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [MofFeatureValueSetter](MofFeatureValueSetter.html) valueSetter)
Registers feature value setter for given MagicDraw UML metamodel class.
Parameters:
`classType` - MagicDraw UML metamodel class
`valueSetter` - feature converter
removeSetter
@OpenApivoid removeSetter([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) featureName)
Removes feature value setter.
Parameters:
`classType` - MagicDraw UML metamodel class
`featureName` - feature

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature</a></div>
<h1 class="title" title="Interface MofUml2FeatureValueSettersManager">Interface MofUml2FeatureValueSettersManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../../v3/imp0rt/convert/feature/MofUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert.feature">MofUml2FeatureValueSettersManager</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofUml2FeatureValueSettersManagerImpl</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MofUml2FeatureValueSettersManager</span></div>
<div class="block">Registers FeatureValueSetter for MagicDraw UML model metaclasses</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addSetter(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofFeatureValueSetter)">addSetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a href="MofFeatureValueSetter.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature">MofFeatureValueSetter</a> valueSetter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers feature value setter for given MagicDraw UML metamodel class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeSetter(java.lang.Class,java.lang.String)">removeSetter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes feature value setter.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="addSetter(java.lang.Class,com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature.MofFeatureValueSetter)">
<h3>addSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addSetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a href="MofFeatureValueSetter.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.feature">MofFeatureValueSetter</a> valueSetter)</span></div>
<div class="block">Registers feature value setter for given MagicDraw UML metamodel class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - MagicDraw UML metamodel class</dd>
<dd><code>valueSetter</code> - feature converter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSetter(java.lang.Class,java.lang.String)">
<h3>removeSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removeSetter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> featureName)</span></div>
<div class="block">Removes feature value setter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - MagicDraw UML metamodel class</dd>
<dd><code>featureName</code> - feature</dd>
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
