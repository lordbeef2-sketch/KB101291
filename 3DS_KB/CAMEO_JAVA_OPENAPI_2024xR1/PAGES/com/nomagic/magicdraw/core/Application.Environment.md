# JAVA OPENAPI: Application.Environment (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/Application.Environment.html
- source_path: `com/nomagic/magicdraw/core/Application.Environment.html`
- source_sha256: `fe25ed223e3378489c86ba2d43f6f84ac34dda47797710eeff415246f9932a20`
- captured_utc: `2026-07-14T16:51:13.348098+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class Application.Environment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.Application.Environment

Enclosing class:
[Application](Application.html)

@OpenApiAllpublic static classApplication.Environment
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Contains application environment specific constants and utility methods.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Environment](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getConfigDir](#getConfigDir())()`
Returns directory where configuration files for each user are stored.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDataDirectory](#getDataDirectory())()`
Returns install root directory + data folder.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getDefaultsDataDirectory](#getDefaultsDataDirectory())()`
Directory in installation root where defaults are saved (custom diagrams, user modes etc.).
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getExamplesDirectory](#getExamplesDirectory())()`
Gets directory of examples.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getInstallRoot](#getInstallRoot())()`
Gets application installation root.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModelLibrariesDirectory](#getModelLibrariesDirectory())()`
Gets directory of modelLibraries.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProfilesDirectory](#getProfilesDirectory())()`
Gets directory of profiles.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceDirectory](#getResourceDirectory())()`
Returns directory of resources.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getTempDir](#getTempDir(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Gets a temp directory which is unique for this application instance.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTemplatesDirectory](#getTemplatesDirectory())()`
Returns install root directory + templates folder.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getUserDataDirectory](#getUserDataDirectory())()`
Directory in user home where config files are saved (custom diagrams, user modes etc.).
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUserHomeDirectory](#getUserHomeDirectory())()`
Returns user home directory.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Environment
public Environment()
 ============ METHOD DETAIL ========== 
Method Details
getDataDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDataDirectory()
Returns install root directory + data folder.
Returns:
the data folder.
getInstallRoot
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getInstallRoot()
Gets application installation root.
Returns:
application installation root.
getConfigDir
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getConfigDir()
Returns directory where configuration files for each user are stored. Creates config dirs if missing.
Returns:
path to configuration directory.
getTemplatesDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTemplatesDirectory()
Returns install root directory + templates folder.
Returns:
templates directory.
getUserHomeDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUserHomeDirectory()
Returns user home directory.
Returns:
user home directory.
getExamplesDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getExamplesDirectory()
Gets directory of examples.
Returns:
examples directory.
getProfilesDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProfilesDirectory()
Gets directory of profiles.
Returns:
profiles directory.
getModelLibrariesDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModelLibrariesDirectory()
Gets directory of modelLibraries.
Returns:
libraries directory
getResourceDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceDirectory()
Returns directory of resources.
Returns:
resources directory.
getDefaultsDataDirectory
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getDefaultsDataDirectory()
Directory in installation root where defaults are saved (custom diagrams, user modes etc.).
Returns:
defaults data directory.
getUserDataDirectory
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getUserDataDirectory()
Directory in user home where config files are saved (custom diagrams, user modes etc.).
Returns:
user data directory.
getTempDir
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getTempDir(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Gets a temp directory which is unique for this application instance.
Parameters:
`path` - path in the temp folder. Returns temp folder root if path is empty.
Returns:
application unique temporary folder.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class Application.Environment">Class Application.Environment</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.Application.Environment</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="Application.html" title="class in com.nomagic.magicdraw.core">Application</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">Application.Environment</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains application environment specific constants and utility methods.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Environment</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfigDir()">getConfigDir</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns directory where configuration files for each user are stored.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDataDirectory()">getDataDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns install root directory + data folder.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultsDataDirectory()">getDefaultsDataDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Directory in installation root where defaults are saved (custom diagrams, user modes etc.).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExamplesDirectory()">getExamplesDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets directory of examples.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstallRoot()">getInstallRoot</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets application installation root.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelLibrariesDirectory()">getModelLibrariesDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets directory of modelLibraries.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfilesDirectory()">getProfilesDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets directory of profiles.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceDirectory()">getResourceDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns directory of resources.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTempDir(java.lang.String)">getTempDir</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a temp directory which is unique for this application instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplatesDirectory()">getTemplatesDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns install root directory + templates folder.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserDataDirectory()">getUserDataDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Directory in user home where config files are saved (custom diagrams, user modes etc.).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserHomeDirectory()">getUserHomeDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns user home directory.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Environment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Environment</span>()</div>
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
<section class="detail" id="getDataDirectory()">
<h3>getDataDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDataDirectory</span>()</div>
<div class="block">Returns install root directory + data folder.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the data folder.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstallRoot()">
<h3>getInstallRoot</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getInstallRoot</span>()</div>
<div class="block">Gets application installation root.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application installation root.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfigDir()">
<h3>getConfigDir</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getConfigDir</span>()</div>
<div class="block">Returns directory where configuration files for each user are stored. Creates config dirs if missing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>path to configuration directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplatesDirectory()">
<h3>getTemplatesDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTemplatesDirectory</span>()</div>
<div class="block">Returns install root directory + templates folder.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>templates directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserHomeDirectory()">
<h3>getUserHomeDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUserHomeDirectory</span>()</div>
<div class="block">Returns user home directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user home directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExamplesDirectory()">
<h3>getExamplesDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExamplesDirectory</span>()</div>
<div class="block">Gets directory of examples.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>examples directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfilesDirectory()">
<h3>getProfilesDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProfilesDirectory</span>()</div>
<div class="block">Gets directory of profiles.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>profiles directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelLibrariesDirectory()">
<h3>getModelLibrariesDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModelLibrariesDirectory</span>()</div>
<div class="block">Gets directory of modelLibraries.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>libraries directory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceDirectory()">
<h3>getResourceDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceDirectory</span>()</div>
<div class="block">Returns directory of resources.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>resources directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultsDataDirectory()">
<h3>getDefaultsDataDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getDefaultsDataDirectory</span>()</div>
<div class="block">Directory in installation root where defaults are saved (custom diagrams, user modes etc.).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>defaults data directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserDataDirectory()">
<h3>getUserDataDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getUserDataDirectory</span>()</div>
<div class="block">Directory in user home where config files are saved (custom diagrams, user modes etc.).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user data directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTempDir(java.lang.String)">
<h3>getTempDir</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTempDir</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Gets a temp directory which is unique for this application instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path in the temp folder. Returns temp folder root if path is empty.</dd>
<dt>Returns:</dt>
<dd>application unique temporary folder.</dd>
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
