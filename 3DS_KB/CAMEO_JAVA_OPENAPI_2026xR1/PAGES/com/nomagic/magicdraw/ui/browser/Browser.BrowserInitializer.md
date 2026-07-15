# JAVA OPENAPI: Browser.BrowserInitializer (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/browser/Browser.BrowserInitializer.html
- source_path: `com/nomagic/magicdraw/ui/browser/Browser.BrowserInitializer.html`
- source_sha256: `de1de28b74c8e7e8492e91d0316e8d8389089878189cd73ebaf1587869418a71`
- captured_utc: `2026-07-14T16:46:00.619809+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Interface Browser.BrowserInitializer

Enclosing class:
`[Browser](Browser.html)`

@OpenApiAllpublic static interfaceBrowser.BrowserInitializer

Browser initializer is an extension point for browser creation. It may be used for adding new trees of panels into the browser.
 It can be used for removing existing trees also. In such case initializer should return null as WindowComponentInfoRegistration.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static class`
`[Browser.BrowserInitializer.WindowComponentInfoRegistration](Browser.BrowserInitializer.WindowComponentInfoRegistration.html)`
Info registration data.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Browser.BrowserInitializer.WindowComponentInfoRegistration](Browser.BrowserInitializer.WindowComponentInfoRegistration.html)`
`[getInfo](#getInfo())()`
Provide info for a new browser tree.
`void`
`[init](#init(com.nomagic.magicdraw.ui.browser.Browser,com.nomagic.magicdraw.core.Project))([Browser](Browser.html) browser,
 [Project](../../core/Project.html) project)`
Init the browser.

============ METHOD DETAIL ========== 
Method Details
init
void init([Browser](Browser.html) browser,
 [Project](../../core/Project.html) project)
Init the browser. This method will be called during browser initialization. Implemented classes may add additional
 trees or panels into the browser using Browser.addTree() or Browser.addPanel(). Existing trees can be removed in this method also
Parameters:
`browser` - the given browser
`project` - current project
getInfo
@CheckForNull[Browser.BrowserInitializer.WindowComponentInfoRegistration](Browser.BrowserInitializer.WindowComponentInfoRegistration.html) getInfo()
Provide info for a new browser tree. This method is called during application startup and supposes return the same info
 as used during tree creation in let's say init() method.
Returns:
browser component info or null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Interface Browser.BrowserInitializer">Interface Browser.BrowserInitializer</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">Browser.BrowserInitializer</span></div>
<div class="block">Browser initializer is an extension point for browser creation. It may be used for adding new trees of panels into the browser.
 It can be used for removing existing trees also. In such case initializer should return null as WindowComponentInfoRegistration.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Browser.BrowserInitializer.WindowComponentInfoRegistration.html" title="class in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer.WindowComponentInfoRegistration</a></code></div>
<div class="col-last even-row-color">
<div class="block">Info registration data.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Browser.BrowserInitializer.WindowComponentInfoRegistration.html" title="class in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer.WindowComponentInfoRegistration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInfo()">getInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Provide info for a new browser tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.ui.browser.Browser,com.nomagic.magicdraw.core.Project)">init</a><wbr/>(<a href="Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a> browser,
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Init the browser.</div>
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
<section class="detail" id="init(com.nomagic.magicdraw.ui.browser.Browser,com.nomagic.magicdraw.core.Project)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a> browser,
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Init the browser. This method will be called during browser initialization. Implemented classes may add additional
 trees or panels into the browser using Browser.addTree() or Browser.addPanel(). Existing trees can be removed in this method also</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>browser</code> - the given browser</dd>
<dd><code>project</code> - current project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInfo()">
<h3>getInfo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Browser.BrowserInitializer.WindowComponentInfoRegistration.html" title="class in com.nomagic.magicdraw.ui.browser">Browser.BrowserInitializer.WindowComponentInfoRegistration</a></span> <span class="element-name">getInfo</span>()</div>
<div class="block">Provide info for a new browser tree. This method is called during application startup and supposes return the same info
 as used during tree creation in let's say init() method.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>browser component info or null</dd>
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
