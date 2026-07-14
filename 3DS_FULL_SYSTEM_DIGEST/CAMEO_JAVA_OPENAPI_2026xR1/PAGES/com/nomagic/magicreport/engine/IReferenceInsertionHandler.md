# JAVA OPENAPI: IReferenceInsertionHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/IReferenceInsertionHandler.html
- source_path: `com/nomagic/magicreport/engine/IReferenceInsertionHandler.html`
- source_sha256: `29e7b784fd158ced38ca4bb19b3945bb482db0b425084d654bfe96182845098c`
- captured_utc: `2026-07-14T16:46:11.877959+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface IReferenceInsertionHandler

All Known Implementing Classes:
`[InsertionHandler](velocity/InsertionHandler.html)`

@OpenApiAllpublic interfaceIReferenceInsertionHandler

Reference 'Stream insertion' event handler. Called with object that will be inserted into stream via
 value.toString().

Since:
February 13, 2008

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[referenceInsert](#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
A call-back which is executed during template merge before a reference value is inserted into the output
 stream.

============ METHOD DETAIL ========== 
Method Details
referenceInsert
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) referenceInsert([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
A call-back which is executed during template merge before a reference value is inserted into the output
 stream. All registered IReferenceInsertionHandler are called in sequence. If no IReferenceInsertionHandler
 are are registered then reference value is inserted into the output stream as is.
Parameters:
`reference` - Reference from template about to be inserted.
`value` - Value about to be inserted (after its `toString()` method is called).
`properties` - the engine properties
Returns:
Object on which `toString()` should be called for output.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface IReferenceInsertionHandler">Interface IReferenceInsertionHandler</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="velocity/InsertionHandler.html" title="class in com.nomagic.magicreport.engine.velocity">InsertionHandler</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IReferenceInsertionHandler</span></div>
<div class="block">Reference 'Stream insertion' event handler. Called with object that will be inserted into stream via
 value.toString().</div>
<dl class="notes">
<dt>Since:</dt>
<dd>February 13, 2008</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#referenceInsert(java.lang.String,java.lang.Object,java.util.Properties)">referenceInsert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A call-back which is executed during template merge before a reference value is inserted into the output
 stream.</div>
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
<section class="detail" id="referenceInsert(java.lang.String,java.lang.Object,java.util.Properties)">
<h3>referenceInsert</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">referenceInsert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">A call-back which is executed during template merge before a reference value is inserted into the output
 stream. All registered IReferenceInsertionHandler are called in sequence. If no IReferenceInsertionHandler
 are are registered then reference value is inserted into the output stream as is.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - Reference from template about to be inserted.</dd>
<dd><code>value</code> - Value about to be inserted (after its <code>toString()</code> method is called).</dd>
<dd><code>properties</code> - the engine properties</dd>
<dt>Returns:</dt>
<dd>Object on which <code>toString()</code> should be called for output.</dd>
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
