# JAVA OPENAPI: ProjectModuleHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/magicreport/tools/ProjectModuleHelper.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ProjectModuleHelper.html`
- source_sha256: `76f301e90449d5abc8a7a66203cb638fa5d0593f982bec306379063e8ef60e1f`
- captured_utc: `2026-07-14T16:51:24.578248+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ProjectModuleHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.magicreport.tools.ProjectModuleHelper

@OpenApiAllpublic classProjectModuleHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectModuleHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescriptionString](#getDescriptionString(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get description of attached project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLatestVersion](#getLatestVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get latest version of specified attached project.
`static [ProjectVersion](ProjectVersion.html)`
`[getProjectVersion](#getProjectVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return project version of attached project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return user friendly representation string about given attached project
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRequiredVersion](#getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get required version of specified attached project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getSharedModule](#getSharedModule(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject module)`
Return a list of project module from specified module.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getSharedModule](#getSharedModule(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Return a list of project module from current project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUsedVersion](#getUsedVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get used version of specified attached project.
`static long`
`[getVersion](#getVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get version number of specified attached project.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersionList](#getVersionList(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return all project versions of attached project.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return a list of project version information from opened server project. 

 The result will be sorted in descending order.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(com.nomagic.ci.persistence.IAttachedProject,java.lang.String))(com.nomagic.ci.persistence.IAttachedProject attachedProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)`
Return a list of project version information from opened server project. 

 The result will be sorted by specified sortType.
`static boolean`
`[isRemote](#isRemote(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Check if given project is remote - from teamwork server or TW Cloud.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectModuleHelper
public ProjectModuleHelper()
 ============ METHOD DETAIL ========== 
Method Details
getSharedModule
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getSharedModule([Project](../../core/Project.html) project)
Return a list of project module from current project.
Parameters:
`project` - a [`Project`](../../core/Project.html)
Returns:
a list of [`ProjectModule`](ProjectModule.html)
getSharedModule
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getSharedModule(com.nomagic.ci.persistence.IAttachedProject module)
Return a list of project module from specified module.
Parameters:
`module` - an `IAttachedProject`
Returns:
a list of [`ProjectModule`](ProjectModule.html)
getDescriptionString
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescriptionString(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get description of attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
module description
getRepresentationString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationString(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return user friendly representation string about given attached project
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
user friendly project representation
isRemote
public static boolean isRemote(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Check if given project is remote - from teamwork server or TW Cloud.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
true if project is from server
getLatestVersion
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLatestVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get latest version of specified attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
latest version
getVersion
public static long getVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get version number of specified attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
version number as long
getUsedVersion
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUsedVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get used version of specified attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
used version
getRequiredVersion
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get required version of specified attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
required version
getProjectVersion
@CheckForNullpublic static [ProjectVersion](ProjectVersion.html) getProjectVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return project version of attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
a [`ProjectVersion`](ProjectVersion.html) of attached project
getVersions
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return a list of project version information from opened server project. 

 The result will be sorted in descending order.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersions
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions(com.nomagic.ci.persistence.IAttachedProject attachedProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)
Return a list of project version information from opened server project. 

 The result will be sorted by specified sortType.
Parameters:
`attachedProject` - an `IAttachedProject`
`sortType` - type of sorting. Specify "asc" sort in descending order. Default is descending sort.
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersionList
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersionList(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return all project versions of attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
list of [`ProjectVersion`](ProjectVersion.html) of attached project

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ProjectModuleHelper">Class ProjectModuleHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ProjectModuleHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectModuleHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectModuleHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionString(com.nomagic.ci.persistence.IAttachedProject)">getDescriptionString</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get description of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLatestVersion(com.nomagic.ci.persistence.IAttachedProject)">getLatestVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get latest version of specified attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectVersion(com.nomagic.ci.persistence.IAttachedProject)">getProjectVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return project version of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationString(com.nomagic.ci.persistence.IAttachedProject)">getRepresentationString</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return user friendly representation string about given attached project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject)">getRequiredVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get required version of specified attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedModule(com.nomagic.ci.persistence.IAttachedProject)">getSharedModule</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject module)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a list of project module from specified module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedModule(com.nomagic.magicdraw.core.Project)">getSharedModule</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a list of project module from current project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedVersion(com.nomagic.ci.persistence.IAttachedProject)">getUsedVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get used version of specified attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion(com.nomagic.ci.persistence.IAttachedProject)">getVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get version number of specified attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionList(com.nomagic.ci.persistence.IAttachedProject)">getVersionList</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all project versions of attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(com.nomagic.ci.persistence.IAttachedProject)">getVersions</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted in descending order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(com.nomagic.ci.persistence.IAttachedProject,java.lang.String)">getVersions</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted by specified sortType.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote(com.nomagic.ci.persistence.IAttachedProject)">isRemote</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given project is remote - from teamwork server or TW Cloud.</div>
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
<h3>ProjectModuleHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectModuleHelper</span>()</div>
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
<section class="detail" id="getSharedModule(com.nomagic.magicdraw.core.Project)">
<h3>getSharedModule</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getSharedModule</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Return a list of project module from current project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core"><code>Project</code></a></dd>
<dt>Returns:</dt>
<dd>a list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedModule(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getSharedModule</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getSharedModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject module)</span></div>
<div class="block">Return a list of project module from specified module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>module</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>a list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptionString(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getDescriptionString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescriptionString</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get description of attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>module description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return user friendly representation string about given attached project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>user friendly project representation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote(com.nomagic.ci.persistence.IAttachedProject)">
<h3>isRemote</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Check if given project is remote - from teamwork server or TW Cloud.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>true if project is from server</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLatestVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getLatestVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLatestVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get latest version of specified attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>latest version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get version number of specified attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>version number as long</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getUsedVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUsedVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get used version of specified attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>used version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getRequiredVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get required version of specified attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getProjectVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></span> <span class="element-name">getProjectVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return project version of attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>a <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted in descending order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(com.nomagic.ci.persistence.IAttachedProject,java.lang.String)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</span></div>
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted by specified sortType.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dd><code>sortType</code> - type of sorting. Specify "asc" sort in descending order. Default is descending sort.</dd>
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionList(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getVersionList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersionList</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return all project versions of attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
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
