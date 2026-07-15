# JAVA OPENAPI: EmfUml2FeatureValueSettersManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/export/convert/feature/EmfUml2FeatureValueSettersManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/export/convert/feature/EmfUml2FeatureValueSettersManager.html`
- source_sha256: `5dbc75d75f61156ec8e9b7f91ee61008421358134cb37b2f0e035776dd6c5a3d`
- captured_utc: `2026-07-14T16:51:18.603168+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.export.convert.feature](package-summary.html)

## Interface EmfUml2FeatureValueSettersManager

All Known Implementing Classes:
`[EmfUml2FeatureValueSettersManager](../../../v3/export/convert/feature/EmfUml2FeatureValueSettersManager.html)`, `com.nomagic.magicdraw.emfuml2xmi.export.convert.feature.EmfUml2FeatureValueSettersManagerImpl`

@OpenApipublic interfaceEmfUml2FeatureValueSettersManager

Registers FeatureValueSetter for Eclipse UML2 model metaclasses

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addSetter](#addSetter(org.eclipse.emf.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.export.convert.feature.EmfFeatureValueSetter))(org.eclipse.emf.ecore.EClass eClass,
 [EmfFeatureValueSetter](EmfFeatureValueSetter.html) valueSetter)`
Registers feature value setter for given Eclipse UML2 metamodel class.
`void`
`[removeSetter](#removeSetter(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)`
Removes feature value setter.

============ METHOD DETAIL ========== 
Method Details
addSetter
@OpenApivoid addSetter(org.eclipse.emf.ecore.EClass eClass,
 [EmfFeatureValueSetter](EmfFeatureValueSetter.html) valueSetter)
Registers feature value setter for given Eclipse UML2 metamodel class.
Parameters:
`eClass` - Eclipse UML2 metamodel class
`valueSetter` - feature converter
removeSetter
@OpenApivoid removeSetter(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.export.convert.feature</a></div>
<h1 class="title" title="Interface EmfUml2FeatureValueSettersManager">Interface EmfUml2FeatureValueSettersManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../../v3/export/convert/feature/EmfUml2FeatureValueSettersManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.export.convert.feature">EmfUml2FeatureValueSettersManager</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.export.convert.feature.EmfUml2FeatureValueSettersManagerImpl</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2FeatureValueSettersManager</span></div>
<div class="block">Registers FeatureValueSetter for Eclipse UML2 model metaclasses</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addSetter(org.eclipse.emf.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.export.convert.feature.EmfFeatureValueSetter)">addSetter</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 <a href="EmfFeatureValueSetter.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.export.convert.feature">EmfFeatureValueSetter</a> valueSetter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers feature value setter for given Eclipse UML2 metamodel class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeSetter(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">removeSetter</a><wbr/>(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</code></div>
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
<section class="detail" id="addSetter(org.eclipse.emf.ecore.EClass,com.nomagic.magicdraw.emfuml2xmi.export.convert.feature.EmfFeatureValueSetter)">
<h3>addSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addSetter</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 <a href="EmfFeatureValueSetter.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.export.convert.feature">EmfFeatureValueSetter</a> valueSetter)</span></div>
<div class="block">Registers feature value setter for given Eclipse UML2 metamodel class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - Eclipse UML2 metamodel class</dd>
<dd><code>valueSetter</code> - feature converter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSetter(org.eclipse.emf.ecore.EClass,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>removeSetter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removeSetter</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</span></div>
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
