# JAVA OPENAPI: ProjectsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/project/ProjectsManager.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectsManager.html`
- source_sha256: `941117e3bb558b245c24bad8fb36592f6c82f3d6563d90b8ec06f5e1f5e5be94`
- captured_utc: `2026-07-14T16:51:16.400140+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class ProjectsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.project.ProjectsManager

All Implemented Interfaces:
`[ProjectPersistenceManager](ProjectPersistenceManager.html)`

@OpenApipublic classProjectsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ProjectPersistenceManager](ProjectPersistenceManager.html)

Stores and manages multiple projects.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addProjectListener](#addProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](ProjectEventListener.html) listener)`
Adds new project listener.
`void`
`[closeProject](#closeProject())()`
Closes current project.
`void`
`[closeProject](#closeProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Closes given project
`[Project](../Project.html)`
`[createProject](#createProject())()`
Creates new project.
`[Project](../Project.html)`
`[createProjectFromTemplate](#createProjectFromTemplate(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templatePath)`
Creates a new project from the given template.
`void`
`[exportModule](#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) prj,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) packages,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 [ProjectDescriptor](ProjectDescriptor.html) module)`
Export local (not teamwork) module into given descriptor
`com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProject](#findAttachedProject(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)`
Find used module according given project descriptor.
`[Project](../Project.html)`
`[findProject](#findProject(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)`
Find loaded project according given project descriptor.
`[Project](../Project.html)`
`[getActiveProject](#getActiveProject())()`
Returns active open project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Project](../Project.html)>`
`[getProjects](#getProjects())()`
Returns list of open projects.
`void`
`[importModule](#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) descriptor)`
Import module into project from given descriptor
`boolean`
`[importProject](#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](ProjectDescriptor.html) pd)`
Import project.
`boolean`
`[isProjectActive](#isProjectActive(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method checks if given project is active at this time.
`void`
`[loadProject](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)`
Loads project from location, described in a project descriptor.
`void`
`[reloadModule](#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)`
Reloads module.
`void`
`[removeProjectListener](#removeProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](ProjectEventListener.html) listener)`
Removes project listener.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporalSave)`
Save module from current project into given location.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Saves module without any additional dependencies checking.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean temporalSave)`
Saves module without any additional dependencies checking.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) saveTo)`
Saves module without any additional dependencies checking.
`boolean`
`[saveModule](#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI,boolean))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) saveTo,
 boolean temporalSave)`
Saves module without any additional dependencies checking.
`boolean`
`[saveProject](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)`
Saves project into location specified by descriptor.
`void`
`[setActiveProject](#setActiveProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Sets given project as active.
`void`
`[sharePackage](#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List))([Project](../Project.html) project,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages)`
Deprecated.
Use [`sharePackage(com.nomagic.magicdraw.core.Project, java.util.List, String)`](#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)).
`void`
`[sharePackage](#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String))([Project](../Project.html) project,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Share given list of packages in project.
`void`
`[unloadModule](#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) moduleDescriptor)`
Unload module
`boolean`
`[useModule](#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) module)`
Use module in given project from given descriptor.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getProjects
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Project](../Project.html)> getProjects()
Returns list of open projects.
Returns:
list of open projects.
isProjectActive
@OpenApipublic boolean isProjectActive(@CheckForNull
 [Project](../Project.html) project)
Method checks if given project is active at this time.
Parameters:
`project` - project to check.
Returns:
true if given project is active.
setActiveProject
@OpenApipublic void setActiveProject(@CheckForNull
 [Project](../Project.html) project)
Sets given project as active. Updates GUI.
Parameters:
`project` - the project to be set as active.
getActiveProject
@OpenApi
@CheckForNullpublic [Project](../Project.html) getActiveProject()
Returns active open project.
Returns:
active project.
addProjectListener
@OpenApipublic void addProjectListener([ProjectEventListener](ProjectEventListener.html) listener)
Adds new project listener.
Parameters:
`listener` - listener to be added.
removeProjectListener
@OpenApipublic void removeProjectListener([ProjectEventListener](ProjectEventListener.html) listener)
Removes project listener.
Parameters:
`listener` - listener to be removed.
loadProject
@OpenApipublic void loadProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)
Loads project from location, described in a project descriptor. Loading is done on EDT.
Specified by:
`[loadProject](ProjectPersistenceManager.html#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`descriptor` - the project descriptor.
`silent` - if true, loads without GUI interruptions.
saveProject
@OpenApipublic boolean saveProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)
Saves project into location specified by descriptor.
Specified by:
`[saveProject](ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`descriptor` - the project descriptor.
`silent` - if true, saves without GUI interruptions.
createProject
@OpenApipublic [Project](../Project.html) createProject()
Creates new project.
Returns:
created project.
createProjectFromTemplate
@OpenApi
@CheckForNullpublic [Project](../Project.html) createProjectFromTemplate([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) templatePath)
Creates a new project from the given template.
Parameters:
`templatePath` - absolute template path
Returns:
created project.
closeProject
@OpenApipublic void closeProject()
Closes current project.
closeProject
@OpenApipublic void closeProject([Project](../Project.html) project)
Closes given project
Parameters:
`project` - project to close
useModule
@OpenApipublic boolean useModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) module)
Use module in given project from given descriptor.
 *Need to update [`ProjectOptions`](../options/ProjectOptions.html) before using local module:* 

`String moduleDir = moduleFile.getParent(); 

 ProjectOptions projectOptions = project.getOptions(); 

 Listdirectories = projectOptions.getModulesDirectories(true); 

 if (!directories.contains(moduleDir)) 

 { 

 projectOptions.addModuleDirectory(moduleDir); 

 }`
Specified by:
`[useModule](ProjectPersistenceManager.html#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`module` - module
Returns:
true if module was used
reloadModule
@OpenApipublic void reloadModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)
Reloads module.
Specified by:
`[reloadModule](ProjectPersistenceManager.html#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - the project.
`projectDescriptor` - the ProjectDescriptor of the module.
importModule
@OpenApipublic void importModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) descriptor)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Import module into project from given descriptor
Specified by:
`[importModule](ProjectPersistenceManager.html#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`descriptor` - descriptor
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if user has no rights to perform this action.
exportModule
@OpenApipublic void exportModule([Project](../Project.html) prj,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) packages,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description,
 [ProjectDescriptor](ProjectDescriptor.html) module)
Export local (not teamwork) module into given descriptor
Specified by:
`[exportModule](ProjectPersistenceManager.html#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`prj` - current project
`packages` - "shared" packages in project
`description` - module description
`module` - module location descriptor
saveModule
@OpenApipublic boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporalSave)
Save module from current project into given location.
Specified by:
`[saveModule](ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`module` - module to save
`silent` - do not show UI messages
`temporalSave` - do not change module location after save
Returns:
true if module was saved
saveModule
@OpenApipublic boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Saves module without any additional dependencies checking.
Specified by:
`[saveModule](ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`module` - module to save
`silent` - save in silent mode
`status` - progress status
Returns:
true if operation was successful
saveModule
@OpenApipublic boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean temporalSave)
Saves module without any additional dependencies checking.
Specified by:
`[saveModule](ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`module` - module to save
`silent` - save in silent mode
`status` - progress status
`temporalSave` - do not change module location after save
Returns:
true if operation was successful
saveModule
@OpenApipublic boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) saveTo)
Saves module without any additional dependencies checking.
Parameters:
`project` - project
`module` - module to save
`status` - status
`silent` - save in silent mode
`saveTo` - where to save module, can be null, then module is saved to module.getURI()
 location
Returns:
true if operation was successful
saveModule
@OpenApipublic boolean saveModule([Project](../Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 @CheckForNull
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) saveTo,
 boolean temporalSave)
Saves module without any additional dependencies checking.
Parameters:
`project` - project
`module` - module to save
`silent` - save in silent mode
`status` - progress status
`saveTo` - where to save module, can be null, then module is saved to module.getURI() location
`temporalSave` - do not change module location after save
Returns:
true if operation was successful
unloadModule
@OpenApipublic void unloadModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) moduleDescriptor)
Unload module
Specified by:
`[unloadModule](ProjectPersistenceManager.html#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`moduleDescriptor` - module descriptor
findAttachedProject
@OpenApi
@CheckForNullpublic com.nomagic.ci.persistence.IAttachedProject findAttachedProject([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)
Find used module according given project descriptor.
Parameters:
`project` - project using module.
`projectDescriptor` - project descriptor of module.
Returns:
found attached project or null
findProject
@OpenApi
@CheckForNullpublic [Project](../Project.html) findProject([ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)
Find loaded project according given project descriptor.
Parameters:
`projectDescriptor` - project descriptor.
Returns:
`null` if project not found.
sharePackage
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void sharePackage([Project](../Project.html) project,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages)
Deprecated.
Use [`sharePackage(com.nomagic.magicdraw.core.Project, java.util.List, String)`](#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)).
Share given list of packages in project.
Parameters:
`project` - Project where packages will be shared.
`packages` - List of packaged, dedicated for sharing.
sharePackage
@OpenApipublic void sharePackage([Project](../Project.html) project,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Share given list of packages in project. On CTS decomposition must be
 locked before sharing.
Parameters:
`project` - Project where packages will be shared.
`packages` - List of packaged, dedicated for sharing.
`description` - share description, null if do not change/set the description.
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html)` - if either some being shared package becomes invalid in the
 main project (that is, has been deleted or moved to a module)
 or is locked by another user
importProject
@OpenApipublic boolean importProject([ProjectDescriptor](ProjectDescriptor.html) pd)
Import project.
Specified by:
`[importProject](ProjectPersistenceManager.html#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`pd` - project descriptor to import.
Returns:
true if project was imported

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class ProjectsManager">Class ProjectsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectsManager</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></span></div>
<div class="block">Stores and manages multiple projects.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">addProjectListener</a><wbr/>(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new project listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProject()">closeProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes current project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProject(com.nomagic.magicdraw.core.Project)">closeProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProject()">createProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates new project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProjectFromTemplate(java.lang.String)">createProjectFromTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templatePath)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new project from the given template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor)">exportModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Export local (not teamwork) module into given descriptor</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProject(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">findAttachedProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find used module according given project descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">findProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find loaded project according given project descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveProject()">getActiveProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns active open project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjects()">getProjects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of open projects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">importModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Import module into project from given descriptor</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">importProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Import project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectActive(com.nomagic.magicdraw.core.Project)">isProjectActive</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method checks if given project is active at this time.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">loadProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads project from location, described in a project descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">reloadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reloads module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">removeProjectListener</a><wbr/>(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes project listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporalSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Save module from current project into given location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean temporalSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo,
 boolean temporalSave)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">saveProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves project into location specified by descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveProject(com.nomagic.magicdraw.core.Project)">setActiveProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets given project as active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List)">sharePackage</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)"><code>sharePackage(com.nomagic.magicdraw.core.Project, java.util.List, String)</code></a>.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)">sharePackage</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Share given list of packages in project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">unloadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unload module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">useModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Use module in given project from given descriptor.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getProjects()">
<h3>getProjects</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;</span> <span class="element-name">getProjects</span>()</div>
<div class="block">Returns list of open projects.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of open projects.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectActive(com.nomagic.magicdraw.core.Project)">
<h3>isProjectActive</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProjectActive</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method checks if given project is active at this time.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to check.</dd>
<dt>Returns:</dt>
<dd>true if given project is active.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveProject(com.nomagic.magicdraw.core.Project)">
<h3>setActiveProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveProject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Sets given project as active. Updates GUI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project to be set as active.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveProject()">
<h3>getActiveProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getActiveProject</span>()</div>
<div class="block">Returns active open project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>active project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>addProjectListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProjectListener</span><wbr/><span class="parameters">(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Adds new project listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>removeProjectListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProjectListener</span><wbr/><span class="parameters">(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Removes project listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">
<h3>loadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</span></div>
<div class="block">Loads project from location, described in a project descriptor. Loading is done on EDT.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">loadProject</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>descriptor</code> - the project descriptor.</dd>
<dd><code>silent</code> - if true, loads without GUI interruptions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">
<h3>saveProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</span></div>
<div class="block">Saves project into location specified by descriptor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">saveProject</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>descriptor</code> - the project descriptor.</dd>
<dd><code>silent</code> - if true, saves without GUI interruptions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProject()">
<h3>createProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">createProject</span>()</div>
<div class="block">Creates new project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProjectFromTemplate(java.lang.String)">
<h3>createProjectFromTemplate</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">createProjectFromTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templatePath)</span></div>
<div class="block">Creates a new project from the given template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templatePath</code> - absolute template path</dd>
<dt>Returns:</dt>
<dd>created project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeProject()">
<h3>closeProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeProject</span>()</div>
<div class="block">Closes current project.</div>
</section>
</li>
<li>
<section class="detail" id="closeProject(com.nomagic.magicdraw.core.Project)">
<h3>closeProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Closes given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to close</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>useModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</span></div>
<div class="block">Use module in given project from given descriptor.
 <p>
<i>Need to update <a href="../options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options"><code>ProjectOptions</code></a> before using local module:</i><br/>
<code>String moduleDir = moduleFile.getParent();<br/>
 ProjectOptions projectOptions = project.getOptions();<br/>
 List<string> directories = projectOptions.getModulesDirectories(true);<br/>
 if (!directories.contains(moduleDir))<br/>
 {<br/>
     projectOptions.addModuleDirectory(moduleDir);<br/>
 }</string></code>
</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">useModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module</dd>
<dt>Returns:</dt>
<dd>true if module was used</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>reloadModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reloadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
<div class="block">Reloads module.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">reloadModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - the project.</dd>
<dd><code>projectDescriptor</code> - the ProjectDescriptor of the module.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>importModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">importModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span>
                  throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Import module into project from given descriptor</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">importModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>descriptor</code> - descriptor</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if user has no rights to perform this action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>exportModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">exportModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</span></div>
<div class="block">Export local (not teamwork) module into given descriptor</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#exportModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,com.nomagic.magicdraw.core.project.ProjectDescriptor)">exportModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>prj</code> - current project</dd>
<dd><code>packages</code> - "shared" packages in project</dd>
<dd><code>description</code> - module description</dd>
<dd><code>module</code> - module location descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporalSave)</span></div>
<div class="block">Save module from current project into given location.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">saveModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save</dd>
<dd><code>silent</code> - do not show UI messages</dd>
<dd><code>temporalSave</code> - do not change module location after save</dd>
<dt>Returns:</dt>
<dd>true if module was saved</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Saves module without any additional dependencies checking.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">saveModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save</dd>
<dd><code>silent</code> - save in silent mode</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if operation was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean temporalSave)</span></div>
<div class="block">Saves module without any additional dependencies checking.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">saveModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save</dd>
<dd><code>silent</code> - save in silent mode</dd>
<dd><code>status</code> - progress status</dd>
<dd><code>temporalSave</code> - do not change module location after save</dd>
<dt>Returns:</dt>
<dd>true if operation was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo)</span></div>
<div class="block">Saves module without any additional dependencies checking.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save</dd>
<dd><code>status</code> - status</dd>
<dd><code>silent</code> - save in silent mode</dd>
<dd><code>saveTo</code> - where to save module, can be null, then module is saved to module.getURI()
                location</dd>
<dt>Returns:</dt>
<dd>true if operation was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI,boolean)">
<h3>saveModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo,
 boolean temporalSave)</span></div>
<div class="block">Saves module without any additional dependencies checking.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module to save</dd>
<dd><code>silent</code> - save in silent mode</dd>
<dd><code>status</code> - progress status</dd>
<dd><code>saveTo</code> - where to save module, can be null, then module is saved to module.getURI() location</dd>
<dd><code>temporalSave</code> - do not change module location after save</dd>
<dt>Returns:</dt>
<dd>true if operation was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>unloadModule</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unloadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleDescriptor)</span></div>
<div class="block">Unload module</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">unloadModule</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>moduleDescriptor</code> - module descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProject(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>findAttachedProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
<div class="block">Find used module according given project descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project using module.</dd>
<dd><code>projectDescriptor</code> - project descriptor of module.</dd>
<dt>Returns:</dt>
<dd>found attached project or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>findProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">findProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
<div class="block">Find loaded project according given project descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectDescriptor</code> - project descriptor.</dd>
<dt>Returns:</dt>
<dd><code>null</code> if project not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sharePackage(com.nomagic.magicdraw.core.Project,java.util.List)">
<h3>sharePackage</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sharePackage</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)"><code>sharePackage(com.nomagic.magicdraw.core.Project, java.util.List, String)</code></a>.</div>
</div>
<div class="block">Share given list of packages in project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project where packages will be shared.</dd>
<dd><code>packages</code> - List of packaged, dedicated for sharing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sharePackage(com.nomagic.magicdraw.core.Project,java.util.List,java.lang.String)">
<h3>sharePackage</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sharePackage</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Share given list of packages in project. On CTS decomposition must be
 locked before sharing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project where packages will be shared.</dd>
<dd><code>packages</code> - List of packaged, dedicated for sharing.</dd>
<dd><code>description</code> - share description, null if do not change/set the description.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - if either some being shared package becomes invalid in the
                          main project (that is, has been deleted or moved to a module)
                          or is locked by another user</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>importProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">importProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</span></div>
<div class="block">Import project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">importProject</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pd</code> - project descriptor to import.</dd>
<dt>Returns:</dt>
<dd>true if project was imported</dd>
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
