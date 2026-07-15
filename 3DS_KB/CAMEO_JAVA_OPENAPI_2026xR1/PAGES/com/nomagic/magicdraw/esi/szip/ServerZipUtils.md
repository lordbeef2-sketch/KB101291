# JAVA OPENAPI: ServerZipUtils (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/esi/szip/ServerZipUtils.html
- source_path: `com/nomagic/magicdraw/esi/szip/ServerZipUtils.html`
- source_sha256: `2082ee93cd4f1f85a1f083cfb7a77b7d4ecfef417025173108f2ade438a82388`
- captured_utc: `2026-07-14T16:45:36.087483+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi.szip](package-summary.html)

## Class ServerZipUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.esi.szip.ServerZipUtils

@OpenApipublic classServerZipUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with server zip files.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[exportServerZip](#exportServerZip(com.nomagic.magicdraw.core.Project,boolean,java.nio.file.Path,com.nomagic.task.ProgressStatus))([Project](../../core/Project.html) project,
 boolean exportUsedProjects,
 [Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) path,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Exports project to the server zip file.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getProjectIDsFromServerZip](#getProjectIDsFromServerZip(java.nio.file.Path))([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file)`
Returns project IDs from the server zip file.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.esi.szip.ProjectInfo>`
`[getProjectsInfosFromServerZip](#getProjectsInfosFromServerZip(java.nio.file.Path))([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file)`
Returns projects information contained in the server zip file.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../../core/project/ProjectDescriptor.html)>`
`[importFromServerZip](#importFromServerZip(java.nio.file.Path,java.util.function.Predicate,java.lang.String))([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> importProject,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) categoryName)`
Imports projects from the server zip file to server.
`static void`
`[updateFromServerZip](#updateFromServerZip(java.nio.file.Path,java.util.Collection))([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../../core/project/ProjectDescriptor.html)> descriptors)`
Updates projects from the server zip file.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
exportServerZip
@OpenApipublic static void exportServerZip([Project](../../core/Project.html) project,
 boolean exportUsedProjects,
 [Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) path,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Exports project to the server zip file.
Parameters:
`project` - project to export
`exportUsedProjects` - to export with used projects - `true`, otherwise - `false`
`path` - a path the projects will be exported
`status` - progress status
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs
importFromServerZip
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../../core/project/ProjectDescriptor.html)> importFromServerZip([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> importProject,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) categoryName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Imports projects from the server zip file to server.
Parameters:
`file` - server zip file
`importProject` - specific projects to import; to import all projects, set predicate to `() -> true`;
 in a multi-resource environment, it's only possible to import all projects at once - `() -> true`
`categoryName` - specific category name to import project; to import to 'Uncategorized' set - `null`;
 in a multi-resource environment, it's not possible to select category, set - `null`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs
updateFromServerZip
@OpenApipublic static void updateFromServerZip([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../../core/project/ProjectDescriptor.html)> descriptors)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Updates projects from the server zip file.
Parameters:
`file` - path to server zip file
`descriptors` - descriptors of project to update;
 in single-resource environment, allows to update one project (1 descriptor) including it's used projects.
 in multi-resource environment must pass all project descriptors.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs
getProjectsInfosFromServerZip
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.esi.szip.ProjectInfo> getProjectsInfosFromServerZip([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns projects information contained in the server zip file.
Parameters:
`file` - path to server zip file
Returns:
list of projects information
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs
getProjectIDsFromServerZip
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getProjectIDsFromServerZip([Path](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html) file)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns project IDs from the server zip file.
Parameters:
`file` - path to server zip file
Returns:
list of project IDs
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi.szip</a></div>
<h1 class="title" title="Class ServerZipUtils">Class ServerZipUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.esi.szip.ServerZipUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ServerZipUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with server zip files.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportServerZip(com.nomagic.magicdraw.core.Project,boolean,java.nio.file.Path,com.nomagic.task.ProgressStatus)">exportServerZip</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean exportUsedProjects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> path,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports project to the server zip file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectIDsFromServerZip(java.nio.file.Path)">getProjectIDsFromServerZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns project IDs from the server zip file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.magicdraw.esi.szip.ProjectInfo&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectsInfosFromServerZip(java.nio.file.Path)">getProjectsInfosFromServerZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects information contained in the server zip file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importFromServerZip(java.nio.file.Path,java.util.function.Predicate,java.lang.String)">importFromServerZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; importProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Imports projects from the server zip file to server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateFromServerZip(java.nio.file.Path,java.util.Collection)">updateFromServerZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates projects from the server zip file.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="exportServerZip(com.nomagic.magicdraw.core.Project,boolean,java.nio.file.Path,com.nomagic.task.ProgressStatus)">
<h3>exportServerZip</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportServerZip</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean exportUsedProjects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> path,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports project to the server zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export</dd>
<dd><code>exportUsedProjects</code> - to export with used projects - <code>true</code>, otherwise - <code>false</code></dd>
<dd><code>path</code> - a path the projects will be exported</dd>
<dd><code>status</code> - progress status</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importFromServerZip(java.nio.file.Path,java.util.function.Predicate,java.lang.String)">
<h3>importFromServerZip</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">importFromServerZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; importProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> categoryName)</span>
                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Imports projects from the server zip file to server.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - server zip file</dd>
<dd><code>importProject</code> - specific projects to import; to import all projects, set predicate to <code>() -&gt; true</code>;
                      in a multi-resource environment, it's only possible to import all projects at once - <code>() -&gt; true</code></dd>
<dd><code>categoryName</code> - specific category name to import project; to import to 'Uncategorized' set - <code>null</code>;
                      in a multi-resource environment, it's not possible to select category, set - <code>null</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateFromServerZip(java.nio.file.Path,java.util.Collection)">
<h3>updateFromServerZip</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateFromServerZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptors)</span>
                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Updates projects from the server zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - path to server zip file</dd>
<dd><code>descriptors</code> - descriptors of project to update;
                    in single-resource environment, allows to update one project (1 descriptor) including it's used projects.
                    in multi-resource environment must pass all project descriptors.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectsInfosFromServerZip(java.nio.file.Path)">
<h3>getProjectsInfosFromServerZip</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.esi.szip.ProjectInfo&gt;</span> <span class="element-name">getProjectsInfosFromServerZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file)</span>
                                                                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns projects information contained in the server zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - path to server zip file</dd>
<dt>Returns:</dt>
<dd>list of projects information</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectIDsFromServerZip(java.nio.file.Path)">
<h3>getProjectIDsFromServerZip</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getProjectIDsFromServerZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file">Path</a> file)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns project IDs from the server zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - path to server zip file</dd>
<dt>Returns:</dt>
<dd>list of project IDs</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
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
