# JAVA OPENAPI: MofFeatureValueSetter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/convert/feature/MofFeatureValueSetter.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/convert/feature/MofFeatureValueSetter.html`
- source_sha256: `4cb75ade11685c628c7deee62fc50a887907788c335e8d5cca830d55daec2b63`
- captured_utc: `2026-07-14T16:55:20.257064+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature](package-summary.html)

## Interface MofFeatureValueSetter

All Known Implementing Classes:
`[MofFeatureValueSetterImpl](MofFeatureValueSetterImpl.html)`

@OpenApipublic interfaceMofFeatureValueSetter

MagicDraw model element feature value setter

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFeatureName](#getFeatureName())()`
Feature to set value.
`void`
`[setValue](#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,org.eclipse.uml2_5_0_2.uml.Element,com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature.EmfUml2ImportFeatureHelper))([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 org.eclipse.uml2_5_0_2.uml.Element eElement,
 [EmfUml2ImportFeatureHelper](EmfUml2ImportFeatureHelper.html) helper)`
Sets MagicDraw model element feature value

============ METHOD DETAIL ========== 
Method Details
setValue
@OpenApivoid setValue([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 org.eclipse.uml2_5_0_2.uml.Element eElement,
 [EmfUml2ImportFeatureHelper](EmfUml2ImportFeatureHelper.html) helper)
Sets MagicDraw model element feature value
Parameters:
`mdElement` - MagicDraw UML2 model element
`eElement` - Eclipse UML2 model element
`helper` - helper
getFeatureName
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFeatureName()
Feature to set value.
Returns:
magicDraw UML2 model element feature name

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature</a></div>
<h1 class="title" title="Interface MofFeatureValueSetter">Interface MofFeatureValueSetter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="MofFeatureValueSetterImpl.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature">MofFeatureValueSetterImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MofFeatureValueSetter</span></div>
<div class="block">MagicDraw model element feature value setter</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFeatureName()">getFeatureName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Feature to set value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,org.eclipse.uml2_5_0_2.uml.Element,com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature.EmfUml2ImportFeatureHelper)">setValue</a><wbr/>(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 org.eclipse.uml2_5_0_2.uml.Element eElement,
 <a href="EmfUml2ImportFeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature">EmfUml2ImportFeatureHelper</a> helper)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets MagicDraw model element feature value</div>
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
<section class="detail" id="setValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,org.eclipse.uml2_5_0_2.uml.Element,com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature.EmfUml2ImportFeatureHelper)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 org.eclipse.uml2_5_0_2.uml.Element eElement,
 <a href="EmfUml2ImportFeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature">EmfUml2ImportFeatureHelper</a> helper)</span></div>
<div class="block">Sets MagicDraw model element feature value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdElement</code> - MagicDraw UML2 model element</dd>
<dd><code>eElement</code> - Eclipse UML2 model element</dd>
<dd><code>helper</code> - helper</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureName()">
<h3>getFeatureName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFeatureName</span>()</div>
<div class="block">Feature to set value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>magicDraw UML2 model element feature name</dd>
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
