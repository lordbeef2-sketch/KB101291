# JAVA OPENAPI: ProjectUtilities (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/ProjectUtilities.html
- source_path: `com/nomagic/magicdraw/core/ProjectUtilities.html`
- source_sha256: `2cc4f0b0483d97722a15362edfdd19284d80b096fa0c96bec4ce19c38b908915`
- captured_utc: `2026-07-14T16:55:12.612979+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class ProjectUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.ProjectUtilities

@OpenApiAllpublic classProjectUtilities
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Project decomposition related utility class.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EXPORTER_DESCRIPTION](#EXPORTER_DESCRIPTION)`
Property for XmiExporterDescription
`protected static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<com.nomagic.ci.persistence.IProject,[XmiExporterDescription](../../persistence/XmiExporterDescription.html)>`
`[mExporterDescriptions](#mExporterDescriptions)`

`protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMOTE_ID_ENCODING](#REMOTE_ID_ENCODING)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectUtilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected static void`
`[addToCache](#addToCache(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription))(com.nomagic.ci.persistence.IProject project,
 [XmiExporterDescription](../../persistence/XmiExporterDescription.html) xmiExporterDescription)`

`protected static void`
`[addToCacheLoaded](#addToCacheLoaded(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription))(com.nomagic.ci.persistence.IProject project,
 [XmiExporterDescription](../../persistence/XmiExporterDescription.html) xmiExporterDescription)`
Adds to cache just loaded modules/projects
`static int`
`[compareVersionNumber](#compareVersionNumber(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionNumber1,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionNumber2)`
Compare given version numbers.
`static int`
`[compareVersions](#compareVersions(com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor))(com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor1,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor2)`
Compare given versions descriptors.
`static com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration`
`[createDefaultProjectAttachmentConfiguration](#createDefaultProjectAttachmentConfiguration(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Create default project attachment configuration with default settings.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[decodeTeamworkRemoteId](#decodeTeamworkRemoteId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) remoteId)`
Deprecated.
teamwork server is end of life
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[encodeTeamworkRemoteId](#encodeTeamworkRemoteId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) remoteId)`
Deprecated.
teamwork server is end of life
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByID](#findAttachedProjectByID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 boolean recursively)`
Find attached project by given id in a given project
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByID](#findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID)`
Find attached project by given id in a given project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByID](#findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 boolean recursively)`
Find attached project by given id in a given project
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByName](#findAttachedProjectByName(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Find attached project by given name in a given project
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByName](#findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Find attached project by given name in a given project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByName](#findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean recursively)`
Find attached project by given name in a given project
`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByNames](#findAttachedProjectByNames(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> names,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> modules)`

`static com.nomagic.ci.persistence.IAttachedProject`
`[findAttachedProjectByProjectID](#findAttachedProjectByProjectID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 boolean recursively)`
Find attached project by given project id
`static com.nomagic.ci.persistence.IProject`
`[findProjectByResourceID](#findProjectByResourceID(com.nomagic.ci.persistence.IPrimaryProject,java.lang.String))(com.nomagic.ci.persistence.IPrimaryProject primaryProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceId)`
Search for project with given resource ID
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject>`
`[getAllAttachedProjects](#getAllAttachedProjects(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Returns projects those are attached directly or indirectly to a given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject>`
`[getAllAttachedProjects](#getAllAttachedProjects(com.nomagic.magicdraw.core.Project))([Project](Project.html) project)`
Return all modules in a given project
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject>`
`[getAllAttachedProjects](#getAllAttachedProjects(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> projects)`
Returns projects those are attached directly or indirectly to a given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject>`
`[getAllAttachedProjectsIncludingPrimary](#getAllAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Returns projects those are attached directly or indirectly to a given project including primary project.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.mounting.IMountPoint>`
`[getAllMountPoints](#getAllMountPoints(com.nomagic.ci.persistence.IPrimaryProject))(com.nomagic.ci.persistence.IPrimaryProject project)`
Return all mount points existing in given primary project (direct and not direct).
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject>`
`[getAllProjects](#getAllProjects(com.nomagic.magicdraw.core.Project))([Project](Project.html) project)`
Return all modules and primary project in a given project
`static com.nomagic.ci.persistence.IAttachedProject`
`[getAttachedProject](#getAttachedProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.common.util.URI))(com.nomagic.ci.persistence.IProject project,
 org.eclipse.emf.common.util.URI uri)`
Look for direct or not direct attached project in a primary project of a given project.
`static com.nomagic.ci.persistence.IAttachedProject`
`[getAttachedProject](#getAttachedProject(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject element)`
Find attached project (module) for a given element
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject>`
`[getAttachedProjects](#getAttachedProjects(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Returns projects those are attached directly to a given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject>`
`[getAttachedProjectsIncludingPrimary](#getAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Returns projects those are attached directly to a given project.Primary attached project can be included also.
`static com.nomagic.ci.persistence.IProject`
`[getAttachingProject](#getAttachingProject(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return first project where given project is attached.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject>`
`[getAttachingProjects](#getAttachingProjects(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return all projects where given project is attached.
`static com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration`
`[getAttachment](#getAttachment(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject parent,
 com.nomagic.ci.persistence.IProject child)`
Return configuration which is used to attach one project to another
`static [AutoLoadKind](modules/AutoLoadKind.html)`
`[getAutoLoadKind](#getAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration))(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration attachment)`
Deprecated.
use public static AutoLoadKind getAutoLoadKind( AbstractProjectAttachmentConfiguration attachment )
`static [AutoLoadKind](modules/AutoLoadKind.html)`
`[getAutoLoadKind](#getAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject project)`
Return load kind of given module in a given project
`static [AutoLoadKind](modules/AutoLoadKind.html)`
`[getAutoLoadKind](#getAutoLoadKind(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration))(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration attachment)`
Return load kind of module from given attachment
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCompatibleVersion](#getCompatibleVersion(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Get compatible version of the project
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElementFor](#getElementFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Return element for a given base element.
`static org.eclipse.emf.common.util.URI`
`[getEMFURI](#getEMFURI(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Convert java net URI to emf uri
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getESIRemoteId](#getESIRemoteId(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Gets ESI remote ID for given project
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getESIRemoteId](#getESIRemoteId(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Gets ESI remote ID
`static [XmiExporterDescription](../../persistence/XmiExporterDescription.html)`
`[getExporterDescription](#getExporterDescription(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Provide information about project version and required resources/plugins for that project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getInternalVersion](#getInternalVersion(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Get internal version of project
`static com.dassault_systemes.modeler.foundation.model.ModelElement`
`[getModelElementFor](#getModelElementFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Return element for a given base element.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getModifiedElements](#getModifiedElements(com.nomagic.magicdraw.core.Project))([Project](Project.html) project)`
Get modified elements.
`static com.nomagic.ci.persistence.mounting.IMountPoint`
`[getMountPoint](#getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> points,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)`
Find mount point in a given collection which mounts a given package.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint>`
`[getMountPoints](#getMountPoints(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Gets all mount points in given project.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.mounting.IMountPoint>`
`[getMountPointsFor](#getMountPointsFor(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject attachedProject)`
Gets mount points for given project, i.e.
`static com.nomagic.ci.persistence.IProject`
`[getOwner](#getOwner(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Deprecated.
use [`getAttachingProject(IProject)`](#getAttachingProject(com.nomagic.ci.persistence.IProject))
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject>`
`[getOwners](#getOwners(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Deprecated.
use [`getAttachingProjects(IProject)`](#getAttachingProjects(com.nomagic.ci.persistence.IProject))
`static [Project](Project.html)`
`[getProject](#getProject(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject iProject)`
Returns MagicDraw project for primary or attached project.
`static com.nomagic.ci.persistence.IProject`
`[getProject](#getProject(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject object)`
Return project in which object resists.
`static com.nomagic.ci.persistence.IProject`
`[getProject](#getProject(org.eclipse.emf.ecore.resource.Resource))(org.eclipse.emf.ecore.resource.Resource resource)`
Return project for a resource.
`static com.nomagic.ci.persistence.IProject`
`[getProjectFor](#getProjectFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Find IProject for a given element
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteId](#getRemoteId(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Retrieves project remote id from given uri.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return remote id for a given project
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Extract remote project id from a given uri.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceID](#getResourceID(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Gets simplified resource id for given project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceID](#getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](project/ProjectDescriptor.html) pd)`
Gets simplified resource id for given project descriptor.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceID](#getResourceID(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Gets simplified resource id for given project location URI.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSaveID](#getSaveID(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Gets current save/commit id for given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getSharedPackages](#getSharedPackages(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return shared packages of a given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getSharedPackagesIncludingReshared](#getSharedPackagesIncludingReshared(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return shared packages of a given project.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getSharedPackagesIncludingResharedRecursively](#getSharedPackagesIncludingResharedRecursively(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return shared packages of a given project.
`static com.nomagic.ci.persistence.sharing.ISharePoint`
`[getSharePoint](#getSharePoint(com.nomagic.ci.persistence.mounting.IMountPoint))(com.nomagic.ci.persistence.mounting.IMountPoint point)`
Find share point corresponding given mount point
`static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html)`
`[getURI](#getURI(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI emfUFI)`
Convert EMF uri to java.net.URI
`static com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getVersion](#getVersion(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return version of given project.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVisibleURI](#getVisibleURI(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Creates uri that can be shown in UI components
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVisibleURI](#getVisibleURI(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Creates uri that can be shown in UI components
`static boolean`
`[isAttachedProjectIDRelevant](#isAttachedProjectIDRelevant(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.ci.persistence.IProject))([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 com.nomagic.ci.persistence.IProject attachedProject)`
Checks if moduleID relevant to attached project
`static boolean`
`[isAttachedProjectRoot](#isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if given element is a root of some module.
`static boolean`
`[isAttachedProjectRoot](#isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.ci.persistence.IAttachedProject))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.ci.persistence.IAttachedProject project)`
Check if given element is a root of given module.
`static boolean`
`[isElementInAttachedProject](#isElementInAttachedProject(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Check if given element belongs to some module
`static boolean`
`[isElementInAttachedProject](#isElementInAttachedProject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if given element belongs to some module
`static boolean`
`[isElementProxy](#isElementProxy(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Checks if given element is proxy or orphan proxy.
`static boolean`
`[isESIUri](#isESIUri(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Checks if given [`URI`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) is ESI project `URI`
`static boolean`
`[isESIUri](#isESIUri(org.eclipse.emf.common.util.URI))(org.eclipse.emf.common.util.URI uri)`
Checks if given `URI` is ESI project
 `URI`
`static boolean`
`[isFromEsiServer](#isFromEsiServer(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if given project is from ESI.
`static boolean`
`[isFromStandardProfile](#isFromStandardProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks, if the given element is a part of the Standard Profile
`static boolean`
`[isFromStandardProfile](#isFromStandardProfile(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject element)`
Checks if element comes from standard profile
`static boolean`
`[isFromTeamworkServer](#isFromTeamworkServer())()`
Deprecated.
teamwork server is end of life
`static boolean`
`[isLoaded](#isLoaded(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Checks if given project loaded.
`static boolean`
`[isLoadedOrLoading](#isLoadedOrLoading(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`

`static boolean`
`[isLoadIndex](#isLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration))(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)`
Check if to load index.
`static boolean`
`[isModule](#isModule(com.nomagic.ci.persistence.DecompositionDescriptor))(com.nomagic.ci.persistence.DecompositionDescriptor r)`
Deprecated.
DecompositionDescriptor is not exposed into Open API
`protected static boolean`
`[isModuleRoot](#isModuleRoot(com.nomagic.ci.persistence.IAttachedProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))(com.nomagic.ci.persistence.IAttachedProject iProject,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isModuleUsageNew](#isModuleUsageNew(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject attachedProject)`
Check if attached project usage from primary project is new (not yet committed to server).
`static boolean`
`[isMountedPackage](#isMountedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pck)`
Check if given package is a mounted(or is a shared root from some module)
`static boolean`
`[isProjectNameValid](#isProjectNameValid(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectName)`
Checks if given project name is valid.
`static boolean`
`[isRemote](#isRemote(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if given project is remote - from teamwork server or ESI.
`static boolean`
`[isSharedElement](#isSharedElement(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))(com.nomagic.ci.persistence.IProject project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if given element belongs to some shared (or reshared) package in a given project
`static boolean`
`[isStandardSystemProfile](#isStandardSystemProfile(com.nomagic.ci.persistence.DecompositionDescriptor))(com.nomagic.ci.persistence.DecompositionDescriptor project)`
Deprecated.
DecompositionDescriptor is not exposed into Open API
`static boolean`
`[isStandardSystemProfile](#isStandardSystemProfile(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if given project is a standard system profile
`static void`
`[setLoadIndex](#setLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,boolean))(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 boolean loadIndex)`
Set if to load index.
`static void`
`[updateConfigurationWithDefaultValues](#updateConfigurationWithDefaultValues(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration))(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration)`
Updates attachment configuration with default values
`static int`
`[versionToInt](#versionToInt(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Deprecated.
use [`versionToLong(String)`](#versionToLong(java.lang.String))
`static long`
`[versionToLong](#versionToLong(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Utility method to convert string representation of version into long
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[versionToString](#versionToString(int))(int version)`
Utility method to convert int representation of version into string
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
mExporterDescriptions
protected static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<com.nomagic.ci.persistence.IProject,[XmiExporterDescription](../../persistence/XmiExporterDescription.html)> mExporterDescriptions
EXPORTER_DESCRIPTION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXPORTER_DESCRIPTION
Property for XmiExporterDescription
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.ProjectUtilities.EXPORTER_DESCRIPTION)
REMOTE_ID_ENCODING
protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMOTE_ID_ENCODING
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.ProjectUtilities.REMOTE_ID_ENCODING)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectUtilities
public ProjectUtilities()
 ============ METHOD DETAIL ========== 
Method Details
createDefaultProjectAttachmentConfiguration
public static com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration createDefaultProjectAttachmentConfiguration(org.eclipse.emf.common.util.URI uri)
Create default project attachment configuration with default settings.
Parameters:
`uri` - uri
Returns:
attachment configuration
updateConfigurationWithDefaultValues
public static void updateConfigurationWithDefaultValues(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration)
Updates attachment configuration with default values
Parameters:
`configuration` - the configuration to update
isLoadIndex
public static boolean isLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)
Check if to load index.
Parameters:
`configuration` - attachment configuration.
Returns:
true if option is set to load index.
setLoadIndex
public static void setLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 boolean loadIndex)
Set if to load index.
Parameters:
`configuration` - attachment configuration.
`loadIndex` - load index.
getAttachedProject
@CheckReturnValue
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject getAttachedProject(@CheckForNull
 org.eclipse.emf.ecore.EObject element)
Find attached project (module) for a given element
Parameters:
`element` - element for which attached project will be returned
Returns:
project or null if element does not belong to any module
getProjectFor
@CheckForNullpublic static com.nomagic.ci.persistence.IProject getProjectFor(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Find IProject for a given element
Parameters:
`element` - element for which attached project will be returned
Returns:
project
findAttachedProjectByID
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByID([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 boolean recursively)
Find attached project by given id in a given project
Parameters:
`project` - project to search in
`moduleID` - module id
`recursively` - search in primary project only or recursively in whole project
Returns:
found module
isAttachedProjectIDRelevant
public static boolean isAttachedProjectIDRelevant([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 com.nomagic.ci.persistence.IProject attachedProject)
Checks if moduleID relevant to attached project
Parameters:
`project` - project
`moduleID` - expected module id
`attachedProject` - module
Returns:
true if moduleID relevant to attached project
findAttachedProjectByID
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByID(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID,
 boolean recursively)
Find attached project by given id in a given project
Parameters:
`project` - project to search in
`moduleID` - module id
`recursively` - search in primary project only or recursively in whole project
Returns:
found module
findAttachedProjectByProjectID
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByProjectID(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectID,
 boolean recursively)
Find attached project by given project id
Parameters:
`project` - project to search in
`projectID` - module id
`recursively` - search in primary project only or recursively in whole project
Returns:
found module
findProjectByResourceID
@CheckForNullpublic static com.nomagic.ci.persistence.IProject findProjectByResourceID(com.nomagic.ci.persistence.IPrimaryProject primaryProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceId)
Search for project with given resource ID
Parameters:
`primaryProject` - scope of searching
`resourceId` - resource ID.
Returns:
found project or null.
findAttachedProjectByName
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByName([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean recursively)
Find attached project by given name in a given project
Parameters:
`project` - project to search in
`name` - module name
`recursively` - search in primary project only or recursively in whole project
Returns:
found module
findAttachedProjectByName
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByName(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Find attached project by given name in a given project
Parameters:
`project` - project to search in
`name` - module name
Returns:
found module
findAttachedProjectByNames
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByNames([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> names,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> modules)
findAttachedProjectByName
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByName([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Find attached project by given name in a given project. Does recursive search.
Parameters:
`project` - project to search in
`name` - module name
Returns:
found module
findAttachedProjectByID
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject findAttachedProjectByID([Project](Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) moduleID)
Find attached project by given id in a given project. Does recursive search.
Parameters:
`project` - project to search in
`moduleID` - module id
Returns:
found module
isAttachedProjectRoot
public static boolean isAttachedProjectRoot(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if given element is a root of some module.
Parameters:
`element` - element
Returns:
true if given element is root for module.
isAttachedProjectRoot
public static boolean isAttachedProjectRoot(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.ci.persistence.IAttachedProject project)
Check if given element is a root of given module.
Parameters:
`element` - element
`project` - module
Returns:
true if given element is root for module
getSharedPackages
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getSharedPackages(com.nomagic.ci.persistence.IProject project)
Return shared packages of a given project. Does not include re-shared packages.
Parameters:
`project` - project
Returns:
shared packages.
getSharedPackagesIncludingReshared
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getSharedPackagesIncludingReshared(com.nomagic.ci.persistence.IProject project)
Return shared packages of a given project. Include also re-shared packages
Parameters:
`project` - project
Returns:
shared packages
getSharedPackagesIncludingResharedRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getSharedPackagesIncludingResharedRecursively(com.nomagic.ci.persistence.IProject project)
Return shared packages of a given project. Include also re-shared packages. Takes direct packages and also from
 attached modules recursively of a given project.
 For ESI project returns module model.
Parameters:
`project` - project
Returns:
shared packages
isElementInAttachedProject
public static boolean isElementInAttachedProject([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if given element belongs to some module
Parameters:
`element` - element
Returns:
true if element belongs to some module
isElementInAttachedProject
public static boolean isElementInAttachedProject(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Check if given element belongs to some module
Parameters:
`element` - element
Returns:
true if element belongs to some module
getAllAttachedProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> getAllAttachedProjects([Project](Project.html) project)
Return all modules in a given project
Parameters:
`project` - project
Returns:
all modules in the Project
getAllProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject> getAllProjects([Project](Project.html) project)
Return all modules and primary project in a given project
Parameters:
`project` - project
Returns:
all modules in the Project, collection is not modifiable
isSharedElement
public static boolean isSharedElement(com.nomagic.ci.persistence.IProject project,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if given element belongs to some shared (or reshared) package in a given project
Parameters:
`project` - project
`element` - element
Returns:
true if element belongs to shared package
getRemoteID
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID(org.eclipse.emf.common.util.URI uri)
Extract remote project id from a given uri.
Parameters:
`uri` - uri
Returns:
remote if or null
getRemoteID
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID(com.nomagic.ci.persistence.IProject project)
Return remote id for a given project
Parameters:
`project` - project
Returns:
remote id
versionToInt
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static int versionToInt(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Deprecated.
use [`versionToLong(String)`](#versionToLong(java.lang.String))
Utility method to convert string representation of version into int
Parameters:
`version` - version
Returns:
version as int
versionToLong
public static long versionToLong(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Utility method to convert string representation of version into long
Parameters:
`version` - version
Returns:
version as long
versionToString
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionToString(int version)
Utility method to convert int representation of version into string
Parameters:
`version` - version
Returns:
version as string
getResourceID
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceID(com.nomagic.ci.persistence.IProject project)
Gets simplified resource id for given project.
 For remote project it returns project id, for local filename.
Parameters:
`project` - project descriptor
Returns:
filename or project id.
getResourceID
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceID([ProjectDescriptor](project/ProjectDescriptor.html) pd)
Gets simplified resource id for given project descriptor. For remote project it returns project id, for local filename.
Parameters:
`pd` - project descriptor
Returns:
filename or project id.
getResourceID
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceID(org.eclipse.emf.common.util.URI uri)
Gets simplified resource id for given project location URI.
 For remote project it returns project id, for local filename.
Parameters:
`uri` - project location.
Returns:
filename or project id.
getAttachedProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> getAttachedProjects(com.nomagic.ci.persistence.IProject project)
Returns projects those are attached directly to a given project.
 Primary attached project is ignored.
Parameters:
`project` - project
Returns:
collection of attached projects
getAllAttachedProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> getAllAttachedProjects(com.nomagic.ci.persistence.IProject project)
Returns projects those are attached directly or indirectly to a given project.
 Primary attached project is ignored.
Parameters:
`project` - project
Returns:
collection of attached projects
getAllAttachedProjectsIncludingPrimary
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject> getAllAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject project)
Returns projects those are attached directly or indirectly to a given project including primary project.
Parameters:
`project` - project
Returns:
collection of attached projects
getAllAttachedProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> getAllAttachedProjects([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IAttachedProject> projects)
Returns projects those are attached directly or indirectly to a given project.
 Primary attached project is ignored.
Parameters:
`projects` - project projects
Returns:
collection of attached projects
getAttachedProjectsIncludingPrimary
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject> getAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject project)
Returns projects those are attached directly to a given project.Primary attached project can be included also.
Parameters:
`project` - project
Returns:
collection of attached projects
getAutoLoadKind
public static [AutoLoadKind](modules/AutoLoadKind.html) getAutoLoadKind(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject project)
Return load kind of given module in a given project
Parameters:
`owner` - project
`project` - module
Returns:
load kind
getAutoLoadKind
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [AutoLoadKind](modules/AutoLoadKind.html) getAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration attachment)
Deprecated.
use public static AutoLoadKind getAutoLoadKind( AbstractProjectAttachmentConfiguration attachment )
Return load kind of module from given attachment
Parameters:
`attachment` - attachment
Returns:
load kind
getAutoLoadKind
public static [AutoLoadKind](modules/AutoLoadKind.html) getAutoLoadKind(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration attachment)
Return load kind of module from given attachment
Parameters:
`attachment` - attachment
Returns:
load kind
getAttachingProject
@CheckForNullpublic static com.nomagic.ci.persistence.IProject getAttachingProject(com.nomagic.ci.persistence.IProject project)
Return first project where given project is attached. Primary project has always priority.
Parameters:
`project` - given project
Returns:
first project where given module is attached.
getAttachingProjects
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject> getAttachingProjects(com.nomagic.ci.persistence.IProject project)
Return all projects where given project is attached.
Parameters:
`project` - given project.
Returns:
all projects where given module is attached.
getOwner
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static com.nomagic.ci.persistence.IProject getOwner(com.nomagic.ci.persistence.IProject project)
Deprecated.
use [`getAttachingProject(IProject)`](#getAttachingProject(com.nomagic.ci.persistence.IProject))
getOwners
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.IProject> getOwners(com.nomagic.ci.persistence.IProject project)
Deprecated.
use [`getAttachingProjects(IProject)`](#getAttachingProjects(com.nomagic.ci.persistence.IProject))
getEMFURI
public static org.eclipse.emf.common.util.URI getEMFURI([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Convert java net URI to emf uri
Parameters:
`uri` - net uri
Returns:
emf uri
getAttachment
@CheckForNullpublic static com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration getAttachment(com.nomagic.ci.persistence.IProject parent,
 com.nomagic.ci.persistence.IProject child)
Return configuration which is used to attach one project to another
Parameters:
`parent` - project which uses another project (directly)
`child` - used directly project
Returns:
found `ProjectAttachmentConfiguration` (for local and teamwork projects) or
 `EsiProjectAttachmentConfiguration` (for Teamwork Cloud projects) or null if such not found.
getURI
public static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) getURI(org.eclipse.emf.common.util.URI emfUFI)
Convert EMF uri to java.net.URI
Parameters:
`emfUFI` - emf uri
Returns:
java net uri
getVersion
@CheckForNullpublic static com.nomagic.ci.persistence.versioning.IVersionDescriptor getVersion(com.nomagic.ci.persistence.IProject project)
Return version of given project.
Parameters:
`project` - project
Returns:
version or null if project has no version
isFromTeamworkServer
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isFromTeamworkServer()
Deprecated.
teamwork server is end of life
Check if given project is from teamwork server.
Returns:
true if project is from server
isFromEsiServer
public static boolean isFromEsiServer(@CheckForNull
 com.nomagic.ci.persistence.IProject project)
Check if given project is from ESI.
Parameters:
`project` - project
Returns:
true if project is from ESI
isRemote
public static boolean isRemote(@CheckForNull
 com.nomagic.ci.persistence.IProject project)
Check if given project is remote - from teamwork server or ESI.
Parameters:
`project` - project
Returns:
true if project is from server
isFromStandardProfile
public static boolean isFromStandardProfile([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Checks, if the given element is a part of the Standard Profile
Parameters:
`element` - element to check
Returns:
true, if the given element is a part of the Standard Profile
getProject
@CheckForNullpublic static [Project](Project.html) getProject(@CheckForNull
 com.nomagic.ci.persistence.IProject iProject)
Returns MagicDraw project for primary or attached project.
Parameters:
`iProject` - primary or attached project
Returns:
[`Project`](Project.html)
getMountPoint
@CheckForNullpublic static com.nomagic.ci.persistence.mounting.IMountPoint getMountPoint([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> points,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) element)
Find mount point in a given collection which mounts a given package.
Parameters:
`points` - mount points
`element` - package
Returns:
found mount point
getSharePoint
@CheckForNullpublic static com.nomagic.ci.persistence.sharing.ISharePoint getSharePoint(com.nomagic.ci.persistence.mounting.IMountPoint point)
Find share point corresponding given mount point
Parameters:
`point` - mount point
Returns:
share point
encodeTeamworkRemoteId
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) encodeTeamworkRemoteId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) remoteId)
Deprecated.
teamwork server is end of life
Encodes Teamwork remote ID
Parameters:
`remoteId` - the raw (not encoded) remote ID
Returns:
encoded ID
decodeTeamworkRemoteId
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) decodeTeamworkRemoteId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) remoteId)
Deprecated.
teamwork server is end of life
Decodes Teamwork remote ID
Parameters:
`remoteId` - the encoded remote ID
Returns:
decoded (raw) remote ID
isESIUri
public static boolean isESIUri(org.eclipse.emf.common.util.URI uri)
Checks if given `URI` is ESI project
 `URI`
Parameters:
`uri` - the `URI` to check
Returns:
`true` if given `URI` is ESI,
 `false` otherwise
isESIUri
public static boolean isESIUri([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Checks if given [`URI`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) is ESI project `URI`
Parameters:
`uri` - the `URI` to check
Returns:
`true` if given `URI` is ESI,
 `false` otherwise
isElementProxy
public static boolean isElementProxy([BaseElement](../uml/BaseElement.html) element)
Checks if given element is proxy or orphan proxy.
Parameters:
`element` - the element to check
Returns:
`true` if given element is proxy or orphan proxy, otherwise - `false`
getESIRemoteId
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getESIRemoteId(org.eclipse.emf.common.util.URI uri)
Gets ESI remote ID
Parameters:
`uri` - the `URI` to get remote ID
 for
Returns:
the remote ID
getESIRemoteId
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getESIRemoteId(com.nomagic.ci.persistence.IProject project)
Gets ESI remote ID for given project
Parameters:
`project` - the project
Returns:
the remote ID
getRemoteId
@CheckReturnValue
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteId(org.eclipse.emf.common.util.URI uri)
Retrieves project remote id from given uri.
Parameters:
`uri` - remote project uri to check.
Returns:
remote project id from project uri.
getMountPoints
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> getMountPoints(com.nomagic.ci.persistence.IProject project)
Gets all mount points in given project. Returns empty set if there are no mount points
Parameters:
`project` - project
Returns:
non-`null` set of all `mount points`
getMountPointsFor
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.mounting.IMountPoint> getMountPointsFor(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject attachedProject)
Gets mount points for given project, i.e. returns all mount points that are mounted share points of given project.
 Returns empty set if there are no mount points to return.
Parameters:
`owner` - owner
`attachedProject` - the project to get mount points for
Returns:
non-`null` set of `mount points` for specific project
getAllMountPoints
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.ci.persistence.mounting.IMountPoint> getAllMountPoints(com.nomagic.ci.persistence.IPrimaryProject project)
Return all mount points existing in given primary project (direct and not direct).
Parameters:
`project` - project
Returns:
all mount points from given project and from all attached
getProject
@CheckForNullpublic static com.nomagic.ci.persistence.IProject getProject(@CheckForNull
 org.eclipse.emf.ecore.EObject object)
Return project in which object resists.
Parameters:
`object` - object
Returns:
found project or null
getProject
@CheckForNullpublic static com.nomagic.ci.persistence.IProject getProject(@CheckForNull
 org.eclipse.emf.ecore.resource.Resource resource)
Return project for a resource.
Parameters:
`resource` - resource
Returns:
found project or null
compareVersions
public static int compareVersions(@CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor1,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor2)
Compare given versions descriptors. *The null descriptor is larger than not null.*
Parameters:
`versionDescriptor1` - first version descriptor (can be null).
`versionDescriptor2` - second version descriptor (can be null).
Returns:
the value 0 if versions are equal; a value less than 0 if first version is less than second;
 and a value greater than 0 if first version is greater than second.
compareVersionNumber
public static int compareVersionNumber(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionNumber1,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionNumber2)
Compare given version numbers.
Parameters:
`versionNumber1` - first version number.
`versionNumber2` - second version number.
Returns:
the value 0 if versions are equal; a value less than 0 if first version is less than second;
 and a value greater than 0 if first version is greater than second.
getAttachedProject
@CheckForNullpublic static com.nomagic.ci.persistence.IAttachedProject getAttachedProject(com.nomagic.ci.persistence.IProject project,
 org.eclipse.emf.common.util.URI uri)
Look for direct or not direct attached project in a primary project of a given project.
Parameters:
`project` - project
`uri` - uri
Returns:
found module
getElementFor
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElementFor(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Return element for a given base element. Returned element can be passed into other utility methods as EObject if needed.
Parameters:
`element` - base element
Returns:
model element
getModelElementFor
@CheckForNullpublic static com.dassault_systemes.modeler.foundation.model.ModelElement getModelElementFor(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Return element for a given base element. Returned element can be passed into other utility methods as EObject if needed.
Parameters:
`element` - base element
Returns:
model element
isMountedPackage
public static boolean isMountedPackage([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) pck)
Check if given package is a mounted(or is a shared root from some module)
Parameters:
`pck` - package
Returns:
true if package is mounted
isModuleRoot
protected static boolean isModuleRoot(com.nomagic.ci.persistence.IAttachedProject iProject,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getInternalVersion
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getInternalVersion(com.nomagic.ci.persistence.IProject project)
Get internal version of project
Parameters:
`project` - project
Returns:
version
getCompatibleVersion
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCompatibleVersion(com.nomagic.ci.persistence.IProject project)
Get compatible version of the project
Parameters:
`project` - project
Returns:
compatible version
isStandardSystemProfile
public static boolean isStandardSystemProfile(com.nomagic.ci.persistence.IProject project)
Check if given project is a standard system profile
Parameters:
`project` - project
Returns:
true if given project is a standard system profile
isStandardSystemProfile
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isStandardSystemProfile(com.nomagic.ci.persistence.DecompositionDescriptor project)
Deprecated.
DecompositionDescriptor is not exposed into Open API
Check if given project is a standard system profile
Parameters:
`project` - project
Returns:
true if given project is a standard system profile
isLoaded
public static boolean isLoaded(com.nomagic.ci.persistence.IProject project)
Checks if given project loaded.
Parameters:
`project` - project
Returns:
true if given project is loaded
isLoadedOrLoading
public static boolean isLoadedOrLoading(com.nomagic.ci.persistence.IProject project)
isModule
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isModule(com.nomagic.ci.persistence.DecompositionDescriptor r)
Deprecated.
DecompositionDescriptor is not exposed into Open API
Returns true if given project has shared points.
Parameters:
`r` - project descriptor to evaluate
Returns:
true if given project descriptor represents a module.
isFromStandardProfile
public static boolean isFromStandardProfile(@CheckForNull
 org.eclipse.emf.ecore.EObject element)
Checks if element comes from standard profile
Parameters:
`element` - element to be checked
Returns:
true if element comes from standard profile.
getModifiedElements
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getModifiedElements([Project](Project.html) project)
Get modified elements.
Parameters:
`project` - project to get elements of.
Returns:
modified elements.
getExporterDescription
@CheckForNullpublic static [XmiExporterDescription](../../persistence/XmiExporterDescription.html) getExporterDescription(com.nomagic.ci.persistence.IProject project)
Provide information about project version and required resources/plugins for that project.
Parameters:
`project` - project
Returns:
description of project
getSaveID
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSaveID(com.nomagic.ci.persistence.IProject project)
Gets current save/commit id for given project.
 The value of the Save ID is a randomly generated unique UUID.
Parameters:
`project` - project
Returns:
save id
addToCacheLoaded
protected static void addToCacheLoaded(com.nomagic.ci.persistence.IProject project,
 [XmiExporterDescription](../../persistence/XmiExporterDescription.html) xmiExporterDescription)
Adds to cache just loaded modules/projects
Parameters:
`project` - project/module
`xmiExporterDescription` - project/module descriptor
addToCache
protected static void addToCache(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 [XmiExporterDescription](../../persistence/XmiExporterDescription.html) xmiExporterDescription)
isModuleUsageNew
public static boolean isModuleUsageNew(com.nomagic.ci.persistence.IProject attachedProject)
Check if attached project usage from primary project is new (not yet committed to server).
 This method does not support checking if the usage is new for Teamwork Server Project therefore
 it always returns `false` in that case.
Parameters:
`attachedProject` - the `IProject` of attached project
Returns:
`true` if the provided project is attached project, and it is a Teamwork Cloud Project
 and if the usage from primary project to attached project exists and if it is new (as defined above).
 Return `false` otherwise
getVisibleURI
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVisibleURI([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Creates uri that can be shown in UI components
Parameters:
`uri` - project location uri
Returns:
visible uri
getVisibleURI
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVisibleURI(org.eclipse.emf.common.util.URI uri)
Creates uri that can be shown in UI components
Parameters:
`uri` - project location uri
Returns:
visible uri
isProjectNameValid
public static boolean isProjectNameValid([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) projectName)
Checks if given project name is valid. Checks if either the given project name is reserved or
 has invalid characters
Parameters:
`projectName` - the project name to check
Returns:
`true` if project name is valid, `false` otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class ProjectUtilities">Class ProjectUtilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.ProjectUtilities</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectUtilities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Project decomposition related utility class.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXPORTER_DESCRIPTION">EXPORTER_DESCRIPTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Property for XmiExporterDescription</div>
</div>
<div class="col-first odd-row-color"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;com.nomagic.ci.persistence.IProject,<wbr/><a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mExporterDescriptions">mExporterDescriptions</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>protected static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REMOTE_ID_ENCODING">REMOTE_ID_ENCODING</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectUtilities</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addToCache(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription)">addToCache</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> xmiExporterDescription)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addToCacheLoaded(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription)">addToCacheLoaded</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> xmiExporterDescription)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds to cache just loaded modules/projects</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compareVersionNumber(java.lang.String,java.lang.String)">compareVersionNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> versionNumber1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> versionNumber2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare given version numbers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compareVersions(com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">compareVersions</a><wbr/>(com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor1,
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare given versions descriptors.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultProjectAttachmentConfiguration(org.eclipse.emf.common.util.URI)">createDefaultProjectAttachmentConfiguration</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create default project attachment configuration with default settings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#decodeTeamworkRemoteId(java.lang.String)">decodeTeamworkRemoteId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> remoteId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#encodeTeamworkRemoteId(java.lang.String)">encodeTeamworkRemoteId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> remoteId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean)">findAttachedProjectByID</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 boolean recursively)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given id in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String)">findAttachedProjectByID</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given id in a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">findAttachedProjectByID</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 boolean recursively)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given id in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByName(com.nomagic.ci.persistence.IProject,java.lang.String)">findAttachedProjectByName</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given name in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String)">findAttachedProjectByName</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given name in a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">findAttachedProjectByName</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean recursively)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given name in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByNames(java.util.Collection,java.util.Collection)">findAttachedProjectByNames</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; names,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; modules)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findAttachedProjectByProjectID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean)">findAttachedProjectByProjectID</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 boolean recursively)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project by given project id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findProjectByResourceID(com.nomagic.ci.persistence.IPrimaryProject,java.lang.String)">findProjectByResourceID</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject primaryProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for project with given resource ID</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllAttachedProjects(com.nomagic.ci.persistence.IProject)">getAllAttachedProjects</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects those are attached directly or indirectly to a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllAttachedProjects(com.nomagic.magicdraw.core.Project)">getAllAttachedProjects</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all modules in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllAttachedProjects(java.util.Collection)">getAllAttachedProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; projects)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects those are attached directly or indirectly to a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject)">getAllAttachedProjectsIncludingPrimary</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects those are attached directly or indirectly to a given project including primary project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllMountPoints(com.nomagic.ci.persistence.IPrimaryProject)">getAllMountPoints</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all mount points existing in given primary project (direct and not direct).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllProjects(com.nomagic.magicdraw.core.Project)">getAllProjects</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all modules and primary project in a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.common.util.URI)">getAttachedProject</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Look for direct or not direct attached project in a primary project of a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedProject(org.eclipse.emf.ecore.EObject)">getAttachedProject</a><wbr/>(org.eclipse.emf.ecore.EObject element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find attached project (module) for a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedProjects(com.nomagic.ci.persistence.IProject)">getAttachedProjects</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects those are attached directly to a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject)">getAttachedProjectsIncludingPrimary</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns projects those are attached directly to a given project.Primary attached project can be included also.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachingProject(com.nomagic.ci.persistence.IProject)">getAttachingProject</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return first project where given project is attached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachingProjects(com.nomagic.ci.persistence.IProject)">getAttachingProjects</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return all projects where given project is attached.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachment(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">getAttachment</a><wbr/>(com.nomagic.ci.persistence.IProject parent,
 com.nomagic.ci.persistence.IProject child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return configuration which is used to attach one project to another</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration)">getAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration attachment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use public static   AutoLoadKind getAutoLoadKind(  AbstractProjectAttachmentConfiguration attachment )</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">getAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return load kind of given module in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoLoadKind(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">getAutoLoadKind</a><wbr/>(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration attachment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return load kind of module from given attachment</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompatibleVersion(com.nomagic.ci.persistence.IProject)">getCompatibleVersion</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get compatible version of the project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementFor(com.nomagic.magicdraw.uml.BaseElement)">getElementFor</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return element for a given base element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEMFURI(java.net.URI)">getEMFURI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert java net URI to emf uri</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getESIRemoteId(com.nomagic.ci.persistence.IProject)">getESIRemoteId</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets ESI remote ID for given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getESIRemoteId(org.eclipse.emf.common.util.URI)">getESIRemoteId</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets ESI remote ID</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExporterDescription(com.nomagic.ci.persistence.IProject)">getExporterDescription</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Provide information about project version and required resources/plugins for that project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInternalVersion(com.nomagic.ci.persistence.IProject)">getInternalVersion</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get internal version of project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementFor(com.nomagic.magicdraw.uml.BaseElement)">getModelElementFor</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return element for a given base element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModifiedElements(com.nomagic.magicdraw.core.Project)">getModifiedElements</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get modified elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.mounting.IMountPoint</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">getMountPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt; points,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find mount point in a given collection which mounts a given package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMountPoints(com.nomagic.ci.persistence.IProject)">getMountPoints</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets all mount points in given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMountPointsFor(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">getMountPointsFor</a><wbr/>(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets mount points for given project, i.e.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getOwner(com.nomagic.ci.persistence.IProject)">getOwner</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAttachingProject(com.nomagic.ci.persistence.IProject)"><code>getAttachingProject(IProject)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getOwners(com.nomagic.ci.persistence.IProject)">getOwners</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAttachingProjects(com.nomagic.ci.persistence.IProject)"><code>getAttachingProjects(IProject)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(com.nomagic.ci.persistence.IProject)">getProject</a><wbr/>(com.nomagic.ci.persistence.IProject iProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns MagicDraw project for primary or attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(org.eclipse.emf.ecore.EObject)">getProject</a><wbr/>(org.eclipse.emf.ecore.EObject object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return project in which object resists.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(org.eclipse.emf.ecore.resource.Resource)">getProject</a><wbr/>(org.eclipse.emf.ecore.resource.Resource resource)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return project for a resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectFor(com.nomagic.magicdraw.uml.BaseElement)">getProjectFor</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find IProject for a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteId(org.eclipse.emf.common.util.URI)">getRemoteId</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves project remote id from given uri.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID(com.nomagic.ci.persistence.IProject)">getRemoteID</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return remote id for a given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID(org.eclipse.emf.common.util.URI)">getRemoteID</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extract remote project id from a given uri.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceID(com.nomagic.ci.persistence.IProject)">getResourceID</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets simplified resource id for given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getResourceID</a><wbr/>(<a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets simplified resource id for given project descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceID(org.eclipse.emf.common.util.URI)">getResourceID</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets simplified resource id for given project location URI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSaveID(com.nomagic.ci.persistence.IProject)">getSaveID</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets current save/commit id for given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedPackages(com.nomagic.ci.persistence.IProject)">getSharedPackages</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return shared packages of a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedPackagesIncludingReshared(com.nomagic.ci.persistence.IProject)">getSharedPackagesIncludingReshared</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return shared packages of a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedPackagesIncludingResharedRecursively(com.nomagic.ci.persistence.IProject)">getSharedPackagesIncludingResharedRecursively</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return shared packages of a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.sharing.ISharePoint</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharePoint(com.nomagic.ci.persistence.mounting.IMountPoint)">getSharePoint</a><wbr/>(com.nomagic.ci.persistence.mounting.IMountPoint point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Find share point corresponding given mount point</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getURI(org.eclipse.emf.common.util.URI)">getURI</a><wbr/>(org.eclipse.emf.common.util.URI emfUFI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert EMF uri to java.net.URI</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion(com.nomagic.ci.persistence.IProject)">getVersion</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return version of given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleURI(java.net.URI)">getVisibleURI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates uri that can be shown in UI components</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleURI(org.eclipse.emf.common.util.URI)">getVisibleURI</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates uri that can be shown in UI components</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAttachedProjectIDRelevant(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.ci.persistence.IProject)">isAttachedProjectIDRelevant</a><wbr/>(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 com.nomagic.ci.persistence.IProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if moduleID relevant to attached project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isAttachedProjectRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element is a root of some module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.ci.persistence.IAttachedProject)">isAttachedProjectRoot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.ci.persistence.IAttachedProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element is a root of given module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInAttachedProject(com.dassault_systemes.modeler.foundation.model.ModelElement)">isElementInAttachedProject</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element belongs to some module</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementInAttachedProject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementInAttachedProject</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element belongs to some module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementProxy(com.nomagic.magicdraw.uml.BaseElement)">isElementProxy</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given element is proxy or orphan proxy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isESIUri(java.net.URI)">isESIUri</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net"><code>URI</code></a> is ESI project <code>URI</code></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isESIUri(org.eclipse.emf.common.util.URI)">isESIUri</a><wbr/>(org.eclipse.emf.common.util.URI uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given <code>URI</code> is ESI project
 <code>URI</code></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFromEsiServer(com.nomagic.ci.persistence.IProject)">isFromEsiServer</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given project is from ESI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFromStandardProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFromStandardProfile</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks, if the given element is a part of the Standard Profile</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFromStandardProfile(org.eclipse.emf.ecore.EObject)">isFromStandardProfile</a><wbr/>(org.eclipse.emf.ecore.EObject element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if element comes from standard profile</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFromTeamworkServer()">isFromTeamworkServer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded(com.nomagic.ci.persistence.IProject)">isLoaded</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given project loaded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoadedOrLoading(com.nomagic.ci.persistence.IProject)">isLoadedOrLoading</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">isLoadIndex</a><wbr/>(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if to load index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isModule(com.nomagic.ci.persistence.DecompositionDescriptor)">isModule</a><wbr/>(com.nomagic.ci.persistence.DecompositionDescriptor r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">DecompositionDescriptor is not exposed into Open API</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isModuleRoot(com.nomagic.ci.persistence.IAttachedProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isModuleRoot</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject iProject,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isModuleUsageNew(com.nomagic.ci.persistence.IProject)">isModuleUsageNew</a><wbr/>(com.nomagic.ci.persistence.IProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if attached project usage from primary project is new (not yet committed to server).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMountedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">isMountedPackage</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pck)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given package is a mounted(or is a shared root from some module)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectNameValid(java.lang.String)">isProjectNameValid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given project name is valid.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote(com.nomagic.ci.persistence.IProject)">isRemote</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given project is remote - from teamwork server or ESI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSharedElement(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSharedElement</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element belongs to some shared (or reshared) package in a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isStandardSystemProfile(com.nomagic.ci.persistence.DecompositionDescriptor)">isStandardSystemProfile</a><wbr/>(com.nomagic.ci.persistence.DecompositionDescriptor project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">DecompositionDescriptor is not exposed into Open API</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStandardSystemProfile(com.nomagic.ci.persistence.IProject)">isStandardSystemProfile</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given project is a standard system profile</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,boolean)">setLoadIndex</a><wbr/>(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 boolean loadIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set if to load index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateConfigurationWithDefaultValues(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration)">updateConfigurationWithDefaultValues</a><wbr/>(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates attachment configuration with default values</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#versionToInt(java.lang.String)">versionToInt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#versionToLong(java.lang.String)"><code>versionToLong(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#versionToLong(java.lang.String)">versionToLong</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Utility method to convert string representation of version into long</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#versionToString(int)">versionToString</a><wbr/>(int version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Utility method to convert int representation of version into string</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="mExporterDescriptions">
<h3>mExporterDescriptions</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;com.nomagic.ci.persistence.IProject,<wbr/><a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a>&gt;</span> <span class="element-name">mExporterDescriptions</span></div>
</section>
</li>
<li>
<section class="detail" id="EXPORTER_DESCRIPTION">
<h3>EXPORTER_DESCRIPTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXPORTER_DESCRIPTION</span></div>
<div class="block">Property for XmiExporterDescription</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.ProjectUtilities.EXPORTER_DESCRIPTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMOTE_ID_ENCODING">
<h3>REMOTE_ID_ENCODING</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMOTE_ID_ENCODING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.ProjectUtilities.REMOTE_ID_ENCODING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectUtilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectUtilities</span>()</div>
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
<section class="detail" id="createDefaultProjectAttachmentConfiguration(org.eclipse.emf.common.util.URI)">
<h3>createDefaultProjectAttachmentConfiguration</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration</span> <span class="element-name">createDefaultProjectAttachmentConfiguration</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Create default project attachment configuration with default settings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri</dd>
<dt>Returns:</dt>
<dd>attachment configuration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateConfigurationWithDefaultValues(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration)">
<h3>updateConfigurationWithDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateConfigurationWithDefaultValues</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration configuration)</span></div>
<div class="block">Updates attachment configuration with default values</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - the configuration to update</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">
<h3>isLoadIndex</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLoadIndex</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration)</span></div>
<div class="block">Check if to load index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - attachment configuration.</dd>
<dt>Returns:</dt>
<dd>true if option is set to load index.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoadIndex(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration,boolean)">
<h3>setLoadIndex</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLoadIndex</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration configuration,
 boolean loadIndex)</span></div>
<div class="block">Set if to load index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - attachment configuration.</dd>
<dd><code>loadIndex</code> - load index.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedProject(org.eclipse.emf.ecore.EObject)">
<h3>getAttachedProject</h3>
<div class="member-signature"><span class="annotations">@CheckReturnValue
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">getAttachedProject</span><wbr/><span class="parameters">(@CheckForNull
 org.eclipse.emf.ecore.EObject element)</span></div>
<div class="block">Find attached project (module) for a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which attached project will be returned</dd>
<dt>Returns:</dt>
<dd>project or null if element does not belong to any module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getProjectFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getProjectFor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Find IProject for a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which attached project will be returned</dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>findAttachedProjectByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByID</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 boolean recursively)</span></div>
<div class="block">Find attached project by given id in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>moduleID</code> - module id</dd>
<dd><code>recursively</code> - search in primary project only or recursively in whole project</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAttachedProjectIDRelevant(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.ci.persistence.IProject)">
<h3>isAttachedProjectIDRelevant</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAttachedProjectIDRelevant</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 com.nomagic.ci.persistence.IProject attachedProject)</span></div>
<div class="block">Checks if moduleID relevant to attached project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>moduleID</code> - expected module id</dd>
<dd><code>attachedProject</code> - module</dd>
<dt>Returns:</dt>
<dd>true if moduleID relevant to attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean)">
<h3>findAttachedProjectByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID,
 boolean recursively)</span></div>
<div class="block">Find attached project by given id in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>moduleID</code> - module id</dd>
<dd><code>recursively</code> - search in primary project only or recursively in whole project</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByProjectID(com.nomagic.ci.persistence.IProject,java.lang.String,boolean)">
<h3>findAttachedProjectByProjectID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByProjectID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectID,
 boolean recursively)</span></div>
<div class="block">Find attached project by given project id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>projectID</code> - module id</dd>
<dd><code>recursively</code> - search in primary project only or recursively in whole project</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findProjectByResourceID(com.nomagic.ci.persistence.IPrimaryProject,java.lang.String)">
<h3>findProjectByResourceID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">findProjectByResourceID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject primaryProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceId)</span></div>
<div class="block">Search for project with given resource ID</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primaryProject</code> - scope of searching</dd>
<dd><code>resourceId</code> - resource ID.</dd>
<dt>Returns:</dt>
<dd>found project or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>findAttachedProjectByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByName</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean recursively)</span></div>
<div class="block">Find attached project by given name in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>name</code> - module name</dd>
<dd><code>recursively</code> - search in primary project only or recursively in whole project</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByName(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>findAttachedProjectByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByName</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Find attached project by given name in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>name</code> - module name</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByNames(java.util.Collection,java.util.Collection)">
<h3>findAttachedProjectByNames</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByNames</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; names,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; modules)</span></div>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByName(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>findAttachedProjectByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByName</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Find attached project by given name in a given project. Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>name</code> - module name</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findAttachedProjectByID(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>findAttachedProjectByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">findAttachedProjectByID</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> moduleID)</span></div>
<div class="block">Find attached project by given id in a given project. Does recursive search.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to search in</dd>
<dd><code>moduleID</code> - module id</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isAttachedProjectRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAttachedProjectRoot</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element is a root of some module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if given element is root for module.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAttachedProjectRoot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.ci.persistence.IAttachedProject)">
<h3>isAttachedProjectRoot</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAttachedProjectRoot</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.ci.persistence.IAttachedProject project)</span></div>
<div class="block">Check if given element is a root of given module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>project</code> - module</dd>
<dt>Returns:</dt>
<dd>true if given element is root for module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedPackages(com.nomagic.ci.persistence.IProject)">
<h3>getSharedPackages</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getSharedPackages</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return shared packages of a given project. Does not include re-shared packages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>shared packages.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedPackagesIncludingReshared(com.nomagic.ci.persistence.IProject)">
<h3>getSharedPackagesIncludingReshared</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getSharedPackagesIncludingReshared</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return shared packages of a given project. Include also re-shared packages</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>shared packages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedPackagesIncludingResharedRecursively(com.nomagic.ci.persistence.IProject)">
<h3>getSharedPackagesIncludingResharedRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getSharedPackagesIncludingResharedRecursively</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return shared packages of a given project. Include also re-shared packages. Takes direct packages and also from
 attached modules recursively of a given project.
 For ESI project returns module model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>shared packages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInAttachedProject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isElementInAttachedProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isElementInAttachedProject</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element belongs to some module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element belongs to some module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementInAttachedProject(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>isElementInAttachedProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isElementInAttachedProject</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Check if given element belongs to some module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element belongs to some module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllAttachedProjects(com.nomagic.magicdraw.core.Project)">
<h3>getAllAttachedProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</span> <span class="element-name">getAllAttachedProjects</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Return all modules in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>all modules in the Project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllProjects(com.nomagic.magicdraw.core.Project)">
<h3>getAllProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</span> <span class="element-name">getAllProjects</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Return all modules and primary project in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>all modules in the Project, collection is not modifiable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSharedElement(com.nomagic.ci.persistence.IProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSharedElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSharedElement</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element belongs to some shared (or reshared) package in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element belongs to shared package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteID(org.eclipse.emf.common.util.URI)">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Extract remote project id from a given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri</dd>
<dt>Returns:</dt>
<dd>remote if or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteID(com.nomagic.ci.persistence.IProject)">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return remote id for a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>remote id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="versionToInt(java.lang.String)">
<h3>versionToInt</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">versionToInt</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#versionToLong(java.lang.String)"><code>versionToLong(String)</code></a></div>
</div>
<div class="block">Utility method to convert string representation of version into int</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - version</dd>
<dt>Returns:</dt>
<dd>version as int</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="versionToLong(java.lang.String)">
<h3>versionToLong</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">versionToLong</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Utility method to convert string representation of version into long</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - version</dd>
<dt>Returns:</dt>
<dd>version as long</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="versionToString(int)">
<h3>versionToString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">versionToString</span><wbr/><span class="parameters">(int version)</span></div>
<div class="block">Utility method to convert int representation of version into string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - version</dd>
<dt>Returns:</dt>
<dd>version as string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceID(com.nomagic.ci.persistence.IProject)">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Gets simplified resource id for given project.
 For remote project it returns project id, for local filename.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project descriptor</dd>
<dt>Returns:</dt>
<dd>filename or project id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceID(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceID</span><wbr/><span class="parameters">(<a href="project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> pd)</span></div>
<div class="block">Gets simplified resource id for given project descriptor. For remote project it returns project id, for local filename.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pd</code> - project descriptor</dd>
<dt>Returns:</dt>
<dd>filename or project id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceID(org.eclipse.emf.common.util.URI)">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceID</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Gets simplified resource id for given project location URI.
 For remote project it returns project id, for local filename.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - project location.</dd>
<dt>Returns:</dt>
<dd>filename or project id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedProjects(com.nomagic.ci.persistence.IProject)">
<h3>getAttachedProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</span> <span class="element-name">getAttachedProjects</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Returns projects those are attached directly to a given project.
 Primary attached project is ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of attached projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllAttachedProjects(com.nomagic.ci.persistence.IProject)">
<h3>getAllAttachedProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</span> <span class="element-name">getAllAttachedProjects</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Returns projects those are attached directly or indirectly to a given project.
 Primary attached project is ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of attached projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject)">
<h3>getAllAttachedProjectsIncludingPrimary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</span> <span class="element-name">getAllAttachedProjectsIncludingPrimary</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Returns projects those are attached directly or indirectly to a given project including primary project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of attached projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllAttachedProjects(java.util.Collection)">
<h3>getAllAttachedProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt;</span> <span class="element-name">getAllAttachedProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IAttachedProject&gt; projects)</span></div>
<div class="block">Returns projects those are attached directly or indirectly to a given project.
 Primary attached project is ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projects</code> - project projects</dd>
<dt>Returns:</dt>
<dd>collection of attached projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedProjectsIncludingPrimary(com.nomagic.ci.persistence.IProject)">
<h3>getAttachedProjectsIncludingPrimary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</span> <span class="element-name">getAttachedProjectsIncludingPrimary</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Returns projects those are attached directly to a given project.Primary attached project can be included also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>collection of attached projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoLoadKind(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">
<h3>getAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></span> <span class="element-name">getAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return load kind of given module in a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - project</dd>
<dd><code>project</code> - module</dd>
<dt>Returns:</dt>
<dd>load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoLoadKind(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration)">
<h3>getAutoLoadKind</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></span> <span class="element-name">getAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.decomposition.ProjectAttachmentConfiguration attachment)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use public static   AutoLoadKind getAutoLoadKind(  AbstractProjectAttachmentConfiguration attachment )</div>
</div>
<div class="block">Return load kind of module from given attachment</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachment</code> - attachment</dd>
<dt>Returns:</dt>
<dd>load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoLoadKind(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration)">
<h3>getAutoLoadKind</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></span> <span class="element-name">getAutoLoadKind</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration attachment)</span></div>
<div class="block">Return load kind of module from given attachment</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachment</code> - attachment</dd>
<dt>Returns:</dt>
<dd>load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachingProject(com.nomagic.ci.persistence.IProject)">
<h3>getAttachingProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getAttachingProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return first project where given project is attached. Primary project has always priority.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - given project</dd>
<dt>Returns:</dt>
<dd>first project where given module is attached.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachingProjects(com.nomagic.ci.persistence.IProject)">
<h3>getAttachingProjects</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</span> <span class="element-name">getAttachingProjects</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return all projects where given project is attached.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - given project.</dd>
<dt>Returns:</dt>
<dd>all projects where given module is attached.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwner(com.nomagic.ci.persistence.IProject)">
<h3>getOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getOwner</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAttachingProject(com.nomagic.ci.persistence.IProject)"><code>getAttachingProject(IProject)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getOwners(com.nomagic.ci.persistence.IProject)">
<h3>getOwners</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.IProject&gt;</span> <span class="element-name">getOwners</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAttachingProjects(com.nomagic.ci.persistence.IProject)"><code>getAttachingProjects(IProject)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getEMFURI(java.net.URI)">
<h3>getEMFURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">getEMFURI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Convert java net URI to emf uri</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - net uri</dd>
<dt>Returns:</dt>
<dd>emf uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachment(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">
<h3>getAttachment</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration</span> <span class="element-name">getAttachment</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject parent,
 com.nomagic.ci.persistence.IProject child)</span></div>
<div class="block">Return configuration which is used to attach one project to another</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - project which uses another project (directly)</dd>
<dd><code>child</code> - used directly project</dd>
<dt>Returns:</dt>
<dd>found <code>ProjectAttachmentConfiguration</code> (for local and teamwork projects) or
 <code>EsiProjectAttachmentConfiguration</code> (for Teamwork Cloud projects) or null if such not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURI(org.eclipse.emf.common.util.URI)">
<h3>getURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">getURI</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI emfUFI)</span></div>
<div class="block">Convert EMF uri to java.net.URI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>emfUFI</code> - emf uri</dd>
<dt>Returns:</dt>
<dd>java net uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.ci.persistence.IProject)">
<h3>getVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return version of given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>version or null if project has no version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFromTeamworkServer()">
<h3>isFromTeamworkServer</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFromTeamworkServer</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
<div class="block">Check if given project is from teamwork server.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is from server</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFromEsiServer(com.nomagic.ci.persistence.IProject)">
<h3>isFromEsiServer</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFromEsiServer</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if given project is from ESI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if project is from ESI</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote(com.nomagic.ci.persistence.IProject)">
<h3>isRemote</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if given project is remote - from teamwork server or ESI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if project is from server</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFromStandardProfile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFromStandardProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFromStandardProfile</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Checks, if the given element is a part of the Standard Profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true, if the given element is a part of the Standard Profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(com.nomagic.ci.persistence.IProject)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ci.persistence.IProject iProject)</span></div>
<div class="block">Returns MagicDraw project for primary or attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iProject</code> - primary or attached project</dd>
<dt>Returns:</dt>
<dd><a href="Project.html" title="class in com.nomagic.magicdraw.core"><code>Project</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMountPoint(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>getMountPoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.mounting.IMountPoint</span> <span class="element-name">getMountPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt; points,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> element)</span></div>
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
<section class="detail" id="getSharePoint(com.nomagic.ci.persistence.mounting.IMountPoint)">
<h3>getSharePoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.sharing.ISharePoint</span> <span class="element-name">getSharePoint</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.mounting.IMountPoint point)</span></div>
<div class="block">Find share point corresponding given mount point</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - mount point</dd>
<dt>Returns:</dt>
<dd>share point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="encodeTeamworkRemoteId(java.lang.String)">
<h3>encodeTeamworkRemoteId</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">encodeTeamworkRemoteId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> remoteId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
<div class="block">Encodes Teamwork remote ID</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>remoteId</code> - the raw (not encoded) remote ID</dd>
<dt>Returns:</dt>
<dd>encoded ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="decodeTeamworkRemoteId(java.lang.String)">
<h3>decodeTeamworkRemoteId</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">decodeTeamworkRemoteId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> remoteId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">teamwork server is end of life</div>
</div>
<div class="block">Decodes Teamwork remote ID</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>remoteId</code> - the encoded remote ID</dd>
<dt>Returns:</dt>
<dd>decoded (raw) remote ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isESIUri(org.eclipse.emf.common.util.URI)">
<h3>isESIUri</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isESIUri</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Checks if given <code>URI</code> is ESI project
 <code>URI</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - the <code>URI</code> to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> if given <code>URI</code> is ESI,
 <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isESIUri(java.net.URI)">
<h3>isESIUri</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isESIUri</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Checks if given <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net"><code>URI</code></a> is ESI project <code>URI</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - the <code>URI</code> to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> if given <code>URI</code> is ESI,
 <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementProxy(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isElementProxy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isElementProxy</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if given element is proxy or orphan proxy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> if given element is proxy or orphan proxy, otherwise - <code>false</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getESIRemoteId(org.eclipse.emf.common.util.URI)">
<h3>getESIRemoteId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getESIRemoteId</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Gets ESI remote ID</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - the <code>URI</code> to get remote ID
            for</dd>
<dt>Returns:</dt>
<dd>the remote ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getESIRemoteId(com.nomagic.ci.persistence.IProject)">
<h3>getESIRemoteId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getESIRemoteId</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Gets ESI remote ID for given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>the remote ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteId(org.eclipse.emf.common.util.URI)">
<h3>getRemoteId</h3>
<div class="member-signature"><span class="annotations">@CheckReturnValue
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteId</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Retrieves project remote id from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - remote project uri to check.</dd>
<dt>Returns:</dt>
<dd>remote project id from project uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMountPoints(com.nomagic.ci.persistence.IProject)">
<h3>getMountPoints</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</span> <span class="element-name">getMountPoints</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Gets all mount points in given project. Returns empty set if there are no mount points</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>non-<code>null</code> set of all <code>mount points</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMountPointsFor(com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IProject)">
<h3>getMountPointsFor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</span> <span class="element-name">getMountPointsFor</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject owner,
 com.nomagic.ci.persistence.IProject attachedProject)</span></div>
<div class="block">Gets mount points for given project, i.e. returns all mount points that are mounted share points of given project.
 Returns empty set if there are no mount points to return.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner</dd>
<dd><code>attachedProject</code> - the project to get mount points for</dd>
<dt>Returns:</dt>
<dd>non-<code>null</code> set of <code>mount points</code> for specific project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllMountPoints(com.nomagic.ci.persistence.IPrimaryProject)">
<h3>getAllMountPoints</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</span> <span class="element-name">getAllMountPoints</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject project)</span></div>
<div class="block">Return all mount points existing in given primary project (direct and not direct).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>all mount points from given project and from all attached</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(org.eclipse.emf.ecore.EObject)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 org.eclipse.emf.ecore.EObject object)</span></div>
<div class="block">Return project in which object resists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - object</dd>
<dt>Returns:</dt>
<dd>found project or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(org.eclipse.emf.ecore.resource.Resource)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 org.eclipse.emf.ecore.resource.Resource resource)</span></div>
<div class="block">Return project for a resource.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resource</code> - resource</dd>
<dt>Returns:</dt>
<dd>found project or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareVersions(com.nomagic.ci.persistence.versioning.IVersionDescriptor,com.nomagic.ci.persistence.versioning.IVersionDescriptor)">
<h3>compareVersions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">compareVersions</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor1,
 @CheckForNull
 com.nomagic.ci.persistence.versioning.IVersionDescriptor versionDescriptor2)</span></div>
<div class="block">Compare given versions descriptors. <em>The null descriptor is larger than not null.</em></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>versionDescriptor1</code> - first version descriptor (can be null).</dd>
<dd><code>versionDescriptor2</code> - second version descriptor (can be null).</dd>
<dt>Returns:</dt>
<dd>the value 0 if versions are equal; a value less than 0 if first version is less than second;
 and a value greater than 0 if first version is greater than second.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareVersionNumber(java.lang.String,java.lang.String)">
<h3>compareVersionNumber</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">compareVersionNumber</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> versionNumber1,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> versionNumber2)</span></div>
<div class="block">Compare given version numbers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>versionNumber1</code> - first version number.</dd>
<dd><code>versionNumber2</code> - second version number.</dd>
<dt>Returns:</dt>
<dd>the value 0 if versions are equal; a value less than 0 if first version is less than second;
 and a value greater than 0 if first version is greater than second.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachedProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.common.util.URI)">
<h3>getAttachedProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">getAttachedProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Look for direct or not direct attached project in a primary project of a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>uri</code> - uri</dd>
<dt>Returns:</dt>
<dd>found module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getElementFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElementFor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return element for a given base element. Returned element can be passed into other utility methods as EObject if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - base element</dd>
<dt>Returns:</dt>
<dd>model element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElementFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getModelElementFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">getModelElementFor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return element for a given base element. Returned element can be passed into other utility methods as EObject if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - base element</dd>
<dt>Returns:</dt>
<dd>model element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMountedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>isMountedPackage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMountedPackage</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> pck)</span></div>
<div class="block">Check if given package is a mounted(or is a shared root from some module)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pck</code> - package</dd>
<dt>Returns:</dt>
<dd>true if package is mounted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isModuleRoot(com.nomagic.ci.persistence.IAttachedProject,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isModuleRoot</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">boolean</span> <span class="element-name">isModuleRoot</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject iProject,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInternalVersion(com.nomagic.ci.persistence.IProject)">
<h3>getInternalVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getInternalVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Get internal version of project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCompatibleVersion(com.nomagic.ci.persistence.IProject)">
<h3>getCompatibleVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCompatibleVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Get compatible version of the project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>compatible version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStandardSystemProfile(com.nomagic.ci.persistence.IProject)">
<h3>isStandardSystemProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStandardSystemProfile</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if given project is a standard system profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if given project is a standard system profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStandardSystemProfile(com.nomagic.ci.persistence.DecompositionDescriptor)">
<h3>isStandardSystemProfile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStandardSystemProfile</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.DecompositionDescriptor project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">DecompositionDescriptor is not exposed into Open API</div>
</div>
<div class="block">Check if given project is a standard system profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if given project is a standard system profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoaded(com.nomagic.ci.persistence.IProject)">
<h3>isLoaded</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Checks if given project loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if given project is loaded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoadedOrLoading(com.nomagic.ci.persistence.IProject)">
<h3>isLoadedOrLoading</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLoadedOrLoading</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="isModule(com.nomagic.ci.persistence.DecompositionDescriptor)">
<h3>isModule</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.DecompositionDescriptor r)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">DecompositionDescriptor is not exposed into Open API</div>
</div>
<div class="block">Returns true if given project has shared points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - project descriptor to evaluate</dd>
<dt>Returns:</dt>
<dd>true if given project descriptor represents a module.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFromStandardProfile(org.eclipse.emf.ecore.EObject)">
<h3>isFromStandardProfile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFromStandardProfile</span><wbr/><span class="parameters">(@CheckForNull
 org.eclipse.emf.ecore.EObject element)</span></div>
<div class="block">Checks if element comes from standard profile</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be checked</dd>
<dt>Returns:</dt>
<dd>true if element comes from standard profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModifiedElements(com.nomagic.magicdraw.core.Project)">
<h3>getModifiedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getModifiedElements</span><wbr/><span class="parameters">(<a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Get modified elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to get elements of.</dd>
<dt>Returns:</dt>
<dd>modified elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExporterDescription(com.nomagic.ci.persistence.IProject)">
<h3>getExporterDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></span> <span class="element-name">getExporterDescription</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Provide information about project version and required resources/plugins for that project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>description of project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSaveID(com.nomagic.ci.persistence.IProject)">
<h3>getSaveID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSaveID</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Gets current save/commit id for given project.
 The value of the Save ID is a randomly generated unique UUID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>save id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToCacheLoaded(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription)">
<h3>addToCacheLoaded</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">addToCacheLoaded</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> xmiExporterDescription)</span></div>
<div class="block">Adds to cache just loaded modules/projects</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project/module</dd>
<dd><code>xmiExporterDescription</code> - project/module descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToCache(com.nomagic.ci.persistence.IProject,com.nomagic.persistence.XmiExporterDescription)">
<h3>addToCache</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">addToCache</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 @CheckForNull
 <a href="../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a> xmiExporterDescription)</span></div>
</section>
</li>
<li>
<section class="detail" id="isModuleUsageNew(com.nomagic.ci.persistence.IProject)">
<h3>isModuleUsageNew</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isModuleUsageNew</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject attachedProject)</span></div>
<div class="block">Check if attached project usage from primary project is new (not yet committed to server).
 This method does not support checking if the usage is new for Teamwork Server Project therefore
 it always returns <code>false</code> in that case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - the <code>IProject</code> of attached project</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the provided project is attached project, and it is a Teamwork Cloud Project
 and if the usage from primary project to attached project exists and if it is new (as defined above).
 Return <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleURI(java.net.URI)">
<h3>getVisibleURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleURI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Creates uri that can be shown in UI components</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - project location uri</dd>
<dt>Returns:</dt>
<dd>visible uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleURI(org.eclipse.emf.common.util.URI)">
<h3>getVisibleURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVisibleURI</span><wbr/><span class="parameters">(org.eclipse.emf.common.util.URI uri)</span></div>
<div class="block">Creates uri that can be shown in UI components</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - project location uri</dd>
<dt>Returns:</dt>
<dd>visible uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProjectNameValid(java.lang.String)">
<h3>isProjectNameValid</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isProjectNameValid</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectName)</span></div>
<div class="block">Checks if given project name is valid. Checks if either the given project name is reserved or
 has invalid characters</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectName</code> - the project name to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> if project name is valid, <code>false</code> otherwise</dd>
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
