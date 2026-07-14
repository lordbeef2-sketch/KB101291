# JAVA OPENAPI: IObserverMessage (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/IObserverMessage.html
- source_path: `com/nomagic/magicreport/engine/IObserverMessage.html`
- source_sha256: `265e3030cddb3d8d0494c0e1404cd2f998208151315872c519fc4f46ca388688`
- captured_utc: `2026-07-14T16:46:11.806958+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface IObserverMessage

All Superinterfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

All Known Implementing Classes:
`[Image](../Image.html)`, `[ObserverMessageWrapper](ObserverMessageWrapper.html)`, `[ODFTemplate](../ODFTemplate.html)`, `[OOXMLTemplate](../OOXMLTemplate.html)`, `[ReportSVGIcon](../ReportSVGIcon.html)`, `[SVGIcon](../SVGIcon.html)`, `[Template](../Template.html)`

@OpenApiAllpublic interfaceIObserverMessageextends [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

A `ObserverMessage` provides the way for a `Observable` processor to report name, and
 other notices.

Since:
Sep 21, 2007

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Return name of this object.

============ METHOD DETAIL ========== 
Method Details
getName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Return name of this object.
Returns:
name of this object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface IObserverMessage">Interface IObserverMessage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../Image.html" title="class in com.nomagic.magicreport">Image</a></code>, <code><a href="ObserverMessageWrapper.html" title="class in com.nomagic.magicreport.engine">ObserverMessageWrapper</a></code>, <code><a href="../ODFTemplate.html" title="class in com.nomagic.magicreport">ODFTemplate</a></code>, <code><a href="../OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a></code>, <code><a href="../ReportSVGIcon.html" title="class in com.nomagic.magicreport">ReportSVGIcon</a></code>, <code><a href="../SVGIcon.html" title="class in com.nomagic.magicreport">SVGIcon</a></code>, <code><a href="../Template.html" title="class in com.nomagic.magicreport">Template</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IObserverMessage</span><span class="extends-implements">
extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">A <code>ObserverMessage</code> provides the way for a <code>Observable</code> processor to report name, and
 other notices.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 21, 2007</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return name of this object.</div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Return name of this object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of this object</dd>
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
