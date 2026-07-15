# JAVA OPENAPI: ModulesService (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/core/modules/ModulesService.html
- source_path: `com/nomagic/magicdraw/core/modules/ModulesService.html`
- source_sha256: `ec287d8d985158cfbe4a943cc1f02150ff0e8012bc46486a6571bc6115305740`
- captured_utc: `2026-07-14T16:55:11.853969+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.modules](package-summary.html)

## Class ModulesService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.modules.ModulesService

@OpenApiAllpublic classModulesService
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
An utility class to work with modules (attached projects). This class provides set of utility
 methods to change decomposition state of project - attach, detach, load, unload or changed
 attachment properties of modules.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ModulesService.ModuleHasElementWithSameIDAsInPrimaryException](ModulesService.ModuleHasElementWithSameIDAsInPrimaryException.html)`
An exception that indicates that module cannot be imported because there is an element with
 same Local ID in the primary project
`static class`
`[ModulesService.ModuleHasOrphanProxiesException](ModulesService.ModuleHasOrphanProxiesException.html)`

`static class`
`[ModulesService.UsedViaReadOnlyAutomaticUsageException](ModulesService.UsedViaReadOnlyAutomaticUsageException.html)`
Thrown when module(s) can not be removed due to all paths from primary
 project to it contains a read only `automatic` usage
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModulesService](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static com.nomagic.ci.persistence.IAttachedProject`
`[attachModule](#attachModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Mounts module into current project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[attachModuleOnTask](#attachModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration))(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)`
Mounts module into current project.
`static boolean`
`[detachModules](#detachModules(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Removes all given modules usages.
`static boolean`
`[detachModulesAndRemoveUnreachable](#detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Removes all given module usages.
`static boolean`
`[detachModulesAndRemoveUnreachable](#detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Removes all given module usages.
`static boolean`
`[detachModulesAndRemoveUnreachableOnTask](#detachModulesAndRemoveUnreachableOnTask(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages)`
Removes all given module usages.
`static boolean`
`[detachModulesOnTask](#detachModulesOnTask(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages)`
Removes all given modules usages.
`static com.nomagic.ci.persistence.IAttachedProject`
`[findOrLoadLocalModule](#findOrLoadLocalModule(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](../Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filePath,
 boolean allowUI)`
Attaches local module from given path into a given project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[findOrLoadModule](#findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean))([Project](../Project.html) project,
 [ProjectDescriptor](../project/ProjectDescriptor.html) moduleLocation,
 boolean allowUI)`
Looks for existing module in a given project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[findOrLoadModule](#findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean))([Project](../Project.html) project,
 [ProjectDescriptor](../project/ProjectDescriptor.html) moduleLocation,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor,
 boolean allowUI)`
Looks for already attached module in a given project.
`static com.nomagic.ci.persistence.mounting.IMountPoint`
`[getMountPoint](#getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> points,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)`
Find mount point in a given collection which mounts a given package.
`static void`
`[importModule](#importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`

`static void`
`[importModule](#importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus,boolean))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor,
 boolean regenerateElementIDs)`
Removes module descriptor and makes all its contents as it is local project content.
`static void`
`[importModuleOnTask](#importModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module)`
Removes module descriptor and makes all its contents as it is local project content.
`static void`
`[importModuleOnTask](#importModuleOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean,boolean,java.util.Map,com.nomagic.task.ProgressStatus))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean newIDs,
 boolean ignoreDirty,
 boolean checkModulePassword,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> importOptions,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Imports given module into given project using given configuration
`static boolean`
`[processException](#processException(com.nomagic.magicdraw.core.Project,java.lang.Exception,java.lang.String))([Project](../Project.html) prj,
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) e,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) failedOperationMessage)`

`static void`
`[reMount](#reMount(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[MountedPackageInfo](MountedPackageInfo.html)> mountedPackagesInfo,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Re-mount given module on different mount points.
`static void`
`[reMountOnTask](#reMountOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[MountedPackageInfo](MountedPackageInfo.html)> mountedPackagesInfo)`
Change mount point location
`static void`
`[removeModules](#removeModules(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus))([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.IAttachedProject> selectedModules,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Removes the selected modules
`static void`
`[removeModulesOnTask](#removeModulesOnTask(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback))([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.IAttachedProject> selectedModules,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation)`
Removes the selected modules on task
`static void`
`[setAutoLoadKind](#setAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind))(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) autoLoadKind)`
Set auto load kind for a given configuration.
`static void`
`[setAutoLoadKind](#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) kind)`
Set module load kind
`static void`
`[setAutoLoadKind](#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) kind,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Set module load kind
`static void`
`[setAutoLoadKind](#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [AutoLoadKind](AutoLoadKind.html) kind,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Set module load kind
`static void`
`[setAutoLoadKindOnTask](#setAutoLoadKindOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [AutoLoadKind](AutoLoadKind.html) kind)`
Set module load kind
`static void`
`[setCompatibleVersion](#setCompatibleVersion(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Set compatible version for a given project
`static void`
`[setInternalVersion](#setInternalVersion(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Set internal version for a given project
`static void`
`[setReadOnly](#setReadOnly(java.util.Collection,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 boolean readOnly,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Make module usage readonly
`static void`
`[setReadOnlyOnTask](#setReadOnlyOnTask(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 boolean readOnly)`
Make module usage readonly
`static void`
`[setReShared](#setReShared(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Re-share given module in a given project
`static void`
`[setReSharedOnTask](#setReSharedOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean))(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared)`
Reshare given module in a given project
`static void`
`[setSharePreferredPath](#setSharePreferredPath(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Set preferred path for mounting for given shared package
`static void`
`[setSharePreferredPathOnTask](#setSharePreferredPathOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Set preferred path for mounting for given shared package
`static void`
`[setStandardSystemProfile](#setStandardSystemProfile(com.nomagic.ci.persistence.IProject,boolean))(com.nomagic.ci.persistence.IProject project,
 boolean standard)`
Mark given project as "standard system profile".
`static void`
`[setStickyVersion](#setStickyVersion(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Set sticky version for given modules usages.
`static void`
`[setStickyVersionOnTask](#setStickyVersionOnTask(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version)`
Set sticky version for given modules usages.
`static void`
`[setUsedVersion](#setUsedVersion(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Set "used" version for a given module.
`static void`
`[setUsedVersionOnTask](#setUsedVersionOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Set "used" version for a given module
`static com.nomagic.ci.persistence.sharing.ISharePoint`
`[share](#share(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Share given package in a given project
`static com.nomagic.ci.persistence.sharing.ISharePoint`
`[shareOnTask](#shareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)`
Share given package in a given project
`static void`
`[unShare](#unShare(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Un-share given package from a given project
`static void`
`[unShareOnTask](#unShareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg)`
Un-share given package from a given project
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModulesService
public ModulesService()
 ============ METHOD DETAIL ========== 
Method Details
attachModule
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject attachModule(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Mounts module into current project. Default mount path is used.
Parameters:
`owner` - owner to attach module to
`configuration` - configuration
`monitor` - progress status
Returns:
module descriptor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of persistence problems
attachModuleOnTask
public static com.nomagic.ci.persistence.IAttachedProject attachModuleOnTask(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)
Mounts module into current project. Default mount path is used.
Parameters:
`project` - project
`configuration` - configuration
Returns:
module descriptor
reMount
public static void reMount(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[MountedPackageInfo](MountedPackageInfo.html)> mountedPackagesInfo,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
Re-mount given module on different mount points.
Parameters:
`owner` - module owner
`module` - module to remount
`mountedPackagesInfo` - new information about mount points
`monitor` - progress monitor
reMountOnTask
public static void reMountOnTask(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[MountedPackageInfo](MountedPackageInfo.html)> mountedPackagesInfo)
Change mount point location
Parameters:
`owner` - project
`module` - module
`mountedPackagesInfo` - new mounting information
detachModules
public static boolean detachModules([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes all given modules usages. If module is used more than one time only remove usage, in
 other case module data will be disposed.
Parameters:
`usages` - modules to remove
`monitor` - monitor
Returns:
true if all modules were detached, false if user cancelled operation
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - if detach fails.
detachModulesAndRemoveUnreachable
public static boolean detachModulesAndRemoveUnreachable([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes all given module usages. If new modules become manually unreachable during the
 operation - they will be removed too if possible
Parameters:
`usages` - the usages to remove
`monitor` - the progress monitor for the operation
Returns:
true if all modules were detached, false if user cancelled operation
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
detachModulesAndRemoveUnreachable
public static boolean detachModulesAndRemoveUnreachable([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes all given module usages. If new modules become manually
 unreachable during the operation - they will be removed too if possible
Parameters:
`usages` - the usages to remove
`removeConfirmation` - remove confirmation
`monitor` - the progress monitor for the operation
Returns:
true if all modules were detached, false if user cancelled
 operation
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
detachModulesAndRemoveUnreachableOnTask
public static boolean detachModulesAndRemoveUnreachableOnTask([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages)
Removes all given module usages. If new modules become manually
 unreachable during the operation - they will be removed too if possible
Parameters:
`usages` - the usages to remove
Returns:
true if all modules were detached, false if user cancelled
 operation
detachModulesOnTask
public static boolean detachModulesOnTask([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages)
Removes all given modules usages. If module is used more than one time only remove usage, in
 other case module data will be disposed.
Parameters:
`usages` - module usages to remove
Returns:
true if all modules were detached, false if user cancelled operation
removeModules
public static void removeModules([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.IAttachedProject> selectedModules,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
 throws [ModulesService.UsedViaReadOnlyAutomaticUsageException](ModulesService.UsedViaReadOnlyAutomaticUsageException.html),
com.nomagic.ci.persistence.PersistenceException
Removes the selected modules
Parameters:
`selectedModules` - the modules to remove
`removeConfirmation` - the confirmation call back that will be used to confirm the
 remove
`progress` - the progress monitor for the operation
Throws:
`[ModulesService.UsedViaReadOnlyAutomaticUsageException](ModulesService.UsedViaReadOnlyAutomaticUsageException.html)`
`com.nomagic.ci.persistence.PersistenceException`
removeModulesOnTask
public static void removeModulesOnTask([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.IAttachedProject> selectedModules,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation)
Removes the selected modules on task
Parameters:
`selectedModules` - the modules to remove
`removeConfirmation` - the confirmation call back that will be used to confirm the remove
importModule
public static void importModule(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
importModule
public static void importModule(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor,
 boolean regenerateElementIDs)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes module descriptor and makes all its contents as it is local project content.
Parameters:
`owner` - module owner
`module` - to import
`monitor` - progress status
`regenerateElementIDs` - if true module element id will be generated
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception is something goes wrong
getMountPoint
@CheckForNullpublic static com.nomagic.ci.persistence.mounting.IMountPoint getMountPoint([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> points,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)
Find mount point in a given collection which mounts a given package.
Parameters:
`points` - mount points
`element` - package
Returns:
found mount point
importModuleOnTask
public static void importModuleOnTask(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module)
Removes module descriptor and makes all its contents as it is local project content.
Parameters:
`owner` - module owner
`module` - to import
importModuleOnTask
public static void importModuleOnTask([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean newIDs,
 boolean ignoreDirty,
 boolean checkModulePassword,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> importOptions,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Imports given module into given project using given configuration
Parameters:
`project` - the context project
`owner` - the project to import to
`module` - the module to import
`newIDs` - `true` if element IDs should be changed
`ignoreDirty` - `true` if project dirty state should be ignored
`checkModulePassword` - `true` if module password should be checked,
 `false` if not
`importOptions` - import implementation dependent options (passed to
 `IProjectJoiningService.join(IAttachedProject, com.nomagic.ci.persistence.local.decomposition.IProjectJoiningFeatureProvider, Map, ProgressStatus)`)
`progress` - the progress to use (optional, will report to a separate progress if not
 provided)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
processException
public static boolean processException(@CheckForNull
 [Project](../Project.html) prj,
 [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) e,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) failedOperationMessage)
setReadOnly
public static void setReadOnly([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 boolean readOnly,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Make module usage readonly
Parameters:
`usages` - module usages
`readOnly` - readonly flag
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some persistence problem
setReadOnlyOnTask
public static void setReadOnlyOnTask([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 boolean readOnly)
Make module usage readonly
Parameters:
`usages` - module usages
`readOnly` - readonly flag
setAutoLoadKind
public static void setAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) autoLoadKind)
Set auto load kind for a given configuration.
Parameters:
`configuration` - configuration to change auto load.
`autoLoadKind` - auto load kind
setAutoLoadKind
public static void setAutoLoadKind(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) kind,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Set module load kind
Parameters:
`owner` - module owner
`configuration` - attachment configuration
`kind` - load kind
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some persistence problem
setAutoLoadKind
public static void setAutoLoadKind(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 [AutoLoadKind](AutoLoadKind.html) kind)
Set module load kind
Parameters:
`owner` - module owner
`configuration` - attachment configuration
`kind` - load kind
setAutoLoadKind
public static void setAutoLoadKind(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [AutoLoadKind](AutoLoadKind.html) kind,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Set module load kind
Parameters:
`owner` - module owner
`module` - module
`kind` - load kind
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some persistence problem
setAutoLoadKindOnTask
public static void setAutoLoadKindOnTask(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [AutoLoadKind](AutoLoadKind.html) kind)
Set module load kind
Parameters:
`owner` - module owner
`module` - module
`kind` - load kind
setReSharedOnTask
public static void setReSharedOnTask(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared)
Reshare given module in a given project
Parameters:
`project` - project
`module` - module
`reShared` - add or remove re-sharing
setReShared
public static void setReShared(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
Re-share given module in a given project
Parameters:
`project` - project
`module` - module
`reShared` - add ore remove re-sharing
`monitor` - monitor
shareOnTask
public static com.nomagic.ci.persistence.sharing.ISharePoint shareOnTask(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Share given package in a given project
Parameters:
`project` - project
`pkg` - package to share
`path` - preferred path for mounting
Returns:
share point
share
public static com.nomagic.ci.persistence.sharing.ISharePoint share(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException,
com.nomagic.ci.persistence.LockAcquisitionException
Share given package in a given project
Parameters:
`project` - project
`pkg` - package to share
`path` - preferred path for mounting
`monitor` - monitor
Returns:
share point
Throws:
`com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException`
`com.nomagic.ci.persistence.LockAcquisitionException` - if locking required elements fails during the operation
setSharePreferredPathOnTask
public static void setSharePreferredPathOnTask(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)
Set preferred path for mounting for given shared package
Parameters:
`project` - project
`pkg` - package
`path` - preferred mounting path
setSharePreferredPath
public static void setSharePreferredPath(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException
Set preferred path for mounting for given shared package
Parameters:
`project` - project
`pkg` - package
`path` - preferred mounting path
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException`
setStandardSystemProfile
public static void setStandardSystemProfile(com.nomagic.ci.persistence.IProject project,
 boolean standard)
Mark given project as "standard system profile".
Parameters:
`project` - project
`standard` - mark as standard profile
setInternalVersion
public static void setInternalVersion(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Set internal version for a given project
Parameters:
`project` - project
`version` - version
setCompatibleVersion
public static void setCompatibleVersion(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Set compatible version for a given project
Parameters:
`project` - project
`version` - version
setUsedVersionOnTask
public static void setUsedVersionOnTask(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Set "used" version for a given module
Parameters:
`owner` - module owner
`module` - module
`version` - version
setUsedVersion
public static void setUsedVersion(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Set "used" version for a given module.
Parameters:
`owner` - module owner
`module` - module
`version` - version
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - if any persistence problem
unShare
public static void unShare(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException,
com.nomagic.ci.persistence.LockAcquisitionException
Un-share given package from a given project
Parameters:
`project` - project
`pkg` - package to un-share
`monitor` - monitor
Throws:
`com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException`
`com.nomagic.ci.persistence.LockAcquisitionException` - if locking required elements fails during the operation
unShareOnTask
public static void unShareOnTask(com.nomagic.ci.persistence.IProject project,
 [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pkg)
Un-share given package from a given project
Parameters:
`project` - project
`pkg` - package to un-share
setStickyVersion
public static void setStickyVersion([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws com.nomagic.ci.persistence.PersistenceException
Set sticky version for given modules usages.
Parameters:
`usages` - usages
`version` - sticky version(null if no sticky version
`monitor` - progress monitor
Throws:
`com.nomagic.ci.persistence.PersistenceException` - in case of some persistence problem
setStickyVersionOnTask
public static void setStickyVersionOnTask([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](ModuleUsage.html)> usages,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version)
Set sticky version for given modules usages.
Parameters:
`usages` - usages
`version` - sticky version(null if no sticky version
findOrLoadLocalModule
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findOrLoadLocalModule([Project](../Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filePath,
 boolean allowUI)
Attaches local module from given path into a given project. Does nothing if such module is
 already attached.
Parameters:
`project` - project
`filePath` - full path to module file
`allowUI` - allow to show error messages to user
Returns:
attached module
findOrLoadModule
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findOrLoadModule([Project](../Project.html) project,
 [ProjectDescriptor](../project/ProjectDescriptor.html) moduleLocation,
 boolean allowUI)
Looks for existing module in a given project. If found, attaches it directly in project. If
 module is not found, attaches and loads it.
Parameters:
`project` - project where module is searched of loaded.
`moduleLocation` - module descriptor to load.
`allowUI` - allow to show error messages to user
Returns:
found or loaded module. Null if failure.
findOrLoadModule
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findOrLoadModule([Project](../Project.html) project,
 @CheckForNull
 [ProjectDescriptor](../project/ProjectDescriptor.html) moduleLocation,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) monitor,
 boolean allowUI)
Looks for already attached module in a given project. or attaches a new one. If such module
 is already attached not directly, attaches it directly in a given project. Activates given
 project if it is not active yet. If module is not found, attaches and loads it.
Parameters:
`project` - project where module is searched of loaded.
`moduleLocation` - module descriptor to load.
`monitor` - monitor where display status, if null new progress bar is shown.
`allowUI` - allow to show error messages to user
Returns:
found or newly attached module. Null if failure.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.modules</a></div>
<h1 class="title" title="Class ModulesService">Class ModulesService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.modules.ModulesService</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ModulesService</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">An utility class to work with modules (attached projects). This class provides set of utility
 methods to change decomposition state of project - attach, detach, load, unload or changed
 attachment properties of modules.</div>
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
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModulesService.ModuleHasElementWithSameIDAsInPrimaryException.html" title="class in com.nomagic.magicdraw.core.modules">ModulesService.ModuleHasElementWithSameIDAsInPrimaryException</a></code></div>
<div class="col-last even-row-color">
<div class="block">An exception that indicates that module cannot be imported because there is an element with
 same Local ID in the primary project</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ModulesService.ModuleHasOrphanProxiesException.html" title="class in com.nomagic.magicdraw.core.modules">ModulesService.ModuleHasOrphanProxiesException</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModulesService.UsedViaReadOnlyAutomaticUsageException.html" title="class in com.nomagic.magicdraw.core.modules">ModulesService.UsedViaReadOnlyAutomaticUsageException</a></code></div>
<div class="col-last even-row-color">
<div class="block">Thrown when module(s) can not be removed due to all paths from primary
 project to it contains a read only <code>automatic</code> usage</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ModulesService</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#attachModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,com.nomagic.task.ProgressStatus)">attachModule</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Mounts module into current project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#attachModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">attachModuleOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Mounts module into current project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModules(java.util.Collection,com.nomagic.task.ProgressStatus)">detachModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all given modules usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus)">detachModulesAndRemoveUnreachable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all given module usages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.task.ProgressStatus)">detachModulesAndRemoveUnreachable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all given module usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesAndRemoveUnreachableOnTask(java.util.Collection)">detachModulesAndRemoveUnreachableOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all given module usages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesOnTask(java.util.Collection)">detachModulesOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all given modules usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrLoadLocalModule(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">findOrLoadLocalModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 boolean allowUI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Attaches local module from given path into a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">findOrLoadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleLocation,
 boolean allowUI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for existing module in a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">findOrLoadModule</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleLocation,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor,
 boolean allowUI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for already attached module in a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.mounting.IMountPoint</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">getMountPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt; points,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find mount point in a given collection which mounts a given package.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus)">importModule</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus,boolean)">importModule</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor,
 boolean regenerateElementIDs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes module descriptor and makes all its contents as it is local project content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">importModuleOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes module descriptor and makes all its contents as it is local project content.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importModuleOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean,boolean,java.util.Map,com.nomagic.task.ProgressStatus)">importModuleOnTask</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean newIDs,
 boolean ignoreDirty,
 boolean checkModulePassword,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; importOptions,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Imports given module into given project using given configuration</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#processException(com.nomagic.magicdraw.core.Project,java.lang.Exception,java.lang.String)">processException</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> failedOperationMessage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reMount(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection,com.nomagic.task.ProgressStatus)">reMount</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="MountedPackageInfo.html" title="class in com.nomagic.magicdraw.core.modules">MountedPackageInfo</a>&gt; mountedPackagesInfo,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Re-mount given module on different mount points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reMountOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">reMountOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="MountedPackageInfo.html" title="class in com.nomagic.magicdraw.core.modules">MountedPackageInfo</a>&gt; mountedPackagesInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Change mount point location</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeModules(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus)">removeModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; selectedModules,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the selected modules</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeModulesOnTask(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback)">removeModulesOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; selectedModules,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the selected modules on task</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind)">setAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> autoLoadKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set auto load kind for a given configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind)">setAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set module load kind</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus)">setAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set module load kind</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus)">setAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set module load kind</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoadKindOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind)">setAutoLoadKindOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set module load kind</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompatibleVersion(com.nomagic.ci.persistence.IProject,java.lang.String)">setCompatibleVersion</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set compatible version for a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setInternalVersion(com.nomagic.ci.persistence.IProject,java.lang.String)">setInternalVersion</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set internal version for a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReadOnly(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">setReadOnly</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 boolean readOnly,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Make module usage readonly</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReadOnlyOnTask(java.util.Collection,boolean)">setReadOnlyOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 boolean readOnly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Make module usage readonly</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReShared(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)">setReShared</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Re-share given module in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReSharedOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean)">setReSharedOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reshare given module in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSharePreferredPath(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus)">setSharePreferredPath</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set preferred path for mounting for given shared package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSharePreferredPathOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">setSharePreferredPathOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set preferred path for mounting for given shared package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStandardSystemProfile(com.nomagic.ci.persistence.IProject,boolean)">setStandardSystemProfile</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 boolean standard)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Mark given project as "standard system profile".</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStickyVersion(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.task.ProgressStatus)">setStickyVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set sticky version for given modules usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setStickyVersionOnTask(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">setStickyVersionOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set sticky version for given modules usages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setUsedVersion(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String,com.nomagic.task.ProgressStatus)">setUsedVersion</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set "used" version for a given module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setUsedVersionOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String)">setUsedVersionOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set "used" version for a given module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.sharing.ISharePoint</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#share(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus)">share</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Share given package in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.sharing.ISharePoint</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#shareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">shareOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Share given package in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unShare(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.task.ProgressStatus)">unShare</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Un-share given package from a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unShareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">unShareOnTask</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Un-share given package from a given project</div>
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
<h3>ModulesService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModulesService</span>()</div>
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
<section class="detail" id="attachModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,com.nomagic.task.ProgressStatus)">
<h3>attachModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">attachModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                                                throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Mounts module into current project. Default mount path is used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner to attach module to</dd>
<dd><code>configuration</code> - configuration</dd>
<dd><code>monitor</code> - progress status</dd>
<dt>Returns:</dt>
<dd>module descriptor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of persistence problems</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="attachModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">
<h3>attachModuleOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">attachModuleOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)</span></div>
<div class="block">Mounts module into current project. Default mount path is used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>configuration</code> - configuration</dd>
<dt>Returns:</dt>
<dd>module descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reMount(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>reMount</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">reMount</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="MountedPackageInfo.html" title="class in com.nomagic.magicdraw.core.modules">MountedPackageInfo</a>&gt; mountedPackagesInfo,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span></div>
<div class="block">Re-mount given module on different mount points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - module to remount</dd>
<dd><code>mountedPackagesInfo</code> - new information about mount points</dd>
<dd><code>monitor</code> - progress monitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reMountOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.util.Collection)">
<h3>reMountOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">reMountOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="MountedPackageInfo.html" title="class in com.nomagic.magicdraw.core.modules">MountedPackageInfo</a>&gt; mountedPackagesInfo)</span></div>
<div class="block">Change mount point location</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - project</dd>
<dd><code>module</code> - module</dd>
<dd><code>mountedPackagesInfo</code> - new mounting information</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModules(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>detachModules</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes all given modules usages. If module is used more than one time only remove usage, in
 other case module data will be disposed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - modules to remove</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Returns:</dt>
<dd>true if all modules were detached, false if user cancelled operation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if detach fails.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>detachModulesAndRemoveUnreachable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesAndRemoveUnreachable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes all given module usages. If new modules become manually unreachable during the
 operation - they will be removed too if possible</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - the usages to remove</dd>
<dd><code>monitor</code> - the progress monitor for the operation</dd>
<dt>Returns:</dt>
<dd>true if all modules were detached, false if user cancelled operation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesAndRemoveUnreachable(java.util.Collection,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus)">
<h3>detachModulesAndRemoveUnreachable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesAndRemoveUnreachable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes all given module usages. If new modules become manually
 unreachable during the operation - they will be removed too if possible</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - the usages to remove</dd>
<dd><code>removeConfirmation</code> - remove confirmation</dd>
<dd><code>monitor</code> - the progress monitor for the operation</dd>
<dt>Returns:</dt>
<dd>true if all modules were detached, false if user cancelled
 operation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesAndRemoveUnreachableOnTask(java.util.Collection)">
<h3>detachModulesAndRemoveUnreachableOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesAndRemoveUnreachableOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</span></div>
<div class="block">Removes all given module usages. If new modules become manually
 unreachable during the operation - they will be removed too if possible</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - the usages to remove</dd>
<dt>Returns:</dt>
<dd>true if all modules were detached, false if user cancelled
 operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesOnTask(java.util.Collection)">
<h3>detachModulesOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</span></div>
<div class="block">Removes all given modules usages. If module is used more than one time only remove usage, in
 other case module data will be disposed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - module usages to remove</dd>
<dt>Returns:</dt>
<dd>true if all modules were detached, false if user cancelled operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeModules(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,com.nomagic.task.ProgressStatus)">
<h3>removeModules</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; selectedModules,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span>
                          throws <span class="exceptions"><a href="ModulesService.UsedViaReadOnlyAutomaticUsageException.html" title="class in com.nomagic.magicdraw.core.modules">ModulesService.UsedViaReadOnlyAutomaticUsageException</a>,
com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Removes the selected modules</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectedModules</code> - the modules to remove</dd>
<dd><code>removeConfirmation</code> - the confirmation call back that will be used to confirm the
                           remove</dd>
<dd><code>progress</code> - the progress monitor for the operation</dd>
<dt>Throws:</dt>
<dd><code><a href="ModulesService.UsedViaReadOnlyAutomaticUsageException.html" title="class in com.nomagic.magicdraw.core.modules">ModulesService.UsedViaReadOnlyAutomaticUsageException</a></code></dd>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeModulesOnTask(java.util.Set,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback)">
<h3>removeModulesOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeModulesOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; selectedModules,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation)</span></div>
<div class="block">Removes the selected modules on task</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectedModules</code> - the modules to remove</dd>
<dd><code>removeConfirmation</code> - the confirmation call back that will be used to confirm the remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus)">
<h3>importModule</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModule(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.task.ProgressStatus,boolean)">
<h3>importModule</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor,
 boolean regenerateElementIDs)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes module descriptor and makes all its contents as it is local project content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - to import</dd>
<dd><code>monitor</code> - progress status</dd>
<dd><code>regenerateElementIDs</code> - if true module element id will be generated</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception is something goes wrong</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>getMountPoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.mounting.IMountPoint</span> <span class="element-name">getMountPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt; points,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</span></div>
<div class="block">Find mount point in a given collection which mounts a given package.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - mount points</dd>
<dd><code>element</code> - package</dd>
<dt>Returns:</dt>
<dd>found mount point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModuleOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">
<h3>importModuleOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importModuleOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module)</span></div>
<div class="block">Removes module descriptor and makes all its contents as it is local project content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - to import</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importModuleOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,boolean,boolean,boolean,java.util.Map,com.nomagic.task.ProgressStatus)">
<h3>importModuleOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importModuleOnTask</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 boolean newIDs,
 boolean ignoreDirty,
 boolean checkModulePassword,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; importOptions,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Imports given module into given project using given configuration</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the context project</dd>
<dd><code>owner</code> - the project to import to</dd>
<dd><code>module</code> - the module to import</dd>
<dd><code>newIDs</code> - <code>true</code> if element IDs should be changed</dd>
<dd><code>ignoreDirty</code> - <code>true</code> if project dirty state should be ignored</dd>
<dd><code>checkModulePassword</code> - <code>true</code> if module password should be checked,
                            <code>false</code> if not</dd>
<dd><code>importOptions</code> - import implementation dependent options (passed to
                            <code>IProjectJoiningService.join(IAttachedProject, com.nomagic.ci.persistence.local.decomposition.IProjectJoiningFeatureProvider, Map, ProgressStatus)</code>)</dd>
<dd><code>progress</code> - the progress to use (optional, will report to a separate progress if not
                            provided)</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="processException(com.nomagic.magicdraw.core.Project,java.lang.Exception,java.lang.String)">
<h3>processException</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">processException</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> failedOperationMessage)</span></div>
</section>
</li>
<li>
<section class="detail" id="setReadOnly(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">
<h3>setReadOnly</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReadOnly</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 boolean readOnly,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                        throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Make module usage readonly</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - module usages</dd>
<dd><code>readOnly</code> - readonly flag</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some persistence problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReadOnlyOnTask(java.util.Collection,boolean)">
<h3>setReadOnlyOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReadOnlyOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 boolean readOnly)</span></div>
<div class="block">Make module usage readonly</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - module usages</dd>
<dd><code>readOnly</code> - readonly flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind)">
<h3>setAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> autoLoadKind)</span></div>
<div class="block">Set auto load kind for a given configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - configuration to change auto load.</dd>
<dd><code>autoLoadKind</code> - auto load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus)">
<h3>setAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                            throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Set module load kind</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>configuration</code> - attachment configuration</dd>
<dd><code>kind</code> - load kind</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some persistence problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration,com.nomagic.magicdraw.core.modules.AutoLoadKind)">
<h3>setAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind)</span></div>
<div class="block">Set module load kind</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>configuration</code> - attachment configuration</dd>
<dd><code>kind</code> - load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind,com.nomagic.task.ProgressStatus)">
<h3>setAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                            throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Set module load kind</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - module</dd>
<dd><code>kind</code> - load kind</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some persistence problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoadKindOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,com.nomagic.magicdraw.core.modules.AutoLoadKind)">
<h3>setAutoLoadKindOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAutoLoadKindOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a href="AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a> kind)</span></div>
<div class="block">Set module load kind</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - module</dd>
<dd><code>kind</code> - load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReSharedOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean)">
<h3>setReSharedOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReSharedOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared)</span></div>
<div class="block">Reshare given module in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module</dd>
<dd><code>reShared</code> - add or remove re-sharing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReShared(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)">
<h3>setReShared</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReShared</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 com.nomagic.ci.persistence.IProject module,
 boolean reShared,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span></div>
<div class="block">Re-share given module in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>module</code> - module</dd>
<dd><code>reShared</code> - add ore remove re-sharing</dd>
<dd><code>monitor</code> - monitor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">
<h3>shareOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.sharing.ISharePoint</span> <span class="element-name">shareOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Share given package in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package to share</dd>
<dd><code>path</code> - preferred path for mounting</dd>
<dt>Returns:</dt>
<dd>share point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="share(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus)">
<h3>share</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.sharing.ISharePoint</span> <span class="element-name">share</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                                            throws <span class="exceptions">com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException,
com.nomagic.ci.persistence.LockAcquisitionException</span></div>
<div class="block">Share given package in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package to share</dd>
<dd><code>path</code> - preferred path for mounting</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Returns:</dt>
<dd>share point</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException</code></dd>
<dd><code>com.nomagic.ci.persistence.LockAcquisitionException</code> - if locking required elements fails during the operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSharePreferredPathOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">
<h3>setSharePreferredPathOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSharePreferredPathOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Set preferred path for mounting for given shared package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package</dd>
<dd><code>path</code> - preferred mounting path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSharePreferredPath(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String,com.nomagic.task.ProgressStatus)">
<h3>setSharePreferredPath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSharePreferredPath</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                  throws <span class="exceptions">com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException</span></div>
<div class="block">Set preferred path for mounting for given shared package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package</dd>
<dd><code>path</code> - preferred mounting path</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStandardSystemProfile(com.nomagic.ci.persistence.IProject,boolean)">
<h3>setStandardSystemProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStandardSystemProfile</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 boolean standard)</span></div>
<div class="block">Mark given project as "standard system profile".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>standard</code> - mark as standard profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInternalVersion(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>setInternalVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setInternalVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Set internal version for a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>version</code> - version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCompatibleVersion(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>setCompatibleVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCompatibleVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Set compatible version for a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>version</code> - version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUsedVersionOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String)">
<h3>setUsedVersionOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setUsedVersionOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Set "used" version for a given module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - module</dd>
<dd><code>version</code> - version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUsedVersion(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject,java.lang.String,com.nomagic.task.ProgressStatus)">
<h3>setUsedVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setUsedVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IAttachedProject module,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                           throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Set "used" version for a given module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - module owner</dd>
<dd><code>module</code> - module</dd>
<dd><code>version</code> - version</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - if any persistence problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unShare(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.task.ProgressStatus)">
<h3>unShare</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unShare</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                    throws <span class="exceptions">com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException,
com.nomagic.ci.persistence.LockAcquisitionException</span></div>
<div class="block">Un-share given package from a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package to un-share</dd>
<dd><code>monitor</code> - monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.local.spi.InvalidProjectObjectException</code></dd>
<dd><code>com.nomagic.ci.persistence.LockAcquisitionException</code> - if locking required elements fails during the operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unShareOnTask(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>unShareOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unShareOnTask</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pkg)</span></div>
<div class="block">Un-share given package from a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>pkg</code> - package to un-share</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStickyVersion(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.task.ProgressStatus)">
<h3>setStickyVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStickyVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                             throws <span class="exceptions">com.nomagic.ci.persistence.PersistenceException</span></div>
<div class="block">Set sticky version for given modules usages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - usages</dd>
<dd><code>version</code> - sticky version(null if no sticky version</dd>
<dd><code>monitor</code> - progress monitor</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.ci.persistence.PersistenceException</code> - in case of some persistence problem</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStickyVersionOnTask(java.util.Collection,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">
<h3>setStickyVersionOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setStickyVersionOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor version)</span></div>
<div class="block">Set sticky version for given modules usages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usages</code> - usages</dd>
<dd><code>version</code> - sticky version(null if no sticky version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrLoadLocalModule(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>findOrLoadLocalModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findOrLoadLocalModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 boolean allowUI)</span></div>
<div class="block">Attaches local module from given path into a given project. Does nothing if such module is
 already attached.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>filePath</code> - full path to module file</dd>
<dd><code>allowUI</code> - allow to show error messages to user</dd>
<dt>Returns:</dt>
<dd>attached module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,boolean)">
<h3>findOrLoadModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findOrLoadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleLocation,
 boolean allowUI)</span></div>
<div class="block">Looks for existing module in a given project. If found, attaches it directly in project. If
 module is not found, attaches and loads it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project where module is searched of loaded.</dd>
<dd><code>moduleLocation</code> - module descriptor to load.</dd>
<dd><code>allowUI</code> - allow to show error messages to user</dd>
<dt>Returns:</dt>
<dd>found or loaded module. Null if failure.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOrLoadModule(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.project.ProjectDescriptor,com.nomagic.task.ProgressStatus,boolean)">
<h3>findOrLoadModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findOrLoadModule</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> moduleLocation,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor,
 boolean allowUI)</span></div>
<div class="block">Looks for already attached module in a given project. or attaches a new one. If such module
 is already attached not directly, attaches it directly in a given project. Activates given
 project if it is not active yet. If module is not found, attaches and loads it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project where module is searched of loaded.</dd>
<dd><code>moduleLocation</code> - module descriptor to load.</dd>
<dd><code>monitor</code> - monitor where display status, if null new progress bar is shown.</dd>
<dd><code>allowUI</code> - allow to show error messages to user</dd>
<dt>Returns:</dt>
<dd>found or newly attached module. Null if failure.</dd>
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
