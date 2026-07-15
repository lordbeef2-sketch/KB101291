# JAVA OPENAPI: ErrorHandler (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/utils/ErrorHandler.html
- source_path: `com/nomagic/utils/ErrorHandler.html`
- source_sha256: `273ebfb8632686901ecf18c6eab72d19b920a2fe6405c5b1595ff648c251d228`
- captured_utc: `2026-07-14T16:56:40.893966+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Interface ErrorHandler<T extends [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)>

Type Parameters:
`T` - type of exception

@OpenApiAllpublic interfaceErrorHandler<T extends [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)>

General purpose exception handler. Handler is used in components which has no ability to decide how to handle errors.
 Handler may ignore, log exception or re throw it or do anything else.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[error](#error(T))([T](ErrorHandler.html) e)`
Handles exception.

============ METHOD DETAIL ========== 
Method Details
error
void error([T](ErrorHandler.html) e)
 throws [T](ErrorHandler.html)
Handles exception.
Parameters:
`e` - occurred exception.
Throws:
`[T](ErrorHandler.html)` - in case this handler does not handles error.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Interface ErrorHandler">Interface ErrorHandler&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type of exception</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ErrorHandler&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt;</span></div>
<div class="block">General purpose exception handler. Handler is used in components which has no ability to decide how to handle errors.
 Handler may ignore, log exception or re throw it or do anything else.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#error(T)">error</a><wbr/>(<a href="ErrorHandler.html" title="type parameter in ErrorHandler">T</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handles exception.</div>
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
<section class="detail" id="error(T)">
<h3 id="error(java.lang.Exception)">error</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">error</span><wbr/><span class="parameters">(<a href="ErrorHandler.html" title="type parameter in ErrorHandler">T</a> e)</span>
    throws <span class="exceptions"><a href="ErrorHandler.html" title="type parameter in ErrorHandler">T</a></span></div>
<div class="block">Handles exception.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - occurred exception.</dd>
<dt>Throws:</dt>
<dd><code><a href="ErrorHandler.html" title="type parameter in ErrorHandler">T</a></code> - in case this handler does not handles error.</dd>
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
