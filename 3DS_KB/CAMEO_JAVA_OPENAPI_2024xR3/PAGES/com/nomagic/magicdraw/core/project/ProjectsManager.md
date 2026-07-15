# JAVA OPENAPI: ProjectsManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/project/ProjectsManager.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectsManager.html`
- source_sha256: `eaf0416ceffe51759bb63e58c8f5d217e009696c8e09cfa51104d80df39aeae8`
- captured_utc: `2026-07-14T16:55:13.729990+00:00`

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

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectsManager](#%3Cinit%3E())()`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addCreatedProject](#addCreatedProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Adds just created project to this manager, but this project activation event will not be fired, because it is still not loaded or initialized from template.
`void`
`[addProjectListener](#addProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](ProjectEventListener.html) listener)`
Adds new project listener.
`void`
`[closeProject](#closeProject())()`
Closes current project.
`void`
`[closeProject](#closeProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Closes given project
`void`
`[closeProjectNoSave](#closeProjectNoSave())()`
Close active project without trying to save it.
`void`
`[closeProjectNoSave](#closeProjectNoSave(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Close project without trying to save it.
`boolean`
`[contains](#contains(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Test if given path exists in projects list.
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
`[findProjectToActivate](#findProjectToActivate())()`
Find project to activate
`void`
`[fireProjectActivated](#fireProjectActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Notifies project event listeners that the given project is activated.
`void`
`[fireProjectActivatedFromGUI](#fireProjectActivatedFromGUI(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires project activated.
`void`
`[fireProjectClosed](#fireProjectClosed(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires project closed event.
`void`
`[fireProjectCreated](#fireProjectCreated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires event when project was created.
`void`
`[fireProjectDeactivated](#fireProjectDeactivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Notifies project event listeners that the given project is deactivated.
`void`
`[fireProjectModelLoaded](#fireProjectModelLoaded(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Fire event when project model is loaded but diagrams are still not loaded.
`void`
`[fireProjectOpened](#fireProjectOpened(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires event when project was opened.
`void`
`[fireProjectOpenedFromGUI](#fireProjectOpenedFromGUI(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires project open.
`void`
`[fireProjectPartAttached](#fireProjectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../modules/ModuleUsage.html) usage)`
Fire event when project or module started using new module.
`void`
`[fireProjectPartDetached](#fireProjectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../modules/ModuleUsage.html) usage)`
Fire event when project or module stops using module.
`void`
`[fireProjectPartLoaded](#fireProjectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject storage)`
Fire event when project model or its part is loaded with diagrams.
`void`
`[fireProjectPartRemoved](#fireProjectPartRemoved(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject storage)`
Fire event when project used project is removed from project
`void`
`[fireProjectPreActivated](#fireProjectPreActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Notifies project event listeners about project pre activation.
`void`
`[fireProjectPreClosed](#fireProjectPreClosed(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires project pre closed event.
`void`
`[fireProjectPreClosedFinal](#fireProjectPreClosedFinal(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method fires project pre closed final event.
`void`
`[fireProjectPreDeactivated](#fireProjectPreDeactivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Notifies project event listeners about project pre deactivation.
`void`
`[fireProjectPreSaved](#fireProjectPreSaved(com.nomagic.magicdraw.core.Project,boolean))([Project](../Project.html) project,
 boolean teamwork)`
Method fires project pre saved event.
`void`
`[fireProjectReplaced](#fireProjectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../Project.html) oldProject,
 [Project](../Project.html) newProject)`
Method fires the ProjectReplaced notification
`void`
`[fireProjectSaved](#fireProjectSaved(com.nomagic.magicdraw.core.Project,boolean))([Project](../Project.html) project,
 boolean teamwork)`
Method fires ProjectSaved event.
`void`
`[fireProjectUsedFromGUI](#fireProjectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)`

`[Project](../Project.html)`
`[getActiveProject](#getActiveProject())()`
Returns active open project.
`[Project](../Project.html)`
`[getEsiProject](#getEsiProject(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Returns ESI project if it is opened and it meets search criteria.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getNameForProject](#getNameForProject())()`
Getter for unique project name : Untitled+number
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getNameForProject](#getNameForProject(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) base,
 boolean avoidNumber)`
Getter for unique project name : "base"+number
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPreferredProjectPath](#getPreferredProjectPath(java.lang.String,com.nomagic.magicdraw.core.Project))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectName,
 [Project](../Project.html) relatedProject)`
Looks for possible path for project with a given name.
`[Project](../Project.html)`
`[getProject](#getProject(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Searches for given path in projects list and returns the project.
`[Project](../Project.html)`
`[getProject](#getProject(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Project](../Project.html)> filter)`
Look for a project for a given predicate.
`[Project](../Project.html)`
`[getProject](#getProject(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Searches for given uri in projects list and returns the project.
`[Project](../Project.html)`
`[getProjectByFileName](#getProjectByFileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)`
Look for a project with a given fileName.
`[Project](../Project.html)`
`[getProjectByName](#getProjectByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Look for a project with a given name.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Project](../Project.html)>`
`[getProjects](#getProjects())()`
Returns list of open projects.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRecentFilePath](#getRecentFilePath())()`
Returns recent file path or examples directory path
`[Project](../Project.html)`
`[getTeamworkProject](#getTeamworkProject(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Look for a teamwork project with a given id and version
`[Project](../Project.html)`
`[getTeamworkProject](#getTeamworkProject(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version,
 boolean checkLatest)`
Look for a teamwork project with a given id and version
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
`boolean`
`[isProjectLoaded](#isProjectLoaded(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Get if project is fully loaded.
`void`
`[loadProject](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 boolean silent)`
Loads project from location, described in a project descriptor.
`void`
`[loadProject](#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Loads new project from given descriptor.
`void`
`[reloadModule](#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) projectDescriptor)`
Reloads module.
`void`
`[removeProject](#removeProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Removes project from storage, does not activate previous one.
`void`
`[removeProjectListener](#removeProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](ProjectEventListener.html) listener)`
Removes project listener.
`void`
`[reportError](#reportError(java.lang.String,java.lang.Exception))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) ex)`

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
`boolean`
`[saveProject](#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean silent)`
Saves or commits project.
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
`void`
`[updateEnvironment](#updateEnvironment(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Updates GUI by given project.
`void`
`[updateEnvironment](#updateEnvironment(com.nomagic.magicdraw.core.Project,boolean))([Project](../Project.html) project,
 boolean wasAlreadyActivated)`
Updates GUI by given project.
`boolean`
`[useModule](#useModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) module)`
Use module in given project from given descriptor.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectsManager
public ProjectsManager()
Constructor.
 ============ METHOD DETAIL ========== 
Method Details
getProjects
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Project](../Project.html)> getProjects()
Returns list of open projects.
Returns:
list of open projects.
updateEnvironment
public void updateEnvironment(@CheckForNull
 [Project](../Project.html) project)
Updates GUI by given project.
Parameters:
`project` - project project
updateEnvironment
public void updateEnvironment(@CheckForNull
 [Project](../Project.html) project,
 boolean wasAlreadyActivated)
Updates GUI by given project.
Parameters:
`project` - project given project
`wasAlreadyActivated` - if project was already activated
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
addCreatedProject
public void addCreatedProject([Project](../Project.html) project)
Adds just created project to this manager, but this project activation event will not be fired, because it is still not loaded or initialized from template.
Parameters:
`project` - created project
getActiveProject
@OpenApi
@CheckForNullpublic [Project](../Project.html) getActiveProject()
Returns active open project.
Returns:
active project.
findProjectToActivate
@CheckForNullpublic [Project](../Project.html) findProjectToActivate()
Find project to activate
Returns:
active project.
removeProject
public void removeProject([Project](../Project.html) project)
Removes project from storage, does not activate previous one.
Parameters:
`project` - project project
getProjectByName
@CheckForNullpublic [Project](../Project.html) getProjectByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Look for a project with a given name.
Parameters:
`name` - the project name
Returns:
found project with given name or a null
getProjectByFileName
@CheckForNullpublic [Project](../Project.html) getProjectByFileName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)
Look for a project with a given fileName.
Parameters:
`fileName` - the project fileName
Returns:
found project with given fileName or a null
getProject
@CheckForNullpublic [Project](../Project.html) getProject([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Project](../Project.html)> filter)
Look for a project for a given predicate.
Parameters:
`filter` - predicate
Returns:
found project or a null. Active project is returned if it matches given predicate
getProject
@CheckForNullpublic [Project](../Project.html) getProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Searches for given path in projects list and returns the project.
Parameters:
`path` - path
Returns:
found project or null
getProject
@CheckForNullpublic [Project](../Project.html) getProject(org.eclipse.emf.common.util.URI uri)
Searches for given uri in projects list and returns the project.
Parameters:
`uri` - uri
Returns:
found project or null
getTeamworkProject
@CheckForNullpublic [Project](../Project.html) getTeamworkProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Look for a teamwork project with a given id and version
Parameters:
`projectID` - the project name
`version` - project version (-1 if not specified)
Returns:
found project
getTeamworkProject
@CheckForNullpublic [Project](../Project.html) getTeamworkProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version,
 boolean checkLatest)
Look for a teamwork project with a given id and version
Parameters:
`projectID` - the project name
`version` - project version (-1 if not specified)
`checkLatest` - flag if to check latest version or not, if version is null, it is not counted as other version if flag is false
Returns:
found project
getEsiProject
@CheckForNullpublic [Project](../Project.html) getEsiProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Returns ESI project if it is opened and it meets search criteria.
Parameters:
`projectID` - remote project id.
`version` - project version.
Returns:
project or null.
contains
public boolean contains([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Test if given path exists in projects list.
Parameters:
`path` - path
Returns:
true if exists
getNameForProject
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getNameForProject()
Getter for unique project name : Untitled+number
Returns:
unique project name
getNameForProject
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getNameForProject([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) base,
 boolean avoidNumber)
Getter for unique project name : "base"+number
Parameters:
`base` - base part of unique name
`avoidNumber` - avoid numbers
Returns:
unique name
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
public void loadProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Loads new project from given descriptor.
Specified by:
`[loadProject](ProjectPersistenceManager.html#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`descriptor` - descriptor
`status` - status monitor
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
saveProject
public boolean saveProject([ProjectDescriptor](ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean silent)
Description copied from interface: `[ProjectPersistenceManager](ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))`
Saves or commits project.
Specified by:
`[saveProject](ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`descriptor` - descriptor of project to save.
`status` - status to display operation status.
`silent` - true if no gui should be shown durring save/commmit
Returns:
false if saving fails.
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
closeProjectNoSave
public void closeProjectNoSave()
Close active project without trying to save it.
closeProjectNoSave
public void closeProjectNoSave(@CheckForNull
 [Project](../Project.html) project)
Close project without trying to save it.
Parameters:
`project` - project to close
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
getRecentFilePath
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRecentFilePath()
Returns recent file path or examples directory path
Returns:
recent file path
getPreferredProjectPath
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPreferredProjectPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectName,
 [Project](../Project.html) relatedProject)
Looks for possible path for project with a given name. Searches among recent projects for project with a given name.
 Also looks in given project (if not null) dir and modules path for a file with a given name.
Parameters:
`projectName` - the given project name
`relatedProject` - related project. Maybe be null
Returns:
preferred path to save a project
unloadModule
@OpenApipublic void unloadModule([Project](../Project.html) project,
 [ProjectDescriptor](ProjectDescriptor.html) moduleDescriptor)
Unload module
Specified by:
`[unloadModule](ProjectPersistenceManager.html#unloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor))` in interface `[ProjectPersistenceManager](ProjectPersistenceManager.html)`
Parameters:
`project` - project
`moduleDescriptor` - module descriptor
isProjectLoaded
public boolean isProjectLoaded([Project](../Project.html) project)
Get if project is fully loaded. We can not work with data while project is loading. Since
 project does not provide synchronization mechanism, we may get concurrent modification
 exceptions. Once project becomes "loaded" it stays loaded until closed.
Parameters:
`project` - project
Returns:
true when particular project is loaded and open - when PROJECT_OPENED event is fired.
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
fireProjectModelLoaded
public void fireProjectModelLoaded([Project](../Project.html) project)
Fire event when project model is loaded but diagrams are still not loaded.
Parameters:
`project` - project which model is loaded.
fireProjectPartLoaded
public void fireProjectPartLoaded([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject storage)
Fire event when project model or its part is loaded with diagrams.
 Event is fired when part of model is loaded and after teamwork update part is loaded and elements is removed.
Parameters:
`project` - the project
`storage` - the part of project is loaded.
fireProjectPartRemoved
public void fireProjectPartRemoved(com.nomagic.ci.persistence.IProject storage)
Fire event when project used project is removed from project
Parameters:
`storage` - the part of project which is removed
fireProjectPartAttached
public void fireProjectPartAttached([ModuleUsage](../modules/ModuleUsage.html) usage)
Fire event when project or module started using new module.
Parameters:
`usage` - added usage.
fireProjectPartDetached
public void fireProjectPartDetached([ModuleUsage](../modules/ModuleUsage.html) usage)
Fire event when project or module stops using module.
Parameters:
`usage` - removed usage.
reportError
public void reportError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) ex)
fireProjectActivated
public void fireProjectActivated([Project](../Project.html) project)
Notifies project event listeners that the given project is activated.
Parameters:
`project` - project that is activated.
fireProjectPreActivated
public void fireProjectPreActivated([Project](../Project.html) project)
Notifies project event listeners about project pre activation.
Parameters:
`project` - project that will be activated.
fireProjectDeactivated
public void fireProjectDeactivated([Project](../Project.html) project)
Notifies project event listeners that the given project is deactivated.
Parameters:
`project` - project that is deactivated.
fireProjectPreDeactivated
public void fireProjectPreDeactivated([Project](../Project.html) project)
Notifies project event listeners about project pre deactivation.
Parameters:
`project` - project that will be deactivated.
fireProjectOpened
public void fireProjectOpened([Project](../Project.html) project)
Method fires event when project was opened.
Parameters:
`project` - project which was opened.
fireProjectCreated
public void fireProjectCreated([Project](../Project.html) project)
Method fires event when project was created.
Parameters:
`project` - project which was created.
fireProjectSaved
public void fireProjectSaved([Project](../Project.html) project,
 boolean teamwork)
Method fires ProjectSaved event.
Parameters:
`project` - saved project.
`teamwork` - true if project saved in teamwork.
fireProjectPreSaved
public void fireProjectPreSaved([Project](../Project.html) project,
 boolean teamwork)
Method fires project pre saved event.
Parameters:
`project` - saved project.
`teamwork` - true if project saved in teamwork.
fireProjectReplaced
public void fireProjectReplaced([Project](../Project.html) oldProject,
 [Project](../Project.html) newProject)
Method fires the ProjectReplaced notification
Parameters:
`oldProject` - project, which was replaced
`newProject` - project, which replaced the old project
See Also:
[`ProjectEventListener.projectReplaced(Project, Project)`](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))
fireProjectClosed
public void fireProjectClosed([Project](../Project.html) project)
Method fires project closed event.
Parameters:
`project` - closed project.
fireProjectPreClosed
public void fireProjectPreClosed([Project](../Project.html) project)
Method fires project pre closed event.
Parameters:
`project` - closed project.
fireProjectPreClosedFinal
public void fireProjectPreClosedFinal([Project](../Project.html) project)
Method fires project pre closed final event.
Parameters:
`project` - closed project.
fireProjectOpenedFromGUI
public void fireProjectOpenedFromGUI([Project](../Project.html) project)
Method fires project open.
Parameters:
`project` - closed project.
fireProjectActivatedFromGUI
public void fireProjectActivatedFromGUI([Project](../Project.html) project)
Method fires project activated.
Parameters:
`project` - closed project.
fireProjectUsedFromGUI
public void fireProjectUsedFromGUI([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)

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
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectsManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCreatedProject(com.nomagic.magicdraw.core.Project)">addCreatedProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds just created project to this manager, but this project activation event will not be fired, because it is still not loaded or initialized from template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">addProjectListener</a><wbr/>(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new project listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProject()">closeProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes current project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProject(com.nomagic.magicdraw.core.Project)">closeProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProjectNoSave()">closeProjectNoSave</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close active project without trying to save it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProjectNoSave(com.nomagic.magicdraw.core.Project)">closeProjectNoSave</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close project without trying to save it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contains(java.lang.String)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test if given path exists in projects list.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findProjectToActivate()">findProjectToActivate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find project to activate</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectActivated(com.nomagic.magicdraw.core.Project)">fireProjectActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies project event listeners that the given project is activated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">fireProjectActivatedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project activated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectClosed(com.nomagic.magicdraw.core.Project)">fireProjectClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project closed event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectCreated(com.nomagic.magicdraw.core.Project)">fireProjectCreated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires event when project was created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectDeactivated(com.nomagic.magicdraw.core.Project)">fireProjectDeactivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies project event listeners that the given project is deactivated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectModelLoaded(com.nomagic.magicdraw.core.Project)">fireProjectModelLoaded</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire event when project model is loaded but diagrams are still not loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectOpened(com.nomagic.magicdraw.core.Project)">fireProjectOpened</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires event when project was opened.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">fireProjectOpenedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project open.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">fireProjectPartAttached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire event when project or module started using new module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">fireProjectPartDetached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire event when project or module stops using  module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject)">fireProjectPartLoaded</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject storage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire event when project model or its part is loaded with diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPartRemoved(com.nomagic.ci.persistence.IProject)">fireProjectPartRemoved</a><wbr/>(com.nomagic.ci.persistence.IProject storage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire event when project used project is removed from project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPreActivated(com.nomagic.magicdraw.core.Project)">fireProjectPreActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies project event listeners about project pre activation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPreClosed(com.nomagic.magicdraw.core.Project)">fireProjectPreClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project pre closed event.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPreClosedFinal(com.nomagic.magicdraw.core.Project)">fireProjectPreClosedFinal</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project pre closed final event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPreDeactivated(com.nomagic.magicdraw.core.Project)">fireProjectPreDeactivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies project event listeners about project pre deactivation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">fireProjectPreSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean teamwork)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires project pre saved event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">fireProjectReplaced</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires the ProjectReplaced notification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectSaved(com.nomagic.magicdraw.core.Project,boolean)">fireProjectSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean teamwork)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method fires ProjectSaved event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireProjectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">fireProjectUsedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveProject()">getActiveProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns active open project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEsiProject(java.lang.String,java.lang.String)">getEsiProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns ESI project if it is opened and it meets search criteria.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameForProject()">getNameForProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for unique project name : Untitled+number</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameForProject(java.lang.String,boolean)">getNameForProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> base,
 boolean avoidNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for unique project name : "base"+number</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredProjectPath(java.lang.String,com.nomagic.magicdraw.core.Project)">getPreferredProjectPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectName,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> relatedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for possible path for project with a given name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(java.lang.String)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches for given path in projects list and returns the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(java.util.function.Predicate)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt; filter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look for a project for a given predicate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(org.eclipse.emf.common.util.URI)">getProject</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches for given uri in projects list and returns the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectByFileName(java.lang.String)">getProjectByFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look for a project with a given fileName.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectByName(java.lang.String)">getProjectByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look for a project with a given name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjects()">getProjects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of open projects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecentFilePath()">getRecentFilePath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns recent file path or examples directory path</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTeamworkProject(java.lang.String,java.lang.String)">getTeamworkProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look for a teamwork project with a given id and version</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTeamworkProject(java.lang.String,java.lang.String,boolean)">getTeamworkProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 boolean checkLatest)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look for a teamwork project with a given id and version</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">importModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Import module into project from given descriptor</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">importProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Import project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectActive(com.nomagic.magicdraw.core.Project)">isProjectActive</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method checks if given project is active at this time.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectLoaded(com.nomagic.magicdraw.core.Project)">isProjectLoaded</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get if project is fully loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">loadProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads project from location, described in a project descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">loadProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads new project from given descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reloadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor)">reloadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reloads module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProject(com.nomagic.magicdraw.core.Project)">removeProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes project from storage, does not activate previous one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProjectListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">removeProjectListener</a><wbr/>(<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes project listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reportError(java.lang.String,java.lang.Exception)">reportError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> ex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 boolean temporalSave)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Save module from current project into given location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean temporalSave)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean,com.nomagic.task.ProgressStatus,java.net.URI,boolean)">saveModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean silent,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> saveTo,
 boolean temporalSave)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves module without any additional dependencies checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">saveProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves project into location specified by descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">saveProject</a><wbr/>(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves or commits project.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateEnvironment(com.nomagic.magicdraw.core.Project)">updateEnvironment</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates GUI by given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateEnvironment(com.nomagic.magicdraw.core.Project,boolean)">updateEnvironment</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean wasAlreadyActivated)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates GUI by given project.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectsManager</span>()</div>
<div class="block">Constructor.</div>
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
<section class="detail" id="updateEnvironment(com.nomagic.magicdraw.core.Project)">
<h3>updateEnvironment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateEnvironment</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Updates GUI by given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateEnvironment(com.nomagic.magicdraw.core.Project,boolean)">
<h3>updateEnvironment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateEnvironment</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean wasAlreadyActivated)</span></div>
<div class="block">Updates GUI by given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project given project</dd>
<dd><code>wasAlreadyActivated</code> - if project was already activated</dd>
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
<section class="detail" id="addCreatedProject(com.nomagic.magicdraw.core.Project)">
<h3>addCreatedProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCreatedProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Adds just created project to this manager, but this project activation event will not be fired, because it is still not loaded or initialized from template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - created project</dd>
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
<section class="detail" id="findProjectToActivate()">
<h3>findProjectToActivate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">findProjectToActivate</span>()</div>
<div class="block">Find project to activate</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>active project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProject(com.nomagic.magicdraw.core.Project)">
<h3>removeProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Removes project from storage, does not activate previous one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectByName(java.lang.String)">
<h3>getProjectByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Look for a project with a given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the project name</dd>
<dt>Returns:</dt>
<dd>found project with given name or a null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectByFileName(java.lang.String)">
<h3>getProjectByFileName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectByFileName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Look for a project with a given fileName.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the project fileName</dd>
<dt>Returns:</dt>
<dd>found project with given fileName or a null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.util.function.Predicate)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt; filter)</span></div>
<div class="block">Look for a project for a given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - predicate</dd>
<dt>Returns:</dt>
<dd>found project or a null. Active project is returned if it matches given predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.lang.String)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Searches for given path in projects list and returns the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dt>Returns:</dt>
<dd>found project or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(org.eclipse.emf.common.util.URI)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Searches for given uri in projects list and returns the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri</dd>
<dt>Returns:</dt>
<dd>found project or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTeamworkProject(java.lang.String,java.lang.String)">
<h3>getTeamworkProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getTeamworkProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Look for a teamwork project with a given id and version</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectID</code> - the project name</dd>
<dd><code>version</code> - project version (-1 if not specified)</dd>
<dt>Returns:</dt>
<dd>found project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTeamworkProject(java.lang.String,java.lang.String,boolean)">
<h3>getTeamworkProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getTeamworkProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 boolean checkLatest)</span></div>
<div class="block">Look for a teamwork project with a given id and version</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectID</code> - the project name</dd>
<dd><code>version</code> - project version (-1 if not specified)</dd>
<dd><code>checkLatest</code> - flag if to check latest version or not, if version is null, it is not counted as other version if flag is false</dd>
<dt>Returns:</dt>
<dd>found project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEsiProject(java.lang.String,java.lang.String)">
<h3>getEsiProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getEsiProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Returns ESI project if it is opened and it meets search criteria.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectID</code> - remote project id.</dd>
<dd><code>version</code> - project version.</dd>
<dt>Returns:</dt>
<dd>project or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(java.lang.String)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Test if given path exists in projects list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dt>Returns:</dt>
<dd>true if exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameForProject()">
<h3>getNameForProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameForProject</span>()</div>
<div class="block">Getter for unique project name : Untitled+number</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>unique project name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameForProject(java.lang.String,boolean)">
<h3>getNameForProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameForProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> base,
 boolean avoidNumber)</span></div>
<div class="block">Getter for unique project name : "base"+number</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>base</code> - base part of unique name</dd>
<dd><code>avoidNumber</code> - avoid numbers</dd>
<dt>Returns:</dt>
<dd>unique name</dd>
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
<section class="detail" id="loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">
<h3>loadProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Loads new project from given descriptor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#loadProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">loadProject</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>descriptor</code> - descriptor</dd>
<dd><code>status</code> - status monitor</dd>
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
<section class="detail" id="saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">
<h3>saveProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">saveProject</span><wbr/><span class="parameters">(<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean silent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">ProjectPersistenceManager</a></code></span></div>
<div class="block">Saves or commits project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPersistenceManager.html#saveProject(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">saveProject</a></code> in interface <code><a href="ProjectPersistenceManager.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPersistenceManager</a></code></dd>
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
<section class="detail" id="closeProjectNoSave()">
<h3>closeProjectNoSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeProjectNoSave</span>()</div>
<div class="block">Close active project without trying to save it.</div>
</section>
</li>
<li>
<section class="detail" id="closeProjectNoSave(com.nomagic.magicdraw.core.Project)">
<h3>closeProjectNoSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeProjectNoSave</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Close project without trying to save it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to close</dd>
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
<section class="detail" id="getRecentFilePath()">
<h3>getRecentFilePath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRecentFilePath</span>()</div>
<div class="block">Returns recent file path or examples directory path</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>recent file path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredProjectPath(java.lang.String,com.nomagic.magicdraw.core.Project)">
<h3>getPreferredProjectPath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPreferredProjectPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectName,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> relatedProject)</span></div>
<div class="block">Looks for possible path for project with a given name. Searches among recent projects for project with a given name.
 Also looks in given project (if not null) dir and modules path for a file with a given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectName</code> - the given project name</dd>
<dd><code>relatedProject</code> - related project. Maybe be null</dd>
<dt>Returns:</dt>
<dd>preferred path to save a project</dd>
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
<section class="detail" id="isProjectLoaded(com.nomagic.magicdraw.core.Project)">
<h3>isProjectLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isProjectLoaded</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Get if project is fully loaded. We can not work with data while project is loading. Since
 project does not provide synchronization mechanism, we may get concurrent modification
 exceptions. Once project becomes "loaded" it stays loaded until closed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true when particular project is loaded and open - when PROJECT_OPENED event is fired.</dd>
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
<li>
<section class="detail" id="fireProjectModelLoaded(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectModelLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectModelLoaded</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Fire event when project model is loaded but diagrams are still not loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which model is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject)">
<h3>fireProjectPartLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPartLoaded</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject storage)</span></div>
<div class="block">Fire event when project model or its part is loaded with diagrams.
 Event is fired when part of model is loaded and after teamwork update part is loaded and elements is removed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dd><code>storage</code> - the part of project is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPartRemoved(com.nomagic.ci.persistence.IProject)">
<h3>fireProjectPartRemoved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPartRemoved</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject storage)</span></div>
<div class="block">Fire event when project used project is removed from project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>storage</code> - the part of project which is removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>fireProjectPartAttached</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPartAttached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block">Fire event when project or module started using new module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - added usage.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>fireProjectPartDetached</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPartDetached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block">Fire event when project or module stops using  module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - removed usage.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reportError(java.lang.String,java.lang.Exception)">
<h3>reportError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reportError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> ex)</span></div>
</section>
</li>
<li>
<section class="detail" id="fireProjectActivated(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Notifies project event listeners that the given project is activated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project that is activated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPreActivated(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectPreActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPreActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Notifies project event listeners about project pre activation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project that will be activated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectDeactivated(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectDeactivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectDeactivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Notifies project event listeners that the given project is deactivated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project that is deactivated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPreDeactivated(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectPreDeactivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPreDeactivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Notifies project event listeners about project pre deactivation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project that will be deactivated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectOpened(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectOpened</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectOpened</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires event when project was opened.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectCreated(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectCreated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectCreated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires event when project was created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>fireProjectSaved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean teamwork)</span></div>
<div class="block">Method fires ProjectSaved event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - saved project.</dd>
<dd><code>teamwork</code> - true if project saved in teamwork.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>fireProjectPreSaved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPreSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean teamwork)</span></div>
<div class="block">Method fires project pre saved event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - saved project.</dd>
<dd><code>teamwork</code> - true if project saved in teamwork.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>fireProjectReplaced</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectReplaced</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</span></div>
<div class="block">Method fires the ProjectReplaced notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldProject</code> - project, which was replaced</dd>
<dd><code>newProject</code> - project, which replaced the old project</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectReplaced(Project, Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectClosed(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires project closed event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - closed project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPreClosed(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectPreClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPreClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires project pre closed event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - closed project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectPreClosedFinal(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectPreClosedFinal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectPreClosedFinal</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires project pre closed final event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - closed project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectOpenedFromGUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectOpenedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires project open.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - closed project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>fireProjectActivatedFromGUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectActivatedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method fires project activated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - closed project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireProjectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">
<h3>fireProjectUsedFromGUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">fireProjectUsedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)</span></div>
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
