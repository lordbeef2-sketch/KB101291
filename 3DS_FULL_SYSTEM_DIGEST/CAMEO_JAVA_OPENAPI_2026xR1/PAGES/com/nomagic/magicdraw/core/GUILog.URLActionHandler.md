# JAVA OPENAPI: GUILog.URLActionHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/GUILog.URLActionHandler.html
- source_path: `com/nomagic/magicdraw/core/GUILog.URLActionHandler.html`
- source_sha256: `6b66da5adf585a53ef9cffe18107fcd53f954b987ed1bdddc0475647961b3a7d`
- captured_utc: `2026-07-14T16:45:28.988388+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Interface GUILog.URLActionHandler

All Known Implementing Classes:
`[GUILog.DefaultURLActionHandler](GUILog.DefaultURLActionHandler.html)`

Enclosing class:
`[GUILog](GUILog.html)`

@OpenApiAllpublic static interfaceGUILog.URLActionHandler

An URL handler

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ACTION_URL_PROTOCOL](#ACTION_URL_PROTOCOL)`
Any action protocol
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[openURL](#openURL(java.lang.String,java.awt.event.InputEvent))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [InputEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html) event)`
Opens given url.

============ FIELD DETAIL =========== 
Field Details
ACTION_URL_PROTOCOL
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ACTION_URL_PROTOCOL
Any action protocol
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.GUILog.URLActionHandler.ACTION_URL_PROTOCOL)
 ============ METHOD DETAIL ========== 
Method Details
openURL
boolean openURL([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [InputEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html) event)
Opens given url.
Parameters:
`url` - url
`event` - event
Returns:
true if url was handled, false if not

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Interface GUILog.URLActionHandler">Interface GUILog.URLActionHandler</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="GUILog.DefaultURLActionHandler.html" title="class in com.nomagic.magicdraw.core">GUILog.DefaultURLActionHandler</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">GUILog.URLActionHandler</span></div>
<div class="block">An URL handler</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTION_URL_PROTOCOL">ACTION_URL_PROTOCOL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Any action protocol</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#openURL(java.lang.String,java.awt.event.InputEvent)">openURL</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html" title="class or interface in java.awt.event">InputEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Opens given url.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="ACTION_URL_PROTOCOL">
<h3>ACTION_URL_PROTOCOL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTION_URL_PROTOCOL</span></div>
<div class="block">Any action protocol</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.GUILog.URLActionHandler.ACTION_URL_PROTOCOL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="openURL(java.lang.String,java.awt.event.InputEvent)">
<h3>openURL</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">openURL</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/InputEvent.html" title="class or interface in java.awt.event">InputEvent</a> event)</span></div>
<div class="block">Opens given url.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
<dd><code>event</code> - event</dd>
<dt>Returns:</dt>
<dd>true if url was handled, false if not</dd>
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
