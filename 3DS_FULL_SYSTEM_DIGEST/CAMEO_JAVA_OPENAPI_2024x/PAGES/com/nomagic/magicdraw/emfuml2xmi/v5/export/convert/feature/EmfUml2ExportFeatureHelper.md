# JAVA OPENAPI: EmfUml2ExportFeatureHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/v5/export/convert/feature/EmfUml2ExportFeatureHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v5/export/convert/feature/EmfUml2ExportFeatureHelper.html`
- source_sha256: `296447349a6f5d4dbec8c372d63ae5bc2b7f4e4287f439270579a434ad989548`
- captured_utc: `2026-07-14T16:51:20.440193+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v5.export.convert.feature](package-summary.html)

## Interface EmfUml2ExportFeatureHelper

All Superinterfaces:
`[BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)`

@OpenApipublic interfaceEmfUml2ExportFeatureHelperextends [BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)

Feature value setter helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.uml2_5_0_2.uml.Element`
`[getEElement](#getEElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement)`
Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.
`org.eclipse.emf_2_10_2.common.util.Enumerator`
`[getEEnumeration](#getEEnumeration(javax.jmi.reflect.RefEnum))(javax.jmi.reflect.RefEnum mdEnumerationLiteral)`
Returns Eclipse UML2 model enumeration corresponding to MagicDraw UML2 model enumeration
`[EmfUml2ExportHelper](../../../helpers/EmfUml2ExportHelper.html)`
`[getEmfHelper](#getEmfHelper())()`
Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2FeatureHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html)
`[getHelper](../../../../helpers/BaseEmfUml2FeatureHelper.html#getHelper())`

============ METHOD DETAIL ========== 
Method Details
getEEnumeration
@OpenApiorg.eclipse.emf_2_10_2.common.util.Enumerator getEEnumeration(javax.jmi.reflect.RefEnum mdEnumerationLiteral)
Returns Eclipse UML2 model enumeration corresponding to MagicDraw UML2 model enumeration
Parameters:
`mdEnumerationLiteral` - MagicDraw UML2 model enumeration
Returns:
Eclipse UML2 model enumeration
getEElement
@OpenApiorg.eclipse.uml2_5_0_2.uml.Element getEElement([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement)
Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.
Parameters:
`mdElement` - MagicDraw UML2 model element
Returns:
Eclipse UML2 model element
getEmfHelper
@OpenApi[EmfUml2ExportHelper](../../../helpers/EmfUml2ExportHelper.html) getEmfHelper()
Return MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.
Returns:
helper

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v5.export.convert.feature</a></div>
<h1 class="title" title="Interface EmfUml2ExportFeatureHelper">Interface EmfUml2ExportFeatureHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../helpers/BaseEmfUml2FeatureHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2FeatureHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ExportFeatureHelper</span><span class="extends-implements">
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2_5_0_2.uml.Element</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getEElement</a><wbr/>(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf_2_10_2.common.util.Enumerator</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEEnumeration(javax.jmi.reflect.RefEnum)">getEEnumeration</a><wbr/>(javax.jmi.reflect.RefEnum mdEnumerationLiteral)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Eclipse UML2 model enumeration corresponding to MagicDraw UML2 model enumeration</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2ExportHelper</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEmfHelper()">getEmfHelper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
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
<section class="detail" id="getEEnumeration(javax.jmi.reflect.RefEnum)">
<h3>getEEnumeration</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">org.eclipse.emf_2_10_2.common.util.Enumerator</span> <span class="element-name">getEEnumeration</span><wbr/><span class="parameters">(javax.jmi.reflect.RefEnum mdEnumerationLiteral)</span></div>
<div class="block">Returns Eclipse UML2 model enumeration corresponding to MagicDraw UML2 model enumeration</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdEnumerationLiteral</code> - MagicDraw UML2 model enumeration</dd>
<dt>Returns:</dt>
<dd>Eclipse UML2 model enumeration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getEElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">org.eclipse.uml2_5_0_2.uml.Element</span> <span class="element-name">getEElement</span><wbr/><span class="parameters">(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement)</span></div>
<div class="block">Returns Eclipse UML2 model element corresponding to MagicDraw UML2 model element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdElement</code> - MagicDraw UML2 model element</dd>
<dt>Returns:</dt>
<dd>Eclipse UML2 model element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEmfHelper()">
<h3>getEmfHelper</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../../../helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2ExportHelper</a></span> <span class="element-name">getEmfHelper</span>()</div>
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
