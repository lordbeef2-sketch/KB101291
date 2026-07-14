# JAVA OPENAPI: CompareUtil (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/merge/CompareUtil.html
- source_path: `com/nomagic/magicdraw/merge/CompareUtil.html`
- source_sha256: `a544e658165b29c60da3b5b8acf34864d4e4fbd5803495922dd4c99e2651b528`
- captured_utc: `2026-07-14T16:55:23.174097+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.merge](package-summary.html)

## Class CompareUtil

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.merge.CompareUtil

Direct Known Subclasses:
`[MergeUtil](MergeUtil.html)`

@OpenApiAllpublic classCompareUtil
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Allows using MagicDraw project merge core to compare projects (find project differences).
 See Open API manual for the usage details.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CompareUtil](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [ProjectDifference](ProjectDifference.html)`
`[compareProjects](#compareProjects(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization))([Project](../core/Project.html) project,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) baseProjectDescriptor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)`
Compare projects.
`static [ProjectDifference](ProjectDifference.html)`
`[getDifference](#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization))([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)`
Discover project difference.
`static [ProjectDifference](ProjectDifference.html)`
`[getDifference](#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization,java.util.Set))([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[ModuleInfo](../diff/ModuleInfo.html)> modules)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`getDifference(Project, ProjectDescriptor, ProjectDescriptor, ErrorHandler, Optimization)`](#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization))
`static void`
`[restore](#restore(com.nomagic.magicdraw.merge.ProjectDifference))([ProjectDifference](ProjectDifference.html) difference)`
Dispose project difference.
`static void`
`[showDifferenceGUI](#showDifferenceGUI(com.nomagic.magicdraw.merge.ProjectDifference))([ProjectDifference](ProjectDifference.html) projectDifference)`
Show project difference GUI.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CompareUtil
public CompareUtil()
 ============ METHOD DETAIL ========== 
Method Details
compareProjects
@CheckForNullpublic static [ProjectDifference](ProjectDifference.html) compareProjects([Project](../core/Project.html) project,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) baseProjectDescriptor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Compare projects. On success project difference is returned and **the base project is active project**.
Parameters:
`project` - target project.
`baseProjectDescriptor` - source project descriptor.
`errorHandler` - invoked if error occurs. Allows to perform custom action.
`optimization` - optimization option.`
Returns:
project difference.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available
getDifference
@CheckForNullpublic static [ProjectDifference](ProjectDifference.html) getDifference([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 @CheckForNull
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Discover project difference. On success project difference is returned and **ancestor project is active project**.
Parameters:
`targetProject` - target project.
`source` - source project descriptor.
`ancestor` - ancestor project descriptor. Used only for 3-way merge, `null` for 2-way merge.
`errorHandler` - invoked if error occurs. Allows to perform custom action.
`optimization` - optimization option.
Returns:
project difference.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available
getDifference
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2022xRefresh2",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@CheckForNullpublic static [ProjectDifference](ProjectDifference.html) getDifference([Project](../core/Project.html) targetProject,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) source,
 @CheckForNull
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) ancestor,
 [ErrorHandler](../../utils/ErrorHandler.html)<[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)> errorHandler,
 [Optimization](Optimization.html) optimization,
 @CheckForNull
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[ModuleInfo](../diff/ModuleInfo.html)> modules)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`getDifference(Project, ProjectDescriptor, ProjectDescriptor, ErrorHandler, Optimization)`](#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization))
Discover project difference. On success project difference is returned and **ancestor
 project is active project**.
Parameters:
`targetProject` - target project.
`source` - source project descriptor.
`ancestor` - ancestor project descriptor. Used only for 3-way merge, `null` for
 2-way merge.
`errorHandler` - invoked if error occurs. Allows to perform custom action.
`optimization` - optimization option.
`modules` - (deprecated - it has no effect in Teamwork Cloud) request modules for read-write merge mode. Restriction/constraints apply for
 read-write module merge mode.
Returns:
project difference.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if merge is not available
restore
public static void restore([ProjectDifference](ProjectDifference.html) difference)
Dispose project difference.
Parameters:
`difference` - project difference.
showDifferenceGUI
public static void showDifferenceGUI([ProjectDifference](ProjectDifference.html) projectDifference)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Show project difference GUI.
Parameters:
`projectDifference` - project difference.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if diff is not available

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.merge</a></div>
<h1 class="title" title="Class CompareUtil">Class CompareUtil</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.merge.CompareUtil</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="MergeUtil.html" title="class in com.nomagic.magicdraw.merge">MergeUtil</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CompareUtil</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Allows using MagicDraw project merge core to compare projects (find project differences).
 See Open API manual for the usage details.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CompareUtil</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compareProjects(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">compareProjects</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> baseProjectDescriptor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare projects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">getDifference</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Discover project difference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization,java.util.Set)">getDifference</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../diff/ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a>&gt; modules)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)"><code>getDifference(Project, ProjectDescriptor, ProjectDescriptor, ErrorHandler, Optimization)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#restore(com.nomagic.magicdraw.merge.ProjectDifference)">restore</a><wbr/>(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> difference)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dispose project difference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showDifferenceGUI(com.nomagic.magicdraw.merge.ProjectDifference)">showDifferenceGUI</a><wbr/>(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> projectDifference)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Show project difference GUI.</div>
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
<h3>CompareUtil</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CompareUtil</span>()</div>
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
<section class="detail" id="compareProjects(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">
<h3>compareProjects</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></span> <span class="element-name">compareProjects</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> baseProjectDescriptor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</span>
                                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Compare projects. On success project difference is returned and <strong>the base project is active project</strong>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - target project.</dd>
<dd><code>baseProjectDescriptor</code> - source project descriptor.</dd>
<dd><code>errorHandler</code> - invoked if error occurs. Allows to perform custom action.</dd>
<dd><code>optimization</code> - optimization option.`</dd>
<dt>Returns:</dt>
<dd>project difference.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)">
<h3>getDifference</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></span> <span class="element-name">getDifference</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 @CheckForNull
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Discover project difference. On success project difference is returned and <strong>ancestor project is active project</strong>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetProject</code> - target project.</dd>
<dd><code>source</code> - source project descriptor.</dd>
<dd><code>ancestor</code> - ancestor project descriptor. Used only for 3-way merge, <code>null</code> for 2-way merge.</dd>
<dd><code>errorHandler</code> - invoked if error occurs. Allows to perform custom action.</dd>
<dd><code>optimization</code> - optimization option.</dd>
<dt>Returns:</dt>
<dd>project difference.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization,java.util.Set)">
<h3>getDifference</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2022xRefresh2",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a></span> <span class="element-name">getDifference</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> targetProject,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> source,
 @CheckForNull
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> ancestor,
 <a href="../../utils/ErrorHandler.html" title="interface in com.nomagic.utils">ErrorHandler</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a>&gt; errorHandler,
 <a href="Optimization.html" title="enum class in com.nomagic.magicdraw.merge">Optimization</a> optimization,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../diff/ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a>&gt; modules)</span>
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#getDifference(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.utils.ErrorHandler,com.nomagic.magicdraw.merge.Optimization)"><code>getDifference(Project, ProjectDescriptor, ProjectDescriptor, ErrorHandler, Optimization)</code></a></div>
</div>
<div class="block">Discover project difference. On success project difference is returned and <strong>ancestor
 project is active project</strong>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetProject</code> - target project.</dd>
<dd><code>source</code> - source project descriptor.</dd>
<dd><code>ancestor</code> - ancestor project descriptor. Used only for 3-way merge, <code>null</code> for
                      2-way merge.</dd>
<dd><code>errorHandler</code> - invoked if error occurs. Allows to perform custom action.</dd>
<dd><code>optimization</code> - optimization option.</dd>
<dd><code>modules</code> - (deprecated - it has no effect in Teamwork Cloud) request modules for read-write merge mode. Restriction/constraints apply for
                      read-write module merge mode.</dd>
<dt>Returns:</dt>
<dd>project difference.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if merge is not available</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="restore(com.nomagic.magicdraw.merge.ProjectDifference)">
<h3>restore</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">restore</span><wbr/><span class="parameters">(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> difference)</span></div>
<div class="block">Dispose project difference.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>difference</code> - project difference.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showDifferenceGUI(com.nomagic.magicdraw.merge.ProjectDifference)">
<h3>showDifferenceGUI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">showDifferenceGUI</span><wbr/><span class="parameters">(<a href="ProjectDifference.html" title="class in com.nomagic.magicdraw.merge">ProjectDifference</a> projectDifference)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Show project difference GUI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectDifference</code> - project difference.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if diff is not available</dd>
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
