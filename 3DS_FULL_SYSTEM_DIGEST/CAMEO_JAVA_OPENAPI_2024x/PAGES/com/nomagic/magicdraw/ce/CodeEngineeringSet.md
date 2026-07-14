# JAVA OPENAPI: CodeEngineeringSet (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ce/CodeEngineeringSet.html
- source_path: `com/nomagic/magicdraw/ce/CodeEngineeringSet.html`
- source_sha256: `229f17a27a5cfbc43dc5be15075c0bc17f72f7358137f7bb595831b1e718578d`
- captured_utc: `2026-07-14T16:51:12.324086+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ce](package-summary.html)

## Interface CodeEngineeringSet

@OpenApiAllpublic interfaceCodeEngineeringSet
Code Engineering Set object.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addAllFilesRecursivelyToCES](#addAllFilesRecursivelyToCES(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) pathDirectory)`
Given a path to directory, adds all directory files recursively to code engineering set.
`void`
`[addElementsToCodeEngineeringSet](#addElementsToCodeEngineeringSet(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)> modelElements)`
Adds list of model elements to code engineering set.
`void`
`[addFilesToCodeEngineeringSet](#addFilesToCodeEngineeringSet(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> file)`
Adds given list of files to code engineering set.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)>`
`[getAllModelElements](#getAllModelElements())()`
Returns all model elements that are in code engineering set.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDialect](#getDialect())()`
Dialect of code engineering set language.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLanguage](#getLanguage())()`
Language of Code Engineering Set.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns name of code engineering set.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getWorkingDirectory](#getWorkingDirectory())()`
Returns working directory of ces.
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getWorkingPackage](#getWorkingPackage())()`
Returns working package of code engineering set.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Sets name of code engineering set.

============ METHOD DETAIL ========== 
Method Details
getWorkingDirectory
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getWorkingDirectory()
Returns working directory of ces.
Returns:
working directory.
addElementsToCodeEngineeringSet
void addElementsToCodeEngineeringSet([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)> modelElements)
Adds list of model elements to code engineering set. Dedicated for forward engineering.
Parameters:
`modelElements` - list of modelElements
addFilesToCodeEngineeringSet
void addFilesToCodeEngineeringSet([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> file)
Adds given list of files to code engineering set. Dedicated for reverse engineering.
Parameters:
`file` - list of files.
addAllFilesRecursivelyToCES
void addAllFilesRecursivelyToCES([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) pathDirectory)
Given a path to directory, adds all directory files recursively to code engineering set.
Parameters:
`pathDirectory` - path to root directory.
getAllModelElements
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[BaseElement](../uml/BaseElement.html)> getAllModelElements()
Returns all model elements that are in code engineering set.
Returns:
List of model elements.
setName
void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Sets name of code engineering set.
Parameters:
`name` - new name of code engineering set.
getName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns name of code engineering set.
Returns:
name of ces.
getWorkingPackage
[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getWorkingPackage()
Returns working package of code engineering set. All model elements added to code engineering
 set should be under working package.
Returns:
package in project, which is working package of code engineering set.
getLanguage
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLanguage()
Language of Code Engineering Set.
Returns:
language.
getDialect
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDialect()
Dialect of code engineering set language.
Returns:
language dialect.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ce</a></div>
<h1 class="title" title="Interface CodeEngineeringSet">Interface CodeEngineeringSet</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">CodeEngineeringSet</span></div>
<div class="block">Code Engineering Set object.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addAllFilesRecursivelyToCES(java.io.File)">addAllFilesRecursivelyToCES</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> pathDirectory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Given a path to directory, adds all directory files recursively to code engineering set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addElementsToCodeEngineeringSet(java.util.List)">addElementsToCodeEngineeringSet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; modelElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds list of model elements to code engineering set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFilesToCodeEngineeringSet(java.util.List)">addFilesToCodeEngineeringSet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds given list of files to code engineering set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAllModelElements()">getAllModelElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all model elements that are in code engineering set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDialect()">getDialect</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Dialect of code engineering set language.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLanguage()">getLanguage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Language of Code Engineering Set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns name of code engineering set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWorkingDirectory()">getWorkingDirectory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns working directory of ces.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWorkingPackage()">getWorkingPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns working package of code engineering set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets name of code engineering set.</div>
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
<section class="detail" id="getWorkingDirectory()">
<h3>getWorkingDirectory</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getWorkingDirectory</span>()</div>
<div class="block">Returns working directory of ces.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>working directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addElementsToCodeEngineeringSet(java.util.List)">
<h3>addElementsToCodeEngineeringSet</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addElementsToCodeEngineeringSet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; modelElements)</span></div>
<div class="block">Adds list of model elements to code engineering set. Dedicated for forward engineering.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelElements</code> - list of modelElements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFilesToCodeEngineeringSet(java.util.List)">
<h3>addFilesToCodeEngineeringSet</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addFilesToCodeEngineeringSet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; file)</span></div>
<div class="block">Adds given list of files to code engineering set. Dedicated for reverse engineering.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - list of files.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAllFilesRecursivelyToCES(java.io.File)">
<h3>addAllFilesRecursivelyToCES</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addAllFilesRecursivelyToCES</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> pathDirectory)</span></div>
<div class="block">Given a path to directory, adds all directory files recursively to code engineering set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathDirectory</code> - path to root directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllModelElements()">
<h3>getAllModelElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getAllModelElements</span>()</div>
<div class="block">Returns all model elements that are in code engineering set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>List of model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets name of code engineering set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - new name of code engineering set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns name of code engineering set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of ces.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWorkingPackage()">
<h3>getWorkingPackage</h3>
<div class="member-signature"><span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getWorkingPackage</span>()</div>
<div class="block">Returns working package of code engineering set. All model elements added to code engineering
 set should be under working package.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>package in project, which is working package of code engineering set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLanguage</span>()</div>
<div class="block">Language of Code Engineering Set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>language.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDialect()">
<h3>getDialect</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDialect</span>()</div>
<div class="block">Dialect of code engineering set language.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>language dialect.</dd>
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
