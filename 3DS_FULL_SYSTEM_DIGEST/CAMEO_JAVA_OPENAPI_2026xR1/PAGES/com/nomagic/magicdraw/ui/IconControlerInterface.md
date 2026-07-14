# JAVA OPENAPI: IconControlerInterface (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/IconControlerInterface.html
- source_path: `com/nomagic/magicdraw/ui/IconControlerInterface.html`
- source_sha256: `a2650bb2c159621daaf2c8fb8612638d100c471d7a1851ddfc2c7226063009d7`
- captured_utc: `2026-07-14T16:45:59.108788+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface IconControlerInterface

All Known Implementing Classes:
`[BitmapIconControler](BitmapIconControler.html)`, `[VectorImageIconControler](VectorImageIconControler.html)`

@OpenApiAll
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public interfaceIconControlerInterface

Deprecated.
use [`IconsFactory`](../icons/IconsFactory.html)

Describe interface for managing icon.
 Responsible for creating IconInterface

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[createIcon](#createIcon())()`
Deprecated.
Creates icon by given class file and path
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getIconPath](#getIconPath())()`
Deprecated.
Returns full icon name.

============ METHOD DETAIL ========== 
Method Details
createIcon
[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) createIcon()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated.
Creates icon by given class file and path
Returns:
Loaded image file
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
getIconPath
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getIconPath()
Deprecated.
Returns full icon name.
Returns:
icon image directory.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface IconControlerInterface">Interface IconControlerInterface</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="BitmapIconControler.html" title="class in com.nomagic.magicdraw.ui">BitmapIconControler</a></code>, <code><a href="VectorImageIconControler.html" title="class in com.nomagic.magicdraw.ui">VectorImageIconControler</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IconControlerInterface</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../icons/IconsFactory.html" title="class in com.nomagic.magicdraw.icons"><code>IconsFactory</code></a></div>
</div>
<div class="block">Describe interface for managing icon.
 Responsible for creating IconInterface</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#createIcon()">createIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates icon by given class file and path</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getIconPath()">getIconPath</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns full icon name.</div>
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
<section class="detail" id="createIcon()">
<h3>createIcon</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">createIcon</span>()
         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates icon by given class file and path</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Loaded image file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconPath()">
<h3>getIconPath</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIconPath</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns full icon name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>icon image directory.</dd>
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
