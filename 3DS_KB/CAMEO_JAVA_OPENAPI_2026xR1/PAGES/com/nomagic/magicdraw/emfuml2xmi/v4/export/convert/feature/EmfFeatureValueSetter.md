# JAVA OPENAPI: EmfFeatureValueSetter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/emfuml2xmi/v4/export/convert/feature/EmfFeatureValueSetter.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v4/export/convert/feature/EmfFeatureValueSetter.html`
- source_sha256: `5bdce4955066cc3b269b85478bcc46b8e5e948c8a11bfd2ba990bd676e57111a`
- captured_utc: `2026-07-14T16:45:35.101470+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature](package-summary.html)

## Interface EmfFeatureValueSetter

All Known Implementing Classes:
`[EmfFeatureValueSetterImpl](EmfFeatureValueSetterImpl.html)`

@OpenApiAllpublic interfaceEmfFeatureValueSetter

Eclipse UML2 model element feature value setter

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf_2_8_1.ecore.EStructuralFeature`
`[getEStructuralFeature](#getEStructuralFeature())()`
Feature to set value.
`void`
`[setValue](#setValue(org.eclipse.uml2_4_0_1.uml.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature.EmfUml2ExportFeatureHelper))(org.eclipse.uml2_4_0_1.uml.Element eElement,
 [Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 [EmfUml2ExportFeatureHelper](EmfUml2ExportFeatureHelper.html) helper)`
Sets Eclipse UML2 model element feature value.

============ METHOD DETAIL ========== 
Method Details
setValue
void setValue(org.eclipse.uml2_4_0_1.uml.Element eElement,
 [Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 [EmfUml2ExportFeatureHelper](EmfUml2ExportFeatureHelper.html) helper)
Sets Eclipse UML2 model element feature value.
Parameters:
`eElement` - Eclipse UML2 model element.
`mdElement` - MagicDraw UML2 model element.
`helper` - helper.
getEStructuralFeature
org.eclipse.emf_2_8_1.ecore.EStructuralFeature getEStructuralFeature()
Feature to set value.
Returns:
Eclipse UML2 model element feature.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature</a></div>
<h1 class="title" title="Interface EmfFeatureValueSetter">Interface EmfFeatureValueSetter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="EmfFeatureValueSetterImpl.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature">EmfFeatureValueSetterImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfFeatureValueSetter</span></div>
<div class="block">Eclipse UML2 model element feature value setter</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf_2_8_1.ecore.EStructuralFeature</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEStructuralFeature()">getEStructuralFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Feature to set value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setValue(org.eclipse.uml2_4_0_1.uml.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature.EmfUml2ExportFeatureHelper)">setValue</a><wbr/>(org.eclipse.uml2_4_0_1.uml.Element eElement,
 <a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 <a href="EmfUml2ExportFeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature">EmfUml2ExportFeatureHelper</a> helper)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets Eclipse UML2 model element feature value.</div>
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
<section class="detail" id="setValue(org.eclipse.uml2_4_0_1.uml.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature.EmfUml2ExportFeatureHelper)">
<h3>setValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(org.eclipse.uml2_4_0_1.uml.Element eElement,
 <a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 <a href="EmfUml2ExportFeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.export.convert.feature">EmfUml2ExportFeatureHelper</a> helper)</span></div>
<div class="block">Sets Eclipse UML2 model element feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eElement</code> - Eclipse UML2 model element.</dd>
<dd><code>mdElement</code> - MagicDraw UML2 model element.</dd>
<dd><code>helper</code> - helper.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEStructuralFeature()">
<h3>getEStructuralFeature</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf_2_8_1.ecore.EStructuralFeature</span> <span class="element-name">getEStructuralFeature</span>()</div>
<div class="block">Feature to set value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 model element feature.</dd>
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
