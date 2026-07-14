# JAVA OPENAPI: DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator.html
- source_path: `com/nomagic/magicdraw/uml2/DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator.html`
- source_sha256: `710af5365c4955663484ee7c6e80dde259d656d7dbbaf96a026516e0e09022be`
- captured_utc: `2026-07-14T16:52:16.292938+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Interface DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator

Enclosing class:
[DocumentationCommentProviderConfigurator](DocumentationCommentProviderConfigurator.html)

public static interfaceDocumentationCommentProviderConfigurator.DocumentationCommentConfigurator

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[configureDocumentation](#configureDocumentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner,
 [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)`

`[Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)>`
`[getDocumentationCommentProvider](#getDocumentationCommentProvider())()`

============ METHOD DETAIL ========== 
Method Details
getDocumentationCommentProvider
[Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)> getDocumentationCommentProvider()
configureDocumentation
void configureDocumentation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner,
 [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) comment)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Interface DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator">Interface DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="DocumentationCommentProviderConfigurator.html" title="class in com.nomagic.magicdraw.uml2">DocumentationCommentProviderConfigurator</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">DocumentationCommentProviderConfigurator.DocumentationCommentConfigurator</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configureDocumentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">configureDocumentation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDocumentationCommentProvider()">getDocumentationCommentProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getDocumentationCommentProvider()">
<h3>getDocumentationCommentProvider</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a>&gt;</span> <span class="element-name">getDocumentationCommentProvider</span>()</div>
</section>
</li>
<li>
<section class="detail" id="configureDocumentation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">
<h3>configureDocumentation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configureDocumentation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> comment)</span></div>
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
