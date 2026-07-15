# JAVA OPENAPI: ProjectPersistenceManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/project/ProjectPersistenceManager.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectPersistenceManager.html`
- source_sha256: `b201950529228cdc9513f3b50178ebf0a536d36a58232f65370961cb61872c3f`
- captured_utc: `2026-07-14T16:51:16.376139+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Interface ProjectPersistenceManager

All Known Implementing Classes:
`[ProjectsManager](ProjectsManager.html)`

@OpenApiAllpublic interfaceProjectPersistenceManager

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[exportModule](#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) prj,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) packages,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 [ProjectDescriptor](ProjectDescriptor.html) module)`
Exports given packages from project into given module.
`void`
`[importModule](#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) prj,
 [ProjectDescriptor](ProjectDescriptor.html) prjDescriptor)`
Loads module by value into given project.
`boolean`
`[importProject](#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](ProjectDescriptor.html) pd)`
Imports given project into the current project by value.
`void`
`[loadProject](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)`
Deprecated.
use [`loadProject(ProjectDescriptor, ProgressStatus)`](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))
`void`
`[loadProject](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Loads given project
`void`
`[reloadModule](#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)`
Reloads module.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporal)`
Deprecated.
use [`saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)`](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus))
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Saves module.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean temporalSave)`
Saves module.
`boolean`
`[saveProject](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)`
Deprecated.
use [`saveProject(ProjectDescriptor, ProgressStatus, boolean)`](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))
`boolean`
`[saveProject](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean silent)`
Saves or commits project.
`void`
`[unloadModule](#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) descriptor)`
Removes unreferenced elements from this module, and makes module not loaded.
`boolean`
`[useModule](#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) prj,
 [ProjectDescriptor](ProjectDescriptor.html) module)`
Loads module by reference into given project.

============ METHOD DETAIL ========== 
Method Details
loadProject
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)void loadProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)
Deprecated.
use [`loadProject(ProjectDescriptor, ProgressStatus)`](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))
loadProject
void loadProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Loads given project
Parameters:
`descriptor` - project to load.
`status` - status to display progress
saveProject
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)boolean saveProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)
Deprecated.
use [`saveProject(ProjectDescriptor, ProgressStatus, boolean)`](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))
saveProject
boolean saveProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean silent)
Saves or commits project.
Parameters:
`descriptor` - descriptor of project to save.
`status` - status to display operation status.
`silent` - true if no gui should be shown durring save/commmit
Returns:
false if saving fails.
saveModule
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporal)
Deprecated.
use [`saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)`](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus))
saveModule
boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Saves module. Local module will be saved to the disk, teamwork committed. For teamwork module it is not recommended
 to use this method directly.
Parameters:
`project` - project
`module` - module to save/commit.
`displayDependenciesDialog` - displays dependencies dialog if there are bad dependencies. To turn off dependency checking
`status` - progress status which display status of current operation. @return false if operation fails.
saveModule
boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean temporalSave)
Saves module. Local module will be saved to the disk, teamwork committed. For teamwork module it is not recommended
 to use this method directly.
Parameters:
`project` - project
`module` - module to save/commit.
`displayDependenciesDialog` - displays dependencies dialog if there are bad dependencies. To turn off dependency checking
`status` - progress status which display status of current operation. @return false if operation fails.
reloadModule
void reloadModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)
Reloads module.
Parameters:
`project` - the project.
`projectDescriptor` - the ProjectDescriptor of the module.
useModule
boolean useModule([Project](../Project.html) prj,
 [ProjectDescriptor](ProjectDescriptor.html) module)
Loads module by reference into given project.
Parameters:
`prj` - the project.
`module` - the ProjectDescriptor of the module.
Returns:
result of operation
unloadModule
void unloadModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) descriptor)
Removes unreferenced elements from this module, and makes module not loaded.
Parameters:
`project` - project
`descriptor` - module descriptor
importModule
void importModule([Project](../Project.html) prj,
 [ProjectDescriptor](ProjectDescriptor.html) prjDescriptor)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Loads module by value into given project.
Parameters:
`prj` - the project.
`prjDescriptor` - the ProjectDescriptor of the module.
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if user has no rights to perform this action.
exportModule
void exportModule([Project](../Project.html) prj,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) packages,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 [ProjectDescriptor](ProjectDescriptor.html) module)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[ReadOnlyModuleException](../modules/ReadOnlyModuleException.html)
Exports given packages from project into given module.
Parameters:
`prj` - the project.
`packages` - the packages from given project. These packages will become roots of the given module.
`description` - the description of module(if null or zero length, description will not be generated).
`module` - the ProjectDescriptor of the module. Current implementation supports only LocalProjectDescriptor.
Throws:
`[ReadOnlyModuleException](../modules/ReadOnlyModuleException.html)` - if trying export package which is already in module and this module is read only
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if given packages have dependencies.
importProject
boolean importProject([ProjectDescriptor](ProjectDescriptor.html) pd)
Imports given project into the current project by value. Does the same as File-Import MagicDraw Project
Parameters:
`pd` - Project descriptor to import.
Returns:
true if operation was successful.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Interface ProjectPersistenceManager">Interface ProjectPersistenceManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ProjectsManager.html" title="class in com.nomagic.magicdraw.core.project">ProjectsManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectPersistenceManager</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor)">exportModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Exports given packages from project into given module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">importModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> prjDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Loads module by value into given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">importProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Imports given project into the current project by value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">loadProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)"><code>loadProject(ProjectDescriptor, ProgressStatus)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">loadProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Loads given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">reloadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reloads module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)"><code>saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Saves module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean temporalSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Saves module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">saveProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)"><code>saveProject(ProjectDescriptor, ProgressStatus, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">saveProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean silent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Saves or commits project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">unloadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes unreferenced elements from this module, and makes module not loaded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">useModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Loads module by reference into given project.</div>
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
<section class="detail" id="loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">
<h3>loadProject</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)"><code>loadProject(ProjectDescriptor, ProgressStatus)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">
<h3>loadProject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Loads given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project to load.</dd>
<dd><code>status</code> - status to display progress</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">
<h3>saveProject</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">boolean</span> <span class="element-name">saveProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)"><code>saveProject(ProjectDescriptor, ProgressStatus, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">
<h3>saveProject</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">saveProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean silent)</span></div>
<div class="block">Saves or commits project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - descriptor of project to save.</dd>
<dd><code>status</code> - status to display operation status.</dd>
<dd><code>silent</code> - true if no gui should be shown durring save/commmit</dd>
<dt>Returns:</dt>
<dd>false if saving fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporal)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)"><code>saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">
<h3>saveModule</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Saves module. Local module will be saved to the disk, teamwork committed. For teamwork module it is not recommended
 to use  this method directly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save/commit.</dd>
<dd><code>displayDependenciesDialog</code> - displays dependencies dialog if there are bad dependencies. To turn off dependency checking</dd>
<dd><code>status</code> - progress status which display status of current operation.    @return false if operation fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">
<h3>saveModule</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean displayDependenciesDialog,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean temporalSave)</span></div>
<div class="block">Saves module. Local module will be saved to the disk, teamwork committed. For teamwork module it is not recommended
 to use  this method directly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save/commit.</dd>
<dd><code>displayDependenciesDialog</code> - displays dependencies dialog if there are bad dependencies. To turn off dependency checking</dd>
<dd><code>status</code> - progress status which display status of current operation.   @return false if operation fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>reloadModule</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">reloadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
<div class="block">Reloads module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project.</dd>
<dd><code>projectDescriptor</code> - the ProjectDescriptor of the module.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>useModule</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">useModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</span></div>
<div class="block">Loads module by reference into given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj</code> - the project.</dd>
<dd><code>module</code> - the ProjectDescriptor of the module.</dd>
<dt>Returns:</dt>
<dd>result of operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>unloadModule</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">unloadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Removes unreferenced elements from this module, and makes module not loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>descriptor</code> - module descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>importModule</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">importModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> prjDescriptor)</span>
           throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Loads module by value into given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj</code> - the project.</dd>
<dd><code>prjDescriptor</code> - the ProjectDescriptor of the module.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if user has no rights to perform this action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>exportModule</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">exportModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a href="../modules/ReadOnlyModuleException.html" title="class in com.nomagic.magicdraw.core.modules">ReadOnlyModuleException</a></span></div>
<div class="block">Exports given packages from project into given module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj</code> - the project.</dd>
<dd><code>packages</code> - the packages from given project. These packages will become roots of the given module.</dd>
<dd><code>description</code> - the description of module(if null or zero length,  description will not be generated).</dd>
<dd><code>module</code> - the ProjectDescriptor of the module. Current implementation supports only LocalProjectDescriptor.</dd>
<dt>Throws:</dt>
<dd><code><a href="../modules/ReadOnlyModuleException.html" title="class in com.nomagic.magicdraw.core.modules">ReadOnlyModuleException</a></code> - if trying export package which is already in module and this module is read only</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if given packages have dependencies.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>importProject</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">importProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</span></div>
<div class="block">Imports given project into the current project by value. Does the same as File-Import MagicDraw Project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pd</code> - Project descriptor to import.</dd>
<dt>Returns:</dt>
<dd>true if operation was successful.</dd>
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
