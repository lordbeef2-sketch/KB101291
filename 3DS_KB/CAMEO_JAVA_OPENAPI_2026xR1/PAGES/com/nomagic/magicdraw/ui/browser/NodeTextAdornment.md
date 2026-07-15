# JAVA OPENAPI: NodeTextAdornment (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/browser/NodeTextAdornment.html
- source_path: `com/nomagic/magicdraw/ui/browser/NodeTextAdornment.html`
- source_sha256: `87c91699f5d894d5549b93b8109a284b574d54a41eb2f32498cb5f670572da2f`
- captured_utc: `2026-07-14T16:46:00.762810+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Interface NodeTextAdornment

@OpenApiAllpublic interfaceNodeTextAdornment

An adornment of the browser tree node text. It can be used when the same element is displayed by different nodes,
 and they need different texts to be displayed. Element text is displayed using [`TextAdornment`](TextAdornment.html).

See Also:
[`TreeNodeAdornmentManager`](TreeNodeAdornmentManager.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[adorn](#adorn(java.lang.String,com.nomagic.magicdraw.ui.browser.Node))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [Node](Node.html) node)`
Adorn given text.

============ METHOD DETAIL ========== 
Method Details
adorn
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) adorn([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 [Node](Node.html) node)
Adorn given text.
Parameters:
`text` - text to adorn
`node` - node that is displayed
Returns:
adorned text

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Interface NodeTextAdornment">Interface NodeTextAdornment</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">NodeTextAdornment</span></div>
<div class="block">An adornment of the browser tree node text. It can be used when the same element is displayed by different nodes,
 and they need different texts to be displayed. Element text is displayed using <a href="TextAdornment.html" title="interface in com.nomagic.magicdraw.ui.browser"><code>TextAdornment</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="TreeNodeAdornmentManager.html" title="class in com.nomagic.magicdraw.ui.browser"><code>TreeNodeAdornmentManager</code></a></li>
</ul>
</dd>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#adorn(java.lang.String,com.nomagic.magicdraw.ui.browser.Node)">adorn</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adorn given text.</div>
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
<section class="detail" id="adorn(java.lang.String,com.nomagic.magicdraw.ui.browser.Node)">
<h3>adorn</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">adorn</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</span></div>
<div class="block">Adorn given text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to adorn</dd>
<dd><code>node</code> - node that is displayed</dd>
<dt>Returns:</dt>
<dd>adorned text</dd>
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
