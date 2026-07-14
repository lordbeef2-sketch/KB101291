# JAVA OPENAPI: FileLocationRegister (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/FileLocationRegister.html
- source_path: `com/nomagic/magicdraw/core/FileLocationRegister.html`
- source_sha256: `72f580b0e3a3dc2651bfe4cdbdd4d1ee921b806e708049daf50c49bf0a4fdbf8`
- captured_utc: `2026-07-14T16:45:28.919388+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Interface FileLocationRegister

All Known Implementing Classes:
`[EnvironmentSpecificFileLocations](EnvironmentSpecificFileLocations.html)`, `[ProjectSpecificLocationRegister](ProjectSpecificLocationRegister.html)`

@OpenApiAllpublic interfaceFileLocationRegister

This interface is used in [`EnvironmentSpecificFileLocations`](EnvironmentSpecificFileLocations.html) and [`ProjectSpecificLocationRegister`](ProjectSpecificLocationRegister.html)
 to manipulate with file locations storing places
 Implement this interface if you need to create new file locations saving type.

See Also:
[`EnvironmentSpecificFileLocations`](EnvironmentSpecificFileLocations.html)
[`ProjectSpecificLocationRegister`](ProjectSpecificLocationRegister.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getFileLocation](#getFileLocation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locationNameID)`
This method should be used to get file object by locationNameID.
`void`
`[setFileLocation](#setFileLocation(java.lang.String,java.io.File))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locationNameID,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
This method should be used to save file by locationNameID.

============ METHOD DETAIL ========== 
Method Details
getFileLocation
[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getFileLocation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locationNameID)
This method should be used to get file object by locationNameID.
Parameters:
`locationNameID` - a unique id for storing/getting file locations.
Returns:
File type object.
setFileLocation
void setFileLocation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) locationNameID,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
This method should be used to save file by locationNameID.
Parameters:
`locationNameID` - a unique id for storing/getting file locations.
`file` - type object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Interface FileLocationRegister">Interface FileLocationRegister</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="EnvironmentSpecificFileLocations.html" title="class in com.nomagic.magicdraw.core">EnvironmentSpecificFileLocations</a></code>, <code><a href="ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core">ProjectSpecificLocationRegister</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">FileLocationRegister</span></div>
<div class="block">This interface is used in <a href="EnvironmentSpecificFileLocations.html" title="class in com.nomagic.magicdraw.core"><code>EnvironmentSpecificFileLocations</code></a> and <a href="ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a>
 to manipulate with file locations storing places
 Implement this interface if you need to create new file locations saving type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="EnvironmentSpecificFileLocations.html" title="class in com.nomagic.magicdraw.core"><code>EnvironmentSpecificFileLocations</code></a></li>
<li><a href="ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core"><code>ProjectSpecificLocationRegister</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFileLocation(java.lang.String)">getFileLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method should be used to get file object by locationNameID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFileLocation(java.lang.String,java.io.File)">setFileLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method should be used to save file by locationNameID.</div>
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
<section class="detail" id="getFileLocation(java.lang.String)">
<h3>getFileLocation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getFileLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID)</span></div>
<div class="block">This method should be used to get file object by locationNameID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationNameID</code> - a unique id for storing/getting file locations.</dd>
<dt>Returns:</dt>
<dd>File type object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFileLocation(java.lang.String,java.io.File)">
<h3>setFileLocation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFileLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">This method should be used to save file by locationNameID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationNameID</code> - a unique id for storing/getting file locations.</dd>
<dd><code>file</code> - type object</dd>
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
