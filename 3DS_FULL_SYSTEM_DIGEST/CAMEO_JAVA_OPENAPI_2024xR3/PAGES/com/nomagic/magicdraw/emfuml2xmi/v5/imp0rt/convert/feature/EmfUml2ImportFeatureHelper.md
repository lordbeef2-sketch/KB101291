# JAVA OPENAPI: EmfUml2ImportFeatureHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/convert/feature/EmfUml2ImportFeatureHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/convert/feature/EmfUml2ImportFeatureHelper.html`
- source_sha256: `a8c977c2387952de7ddfbc943dc1d8f0ba597785c42429dba085e64c112bc7ae`
- captured_utc: `2026-07-14T16:55:20.247064+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature](package-summary.html)

## Interface EmfUml2ImportFeatureHelper

All Superinterfaces:
`[BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)`

@OpenApipublic interfaceEmfUml2ImportFeatureHelperextends [BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)

Feature value setter helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement(org.eclipse.uml2_5_0_2.uml.Element))(org.eclipse.uml2_5_0_2.uml.Element eElement)`
Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.
`[EmfUml2ImportHelper](../../EmfUml2ImportHelper.html)`
`[getMofHelper](#getMofHelper())()`
Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)
`[getHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html#getHelper())`

============ METHOD DETAIL ========== 
Method Details
getElement
@OpenApi[Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement(org.eclipse.uml2_5_0_2.uml.Element eElement)
Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.
Parameters:
`eElement` - MagicDraw UML2 model element
Returns:
Eclipse UML2 model element
getMofHelper
@OpenApi[EmfUml2ImportHelper](../../EmfUml2ImportHelper.html) getMofHelper()
Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.
Returns:
helper

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert.feature</a></div>
<h1 class="title" title="Interface EmfUml2ImportFeatureHelper">Interface EmfUml2ImportFeatureHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../helpers/BaseEmfUml2FeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2FeatureHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ImportFeatureHelper</span><span class="extends-implements">
extends <a href="../../../../helpers/BaseEmfUml2FeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2FeatureHelper</a></span></div>
<div class="block">Feature value setter helper.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement(org.eclipse.uml2_5_0_2.uml.Element)">getElement</a><wbr/>(org.eclipse.uml2_5_0_2.uml.Element eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt">EmfUml2ImportHelper</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMofHelper()">getMofHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2FeatureHelper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../../../../helpers/BaseEmfUml2FeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2FeatureHelper</a></h3>
<code><a href="../../../../helpers/BaseEmfUml2FeatureHelper.html#getHelper()">getHelper</a></code></div>
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
<section class="detail" id="getElement(org.eclipse.uml2_5_0_2.uml.Element)">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span><wbr/><span class="parameters">(org.eclipse.uml2_5_0_2.uml.Element eElement)</span></div>
<div class="block">Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eElement</code> - MagicDraw UML2 model element</dd>
<dt>Returns:</dt>
<dd>Eclipse UML2 model element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMofHelper()">
<h3>getMofHelper</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../../EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt">EmfUml2ImportHelper</a></span> <span class="element-name">getMofHelper</span>()</div>
<div class="block">Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>helper</dd>
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
