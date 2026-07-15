# JAVA OPENAPI: ProjectSpecificLocationRegister (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/ProjectSpecificLocationRegister.html
- source_path: `com/nomagic/magicdraw/core/ProjectSpecificLocationRegister.html`
- source_sha256: `9d9f21f5b5a43080d0f90fb04f12297278a4dbf7bdb64275ed11f1529f1cd3ca`
- captured_utc: `2026-07-14T16:51:13.001096+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class ProjectSpecificLocationRegister

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[Project](Project.html)>
com.nomagic.magicdraw.core.project.service.ProjectService
com.nomagic.magicdraw.core.ProjectSpecificLocationRegister

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`, `[FileLocationRegister](FileLocationRegister.html)`

@OpenApipublic final classProjectSpecificLocationRegister
extends com.nomagic.magicdraw.core.project.service.ProjectService
implements [FileLocationRegister](FileLocationRegister.html)

This class is for storing file locations which depends on project.
 All locations stored is project specific.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ProjectSpecificLocationRegister](ProjectSpecificLocationRegister.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.core.Project))([Project](Project.html) prj)`
Method to get instance.
`void`
`[setFileLocation](#setFileLocation(java.lang.String,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) locationNameID,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Before saving file locations file is checked if it still exist.
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [ProjectSpecificLocationRegister](ProjectSpecificLocationRegister.html) getInstance([Project](Project.html) prj)
Method to get instance.
Parameters:
`prj` - project type object.
Returns:
ProjectSpecificLocationRegister instance.
setFileLocation
@OpenApipublic void setFileLocation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) locationNameID,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Before saving file locations file is checked if it still exist.
 It is done because user may delete directory, rename it, move it...
 If file location does not exist anymore default(project directory) location is used.
Specified by:
`[setFileLocation](FileLocationRegister.html#setFileLocation(java.lang.String,java.io.File))` in interface `[FileLocationRegister](FileLocationRegister.html)`
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
<h1 class="title" title="Class ProjectSpecificLocationRegister">Class ProjectSpecificLocationRegister</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.core.project.service.ProjectService
<div class="inheritance">com.nomagic.magicdraw.core.ProjectSpecificLocationRegister</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code>, <code><a href="FileLocationRegister.html" title="interface in com.nomagic.magicdraw.core">FileLocationRegister</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ProjectSpecificLocationRegister</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.service.ProjectService
implements <a href="FileLocationRegister.html" title="interface in com.nomagic.magicdraw.core">FileLocationRegister</a></span></div>
<div class="block">This class is for storing file locations which depends on project.
 All locations stored is project specific.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core">ProjectSpecificLocationRegister</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.core.Project)">getInstance</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method to get instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFileLocation(java.lang.String,java.io.File)">setFileLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Before saving file locations file is checked if it still exist.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.core.Project)">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectSpecificLocationRegister.html" title="class in com.nomagic.magicdraw.core">ProjectSpecificLocationRegister</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj)</span></div>
<div class="block">Method to get instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj</code> - project type object.</dd>
<dt>Returns:</dt>
<dd>ProjectSpecificLocationRegister instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFileLocation(java.lang.String,java.io.File)">
<h3>setFileLocation</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFileLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> locationNameID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Before saving file locations file is checked if it still exist.
 It is done because user may delete directory, rename it, move it...
 If file location does not exist anymore default(project directory) location is used.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="FileLocationRegister.html#setFileLocation(java.lang.String,java.io.File)">setFileLocation</a></code> in interface <code><a href="FileLocationRegister.html" title="interface in com.nomagic.magicdraw.core">FileLocationRegister</a></code></dd>
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
