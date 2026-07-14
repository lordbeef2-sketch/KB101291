# JAVA OPENAPI: EmfUml2ExportHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/v4/helpers/EmfUml2ExportHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v4/helpers/EmfUml2ExportHelper.html`
- source_sha256: `7dd941833a634db24b6ddb50b589a3a3745a7b54367c4649a8f767f1d7b61e6b`
- captured_utc: `2026-07-14T16:51:20.116188+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v4.helpers](package-summary.html)

## Interface EmfUml2ExportHelper

All Superinterfaces:
`[BaseEElementNameRetriever](../../helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](../../helpers/BaseEmfUml2Helper.html)`, `[EmfUml2Helper](EmfUml2Helper.html)`, `com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider`

@OpenApipublic interfaceEmfUml2ExportHelperextends [EmfUml2Helper](EmfUml2Helper.html), com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider

MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.

========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2Helper](../../helpers/BaseEmfUml2Helper.html)
`[getEElementName](../../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getLogger](../../helpers/BaseEmfUml2Helper.html#getLogger()), [getProject](../../helpers/BaseEmfUml2Helper.html#getProject()), [isMappedElement](../../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markSkippedElement](../../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.v4.helpers.[EmfUml2Helper](EmfUml2Helper.html)
`[getElementClass](EmfUml2Helper.html#getElementClass()), [getStringPrimitiveType](EmfUml2Helper.html#getStringPrimitiveType()), [getUml2JavaPrimitiveTypesLibrary](EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()), [getUml2MetaModel](EmfUml2Helper.html#getUml2MetaModel()), [getUml2PrimitiveTypesLibrary](EmfUml2Helper.html#getUml2PrimitiveTypesLibrary())`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider
`getInteractionExportHelper`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v4.helpers</a></div>
<h1 class="title" title="Interface EmfUml2ExportHelper">Interface EmfUml2ExportHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="../../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code>, <code><a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2Helper</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ExportHelper</span><span class="extends-implements">
extends <a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2Helper</a>, com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</span></div>
<div class="block">MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></h3>
<code><a href="../../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.v4.helpers.<a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2Helper</a></h3>
<code><a href="EmfUml2Helper.html#getElementClass()">getElementClass</a>, <a href="EmfUml2Helper.html#getStringPrimitiveType()">getStringPrimitiveType</a>, <a href="EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>, <a href="EmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a>, <a href="EmfUml2Helper.html#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</h3>
<code>getInteractionExportHelper</code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
