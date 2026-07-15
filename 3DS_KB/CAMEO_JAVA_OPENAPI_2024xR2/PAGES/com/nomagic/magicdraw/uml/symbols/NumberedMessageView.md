# JAVA OPENAPI: NumberedMessageView (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/symbols/NumberedMessageView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/NumberedMessageView.html`
- source_sha256: `e69e67fea789f856512bfa70de38f2298a183c401bd40904d8379c5b4a4790bd`
- captured_utc: `2026-07-14T16:55:54.848451+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Interface NumberedMessageView

All Known Implementing Classes:
`[FoundMessageView](paths/FoundMessageView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView`, `[LostMessageView](paths/LostMessageView.html)`, `[MessageView](shapes/MessageView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView`, `[SeqMessageView](paths/SeqMessageView.html)`, `[SeqSelfMessageView](paths/SeqSelfMessageView.html)`

@OpenApiAllpublic interfaceNumberedMessageView

The numbered message is message which can have its number.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getMessage](#getMessage())()`
Message represented by the view.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNumber](#getNumber())()`
Returns number of the message

============ METHOD DETAIL ========== 
Method Details
getMessage
[Message](../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) getMessage()
Message represented by the view.
Returns:
message represented by the view
getNumber
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNumber()
Returns number of the message
Returns:
nested number of the message

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Interface NumberedMessageView">Interface NumberedMessageView</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="paths/FoundMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">FoundMessageView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.LostFoundMessageView</code>, <code><a href="paths/LostMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LostMessageView</a></code>, <code><a href="shapes/MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView</code>, <code><a href="paths/SeqMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqMessageView</a></code>, <code><a href="paths/SeqSelfMessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">SeqSelfMessageView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">NumberedMessageView</span></div>
<div class="block">The numbered message is message which can have its number.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMessage()">getMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Message represented by the view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNumber()">getNumber</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns number of the message</div>
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
<section class="detail" id="getMessage()">
<h3>getMessage</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getMessage</span>()</div>
<div class="block">Message represented by the view.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>message represented by the view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumber()">
<h3>getNumber</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNumber</span>()</div>
<div class="block">Returns number of the message</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>nested number of the message</dd>
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
