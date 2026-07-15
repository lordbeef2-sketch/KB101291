# JAVA OPENAPI: EsiUtils (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/esi/EsiUtils.html
- source_path: `com/nomagic/magicdraw/esi/EsiUtils.html`
- source_sha256: `f1da30bfa59af7f376ddbf14afe64fd7b86b21d6cdc3efe522c68e9a6423b8d9`
- captured_utc: `2026-07-14T16:45:36.888493+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi](package-summary.html)

## Interface EsiUtils

@OpenApiAllpublic interfaceEsiUtils
API to work with Teamwork Cloud server. Before working with users and projects there must be established connection to Teamwork Cloud server.
 Connection is established with this code:
 `EsiUtils.getTeamworkService().login(new ServerLoginInfo("localhost", "user", "password", false), false);`

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[EsiUtils.ApplyProjectStateResult](EsiUtils.ApplyProjectStateResult.html)`
A structure that is produced by the [`applyProjectState(Project, Project)`](#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)) and
 which holds information about the result of the operation
`static interface`
`[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)`
Branch information.
`static class`
`[EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html)`
Offline project descriptor.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final com.nomagic.magicdraw.esi.project.project.EsiProjectRepository`
`[mProjectRepository](#mProjectRepository)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[NOTIFY_TAG_SEPARATOR](#NOTIFY_TAG_SEPARATOR)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[addCommitTags](#addCommitTags(java.util.List,com.nomagic.magicdraw.core.project.ProjectDescriptor,long))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)`
Add tags for given version.
`default com.nomagic.ci.persistence.IPrimaryProject`
`[addToESI](#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName)`
Add project to the Teamwork Cloud server and open it.
`com.nomagic.ci.persistence.IPrimaryProject`
`[addToESI](#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 boolean addStandardSystemProfiles)`
Add project to the Teamwork Cloud server and open it.
`static com.nomagic.ci.persistence.IPrimaryProject`
`[addToESI](#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ResolveLocalModuleInfo](../teamwork2/local2remote/ResolveLocalModuleInfo.html)> resolveInfos)`
Add project to the Teamwork Cloud server and open it
`static com.nomagic.ci.persistence.IPrimaryProject`
`[addToESI](#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection,com.nomagic.magicdraw.esi.session.RepositorySession))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ResolveLocalModuleInfo](../teamwork2/local2remote/ResolveLocalModuleInfo.html)> resolveInfos,
 com.nomagic.magicdraw.esi.session.RepositorySession session)`

`static [Project](../core/Project.html)`
`[addUpsToTwc](#addUpsToTwc(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Adds a UPS project to Teamwork Cloud (TWC).
`static [EsiUtils.ApplyProjectStateResult](EsiUtils.ApplyProjectStateResult.html)`
`[applyDisconnectedProjectState](#applyDisconnectedProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) source,
 [Project](../core/Project.html) target)`
Applies the state of the source project (local project) to the target project (TWCloud server project), or in other words, overwrites
 the content of the target project with the contents of the source project.
`static [EsiUtils.ApplyProjectStateResult](EsiUtils.ApplyProjectStateResult.html)`
`[applyProjectState](#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) source,
 [Project](../core/Project.html) target)`
Applies the state of the source project to the target project, or in other words, overwrites
 the content of the target project with the contents of the source project.
`void`
`[assignProjectToCategory](#assignProjectToCategory(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String...))([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)... categories)`
Adds or remove project to/from categories.
`org.eclipse.emf.common.util.URI`
`[cloneProject](#cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String))(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription)`
Clones project, new project is created it contains copy of source project with regenerated element ids.
`org.eclipse.emf.common.util.URI`
`[cloneProject](#cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String,java.util.UUID))(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription,
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) targetCategoryID)`
Clones project, new project is created it contains copy of source project with regenerated element ids.
`org.eclipse.emf.common.util.URI`
`[cloneProjectWithUsages](#cloneProjectWithUsages(org.eclipse.emf.common.util.URI,java.lang.String,java.util.Map,java.lang.String,java.util.UUID))(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> usedProjectTargetNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription,
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) targetCategoryID)`
Clones project and its usages, new projects are created, they contain copy of source project and its non standard/system usages with regenerated element ids.
`static void`
`[commitProject](#commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> unlockElements,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../core/modules/ModuleUsage.html)> unlockModules,
 boolean unlockDecomposition,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)`
Commit project.
`static void`
`[commitProject](#commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> unlockElements,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../core/modules/ModuleUsage.html)> unlockModules,
 boolean unlockDecomposition,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 [ProgressStatus](../../task/ProgressStatus.html) monitor)`
Commit project with progress.
`static [Project](../core/Project.html)`
`[convertToLocal](#convertToLocal(com.nomagic.magicdraw.core.Project,java.io.File))([Project](../core/Project.html) project,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Convert given project to local, save and reopen it.
`void`
`[createBranch](#createBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchDescription)`
Create new branch for given project.
`[CategoryInfo](../teamwork2/esi/CategoryInfo.html)`
`[createCategory](#createCategory(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)`
Create projects category in the server.
`[Project](../core/Project.html)`
`[createProject](#createProject(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category)`
Create Teamwork Cloud project.
`static [ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[createProjectDescriptorById](#createProjectDescriptorById(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Returns descriptor of project with given id
`void`
`[deleteBranch](#deleteBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName)`
Delete project branch.
`void`
`[deleteCategory](#deleteCategory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Delete category with given name.
`void`
`[deleteProject](#deleteProject(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) project)`
Delete project from repository.
`static com.nomagic.ci.persistence.IAttachedProject`
`[exportEsiModule](#exportEsiModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,java.lang.String))([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) moduleName)`
Exports module.
`static [EsiUtils](EsiUtils.html)`
`[get](#get())()`
Get instance from active session
`static [EsiUtils](EsiUtils.html)`
`[get](#get(com.nomagic.ci.persistence.IPrimaryProject))(com.nomagic.ci.persistence.IPrimaryProject primary)`
Get instance for provided project session
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.esi.api.info.TagInfo>`
`[getAllCommitTagsInfo](#getAllCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Get all tags for project.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)>`
`[getBranches](#getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Get all branches for given project.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)>`
`[getBranches](#getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../task/ProgressStatus.html) status)`
Get all branches for given project.
`static [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html)`
`[getBranchID](#getBranchID(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI locationURI)`
Gets project branch ID.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[CategoryInfo](../teamwork2/esi/CategoryInfo.html)>`
`[getCategories](#getCategories())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>>`
`[getCategoriesToProjects](#getCategoriesToProjects())()`
Get categories for projects.
`[CategoryInfo](../teamwork2/esi/CategoryInfo.html)`
`[getCategoryInfoByResourceID](#getCategoryInfoByResourceID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourceID)`
Get [`CategoryInfo`](../teamwork2/esi/CategoryInfo.html) for specified twc project resource ID.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getCommitTags](#getCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)`
Get tags names for project version.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.esi.api.info.TagInfo>`
`[getCommitTagsInfo](#getCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor,long))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)`
Get tags for project version.
`static [EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)`
`[getCurrentBranch](#getCurrentBranch(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Gets branch information for the given TWC project part.
`static [ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getDescriptorByBranchID](#getDescriptorByBranchID(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.UUID))([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) branchID)`
Get project descriptor for given branch.
`[ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getDescriptorForBranch](#getDescriptorForBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String))([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName)`
Get project descriptor for given branch.
`static [ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getDescriptorForVersion](#getDescriptorForVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) projectDescriptor,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor)`
Get descriptor for specific version.
`static org.eclipse.emf.common.util.URI`
`[getEMFURI](#getEMFURI(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor>`
`[getIVersionDescriptors](#getIVersionDescriptors(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI locationUri)`
Versions of given project
`long`
`[getLastVersion](#getLastVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Get last project version number.
`com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getLastVersionDescriptor](#getLastVersionDescriptor(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Get last project version descriptor.
`static [ILockProjectService](../teamwork2/locks/ILockProjectService.html)`
`[getLockService](#getLockService(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Provides api to check, request and release locks on various project data.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLoggedUserName](#getLoggedUserName())()`
Returns the currently logged Teamwork Cloud user name.
`static [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getLoggedUserNames](#getLoggedUserNames())()`
Get logged in users if current user has rights to access user list.
`[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)`
`[getNewEsiBranch](#getNewEsiBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchDescription)`
Create new branch for given project.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getNotifyOnNewTags](#getNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)`
Method returns application's notify tags about available project usage update.
`[EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html)`
`[getOfflineProject](#getOfflineProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Returns offline project descriptor of the specified project or null if the project is not saved to offline.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html)>`
`[getOfflineProjects](#getOfflineProjects())()`
Returns all available offline project descriptors.
`[PasswordManager](../teamwork2/esi/protect/PasswordManager.html)`
`[getPasswordManager](#getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Gets password manager for command line utilities
 If session is not present then `null` will be returned.
`[ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getProjectDescriptorByQualifiedName](#getProjectDescriptorByQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Returns project descriptor for given project qualified name.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>`
`[getProjectDescriptorsForEachBranch](#getProjectDescriptorsForEachBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)> branches,
 [ProgressStatus](../../task/ProgressStatus.html) status)`

`void`
`[getProjectDescriptorsWithBranches](#getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> descriptorsWithBranches)`
Collects all project descriptors with branch info for the given project descriptor into the provided collection.
`void`
`[getProjectDescriptorsWithBranches](#getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> descriptorsWithBranches,
 [ProgressStatus](../../task/ProgressStatus.html) status)`
Collects all project descriptors with branch info for the given project descriptor into the provided collection.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>`
`[getProjectDescriptorsWithBranches](#getProjectDescriptorsWithBranches(java.lang.Iterable))([Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> projectDescriptors)`
Invocation of this method returns a [`Collection`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) of [`ProjectDescriptor`](../core/project/ProjectDescriptor.html)s of each
 branch in the given `projectDescriptors`.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>`
`[getProjectDescriptorsWithBranchesByProjectID](#getProjectDescriptorsWithBranchesByProjectID(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> projectIDs)`
Returns project descriptors with available branches for given project IDs.
`default [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProjectIdByQualifiedName](#getProjectIdByQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Returns project id.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProjectName](#getProjectName(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI locationURI)`
Return project name for given URI.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>`
`[getRemoteProjectDescriptors](#getRemoteProjectDescriptors())()`
Returns descriptors of projects stored on server.
`static [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html)`
`[getResourceID](#getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) projectDescriptor)`

`static [ConnectionInfo](session/ConnectionInfo.html)`
`[getServerInfo](#getServerInfo(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Get server information for given project
`static [ITeamworkService](../teamwork2/ITeamworkService.html)`
`[getTeamworkService](#getTeamworkService())()`
Get service for working with Teamwork Cloud.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getUserNames](#getUserNames())()`
Get all users if current user has rights to access user list.
`com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getVersion](#getVersion(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Current version of given project
`default [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor>`
`[getVersions](#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Get all versions of given project.
`static boolean`
`[isModuleUsageNew](#isModuleUsageNew(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject fromProject,
 com.nomagic.ci.persistence.IProject toProject)`
Checks if the project usage exists and is new (not yet committed to server).
`static boolean`
`[isNotifyOnNew](#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)`
Method returns if application should notify about available project usage update.
`static boolean`
`[isProjectChanged](#isProjectChanged(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Method returns `true` when twcloud project has some changed objects in its resource,
 or local project's `StateChangeHandler.isDirty(IProject)` returns `true`
`static [Project](../core/Project.html)`
`[loadFromOffline](#loadFromOffline(com.nomagic.magicdraw.esi.EsiUtils.OfflineProjectDescriptor,com.nomagic.task.ProgressStatus))([EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html) descriptor,
 [ProgressStatus](../../task/ProgressStatus.html) status)`
Loads the offline project.
`static void`
`[moveToUsedProject](#moveToUsedProject(com.nomagic.magicdraw.core.Project,java.util.Map,boolean))([Project](../core/Project.html) project,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[PackageableElement](../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html),[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> moveMap,
 boolean silentMode)`
Moves elements to used project(s).
`void`
`[removeCommitTags](#removeCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)`
Remove all tags from project version.
`static [EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html)`
`[saveToOffline](#saveToOffline(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus,boolean))([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) status,
 boolean delete)`
Saves the specified project to offline.
`static void`
`[setNotifyOnNew](#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 boolean notifyOnNew)`
Method sets if application should notify about available project usage update.
`static void`
`[setNotifyOnNewTags](#setNotifyOnNewTags(com.nomagic.ci.persistence.IPrimaryProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection))(com.nomagic.ci.persistence.IPrimaryProject project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)`
Method sets application's notify tags about available project usage update.
`static void`
`[setNotifyOnNewTags](#setNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)`
Method sets application's notify tags about available project usage update.
`static void`
`[setProjectName](#setProjectName(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String))([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newName)`
Rename project.
`static void`
`[updateModule](#updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.project.ProjectDescriptor,long))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)`
Change given module to another version or branch.
`static void`
`[updateModule](#updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,org.eclipse.emf.common.util.URI,long))([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 org.eclipse.emf.common.util.URI updateFrom,
 long version)`
Change given module to another version or branch.
`static void`
`[updateProject](#updateProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Updates given project.
`static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<com.nomagic.ci.persistence.IAttachedProject,[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)>`
`[updateRequiredProjectUsages](#updateRequiredProjectUsages(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
This method updates project usages to newest version.

============ FIELD DETAIL =========== 
Field Details
mProjectRepository
static final com.nomagic.magicdraw.esi.project.project.EsiProjectRepository mProjectRepository
NOTIFY_TAG_SEPARATOR
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) NOTIFY_TAG_SEPARATOR
 ============ METHOD DETAIL ========== 
Method Details
get
static [EsiUtils](EsiUtils.html) get()
Get instance from active session
Returns:
EsiUtils instance
get
static [EsiUtils](EsiUtils.html) get(com.nomagic.ci.persistence.IPrimaryProject primary)
Get instance for provided project session
Parameters:
`primary` - project
Returns:
EsiUtils instance
getTeamworkService
static [ITeamworkService](../teamwork2/ITeamworkService.html) getTeamworkService()
Get service for working with Teamwork Cloud.
Returns:
service for working with Teamwork Cloud.
getLockService
@CheckForNullstatic [ILockProjectService](../teamwork2/locks/ILockProjectService.html) getLockService(@CheckForNull
 [Project](../core/Project.html) project)
Provides api to check, request and release locks on various project data.
Returns:
lock service.
createProject
@CheckForNull[Project](../core/Project.html) createProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category)
 throws com.nomagic.ci.persistence.PersistenceException
Create Teamwork Cloud project. Project is created only if currently logged user rights allows to create projects.
Parameters:
`name` - project name.
`category` - project category.
Returns:
crated project.
Throws:
`com.nomagic.ci.persistence.PersistenceException`
commitProject
static void commitProject([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> unlockElements,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../core/modules/ModuleUsage.html)> unlockModules,
 boolean unlockDecomposition,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)
Commit project.
Parameters:
`project` - project
`comment` - comment.
`unlockElements` - elements to unlock when committing. The collection specifies which locked elements should be unlocked after successful commit.
 `null` means that no elements should be unlocked.
`unlockModules` - modules to unlock when committing. The collection specifies which project usages (modules) should be unlocked after successful commit.
 `null` means that no project usages should be unlocked.
`unlockDecomposition` - true if decomposition needs to be unlocked when committing.
`tags` - version tags to set.
commitProject
static void commitProject([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> unlockElements,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../core/modules/ModuleUsage.html)> unlockModules,
 boolean unlockDecomposition,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 @CheckForNull
 [ProgressStatus](../../task/ProgressStatus.html) monitor)
Commit project with progress.
Parameters:
`project` - project
`comment` - comment.
`unlockElements` - elements to unlock when committing. The collection specifies which locked elements should be unlocked after successful commit.
 `null` means that no elements should be unlocked.
`unlockModules` - modules to unlock when committing. The collection specifies which project usages (modules) should be unlocked after successful commit.
 `null` means that no project usages should be unlocked.
`unlockDecomposition` - true if decomposition needs to be unlocked when committing.
`tags` - version tags to set.
`monitor` - progress status monitor.
exportEsiModule
@CheckForNullstatic com.nomagic.ci.persistence.IAttachedProject exportEsiModule([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) moduleName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Exports module.
Parameters:
`project` - project.
`packages` - packages to export.
`description` - module description.
`moduleName` - name of module.
Returns:
exported module attached project.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
getRemoteProjectDescriptors
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> getRemoteProjectDescriptors()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns descriptors of projects stored on server.
Returns:
list of remote project descriptors.
Throws:
`[RemoteException](https://docs.oracle.com/en/java/javase/21/docs/api/java.rmi/java/rmi/RemoteException.html)` - in case of some problem
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
getProjectIdByQualifiedName
@CheckForNulldefault [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProjectIdByQualifiedName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns project id.
Parameters:
`qualifiedName` - project qualified name, unique name constructed from project name and it's branches.
 E.g:
 "MyProject" with no branches = "MyProject" 

 "MyProject" branch ["release"] = "MyProject##release" 

 "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"
Returns:
project id
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getProjectDescriptorByQualifiedName
@CheckForNull[ProjectDescriptor](../core/project/ProjectDescriptor.html) getProjectDescriptorByQualifiedName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns project descriptor for given project qualified name.
Parameters:
`qualifiedName` - project qualified name, unique name constructed from project name and its branches.
 Examples:
 "MyProject" with no branches = "MyProject"
 "MyProject" branch ["release"] = "MyProject##release"
 "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"
Returns:
ProjectDescriptor
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getVersions
default [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor> getVersions([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Get all versions of given project.
Parameters:
`descriptor` - project descriptor.
Returns:
list of version information.
addCommitTags
void addCommitTags([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)
Add tags for given version.
Parameters:
`tags` - tags to add.
`descriptor` - project for which version tags is set.
`version` - version for which tags will be added.
getCommitTags
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getCommitTags([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)
Get tags names for project version.
Parameters:
`descriptor` - project descriptor.
`version` - version.
Returns:
list of tags for given version.
getCommitTagsInfo
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.esi.api.info.TagInfo> getCommitTagsInfo([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)
Get tags for project version.
Parameters:
`descriptor` - project descriptor.
`version` - version.
Returns:
list of tags for given version.
getAllCommitTagsInfo
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.esi.api.info.TagInfo> getAllCommitTagsInfo([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Get all tags for project.
Parameters:
`descriptor` - project descriptor.
Returns:
list of tags for given version.
removeCommitTags
void removeCommitTags([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)
Remove all tags from project version.
Parameters:
`descriptor` - project descriptor.
`version` - version.
updateProject
static void updateProject([Project](../core/Project.html) project)
Updates given project. Project is activated before update.
Parameters:
`project` - teamwork project to update.
getProjectName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProjectName(org.eclipse.emf.common.util.URI locationURI)
Return project name for given URI.
Parameters:
`locationURI` - project location.
Returns:
project name.
setProjectName
static void setProjectName([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newName)
 throws com.nomagic.ci.persistence.PersistenceException
Rename project.
Parameters:
`project` - project descriptor
`newName` - new project name.
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some problem
deleteProject
void deleteProject([ProjectDescriptor](../core/project/ProjectDescriptor.html) project)
 throws com.nomagic.ci.persistence.PersistenceException
Delete project from repository.
Parameters:
`project` - project to delete.
Throws:
`com.nomagic.ci.persistence.PersistenceException`
getCategories
[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[CategoryInfo](../teamwork2/esi/CategoryInfo.html)> getCategories()
Returns:
all categories from server.
getCategoriesToProjects
[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>> getCategoriesToProjects()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Get categories for projects.
Returns:
projects in categories.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
getCategoryInfoByResourceID
@CheckForNull[CategoryInfo](../teamwork2/esi/CategoryInfo.html) getCategoryInfoByResourceID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resourceID)
Get [`CategoryInfo`](../teamwork2/esi/CategoryInfo.html) for specified twc project resource ID.
Parameters:
`resourceID` - twc project resource ID
Returns:
instance of [`CategoryInfo`](../teamwork2/esi/CategoryInfo.html) or `null`
createCategory
[CategoryInfo](../teamwork2/esi/CategoryInfo.html) createCategory([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) description)
Create projects category in the server.
Parameters:
`name` - category name
`description` - category description
assignProjectToCategory
void assignProjectToCategory([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)... categories)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Adds or remove project to/from categories. After this method project belongs only to categories specified for this method.
Parameters:
`project` - project to assign or remove from category.
`categories` - categories to which project will be assigned.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
deleteCategory
void deleteCategory([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Delete category with given name.
Parameters:
`name` - category name.
getBranches
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)> getBranches([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Get all branches for given project.
Parameters:
`descriptor` - project descriptor.
Returns:
branches for given project.
getBranches
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)> getBranches([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [ProgressStatus](../../task/ProgressStatus.html) status)
Get all branches for given project.
Parameters:
`descriptor` - project descriptor.
`status` - progress status.
Returns:
branches for given project.
createBranch
void createBranch([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchDescription)
Create new branch for given project.
Parameters:
`descriptor` - project descriptor.
`version` - version from which branch
`branchName` - new branch name.
`branchDescription` - description of new branch.
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)` - in case network or server error occurs when creating branch.
`[InsufficientPermissionsException](InsufficientPermissionsException.html)` - if currently logged in user does not have *Administer Resources* permission
getNewEsiBranch
[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html) getNewEsiBranch([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchDescription)
Create new branch for given project.
Parameters:
`descriptor` - project descriptor.
`version` - version from which branch
`branchName` - new branch name.
`branchDescription` - description of new branch.
Returns:
branch info for specified branch
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)` - in case network or server error occurs when creating branch.
`[InsufficientPermissionsException](InsufficientPermissionsException.html)` - if currently logged in user does not have *Administer Resources* permission
getDescriptorByBranchID
static [ProjectDescriptor](../core/project/ProjectDescriptor.html) getDescriptorByBranchID([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) branchID)
Get project descriptor for given branch. This descriptor can be used to load project from branch.
Parameters:
`project` - project descriptor.
`branchID` - branch id.
Returns:
project descriptor for given branch.
getResourceID
static [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) getResourceID([ProjectDescriptor](../core/project/ProjectDescriptor.html) projectDescriptor)
getDescriptorForBranch
[ProjectDescriptor](../core/project/ProjectDescriptor.html) getDescriptorForBranch([ProjectDescriptor](../core/project/ProjectDescriptor.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName)
Get project descriptor for given branch. This descriptor can be used to load project from branch.
Parameters:
`project` - project descriptor.
`branchName` - branch name.
Returns:
project descriptor for given branch.
getDescriptorForVersion
static [ProjectDescriptor](../core/project/ProjectDescriptor.html) getDescriptorForVersion([ProjectDescriptor](../core/project/ProjectDescriptor.html) projectDescriptor,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor)
Get descriptor for specific version. Can be used to open historic project version.
Parameters:
`projectDescriptor` - project descriptor.
`versionDescriptor` - version.
Returns:
descriptor for specific version.
deleteBranch
void deleteBranch([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) branchName)
Delete project branch.
Parameters:
`descriptor` - project which branch will be deleted.
`branchName` - branch name to delete.
Throws:
`[InsufficientPermissionsException](InsufficientPermissionsException.html)` - if currently logged in user does not have *Administer Resources* permission
addToESI
default com.nomagic.ci.persistence.IPrimaryProject addToESI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName)
 throws com.nomagic.ci.persistence.PersistenceException
Add project to the Teamwork Cloud server and open it.
Parameters:
`project` - project to add.
`esiProjectName` - project name in teamwork cloud server.
Returns:
opened teamwork cloud project.
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some problem
addToESI
com.nomagic.ci.persistence.IPrimaryProject addToESI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 boolean addStandardSystemProfiles)
 throws com.nomagic.ci.persistence.PersistenceException
Add project to the Teamwork Cloud server and open it.
Parameters:
`project` - project to add.
`esiProjectName` - project name in teamwork cloud server.
`addStandardSystemProfiles` - if to add standard/system profiles too.
Returns:
opened teamwork cloud project.
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some problem
addToESI
static com.nomagic.ci.persistence.IPrimaryProject addToESI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 @Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ResolveLocalModuleInfo](../teamwork2/local2remote/ResolveLocalModuleInfo.html)> resolveInfos,
 @CheckForNull
 com.nomagic.magicdraw.esi.session.RepositorySession session)
 throws com.nomagic.ci.persistence.PersistenceException
Throws:
`com.nomagic.ci.persistence.PersistenceException`
addToESI
static com.nomagic.ci.persistence.IPrimaryProject addToESI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) esiProjectName,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags,
 @Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ResolveLocalModuleInfo](../teamwork2/local2remote/ResolveLocalModuleInfo.html)> resolveInfos)
 throws com.nomagic.ci.persistence.PersistenceException
Add project to the Teamwork Cloud server and open it
Parameters:
`project` - the project to add
`esiProjectName` - the name for the new Teamwork Cloud project
`category` - the category to add the project to
`comment` - the commit comment
`tags` - the commit tags
`resolveInfos` - the module resolve info list
Returns:
the added project
Throws:
`com.nomagic.ci.persistence.PersistenceException` - exception if add fails
convertToLocal
@CheckForNullstatic [Project](../core/Project.html) convertToLocal([Project](../core/Project.html) project,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Convert given project to local, save and reopen it.
Parameters:
`project` - project to convert
`file` - project file
Returns:
local project
getLoggedUserName
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLoggedUserName()
Returns the currently logged Teamwork Cloud user name.
Returns:
user name
getServerInfo
@CheckForNullstatic [ConnectionInfo](session/ConnectionInfo.html) getServerInfo([Project](../core/Project.html) project)
Get server information for given project
Parameters:
`project` - project
Returns:
server information or null when project is not server project
getLoggedUserNames
static [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getLoggedUserNames()
Get logged in users if current user has rights to access user list.
Returns:
all user names.
getUserNames
[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getUserNames()
Get all users if current user has rights to access user list.
Returns:
logged in user names.
updateModule
static void updateModule([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 long version)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Change given module to another version or branch.
Parameters:
`project` - project which module is switched.
`module` - module to switch.
`descriptor` - new module descriptor.
`version` - new module version
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
updateModule
static void updateModule([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject module,
 org.eclipse.emf.common.util.URI updateFrom,
 long version)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Change given module to another version or branch.
Parameters:
`project` - project which module is switched.
`module` - module to switch.
`updateFrom` - project location URI.
`version` - new module version
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
setNotifyOnNew
static void setNotifyOnNew([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 boolean notifyOnNew)
Method sets if application should notify about available project usage update.
Parameters:
`project` - Project to which usage setting is applied.
`iAttachedProject` - Usage's attached project to which setting is applied.
`notifyOnNew` - Should notification be shown.
isNotifyOnNew
static boolean isNotifyOnNew([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)
Method returns if application should notify about available project usage update.
 Return `false` by default.
Parameters:
`project` - Project to which's usage setting is applied.
`iAttachedProject` - Usage's attached project to which setting is applied.
Returns:
Should notification be shown. Returns `false` by default.
isProjectChanged
static boolean isProjectChanged([Project](../core/Project.html) project)
Method returns `true` when twcloud project has some changed objects in its resource,
 or local project's `StateChangeHandler.isDirty(IProject)` returns `true`
Parameters:
`project` - project to check for presence of changes
Returns:
`true` when project is changed
addUpsToTwc
@CheckForNullstatic [Project](../core/Project.html) addUpsToTwc([Project](../core/Project.html) project)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Adds a UPS project to Teamwork Cloud (TWC).

 This method converts a UPS project to a TWC project and imports it directly into the TWC server.

 The project state must be suitable for exporting, meaning that the project should be in a consistent state
 with no unsaved changes.
Parameters:
`project` - the project to be added to TWC
Returns:
the project that was added to TWC
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if there is an error during the conversion or import process
setNotifyOnNewTags
static void setNotifyOnNewTags([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)
Method sets application's notify tags about available project usage update.
Parameters:
`project` - Project to which's usage setting is applied.
`iAttachedProject` - Usage's attached project to which setting is applied.
`tags` - Notify tags.
setNotifyOnNewTags
static void setNotifyOnNewTags(com.nomagic.ci.persistence.IPrimaryProject project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> tags)
Method sets application's notify tags about available project usage update.
Parameters:
`project` - Project to which's usage setting is applied.
`iAttachedProject` - Usage's attached project to which setting is applied.
`tags` - Notify tags.
getNotifyOnNewTags
@CheckForNullstatic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getNotifyOnNewTags([Project](../core/Project.html) project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)
Method returns application's notify tags about available project usage update.
Parameters:
`project` - Project to which's usage setting is applied.
`iAttachedProject` - Usage's attached project to which setting is applied.
Returns:
Notify tags.
isModuleUsageNew
static boolean isModuleUsageNew(com.nomagic.ci.persistence.IProject fromProject,
 com.nomagic.ci.persistence.IProject toProject)
Checks if the project usage exists and is new (not yet committed to server).
Parameters:
`fromProject` - the project the usage should be from
`toProject` - the project the usage should be to
Returns:
`true` if the usage from specifed project exists to specified to project
 and if the specified to project is not `null` and if the usage is new
 (as defined above). Return `false` othewise
updateRequiredProjectUsages
static [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<com.nomagic.ci.persistence.IAttachedProject,[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)> updateRequiredProjectUsages([Project](../core/Project.html) project)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
This method updates project usages to newest version. Only usages which have [`isNotifyOnNew(Project, IAttachedProject)`](#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject))
 set to `true` are updated. It can be changed using [`setNotifyOnNew(Project, IAttachedProject, boolean)`](#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean)). If project
 usages is locked by other user or can't be updated for other reasons its update will be skipped.
Parameters:
`project` - Project which usages are updated.
Returns:
Results map. Key - attached project which was updated, value - was update successful.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some problem
See Also:
[`isNotifyOnNew(Project, IAttachedProject)`](#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject))
[`setNotifyOnNew(Project, IAttachedProject, boolean)`](#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean))
applyProjectState
static [EsiUtils.ApplyProjectStateResult](EsiUtils.ApplyProjectStateResult.html) applyProjectState([Project](../core/Project.html) source,
 [Project](../core/Project.html) target)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html),
[ElementLockAcquisitionException](../teamwork2/locks/ElementLockAcquisitionException.html),
[ModuleUsageLockAcquisitionException](../teamwork2/locks/ModuleUsageLockAcquisitionException.html),
[OptionsLockAcquisitionException](../teamwork2/locks/OptionsLockAcquisitionException.html)
Applies the state of the source project to the target project, or in other words, overwrites
 the content of the target project with the contents of the source project. The elements that
 are matched are updated, the not existing elements are removed, and new elements are added.
 Module usages are copied and modules are updated accordingly. To perform the operation
 successfully, all elements of the project, module usages, and options are locked. Any lock
 failure terminates the operation with a specific exception
Parameters:
`source` - the source project from which the state is copied
`target` - the target project to which the state is copied
Returns:
a structure that holds the result of the operation
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if: 1. the projects are the same, 2. any of the projects are
 not ready, 3. any of the projects is not an Teamwork Cloud project, 4. the project IDs
 differ, 5. the target project is not editable
`[ElementLockAcquisitionException](../teamwork2/locks/ElementLockAcquisitionException.html)` - if specific element could not be locked
`[ModuleUsageLockAcquisitionException](../teamwork2/locks/ModuleUsageLockAcquisitionException.html)` - if specific module usage could not be locked
`[OptionsLockAcquisitionException](../teamwork2/locks/OptionsLockAcquisitionException.html)` - if specific options could not be locked
applyDisconnectedProjectState
static [EsiUtils.ApplyProjectStateResult](EsiUtils.ApplyProjectStateResult.html) applyDisconnectedProjectState([Project](../core/Project.html) source,
 [Project](../core/Project.html) target)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html),
[ElementLockAcquisitionException](../teamwork2/locks/ElementLockAcquisitionException.html),
[ModuleUsageLockAcquisitionException](../teamwork2/locks/ModuleUsageLockAcquisitionException.html),
[OptionsLockAcquisitionException](../teamwork2/locks/OptionsLockAcquisitionException.html)
Applies the state of the source project (local project) to the target project (TWCloud server project), or in other words, overwrites
 the content of the target project with the contents of the source project. The elements that
 are matched are updated, the not existing elements are removed, and new elements are added.
 Module usages are copied and modules are updated accordingly. To perform the operation
 successfully, all elements of the project, module usages, and options are locked. Any lock
 failure terminates the operation with a specific exception
Parameters:
`source` - the source project (local project) from which the state is copied
`target` - the target project (server project) to which the state is copied
Returns:
a structure that holds the result of the operation
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if: 1. the projects are the same, 2. any of the projects are
 not ready, 3. the project IDs
 differ, 4. the target project is not editable
`[ElementLockAcquisitionException](../teamwork2/locks/ElementLockAcquisitionException.html)` - if specific element could not be locked
`[ModuleUsageLockAcquisitionException](../teamwork2/locks/ModuleUsageLockAcquisitionException.html)` - if specific module usage could not be locked
`[OptionsLockAcquisitionException](../teamwork2/locks/OptionsLockAcquisitionException.html)` - if specific options could not be locked
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)` - if the method invocation fails because of another reason. Cause of the exception
 should be checked in order find the actual reason of the failure.
getLastVersion
long getLastVersion([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Get last project version number.
Parameters:
`descriptor` - project descriptor for Teamwork Cloud server project.
Returns:
last project version number, -1 - there is no such project or application is not connected to the server.
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)` - in case provided descriptor is not valid for current server.
getLastVersionDescriptor
@CheckForNullcom.nomagic.ci.persistence.versioning.IVersionDescriptor getLastVersionDescriptor([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Get last project version descriptor.
Parameters:
`descriptor` - project descriptor for Teamwork Cloud server project.
Returns:
last project version descriptor, `null` - when there is no such project or application is not connected to the server.
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)` - in case provided descriptor is not valid for current server.
getProjectDescriptorsWithBranches
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> getProjectDescriptorsWithBranches([Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> projectDescriptors)
Invocation of this method returns a [`Collection`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) of [`ProjectDescriptor`](../core/project/ProjectDescriptor.html)s of each
 branch in the given `projectDescriptors`.
Parameters:
`projectDescriptors` - descriptors of the projects, whose branch [`ProjectDescriptor`](../core/project/ProjectDescriptor.html)s should
 be returned
Returns:
project descriptors for each branch of the given `projectDescriptors`
getProjectDescriptorsWithBranchesByProjectID
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> getProjectDescriptorsWithBranchesByProjectID([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> projectIDs)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns project descriptors with available branches for given project IDs.
Parameters:
`projectIDs` - list of project IDs
Returns:
project descriptors with available branches
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any occurs
cloneProject
@CheckForNullorg.eclipse.emf.common.util.URI cloneProject(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Clones project, new project is created it contains copy of source project with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.
Parameters:
`sourceURI` - source project URI
`targetName` - target project name
`targetDescription` - target project description
Returns:
cloned project URI
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - exception in case clone fails
cloneProject
@CheckForNullorg.eclipse.emf.common.util.URI cloneProject(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription,
 @CheckForNull
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) targetCategoryID)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Clones project, new project is created it contains copy of source project with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.
Parameters:
`sourceURI` - source project URI
`targetName` - target project name
`targetDescription` - target project description
`targetCategoryID` - target project category ID
Returns:
cloned project URI
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - exception in case clone fails
cloneProjectWithUsages
@CheckForNullorg.eclipse.emf.common.util.URI cloneProjectWithUsages(org.eclipse.emf.common.util.URI sourceURI,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> usedProjectTargetNames,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) targetDescription,
 @CheckForNull
 [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) targetCategoryID)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Clones project and its usages, new projects are created, they contain copy of source project and its non standard/system usages with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.
Parameters:
`sourceURI` - source project URI
`targetName` - target project name
`usedProjectTargetNames` - used project target names map. Key - used project id, value - target name
`targetDescription` - target project description
`targetCategoryID` - target project category ID
Returns:
cloned project URI
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - exception in case clone fails
getProjectDescriptorsWithBranches
void getProjectDescriptorsWithBranches([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> descriptorsWithBranches)
Collects all project descriptors with branch info for the given project descriptor into the provided collection.
Parameters:
`descriptor` - project descriptor for which to collect project descriptors with branch info
`descriptorsWithBranches` - collection where to add the result
getProjectDescriptorsWithBranches
void getProjectDescriptorsWithBranches([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> descriptorsWithBranches,
 [ProgressStatus](../../task/ProgressStatus.html) status)
Collects all project descriptors with branch info for the given project descriptor into the provided collection.
Parameters:
`descriptor` - project descriptor for which to collect project descriptors with branch info
`descriptorsWithBranches` - collection where to add the result
`status` - progress status
getOfflineProject
@CheckForNull[EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html) getOfflineProject([Project](../core/Project.html) project)
Returns offline project descriptor of the specified project or null if the project is not saved to offline.
Parameters:
`project` - a project.
Returns:
offline project descriptor.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the specified project is not a TWC project.
getOfflineProjects
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html)> getOfflineProjects()
Returns all available offline project descriptors.
Returns:
collection of offline project descriptors.
getProjectDescriptorsForEachBranch
static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> getProjectDescriptorsForEachBranch([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html)> branches,
 [ProgressStatus](../../task/ProgressStatus.html) status)
getBranchID
static [UUID](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html) getBranchID(org.eclipse.emf.common.util.URI locationURI)
Gets project branch ID.
Parameters:
`locationURI` - project location URI
Returns:
branch ID
moveToUsedProject
static void moveToUsedProject([Project](../core/Project.html) project,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[PackageableElement](../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html),[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> moveMap,
 boolean silentMode)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Moves elements to used project(s). The moved elements must be lockable by user, and must have an owner.
 The target package(s) must be in the directly used project, and be lockable by user. Each moved element can be moved to a different target package.
 In addition to the specified elements, additional elements (such as interrelations) might be selected to be moved together.
 See `MoveRelationManager.collectRelationsToMove(java.util.Map<com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element>)`.
Parameters:
`project` - the main project
`moveMap` - elements move map
`silentMode` - if true, will move in silent mode
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case moving elements fails
getCurrentBranch
@CheckForNullstatic [EsiUtils.EsiBranchInfo](EsiUtils.EsiBranchInfo.html) getCurrentBranch(com.nomagic.ci.persistence.IProject project)
Gets branch information for the given TWC project part. If TWC project
 part is not linked with TWC project (like standard profiles) or user has no permission to read then
 `null` will be returned.
Parameters:
`project` - project part
Returns:
branch information
getPasswordManager
@CheckForNull[PasswordManager](../teamwork2/esi/protect/PasswordManager.html) getPasswordManager([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
Gets password manager for command line utilities
 If session is not present then `null` will be returned.
Parameters:
`descriptor` - versionable project descriptor
Returns:
PasswordManager or null if session is not initialized
getEMFURI
static org.eclipse.emf.common.util.URI getEMFURI(@Nonnull
 [ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
saveToOffline
static [EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html) saveToOffline([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) status,
 boolean delete)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html),
com.nomagic.ci.persistence.PersistenceException
Saves the specified project to offline.
Parameters:
`project` - a project.
`status` - a progress status.
`delete` - delete previous saved offline project if true.
Returns:
offline project descriptor.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the specified project is not a TWC project.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if any I/O errors occurs.
`com.nomagic.ci.persistence.PersistenceException` - if persistence related problem occurs.
loadFromOffline
@CheckForNullstatic [Project](../core/Project.html) loadFromOffline([EsiUtils.OfflineProjectDescriptor](EsiUtils.OfflineProjectDescriptor.html) descriptor,
 [ProgressStatus](../../task/ProgressStatus.html) status)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Loads the offline project.
Parameters:
`descriptor` - specifies which offline project to load.
`status` - progress status.
Returns:
loaded project or null if the offline project was not loaded.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if offline project loading fails.
createProjectDescriptorById
static [ProjectDescriptor](../core/project/ProjectDescriptor.html) createProjectDescriptorById([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Returns descriptor of project with given id
Parameters:
`id` - project id
Returns:
descriptor
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
getIVersionDescriptors
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor> getIVersionDescriptors(org.eclipse.emf.common.util.URI locationUri)
Versions of given project
Parameters:
`locationUri` - location uri.
Returns:
versions
getVersion
com.nomagic.ci.persistence.versioning.IVersionDescriptor getVersion([Project](../core/Project.html) project)
Current version of given project
Parameters:
`project` - project
Returns:
versions

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi</a></div>
<h1 class="title" title="Interface EsiUtils">Interface EsiUtils</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EsiUtils</span></div>
<div class="block">API to work with Teamwork Cloud server. Before working with users and projects there must be established connection to Teamwork Cloud server.
 Connection is established with this code:
 <p> <hr/> <code>
 EsiUtils.getTeamworkService().login(new ServerLoginInfo("localhost", "user", "password", false), false);
 </code><hr/> </p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="EsiUtils.ApplyProjectStateResult.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.ApplyProjectStateResult</a></code></div>
<div class="col-last even-row-color">
<div class="block">A structure that is produced by the <a href="#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)"><code>applyProjectState(Project, Project)</code></a> and
 which holds information about the result of the operation</div>
</div>
<div class="col-first odd-row-color"><code>static interface </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Branch information.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></code></div>
<div class="col-last even-row-color">
<div class="block">Offline project descriptor.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final com.nomagic.magicdraw.esi.project.project.EsiProjectRepository</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mProjectRepository">mProjectRepository</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NOTIFY_TAG_SEPARATOR">NOTIFY_TAG_SEPARATOR</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addCommitTags(java.util.List,com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">addCommitTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Add tags for given version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default com.nomagic.ci.persistence.IPrimaryProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String)">addToESI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Add project to the Teamwork Cloud server and open it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.IPrimaryProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">addToESI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 boolean addStandardSystemProfiles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Add project to the Teamwork Cloud server and open it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static com.nomagic.ci.persistence.IPrimaryProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection)">addToESI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../teamwork2/local2remote/ResolveLocalModuleInfo.html" title="class in com.nomagic.magicdraw.teamwork2.local2remote">ResolveLocalModuleInfo</a>&gt; resolveInfos)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Add project to the Teamwork Cloud server and open it</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static com.nomagic.ci.persistence.IPrimaryProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection,com.nomagic.magicdraw.esi.session.RepositorySession)">addToESI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../teamwork2/local2remote/ResolveLocalModuleInfo.html" title="class in com.nomagic.magicdraw.teamwork2.local2remote">ResolveLocalModuleInfo</a>&gt; resolveInfos,
 com.nomagic.magicdraw.esi.session.RepositorySession session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#addUpsToTwc(com.nomagic.magicdraw.core.Project)">addUpsToTwc</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Adds a UPS project to Teamwork Cloud (TWC).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.ApplyProjectStateResult.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.ApplyProjectStateResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#applyDisconnectedProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">applyDisconnectedProjectState</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> source,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Applies the state of the source project (local project) to the target project (TWCloud server project), or in other words, overwrites
 the content of the target project with the contents of the source project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.ApplyProjectStateResult.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.ApplyProjectStateResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">applyProjectState</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> source,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Applies the state of the source project to the target project, or in other words, overwrites
 the content of the target project with the contents of the source project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#assignProjectToCategory(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String...)">assignProjectToCategory</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... categories)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds or remove project to/from categories.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String)">cloneProject</a><wbr/>(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Clones project, new project is created it contains copy of source project with regenerated element ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String,java.util.UUID)">cloneProject</a><wbr/>(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> targetCategoryID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Clones project, new project is created it contains copy of source project with regenerated element ids.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#cloneProjectWithUsages(org.eclipse.emf.common.util.URI,java.lang.String,java.util.Map,java.lang.String,java.util.UUID)">cloneProjectWithUsages</a><wbr/>(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; usedProjectTargetNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> targetCategoryID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Clones project and its usages, new projects are created, they contain copy of source project and its non standard/system usages with regenerated element ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List)">commitProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; unlockElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; unlockModules,
 boolean unlockDecomposition,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Commit project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List,com.nomagic.task.ProgressStatus)">commitProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; unlockElements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; unlockModules,
 boolean unlockDecomposition,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Commit project with progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#convertToLocal(com.nomagic.magicdraw.core.Project,java.io.File)">convertToLocal</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Convert given project to local, save and reopen it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String)">createBranch</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchDescription)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create new branch for given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCategory(java.lang.String,java.lang.String)">createCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create projects category in the server.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createProject(java.lang.String,java.lang.String)">createProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create Teamwork Cloud project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#createProjectDescriptorById(java.lang.String)">createProjectDescriptorById</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Returns descriptor of project with given id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#deleteBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">deleteBranch</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Delete project branch.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#deleteCategory(java.lang.String)">deleteCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Delete category with given name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#deleteProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">deleteProject</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Delete project from repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#exportEsiModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,java.lang.String)">exportEsiModule</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Exports module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#get()">get</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get instance from active session</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#get(com.nomagic.ci.persistence.IPrimaryProject)">get</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject primary)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get instance for provided project session</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.esi.api.info.TagInfo&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAllCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getAllCommitTagsInfo</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get all tags for project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getBranches</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get all branches for given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">getBranches</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get all branches for given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getBranchID(org.eclipse.emf.common.util.URI)">getBranchID</a><wbr/>(org.eclipse.emf.common.util.URI locationURI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Gets project branch ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCategories()">getCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCategoriesToProjects()">getCategoriesToProjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get categories for projects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCategoryInfoByResourceID(java.lang.String)">getCategoryInfoByResourceID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get <a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi"><code>CategoryInfo</code></a> for specified twc project resource ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">getCommitTags</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get tags names for project version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.esi.api.info.TagInfo&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">getCommitTagsInfo</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get tags for project version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getCurrentBranch(com.nomagic.ci.persistence.IProject)">getCurrentBranch</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Gets branch information for the given TWC project part.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getDescriptorByBranchID(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.UUID)">getDescriptorByBranchID</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> branchID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get project descriptor for given branch.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDescriptorForBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">getDescriptorForBranch</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get project descriptor for given branch.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getDescriptorForVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">getDescriptorForVersion</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get descriptor for specific version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static org.eclipse.emf.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getEMFURI(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getEMFURI</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIVersionDescriptors(org.eclipse.emf.common.util.URI)">getIVersionDescriptors</a><wbr/>(org.eclipse.emf.common.util.URI locationUri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Versions of given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLastVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getLastVersion</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get last project version number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLastVersionDescriptor(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getLastVersionDescriptor</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get last project version descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../teamwork2/locks/ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getLockService(com.nomagic.magicdraw.core.Project)">getLockService</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Provides api to check, request and release locks on various project data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLoggedUserName()">getLoggedUserName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the currently logged Teamwork Cloud user name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getLoggedUserNames()">getLoggedUserNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get logged in users if current user has rights to access user list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNewEsiBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String)">getNewEsiBranch</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchDescription)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create new branch for given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)">getNotifyOnNewTags</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method returns application's notify tags about available project usage update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOfflineProject(com.nomagic.magicdraw.core.Project)">getOfflineProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns offline project descriptor of the specified project or null if the project is not saved to offline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOfflineProjects()">getOfflineProjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all available offline project descriptors.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../teamwork2/esi/protect/PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getPasswordManager</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets password manager for command line utilities
 If session is not present then <code>null</code> will be returned.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectDescriptorByQualifiedName(java.lang.String)">getProjectDescriptorByQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns project descriptor for given project qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getProjectDescriptorsForEachBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus)">getProjectDescriptorsForEachBranch</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt; branches,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection)">getProjectDescriptorsWithBranches</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptorsWithBranches)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collects all project descriptors with branch info for the given project descriptor into the provided collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus)">getProjectDescriptorsWithBranches</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptorsWithBranches,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collects all project descriptors with branch info for the given project descriptor into the provided collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectDescriptorsWithBranches(java.lang.Iterable)">getProjectDescriptorsWithBranches</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; projectDescriptors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Invocation of this method returns a <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util"><code>Collection</code></a> of <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project"><code>ProjectDescriptor</code></a>s of each
 branch in the given <code>projectDescriptors</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectDescriptorsWithBranchesByProjectID(java.util.List)">getProjectDescriptorsWithBranchesByProjectID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; projectIDs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns project descriptors with available branches for given project IDs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getProjectIdByQualifiedName(java.lang.String)">getProjectIdByQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns project id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectName(org.eclipse.emf.common.util.URI)">getProjectName</a><wbr/>(org.eclipse.emf.common.util.URI locationURI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return project name for given URI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRemoteProjectDescriptors()">getRemoteProjectDescriptors</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns descriptors of projects stored on server.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getResourceID</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="session/ConnectionInfo.html" title="class in com.nomagic.magicdraw.esi.session">ConnectionInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getServerInfo(com.nomagic.magicdraw.core.Project)">getServerInfo</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get server information for given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../teamwork2/ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#getTeamworkService()">getTeamworkService</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Get service for working with Teamwork Cloud.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUserNames()">getUserNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get all users if current user has rights to access user list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVersion(com.nomagic.magicdraw.core.Project)">getVersion</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Current version of given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getVersions</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Get all versions of given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#isModuleUsageNew(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">isModuleUsageNew</a><wbr/>(com.nomagic.ci.persistence.IProject fromProject,
 com.nomagic.ci.persistence.IProject toProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Checks if the project usage exists and is new (not yet committed to server).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)">isNotifyOnNew</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method returns if application should notify about available project usage update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#isProjectChanged(com.nomagic.magicdraw.core.Project)">isProjectChanged</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method returns <code>true</code> when twcloud project has some changed objects in its resource,
 or local project's <code>StateChangeHandler.isDirty(IProject)</code> returns <code>true</code></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#loadFromOffline(com.nomagic.magicdraw.esi.EsiUtils.OfflineProjectDescriptor,com.nomagic.task.ProgressStatus)">loadFromOffline</a><wbr/>(<a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a> descriptor,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Loads the offline project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#moveToUsedProject(com.nomagic.magicdraw.core.Project,java.util.Map,boolean)">moveToUsedProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>,<wbr/><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; moveMap,
 boolean silentMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Moves elements to used project(s).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">removeCommitTags</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Remove all tags from project version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#saveToOffline(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus,boolean)">saveToOffline</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean delete)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Saves the specified project to offline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean)">setNotifyOnNew</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 boolean notifyOnNew)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method sets if application should notify about available project usage update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#setNotifyOnNewTags(com.nomagic.ci.persistence.IPrimaryProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">setNotifyOnNewTags</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method sets application's notify tags about available project usage update.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#setNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">setNotifyOnNewTags</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Method sets application's notify tags about available project usage update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#setProjectName(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">setProjectName</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Rename project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">updateModule</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Change given module to another version or branch.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,org.eclipse.emf.common.util.URI,long)">updateModule</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 org.eclipse.emf.common.util.URI updateFrom,
 long version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Change given module to another version or branch.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#updateProject(com.nomagic.magicdraw.core.Project)">updateProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Updates given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;com.nomagic.ci.persistence.IAttachedProject,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#updateRequiredProjectUsages(com.nomagic.magicdraw.core.Project)">updateRequiredProjectUsages</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">This method updates project usages to newest version.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="mProjectRepository">
<h3>mProjectRepository</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">com.nomagic.magicdraw.esi.project.project.EsiProjectRepository</span> <span class="element-name">mProjectRepository</span></div>
</section>
</li>
<li>
<section class="detail" id="NOTIFY_TAG_SEPARATOR">
<h3>NOTIFY_TAG_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NOTIFY_TAG_SEPARATOR</span></div>
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
<section class="detail" id="get()">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></span> <span class="element-name">get</span>()</div>
<div class="block">Get instance from active session</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>EsiUtils instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(com.nomagic.ci.persistence.IPrimaryProject)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject primary)</span></div>
<div class="block">Get instance for provided project session</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primary</code> - project</dd>
<dt>Returns:</dt>
<dd>EsiUtils instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTeamworkService()">
<h3>getTeamworkService</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="../teamwork2/ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span> <span class="element-name">getTeamworkService</span>()</div>
<div class="block">Get service for working with Teamwork Cloud.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>service for working with Teamwork Cloud.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockService(com.nomagic.magicdraw.core.Project)">
<h3>getLockService</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="../teamwork2/locks/ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></span> <span class="element-name">getLockService</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Provides api to check, request and release locks on various project data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>lock service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProject(java.lang.String,java.lang.String)">
<h3>createProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">createProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</span>
               throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Create Teamwork Cloud project. Project is created only if currently logged user rights allows to create projects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - project name.</dd>
<dd><code>category</code> - project category.</dd>
<dt>Returns:</dt>
<dd>crated project.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List)">
<h3>commitProject</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">commitProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; unlockElements,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; unlockModules,
 boolean unlockDecomposition,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</span></div>
<div class="block">Commit project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>comment</code> - comment.</dd>
<dd><code>unlockElements</code> - elements to unlock when committing. The collection specifies which locked elements should be unlocked after successful commit.
                            <code>null</code> means that no elements should be unlocked.</dd>
<dd><code>unlockModules</code> - modules to unlock when committing. The collection specifies which project usages (modules) should be unlocked after successful commit.
                            <code>null</code> means that no project usages should be unlocked.</dd>
<dd><code>unlockDecomposition</code> - true if decomposition needs to be unlocked when committing.</dd>
<dd><code>tags</code> - version tags to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="commitProject(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.Collection,java.util.Collection,boolean,java.util.List,com.nomagic.task.ProgressStatus)">
<h3>commitProject</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">commitProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; unlockElements,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; unlockModules,
 boolean unlockDecomposition,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 @CheckForNull
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span></div>
<div class="block">Commit project with progress.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>comment</code> - comment.</dd>
<dd><code>unlockElements</code> - elements to unlock when committing. The collection specifies which locked elements should be unlocked after successful commit.
                            <code>null</code> means that no elements should be unlocked.</dd>
<dd><code>unlockModules</code> - modules to unlock when committing. The collection specifies which project usages (modules) should be unlocked after successful commit.
                            <code>null</code> means that no project usages should be unlocked.</dd>
<dd><code>unlockDecomposition</code> - true if decomposition needs to be unlocked when committing.</dd>
<dd><code>tags</code> - version tags to set.</dd>
<dd><code>monitor</code> - progress status monitor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportEsiModule(com.nomagic.magicdraw.core.Project,java.util.Collection,java.lang.String,java.lang.String)">
<h3>exportEsiModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">exportEsiModule</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleName)</span>
                                                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>packages</code> - packages to export.</dd>
<dd><code>description</code> - module description.</dd>
<dd><code>moduleName</code> - name of module.</dd>
<dt>Returns:</dt>
<dd>exported module attached project.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteProjectDescriptors()">
<h3>getRemoteProjectDescriptors</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getRemoteProjectDescriptors</span>()
                                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns descriptors of projects stored on server.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of remote project descriptors.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.rmi/java/rmi/RemoteException.html" title="class or interface in java.rmi">RemoteException</a></code> - in case of some problem</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectIdByQualifiedName(java.lang.String)">
<h3>getProjectIdByQualifiedName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectIdByQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns project id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - project qualified name, unique name constructed from project name and it's branches.
                      <p>E.g:</p>
                      "MyProject" with no branches = "MyProject"<br/>
                      "MyProject" branch ["release"] = "MyProject##release"<br/>
                      "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"<br/></dd>
<dt>Returns:</dt>
<dd>project id</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorByQualifiedName(java.lang.String)">
<h3>getProjectDescriptorByQualifiedName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getProjectDescriptorByQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns project descriptor for given project qualified name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - project qualified name, unique name constructed from project name and its branches.
                      Examples:
                      "MyProject" with no branches = "MyProject"
                      "MyProject" branch ["release"] = "MyProject##release"
                      "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"</dd>
<dt>Returns:</dt>
<dd>ProjectDescriptor</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Get all versions of given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dt>Returns:</dt>
<dd>list of version information.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCommitTags(java.util.List,com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">
<h3>addCommitTags</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addCommitTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</span></div>
<div class="block">Add tags for given version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tags</code> - tags to add.</dd>
<dd><code>descriptor</code> - project for which version tags is set.</dd>
<dd><code>version</code> - version for which tags will be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">
<h3>getCommitTags</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCommitTags</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</span></div>
<div class="block">Get tags names for project version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>version</code> - version.</dd>
<dt>Returns:</dt>
<dd>list of tags for given version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">
<h3>getCommitTagsInfo</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.esi.api.info.TagInfo&gt;</span> <span class="element-name">getCommitTagsInfo</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</span></div>
<div class="block">Get tags for project version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>version</code> - version.</dd>
<dt>Returns:</dt>
<dd>list of tags for given version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllCommitTagsInfo(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getAllCommitTagsInfo</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.esi.api.info.TagInfo&gt;</span> <span class="element-name">getAllCommitTagsInfo</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Get all tags for project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dt>Returns:</dt>
<dd>list of tags for given version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCommitTags(com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">
<h3>removeCommitTags</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeCommitTags</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</span></div>
<div class="block">Remove all tags from project version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>version</code> - version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateProject(com.nomagic.magicdraw.core.Project)">
<h3>updateProject</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">updateProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Updates given project. Project is activated before update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - teamwork project to update.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectName(org.eclipse.emf.common.util.URI)">
<h3>getProjectName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectName</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI locationURI)</span></div>
<div class="block">Return project name for given URI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationURI</code> - project location.</dd>
<dt>Returns:</dt>
<dd>project name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProjectName(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">
<h3>setProjectName</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">setProjectName</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newName)</span>
                    throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Rename project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project descriptor</dd>
<dd><code>newName</code> - new project name.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteProject(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>deleteProject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">deleteProject</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project)</span>
            throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Delete project from repository.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to delete.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategories()">
<h3>getCategories</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a>&gt;</span> <span class="element-name">getCategories</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all categories from server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategoriesToProjects()">
<h3>getCategoriesToProjects</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;&gt;</span> <span class="element-name">getCategoriesToProjects</span>()
                                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Get categories for projects.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>projects in categories.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategoryInfoByResourceID(java.lang.String)">
<h3>getCategoryInfoByResourceID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a></span> <span class="element-name">getCategoryInfoByResourceID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceID)</span></div>
<div class="block">Get <a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi"><code>CategoryInfo</code></a> for specified twc project resource ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourceID</code> - twc project resource ID</dd>
<dt>Returns:</dt>
<dd>instance of <a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi"><code>CategoryInfo</code></a> or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCategory(java.lang.String,java.lang.String)">
<h3>createCategory</h3>
<div class="member-signature"><span class="return-type"><a href="../teamwork2/esi/CategoryInfo.html" title="class in com.nomagic.magicdraw.teamwork2.esi">CategoryInfo</a></span> <span class="element-name">createCategory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Create projects category in the server.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - category name</dd>
<dd><code>description</code> - category description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="assignProjectToCategory(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String...)">
<h3>assignProjectToCategory</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">assignProjectToCategory</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... categories)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Adds or remove project to/from categories. After this method project belongs only to categories specified for this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to assign or remove from category.</dd>
<dd><code>categories</code> - categories to which project will be assigned.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteCategory(java.lang.String)">
<h3>deleteCategory</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">deleteCategory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Delete category with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - category name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getBranches</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt;</span> <span class="element-name">getBranches</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Get all branches for given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dt>Returns:</dt>
<dd>branches for given project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus)">
<h3>getBranches</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt;</span> <span class="element-name">getBranches</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Get all branches for given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>status</code> - progress status.</dd>
<dt>Returns:</dt>
<dd>branches for given project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String)">
<h3>createBranch</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">createBranch</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchDescription)</span></div>
<div class="block">Create new branch for given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>version</code> - version from which branch</dd>
<dd><code>branchName</code> - new branch name.</dd>
<dd><code>branchDescription</code> - description of new branch.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - in case network or server error occurs when creating branch.</dd>
<dd><code><a href="InsufficientPermissionsException.html" title="class in com.nomagic.magicdraw.esi">InsufficientPermissionsException</a></code> - if currently logged in user does not have <em>Administer Resources</em> permission</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNewEsiBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,long,java.lang.String,java.lang.String)">
<h3>getNewEsiBranch</h3>
<div class="member-signature"><span class="return-type"><a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a></span> <span class="element-name">getNewEsiBranch</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchDescription)</span></div>
<div class="block">Create new branch for given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor.</dd>
<dd><code>version</code> - version from which branch</dd>
<dd><code>branchName</code> - new branch name.</dd>
<dd><code>branchDescription</code> - description of new branch.</dd>
<dt>Returns:</dt>
<dd>branch info for specified branch</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - in case network or server error occurs when creating branch.</dd>
<dd><code><a href="InsufficientPermissionsException.html" title="class in com.nomagic.magicdraw.esi">InsufficientPermissionsException</a></code> - if currently logged in user does not have <em>Administer Resources</em> permission</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptorByBranchID(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.UUID)">
<h3>getDescriptorByBranchID</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getDescriptorByBranchID</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> branchID)</span></div>
<div class="block">Get project descriptor for given branch. This descriptor can be used to load project from branch.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project descriptor.</dd>
<dd><code>branchID</code> - branch id.</dd>
<dt>Returns:</dt>
<dd>project descriptor for given branch.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getResourceID</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDescriptorForBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">
<h3>getDescriptorForBranch</h3>
<div class="member-signature"><span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getDescriptorForBranch</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName)</span></div>
<div class="block">Get project descriptor for given branch. This descriptor can be used to load project from branch.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project descriptor.</dd>
<dd><code>branchName</code> - branch name.</dd>
<dt>Returns:</dt>
<dd>project descriptor for given branch.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptorForVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">
<h3>getDescriptorForVersion</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getDescriptorForVersion</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor)</span></div>
<div class="block">Get descriptor for specific version. Can be used to open historic project version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectDescriptor</code> - project descriptor.</dd>
<dd><code>versionDescriptor</code> - version.</dd>
<dt>Returns:</dt>
<dd>descriptor for specific version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.lang.String)">
<h3>deleteBranch</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">deleteBranch</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> branchName)</span></div>
<div class="block">Delete project branch.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project which branch will be deleted.</dd>
<dd><code>branchName</code> - branch name to delete.</dd>
<dt>Throws:</dt>
<dd><code><a href="InsufficientPermissionsException.html" title="class in com.nomagic.magicdraw.esi">InsufficientPermissionsException</a></code> - if currently logged in user does not have <em>Administer Resources</em> permission</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToESI(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>addToESI</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">com.nomagic.ci.persistence.IPrimaryProject</span> <span class="element-name">addToESI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName)</span>
                                                     throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Add project to the Teamwork Cloud server and open it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to add.</dd>
<dd><code>esiProjectName</code> - project name in teamwork cloud server.</dd>
<dt>Returns:</dt>
<dd>opened teamwork cloud project.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>addToESI</h3>
<div class="member-signature"><span class="return-type">com.nomagic.ci.persistence.IPrimaryProject</span> <span class="element-name">addToESI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 boolean addStandardSystemProfiles)</span>
                                             throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Add project to the Teamwork Cloud server and open it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to add.</dd>
<dd><code>esiProjectName</code> - project name in teamwork cloud server.</dd>
<dd><code>addStandardSystemProfiles</code> - if to add standard/system profiles too.</dd>
<dt>Returns:</dt>
<dd>opened teamwork cloud project.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection,com.nomagic.magicdraw.esi.session.RepositorySession)">
<h3>addToESI</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">com.nomagic.ci.persistence.IPrimaryProject</span> <span class="element-name">addToESI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 @Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../teamwork2/local2remote/ResolveLocalModuleInfo.html" title="class in com.nomagic.magicdraw.teamwork2.local2remote">ResolveLocalModuleInfo</a>&gt; resolveInfos,
 @CheckForNull
 com.nomagic.magicdraw.esi.session.RepositorySession session)</span>
                                                    throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToESI(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Collection)">
<h3>addToESI</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">com.nomagic.ci.persistence.IPrimaryProject</span> <span class="element-name">addToESI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> esiProjectName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 @Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../teamwork2/local2remote/ResolveLocalModuleInfo.html" title="class in com.nomagic.magicdraw.teamwork2.local2remote">ResolveLocalModuleInfo</a>&gt; resolveInfos)</span>
                                                    throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Add project to the Teamwork Cloud server and open it</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project to add</dd>
<dd><code>esiProjectName</code> - the name for the new Teamwork Cloud project</dd>
<dd><code>category</code> - the category to add the project to</dd>
<dd><code>comment</code> - the commit comment</dd>
<dd><code>tags</code> - the commit tags</dd>
<dd><code>resolveInfos</code> - the module resolve info list</dd>
<dt>Returns:</dt>
<dd>the added project</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - exception if add fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertToLocal(com.nomagic.magicdraw.core.Project,java.io.File)">
<h3>convertToLocal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">convertToLocal</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Convert given project to local, save and reopen it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to convert</dd>
<dd><code>file</code> - project file</dd>
<dt>Returns:</dt>
<dd>local project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoggedUserName()">
<h3>getLoggedUserName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLoggedUserName</span>()</div>
<div class="block">Returns the currently logged Teamwork Cloud user name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getServerInfo(com.nomagic.magicdraw.core.Project)">
<h3>getServerInfo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="session/ConnectionInfo.html" title="class in com.nomagic.magicdraw.esi.session">ConnectionInfo</a></span> <span class="element-name">getServerInfo</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Get server information for given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>server information or null when project is not server project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoggedUserNames()">
<h3>getLoggedUserNames</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getLoggedUserNames</span>()</div>
<div class="block">Get logged in users if current user has rights to access user list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all user names.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserNames()">
<h3>getUserNames</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getUserNames</span>()</div>
<div class="block">Get all users if current user has rights to access user list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>logged in user names.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.project.ProjectDescriptor,long)">
<h3>updateModule</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">updateModule</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 long version)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Change given module to another version or branch.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which module is switched.</dd>
<dd><code>module</code> - module to switch.</dd>
<dd><code>descriptor</code> - new module descriptor.</dd>
<dd><code>version</code> - new module version</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateModule(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,org.eclipse.emf.common.util.URI,long)">
<h3>updateModule</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">updateModule</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject module,
 org.eclipse.emf.common.util.URI updateFrom,
 long version)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Change given module to another version or branch.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which module is switched.</dd>
<dd><code>module</code> - module to switch.</dd>
<dd><code>updateFrom</code> - project location URI.</dd>
<dd><code>version</code> - new module version</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean)">
<h3>setNotifyOnNew</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">setNotifyOnNew</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 boolean notifyOnNew)</span></div>
<div class="block">Method sets if application should notify about available project usage update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project to which usage setting is applied.</dd>
<dd><code>iAttachedProject</code> - Usage's attached project to which setting is applied.</dd>
<dd><code>notifyOnNew</code> - Should notification be shown.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)">
<h3>isNotifyOnNew</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">boolean</span> <span class="element-name">isNotifyOnNew</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)</span></div>
<div class="block">Method returns if application should notify about available project usage update.
 Return <code>false</code> by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project to which's usage setting is applied.</dd>
<dd><code>iAttachedProject</code> - Usage's attached project to which setting is applied.</dd>
<dt>Returns:</dt>
<dd>Should notification be shown. Returns <code>false</code> by default.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectChanged(com.nomagic.magicdraw.core.Project)">
<h3>isProjectChanged</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">boolean</span> <span class="element-name">isProjectChanged</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method returns <code>true</code> when twcloud project has some changed objects in its resource,
 or local project's <code>StateChangeHandler.isDirty(IProject)</code> returns <code>true</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to check for presence of changes</dd>
<dt>Returns:</dt>
<dd><code>true</code> when project is changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addUpsToTwc(com.nomagic.magicdraw.core.Project)">
<h3>addUpsToTwc</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">addUpsToTwc</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Adds a UPS project to Teamwork Cloud (TWC).

 <p>This method converts a UPS project to a TWC project and imports it directly into the TWC server.

 <p>The project state must be suitable for exporting, meaning that the project should be in a consistent state
 with no unsaved changes.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project to be added to TWC</dd>
<dt>Returns:</dt>
<dd>the project that was added to TWC</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if there is an error during the conversion or import process</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">
<h3>setNotifyOnNewTags</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">setNotifyOnNewTags</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</span></div>
<div class="block">Method sets application's notify tags about available project usage update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project to which's usage setting is applied.</dd>
<dd><code>iAttachedProject</code> - Usage's attached project to which setting is applied.</dd>
<dd><code>tags</code> - Notify tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNotifyOnNewTags(com.nomagic.ci.persistence.IPrimaryProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">
<h3>setNotifyOnNewTags</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">setNotifyOnNewTags</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</span></div>
<div class="block">Method sets application's notify tags about available project usage update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project to which's usage setting is applied.</dd>
<dd><code>iAttachedProject</code> - Usage's attached project to which setting is applied.</dd>
<dd><code>tags</code> - Notify tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotifyOnNewTags(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)">
<h3>getNotifyOnNewTags</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNotifyOnNewTags</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IAttachedProject iAttachedProject)</span></div>
<div class="block">Method returns application's notify tags about available project usage update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project to which's usage setting is applied.</dd>
<dd><code>iAttachedProject</code> - Usage's attached project to which setting is applied.</dd>
<dt>Returns:</dt>
<dd>Notify tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModuleUsageNew(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">
<h3>isModuleUsageNew</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">boolean</span> <span class="element-name">isModuleUsageNew</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject fromProject,
 com.nomagic.ci.persistence.IProject toProject)</span></div>
<div class="block">Checks if the project usage exists and is new (not yet committed to server).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fromProject</code> - the project the usage should be from</dd>
<dd><code>toProject</code> - the project the usage should be to</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the usage from specifed project exists to specified to project
 and if the specified to project is not <code>null</code> and if the usage is new
 (as defined above). Return <code>false</code> othewise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateRequiredProjectUsages(com.nomagic.magicdraw.core.Project)">
<h3>updateRequiredProjectUsages</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;com.nomagic.ci.persistence.IAttachedProject,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">updateRequiredProjectUsages</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span>
                                                                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">This method updates project usages to newest version. Only usages which have <a href="#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)"><code>isNotifyOnNew(Project, IAttachedProject)</code></a>
 set to <code>true</code> are updated. It can be changed using <a href="#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean)"><code>setNotifyOnNew(Project, IAttachedProject, boolean)</code></a>. If project
 usages is locked by other user or can't be updated for other reasons its update will be skipped.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - Project which usages are updated.</dd>
<dt>Returns:</dt>
<dd>Results map. Key - attached project which was updated, value - was update successful.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some problem</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#isNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject)"><code>isNotifyOnNew(Project, IAttachedProject)</code></a></li>
<li><a href="#setNotifyOnNew(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IAttachedProject,boolean)"><code>setNotifyOnNew(Project, IAttachedProject, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>applyProjectState</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.ApplyProjectStateResult.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.ApplyProjectStateResult</a></span> <span class="element-name">applyProjectState</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> source,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> target)</span>
                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a>,
<a href="../teamwork2/locks/ElementLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ElementLockAcquisitionException</a>,
<a href="../teamwork2/locks/ModuleUsageLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ModuleUsageLockAcquisitionException</a>,
<a href="../teamwork2/locks/OptionsLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">OptionsLockAcquisitionException</a></span></div>
<div class="block">Applies the state of the source project to the target project, or in other words, overwrites
 the content of the target project with the contents of the source project. The elements that
 are matched are updated, the not existing elements are removed, and new elements are added.
 Module usages are copied and modules are updated accordingly. To perform the operation
 successfully, all elements of the project, module usages, and options are locked. Any lock
 failure terminates the operation with a specific exception</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - the source project from which the state is copied</dd>
<dd><code>target</code> - the target project to which the state is copied</dd>
<dt>Returns:</dt>
<dd>a structure that holds the result of the operation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if: 1. the projects are the same, 2. any of the projects are
                                             not ready, 3. any of the projects is not an Teamwork Cloud project, 4. the project IDs
                                             differ, 5. the target project is not editable</dd>
<dd><code><a href="../teamwork2/locks/ElementLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ElementLockAcquisitionException</a></code> - if specific element could not be locked</dd>
<dd><code><a href="../teamwork2/locks/ModuleUsageLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ModuleUsageLockAcquisitionException</a></code> - if specific module usage could not be locked</dd>
<dd><code><a href="../teamwork2/locks/OptionsLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">OptionsLockAcquisitionException</a></code> - if specific options could not be locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyDisconnectedProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>applyDisconnectedProjectState</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.ApplyProjectStateResult.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.ApplyProjectStateResult</a></span> <span class="element-name">applyDisconnectedProjectState</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> source,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> target)</span>
                                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a>,
<a href="../teamwork2/locks/ElementLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ElementLockAcquisitionException</a>,
<a href="../teamwork2/locks/ModuleUsageLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ModuleUsageLockAcquisitionException</a>,
<a href="../teamwork2/locks/OptionsLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">OptionsLockAcquisitionException</a></span></div>
<div class="block">Applies the state of the source project (local project) to the target project (TWCloud server project), or in other words, overwrites
 the content of the target project with the contents of the source project. The elements that
 are matched are updated, the not existing elements are removed, and new elements are added.
 Module usages are copied and modules are updated accordingly. To perform the operation
 successfully, all elements of the project, module usages, and options are locked. Any lock
 failure terminates the operation with a specific exception</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - the source project (local project) from which the state is copied</dd>
<dd><code>target</code> - the target project (server project) to which the state is copied</dd>
<dt>Returns:</dt>
<dd>a structure that holds the result of the operation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if: 1. the projects are the same, 2. any of the projects are
                                             not ready, 3. the project IDs
                                             differ, 4. the target project is not editable</dd>
<dd><code><a href="../teamwork2/locks/ElementLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ElementLockAcquisitionException</a></code> - if specific element could not be locked</dd>
<dd><code><a href="../teamwork2/locks/ModuleUsageLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ModuleUsageLockAcquisitionException</a></code> - if specific module usage could not be locked</dd>
<dd><code><a href="../teamwork2/locks/OptionsLockAcquisitionException.html" title="class in com.nomagic.magicdraw.teamwork2.locks">OptionsLockAcquisitionException</a></code> - if specific options could not be locked</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - if the method invocation fails because of another reason. Cause of the exception
                                             should be checked in order find the actual reason of the failure.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getLastVersion</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getLastVersion</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Get last project version number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor for Teamwork Cloud server project.</dd>
<dt>Returns:</dt>
<dd>last project version number, -1 - there is no such project or application is not connected to the server.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - in case provided descriptor is not valid for current server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastVersionDescriptor(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getLastVersionDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getLastVersionDescriptor</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Get last project version descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor for Teamwork Cloud server project.</dd>
<dt>Returns:</dt>
<dd>last project version descriptor, <code>null</code> - when there is no such project or application is not connected to the server.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code> - in case provided descriptor is not valid for current server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorsWithBranches(java.lang.Iterable)">
<h3>getProjectDescriptorsWithBranches</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getProjectDescriptorsWithBranches</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; projectDescriptors)</span></div>
<div class="block">Invocation of this method returns a <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util"><code>Collection</code></a> of <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project"><code>ProjectDescriptor</code></a>s of each
 branch in the given <code>projectDescriptors</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectDescriptors</code> - descriptors of the projects, whose branch <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project"><code>ProjectDescriptor</code></a>s should
                           be returned</dd>
<dt>Returns:</dt>
<dd>project descriptors for each branch of the given <code>projectDescriptors</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorsWithBranchesByProjectID(java.util.List)">
<h3>getProjectDescriptorsWithBranchesByProjectID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getProjectDescriptorsWithBranchesByProjectID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; projectIDs)</span>
                                                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns project descriptors with available branches for given project IDs.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectIDs</code> - list of project IDs</dd>
<dt>Returns:</dt>
<dd>project descriptors with available branches</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String)">
<h3>cloneProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">cloneProject</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Clones project, new project is created it contains copy of source project with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceURI</code> - source project URI</dd>
<dd><code>targetName</code> - target project name</dd>
<dd><code>targetDescription</code> - target project description</dd>
<dt>Returns:</dt>
<dd>cloned project URI</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception in case clone fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneProject(org.eclipse.emf.common.util.URI,java.lang.String,java.lang.String,java.util.UUID)">
<h3>cloneProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">cloneProject</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> targetCategoryID)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Clones project, new project is created it contains copy of source project with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceURI</code> - source project URI</dd>
<dd><code>targetName</code> - target project name</dd>
<dd><code>targetDescription</code> - target project description</dd>
<dd><code>targetCategoryID</code> - target project category ID</dd>
<dt>Returns:</dt>
<dd>cloned project URI</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception in case clone fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneProjectWithUsages(org.eclipse.emf.common.util.URI,java.lang.String,java.util.Map,java.lang.String,java.util.UUID)">
<h3>cloneProjectWithUsages</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">cloneProjectWithUsages</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI sourceURI,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; usedProjectTargetNames,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> targetDescription,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> targetCategoryID)</span>
                                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Clones project and its usages, new projects are created, they contain copy of source project and its non standard/system usages with regenerated element ids.
 Application must be logged in the server, logged in user should have permission to create new project and read source project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceURI</code> - source project URI</dd>
<dd><code>targetName</code> - target project name</dd>
<dd><code>usedProjectTargetNames</code> - used project target names map. Key - used project id, value - target name</dd>
<dd><code>targetDescription</code> - target project description</dd>
<dd><code>targetCategoryID</code> - target project category ID</dd>
<dt>Returns:</dt>
<dd>cloned project URI</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception in case clone fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection)">
<h3>getProjectDescriptorsWithBranches</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">getProjectDescriptorsWithBranches</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptorsWithBranches)</span></div>
<div class="block">Collects all project descriptors with branch info for the given project descriptor into the provided collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor for which to collect project descriptors with branch info</dd>
<dd><code>descriptorsWithBranches</code> - collection where to add the result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorsWithBranches(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>getProjectDescriptorsWithBranches</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">getProjectDescriptorsWithBranches</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt; descriptorsWithBranches,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Collects all project descriptors with branch info for the given project descriptor into the provided collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - project descriptor for which to collect project descriptors with branch info</dd>
<dd><code>descriptorsWithBranches</code> - collection where to add the result</dd>
<dd><code>status</code> - progress status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOfflineProject(com.nomagic.magicdraw.core.Project)">
<h3>getOfflineProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></span> <span class="element-name">getOfflineProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns offline project descriptor of the specified project or null if the project is not saved to offline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dt>Returns:</dt>
<dd>offline project descriptor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the specified project is not a TWC project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOfflineProjects()">
<h3>getOfflineProjects</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a>&gt;</span> <span class="element-name">getOfflineProjects</span>()</div>
<div class="block">Returns all available offline project descriptors.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of offline project descriptors.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorsForEachBranch(com.nomagic.magicdraw.core.project.ProjectDescriptor,java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>getProjectDescriptorsForEachBranch</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getProjectDescriptorsForEachBranch</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a>&gt; branches,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBranchID(org.eclipse.emf.common.util.URI)">
<h3>getBranchID</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getBranchID</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI locationURI)</span></div>
<div class="block">Gets project branch ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationURI</code> - project location URI</dd>
<dt>Returns:</dt>
<dd>branch ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveToUsedProject(com.nomagic.magicdraw.core.Project,java.util.Map,boolean)">
<h3>moveToUsedProject</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">moveToUsedProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>,<wbr/><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; moveMap,
 boolean silentMode)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Moves elements to used project(s). The moved elements must be lockable by user, and must have an owner.
 The target package(s) must be in the directly used project, and be lockable by user. Each moved element can be moved to a different target package.
 In addition to the specified elements, additional elements (such as interrelations) might be selected to be moved together.
 See <code>MoveRelationManager.collectRelationsToMove(java.util.Map&lt;com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement, com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element&gt;)</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the main project</dd>
<dd><code>moveMap</code> - elements move map</dd>
<dd><code>silentMode</code> - if true, will move in silent mode</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case moving elements fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentBranch(com.nomagic.ci.persistence.IProject)">
<h3>getCurrentBranch</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.EsiBranchInfo.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils.EsiBranchInfo</a></span> <span class="element-name">getCurrentBranch</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Gets branch information for the given TWC project part. If TWC project
 part is not linked with TWC project (like standard profiles) or user has no permission to read then
 <code>null</code> will be returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project part</dd>
<dt>Returns:</dt>
<dd>branch information</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPasswordManager(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getPasswordManager</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../teamwork2/esi/protect/PasswordManager.html" title="interface in com.nomagic.magicdraw.teamwork2.esi.protect">PasswordManager</a></span> <span class="element-name">getPasswordManager</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
<div class="block">Gets password manager for command line utilities
 If session is not present then <code>null</code> will be returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - versionable project descriptor</dd>
<dt>Returns:</dt>
<dd>PasswordManager or null if session is not initialized</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEMFURI(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getEMFURI</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">getEMFURI</span><wbr/><span class="parameters">(@Nonnull
 <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span></div>
</section>
</li>
<li>
<section class="detail" id="saveToOffline(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus,boolean)">
<h3>saveToOffline</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></span> <span class="element-name">saveToOffline</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean delete)</span>
                                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Saves the specified project to offline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>status</code> - a progress status.</dd>
<dd><code>delete</code> - delete previous saved offline project if true.</dd>
<dt>Returns:</dt>
<dd>offline project descriptor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the specified project is not a TWC project.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if any I/O errors occurs.</dd>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - if persistence related problem occurs.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadFromOffline(com.nomagic.magicdraw.esi.EsiUtils.OfflineProjectDescriptor,com.nomagic.task.ProgressStatus)">
<h3>loadFromOffline</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">loadFromOffline</span><wbr/><span class="parameters">(<a href="EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a> descriptor,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Loads the offline project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - specifies which offline project to load.</dd>
<dd><code>status</code> - progress status.</dd>
<dt>Returns:</dt>
<dd>loaded project or null if the offline project was not loaded.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if offline project loading fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProjectDescriptorById(java.lang.String)">
<h3>createProjectDescriptorById</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createProjectDescriptorById</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span>
                                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Returns descriptor of project with given id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - project id</dd>
<dt>Returns:</dt>
<dd>descriptor</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIVersionDescriptors(org.eclipse.emf.common.util.URI)">
<h3>getIVersionDescriptors</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</span> <span class="element-name">getIVersionDescriptors</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI locationUri)</span></div>
<div class="block">Versions of given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationUri</code> - location uri.</dd>
<dt>Returns:</dt>
<dd>versions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.magicdraw.core.Project)">
<h3>getVersion</h3>
<div class="member-signature"><span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Current version of given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>versions</dd>
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
