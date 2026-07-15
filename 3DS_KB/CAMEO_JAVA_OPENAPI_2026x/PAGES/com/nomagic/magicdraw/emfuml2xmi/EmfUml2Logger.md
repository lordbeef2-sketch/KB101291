# JAVA OPENAPI: EmfUml2Logger (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emfuml2xmi/EmfUml2Logger.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/EmfUml2Logger.html`
- source_sha256: `29dae54dfe205a22bab353ae7a324d94ddf1d4dc8b533f22aab94b23f1de6007`
- captured_utc: `2026-07-14T16:57:55.881511+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi](package-summary.html)

## Interface EmfUml2Logger

@OpenApiAllpublic interfaceEmfUml2Logger
Eclipse UML2 XMI logger

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[error](#error(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) throwable)`
Error message.
`void`
`[log](#log(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Simple log message.
`void`
`[warn](#warn(java.lang.String,com.nomagic.magicdraw.emfuml2xmi.Link%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pattern,
 com.nomagic.magicdraw.emfuml2xmi.Link[] links)`
Logs warning.

============ METHOD DETAIL ========== 
Method Details
warn
void warn([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pattern,
 com.nomagic.magicdraw.emfuml2xmi.Link[] links)
Logs warning.
Parameters:
`pattern` - warning pattern.
`links` - links.
log
void log([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Simple log message.
Parameters:
`message` - message.
error
void error([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) throwable)
Error message.
Parameters:
`message` - message.
`throwable` - exception.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi</a></div>
<h1 class="title" title="Interface EmfUml2Logger">Interface EmfUml2Logger</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2Logger</span></div>
<div class="block">Eclipse UML2 XMI logger</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#error(java.lang.String,java.lang.Throwable)">error</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Error message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#log(java.lang.String)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Simple log message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#warn(java.lang.String,com.nomagic.magicdraw.emfuml2xmi.Link%5B%5D)">warn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 com.nomagic.magicdraw.emfuml2xmi.Link[] links)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Logs warning.</div>
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
<section class="detail" id="warn(java.lang.String,com.nomagic.magicdraw.emfuml2xmi.Link[])">
<h3>warn</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">warn</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 com.nomagic.magicdraw.emfuml2xmi.Link[] links)</span></div>
<div class="block">Logs warning.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pattern</code> - warning pattern.</dd>
<dd><code>links</code> - links.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String)">
<h3>log</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Simple log message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="error(java.lang.String,java.lang.Throwable)">
<h3>error</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">error</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Error message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message.</dd>
<dd><code>throwable</code> - exception.</dd>
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
