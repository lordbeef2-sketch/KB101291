# JAVA OPENAPI: LicensedPlugin (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/plugins/LicensedPlugin.html
- source_path: `com/nomagic/magicdraw/plugins/LicensedPlugin.html`
- source_sha256: `062e5092372498a51580dda8426957a2d407b2e95f8087202f783aea0a08a442`
- captured_utc: `2026-07-14T16:58:00.237560+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.plugins](package-summary.html)

## Interface LicensedPlugin

@OpenApiAllpublic interfaceLicensedPlugin
Licensed (commercial) plugin

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getActivationInstructions](#getActivationInstructions())()`
Returns plugin activation instructions
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getBuildInfo](#getBuildInfo())()`
Returns build info for plugin.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEULA](#getEULA())()`
Returns End User License Agreement text
`boolean`
`[isReaderMode](#isReaderMode())()`
Checks if plugin is in reader mode.
`void`
`[setReaderMode](#setReaderMode(boolean))(boolean reader)`
Sets reader mode for plugin

============ METHOD DETAIL ========== 
Method Details
setReaderMode
void setReaderMode(boolean reader)
Sets reader mode for plugin
Parameters:
`reader` - true if reader, otherwise false.
isReaderMode
boolean isReaderMode()
Checks if plugin is in reader mode.
Returns:
true if plugin works in reader mode. No editing should be allowed.
getEULA
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEULA()
Returns End User License Agreement text
Returns:
EULA text
getActivationInstructions
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getActivationInstructions()
Returns plugin activation instructions
Returns:
instructions HTML text
getBuildInfo
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getBuildInfo()
Returns build info for plugin. Can return null if such information is not available.
Returns:
build info.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.plugins</a></div>
<h1 class="title" title="Interface LicensedPlugin">Interface LicensedPlugin</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">LicensedPlugin</span></div>
<div class="block">Licensed (commercial) plugin</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActivationInstructions()">getActivationInstructions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns plugin activation instructions</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBuildInfo()">getBuildInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns build info for plugin.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEULA()">getEULA</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns End User License Agreement text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isReaderMode()">isReaderMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if plugin is in reader mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReaderMode(boolean)">setReaderMode</a><wbr/>(boolean reader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets reader mode for plugin</div>
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
<section class="detail" id="setReaderMode(boolean)">
<h3>setReaderMode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReaderMode</span><wbr/><span class="parameters">(boolean reader)</span></div>
<div class="block">Sets reader mode for plugin</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reader</code> - true if reader, otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReaderMode()">
<h3>isReaderMode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isReaderMode</span>()</div>
<div class="block">Checks if plugin is in reader mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if plugin works in reader mode. No editing should be allowed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEULA()">
<h3>getEULA</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEULA</span>()</div>
<div class="block">Returns End User License Agreement text</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>EULA text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivationInstructions()">
<h3>getActivationInstructions</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getActivationInstructions</span>()</div>
<div class="block">Returns plugin activation instructions</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instructions HTML text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBuildInfo()">
<h3>getBuildInfo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBuildInfo</span>()</div>
<div class="block">Returns build info for plugin. Can return null if such information is not available.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>build info.</dd>
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
