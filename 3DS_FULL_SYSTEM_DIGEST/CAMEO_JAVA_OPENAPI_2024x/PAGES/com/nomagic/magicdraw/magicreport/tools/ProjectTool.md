# JAVA OPENAPI: ProjectTool (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/magicreport/tools/ProjectTool.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ProjectTool.html`
- source_sha256: `052e478633228b15a75498baac59d838f84e16a31bd896cca88838333ad4c86d`
- captured_utc: `2026-07-14T16:51:24.277244+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ProjectTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.Tool
com.nomagic.magicdraw.magicreport.tools.ProjectTool

All Implemented Interfaces:
`com.nomagic.magicreport.engine.ITool`, `com.nomagic.magicreport.IVariable`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classProjectTool
extends com.nomagic.magicreport.engine.Tool

A MagicDraw project wrapper.

Since:
Dec 7, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ProjectTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool
`com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.Tool
`context, properties`
Fields inherited from interface com.nomagic.magicreport.engine.ITool
`VOID`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllElementId](#getAllElementId())()`
Return the collection of all element id in the project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getAllModels](#getAllModels())()`
Returns a list of models in the project (the primary model of the project and all the models of the modules
 (attached projects)).
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getAuxiliaryResource](#getAuxiliaryResource())()`
Get list of auxiliary resource modules in the project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Get project description.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get project description from specified attached project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get project description from specified project module.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)>`
`[getDiagrams](#getDiagrams())()`
Return all existing diagrams stored in this Project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)>`
`[getDiagrams](#getDiagrams(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Return existing diagrams of given type stored in Project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDirectory](#getDirectory())()`
Return project directory.
`[BaseElement](../../uml/BaseElement.html)`
`[getElementByID](#getElementByID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Return the Element with given id.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getExtension](#getExtension())()`
Return project file extension.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileName](#getFileName())()`
Method returns file name of this project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLatestVersion](#getLatestVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get latest version of attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLatestVersion](#getLatestVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get latest version of project module
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getLocalModule](#getLocalModule())()`
Get list of used local modules in the project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getLocalModule](#getLocalModule(boolean))(boolean includeAuxiliary)`
Get list of used local modules in the project.
`[Model](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getModel](#getModel())()`
Deprecated.
use ProjectTool#getPrimaryModel()
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getModuleList](#getModuleList())()`
Get list of used local modules excluding auxiliary resource in the project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getModuleList](#getModuleList(boolean))(boolean includeAuxiliary)`
Get list of used server and local modules in the project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Return project name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)>`
`[getPresentationDiagrams](#getPresentationDiagrams())()`
Return all existing presentation diagrams stored in this Project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)>`
`[getPresentationDiagrams](#getPresentationDiagrams(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Return existing presentation diagrams of given type stored in Project.
`[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getPrimaryModel](#getPrimaryModel())()`
Returns the primary (main) model of the project (not including the ones from modules).
`[ProjectVersion](ProjectVersion.html)`
`[getProjectVersion](#getProjectVersion())()`
Get current project version of current project
`[ProjectVersion](ProjectVersion.html)`
`[getProjectVersion](#getProjectVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return project version of attached Project.
`[ProjectVersion](ProjectVersion.html)`
`[getProjectVersion](#getProjectVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get a project version of project module
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return user friendly representation string about given attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Return user friendly representation string about given project module
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRequiredVersion](#getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get required version of attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRequiredVersion](#getRequiredVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get required version of project module
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getServerModule](#getServerModule())()`
Get list of used server modules in the project exclude auxiliary resource.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getServerModule](#getServerModule(boolean))(boolean includeAuxiliary)`
Get list of used server modules in the project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getSharedModule](#getSharedModule())()`
Return a list of shared module from current project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getSharedModule](#getSharedModule(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return a list of shared module [`ProjectModule`](ProjectModule.html) from specified module.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)>`
`[getSharedModule](#getSharedModule(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Return a list of shared module from specified module.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`
Return project title.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUsedVersion](#getUsedVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get used version of attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUsedVersion](#getUsedVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get used version of project module
`long`
`[getVersion](#getVersion())()`
Return project version number.
`long`
`[getVersion](#getVersion(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Get current version of attached project.
`long`
`[getVersion](#getVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Get current version of project module
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersionList](#getVersionList())()`
Return a list of project version information from opened server project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersionList](#getVersionList(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
Return all project versions of attached project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersionList](#getVersionList(com.nomagic.magicdraw.magicreport.tools.ProjectModule))([ProjectModule](ProjectModule.html) projectModule)`
Return all project versions of project module.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions())()`
Return a list of project version information from opened server project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(boolean))(boolean ascendingOrder)`
Return a list of project version information from opened server project. 

 if ascendingOrder is true, the result will be sorted in ascending order.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../../core/project/ProjectDescriptor.html) projectDescriptor)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)`
Return a list of project version information from opened server project. 

 The result will be sorted by specified sortType.
`int`
`[getXmiVersion](#getXmiVersion())()`
Return the projects XMI version.
`boolean`
`[isDirty](#isDirty())()`
Return true if this project was modified after last save/load.
`boolean`
`[isRemote](#isRemote())()`
Return the remote or not remote state of the project.
Methods inherited from class com.nomagic.magicreport.engine.Tool
`clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.ITool
`clearTool`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ProjectTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectTool
public ProjectTool()
 ============ METHOD DETAIL ========== 
Method Details
getDiagrams
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> getDiagrams()
Return all existing diagrams stored in this Project.
Returns:
collection of Diagram instance.
getDiagrams
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> getDiagrams([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Return existing diagrams of given type stored in Project.
Parameters:
`type` - the given diagrams type.
Returns:
collection of Diagram instance.
getPresentationDiagrams
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)> getPresentationDiagrams()
Return all existing presentation diagrams stored in this Project.
Returns:
collection of diagram views.
getPresentationDiagrams
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html)> getPresentationDiagrams([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Return existing presentation diagrams of given type stored in Project.
Parameters:
`type` - the given diagrams type.
Returns:
collection of diagram views.
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Return project name.
Returns:
project name.
getTitle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()
Return project title.
Returns:
project title
getExtension
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getExtension()
Return project file extension.
Returns:
project file extension.
getDirectory
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDirectory()
Return project directory.
Returns:
project location directory.
getFileName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileName()
Method returns file name of this project. If file name is undefined returns project name.
Returns:
file name of this project.
isRemote
public boolean isRemote()
Return the remote or not remote state of the project.
Returns:
true if project is a remote project, false otherwise.
isDirty
public boolean isDirty()
Return true if this project was modified after last save/load.
Returns:
true if this project was modified after last save/load.
getElementByID
@CheckForNullpublic [BaseElement](../../uml/BaseElement.html) getElementByID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Return the Element with given id.
Parameters:
`id` - the id of the element.
Returns:
the Element with given id or null if Element with such id is not registered in the project.
getAllElementId
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllElementId()
Return the collection of all element id in the project.
Returns:
the collection of all element id in the project.
getXmiVersion
public int getXmiVersion()
Return the projects XMI version.
Returns:
xmi version
getModel
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [Model](../../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) getModel()
Deprecated.
use ProjectTool#getPrimaryModel()
Returns the primary (main) model of the project (not including the ones from modules). This method should
 not be called anymore for Cameo Enterprise Data Warehouse projects, because the returned model does not
 include the root models of modules (attached projects). [`getPrimaryModel()`](#getPrimaryModel()) should be used instead as
 needed.
Returns:
Model
getPrimaryModel
@CheckForNullpublic [Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getPrimaryModel()
Returns the primary (main) model of the project (not including the ones from modules).
Returns:
Model
getAllModels
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getAllModels()
Returns a list of models in the project (the primary model of the project and all the models of the modules
 (attached projects)).
Returns:
models.
getVersion
public long getVersion()
Return project version number.
Returns:
project version number
getProjectVersion
public [ProjectVersion](ProjectVersion.html) getProjectVersion()
Get current project version of current project
Returns:
a current [`ProjectVersion`](ProjectVersion.html) of current project
getVersions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions()
Return a list of project version information from opened server project.
 The result will be sorted in descending order.
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)
Return a list of project version information from opened server project. 

 The result will be sorted by specified sortType.
Parameters:
`sortType` - type of sorting. Specify "asc" sort in ascending order. Default is descending sort.
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions(boolean ascendingOrder)
Return a list of project version information from opened server project. 

 if ascendingOrder is true, the result will be sorted in ascending order.
Parameters:
`ascendingOrder` - true to sort in ascending order
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersionList
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersionList()
Return a list of project version information from opened server project.
Returns:
List of [`ProjectVersion`](ProjectVersion.html)
getVersions
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions([ProjectDescriptor](../../core/project/ProjectDescriptor.html) projectDescriptor)
getVersion
public long getVersion([ProjectModule](ProjectModule.html) projectModule)
Get current version of project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
current version
getVersionList
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersionList(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return all project versions of attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
list of [`ProjectVersion`](ProjectVersion.html) of attached project
getVersionList
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersionList([ProjectModule](ProjectModule.html) projectModule)
Return all project versions of project module.
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
list of [`ProjectVersion`](ProjectVersion.html) of project module
getVersion
public long getVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get current version of attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
current version
getProjectVersion
public [ProjectVersion](ProjectVersion.html) getProjectVersion([ProjectModule](ProjectModule.html) projectModule)
Get a project version of project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
a [`ProjectVersion`](ProjectVersion.html) of project module
getProjectVersion
public [ProjectVersion](ProjectVersion.html) getProjectVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return project version of attached Project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
a [`ProjectVersion`](ProjectVersion.html) of specified attached project
getRepresentationString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationString([ProjectModule](ProjectModule.html) projectModule)
Return user friendly representation string about given project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
user friendly project representation
getRepresentationString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationString(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return user friendly representation string about given attached project
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
user friendly project representation
getUsedVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUsedVersion([ProjectModule](ProjectModule.html) projectModule)
Get used version of project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
used version
getUsedVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUsedVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get used version of attached project
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
used version
getRequiredVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRequiredVersion([ProjectModule](ProjectModule.html) projectModule)
Get required version of project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
required version
getRequiredVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get required version of attached project
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
required version
getLatestVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLatestVersion([ProjectModule](ProjectModule.html) projectModule)
Get latest version of project module
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
required version
getLatestVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLatestVersion(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get latest version of attached project
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
required version
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Get project description.
Returns:
project description
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Get project description from specified attached project.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
project description
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription([ProjectModule](ProjectModule.html) projectModule)
Get project description from specified project module.
Parameters:
`projectModule` - projectModule [`ProjectModule`](ProjectModule.html)
Returns:
project description
getSharedModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getSharedModule()
Return a list of shared module from current project.
Returns:
a list of [`ProjectModule`](ProjectModule.html)
getSharedModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getSharedModule([ProjectModule](ProjectModule.html) projectModule)
Return a list of shared module from specified module.
Parameters:
`projectModule` - a [`ProjectModule`](ProjectModule.html)
Returns:
a list of [`ProjectModule`](ProjectModule.html)
getSharedModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getSharedModule(com.nomagic.ci.persistence.IAttachedProject attachedProject)
Return a list of shared module [`ProjectModule`](ProjectModule.html) from specified module.
Parameters:
`attachedProject` - an `IAttachedProject`
Returns:
a list of [`ProjectModule`](ProjectModule.html)
getModuleList
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getModuleList()
Get list of used local modules excluding auxiliary resource in the project.
Returns:
list of used server and local [`ProjectModule`](ProjectModule.html)
getModuleList
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getModuleList(boolean includeAuxiliary)
Get list of used server and local modules in the project.
Parameters:
`includeAuxiliary` - if true, the auxiliary resources will be included. 
Default value is False.
Returns:
list of used server and local [`ProjectModule`](ProjectModule.html)
getServerModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getServerModule()
Get list of used server modules in the project exclude auxiliary resource.
Returns:
list of used server modules [`ProjectModule`](ProjectModule.html)
getServerModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getServerModule(boolean includeAuxiliary)
Get list of used server modules in the project.
Parameters:
`includeAuxiliary` - if true, the auxiliary resources will be included. 
Default value is False.
Returns:
list of used server [`ProjectModule`](ProjectModule.html)
getLocalModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getLocalModule()
Get list of used local modules in the project.
Returns:
list of used local [`ProjectModule`](ProjectModule.html)
getLocalModule
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getLocalModule(boolean includeAuxiliary)
Get list of used local modules in the project.
Parameters:
`includeAuxiliary` - if true, the auxiliary resources will be included. 
Default value is False.
Returns:
list of used local [`ProjectModule`](ProjectModule.html)
getAuxiliaryResource
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ProjectModule](ProjectModule.html)> getAuxiliaryResource()
Get list of auxiliary resource modules in the project.
Returns:
list of [`ProjectModule`](ProjectModule.html) that are auxiliary resources.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ProjectTool">Class ProjectTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.Tool
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ProjectTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicreport.engine.ITool</code>, <code>com.nomagic.magicreport.IVariable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectTool</span>
<span class="extends-implements">extends com.nomagic.magicreport.engine.Tool</span></div>
<div class="block">A MagicDraw project wrapper.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 7, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ProjectTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool</h2>
<code>com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void</code></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains a context name.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>context, properties</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>VOID</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectTool</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllElementId()">getAllElementId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the collection of all element id in the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllModels()">getAllModels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of models in the project (the primary model of the project and all the models of the modules
 (attached projects)).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAuxiliaryResource()">getAuxiliaryResource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of auxiliary resource modules in the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription(com.nomagic.ci.persistence.IAttachedProject)">getDescription</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project description from specified attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getDescription</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project description from specified project module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagrams()">getDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return all existing diagrams stored in this Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagrams(java.lang.String)">getDiagrams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return existing diagrams of given type stored in Project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectory()">getDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project directory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByID(java.lang.String)">getElementByID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the Element with given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtension()">getExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project file extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileName()">getFileName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns file name of this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLatestVersion(com.nomagic.ci.persistence.IAttachedProject)">getLatestVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get latest version of attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLatestVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getLatestVersion</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get latest version of project module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocalModule()">getLocalModule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used local modules in the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocalModule(boolean)">getLocalModule</a><wbr/>(boolean includeAuxiliary)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used local modules in the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getModel()">getModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProjectTool#getPrimaryModel()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModuleList()">getModuleList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used local modules excluding auxiliary resource in the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModuleList(boolean)">getModuleList</a><wbr/>(boolean includeAuxiliary)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used server and local modules in the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationDiagrams()">getPresentationDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return all existing presentation diagrams stored in this Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationDiagrams(java.lang.String)">getPresentationDiagrams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return existing presentation diagrams of given type stored in Project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimaryModel()">getPrimaryModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the primary (main) model of the project (not including the ones from modules).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectVersion()">getProjectVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current project version of current project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectVersion(com.nomagic.ci.persistence.IAttachedProject)">getProjectVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project version of attached Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getProjectVersion</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get a project version of project module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationString(com.nomagic.ci.persistence.IAttachedProject)">getRepresentationString</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return user friendly representation string about given attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationString(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getRepresentationString</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return user friendly representation string about given project module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject)">getRequiredVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get required version of attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getRequiredVersion</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get required version of project module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getServerModule()">getServerModule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used server modules in the project exclude auxiliary resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getServerModule(boolean)">getServerModule</a><wbr/>(boolean includeAuxiliary)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of used server modules in the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedModule()">getSharedModule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of shared module from current project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedModule(com.nomagic.ci.persistence.IAttachedProject)">getSharedModule</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of shared module <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a> from specified module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSharedModule(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getSharedModule</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of shared module from specified module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project title.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedVersion(com.nomagic.ci.persistence.IAttachedProject)">getUsedVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get used version of attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getUsedVersion</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get used version of project module</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project version number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion(com.nomagic.ci.persistence.IAttachedProject)">getVersion</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current version of attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getVersion</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current version of project module</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionList()">getVersionList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionList(com.nomagic.ci.persistence.IAttachedProject)">getVersionList</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return all project versions of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionList(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">getVersionList</a><wbr/>(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return all project versions of project module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions()">getVersions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(boolean)">getVersions</a><wbr/>(boolean ascendingOrder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.<br/>
 if ascendingOrder is true, the result will be sorted in ascending order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getVersions</a><wbr/>(<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(java.lang.String)">getVersions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted by specified sortType.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getXmiVersion()">getXmiVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the projects XMI version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty()">isDirty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if this project was modified after last save/load.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the remote or not remote state of the project.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>clearTool</code></div>
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
<section class="detail" id="CONTEXT_NAME">
<h3>CONTEXT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ProjectTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<h3>ProjectTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectTool</span>()</div>
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
<section class="detail" id="getDiagrams()">
<h3>getDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">getDiagrams</span>()</div>
<div class="block">Return all existing diagrams stored in this Project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of Diagram instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagrams(java.lang.String)">
<h3>getDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">getDiagrams</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Return existing diagrams of given type stored in Project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the given diagrams type.</dd>
<dt>Returns:</dt>
<dd>collection of Diagram instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationDiagrams()">
<h3>getPresentationDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getPresentationDiagrams</span>()</div>
<div class="block">Return all existing presentation diagrams stored in this Project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of diagram views.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationDiagrams(java.lang.String)">
<h3>getPresentationDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getPresentationDiagrams</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Return existing presentation diagrams of given type stored in Project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the given diagrams type.</dd>
<dt>Returns:</dt>
<dd>collection of diagram views.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Return project name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<div class="block">Return project title.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtension()">
<h3>getExtension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExtension</span>()</div>
<div class="block">Return project file extension.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project file extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectory()">
<h3>getDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDirectory</span>()</div>
<div class="block">Return project directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project location directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileName()">
<h3>getFileName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileName</span>()</div>
<div class="block">Method returns file name of this project. If file name is undefined returns project name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>file name of this project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote()">
<h3>isRemote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span>()</div>
<div class="block">Return the remote or not remote state of the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is a remote project, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirty()">
<h3>isDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span>()</div>
<div class="block">Return true if this project was modified after last save/load.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this project was modified after last save/load.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementByID(java.lang.String)">
<h3>getElementByID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElementByID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Return the Element with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the element.</dd>
<dt>Returns:</dt>
<dd>the Element with given id or null if Element with such id is not registered in the project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllElementId()">
<h3>getAllElementId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllElementId</span>()</div>
<div class="block">Return the collection of all element id in the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the collection of all element id in the project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getXmiVersion()">
<h3>getXmiVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getXmiVersion</span>()</div>
<div class="block">Return the projects XMI version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>xmi version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModel()">
<h3>getModel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getModel</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ProjectTool#getPrimaryModel()</div>
</div>
<div class="block">Returns the primary (main) model of the project (not including the ones from modules). This method should
 not be called anymore for Cameo Enterprise Data Warehouse projects, because the returned model does not
 include the root models of modules (attached projects). <a href="#getPrimaryModel()"><code>getPrimaryModel()</code></a> should be used instead as
 needed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimaryModel()">
<h3>getPrimaryModel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getPrimaryModel</span>()</div>
<div class="block">Returns the primary (main) model of the project (not including the ones from modules).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllModels()">
<h3>getAllModels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getAllModels</span>()</div>
<div class="block">Returns a list of models in the project (the primary model of the project and all the models of the modules
 (attached projects)).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>models.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getVersion</span>()</div>
<div class="block">Return project version number.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project version number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectVersion()">
<h3>getProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></span> <span class="element-name">getProjectVersion</span>()</div>
<div class="block">Get current project version of current project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a current <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of current project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions()">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span>()</div>
<div class="block">Return a list of project version information from opened server project.
 The result will be sorted in descending order.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(java.lang.String)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</span></div>
<div class="block">Return a list of project version information from opened server project.<br/>
 The result will be sorted by specified sortType.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortType</code> - type of sorting. Specify "asc" sort in ascending order. Default is descending sort.</dd>
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(boolean)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(boolean ascendingOrder)</span></div>
<div class="block">Return a list of project version information from opened server project.<br/>
 if ascendingOrder is true, the result will be sorted in ascending order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ascendingOrder</code> - true to sort in ascending order</dd>
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionList()">
<h3>getVersionList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersionList</span>()</div>
<div class="block">Return a list of project version information from opened server project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>List of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> projectDescriptor)</span></div>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get current version of project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>current version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionList(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getVersionList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersionList</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return all project versions of attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionList(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getVersionList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersionList</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Return all project versions of project module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of project module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get current version of attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>current version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></span> <span class="element-name">getProjectVersion</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get a project version of project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>a <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of project module</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></span> <span class="element-name">getProjectVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return project version of attached Project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>a <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of specified attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Return user friendly representation string about given project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>user friendly project representation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
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
<section class="detail" id="getUsedVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getUsedVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUsedVersion</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get used version of project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>used version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getUsedVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUsedVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get used version of attached project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>used version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getRequiredVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredVersion</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get required version of project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getRequiredVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get required version of attached project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLatestVersion(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getLatestVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLatestVersion</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get latest version of project module</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLatestVersion(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getLatestVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLatestVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get latest version of attached project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Get project description.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Get project description from specified attached project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>project description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Get project description from specified project module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - projectModule <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>project description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedModule()">
<h3>getSharedModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getSharedModule</span>()</div>
<div class="block">Return a list of shared module from current project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedModule(com.nomagic.magicdraw.magicreport.tools.ProjectModule)">
<h3>getSharedModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getSharedModule</span><wbr/><span class="parameters">(<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a> projectModule)</span></div>
<div class="block">Return a list of shared module from specified module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectModule</code> - a <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
<dt>Returns:</dt>
<dd>a list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSharedModule(com.nomagic.ci.persistence.IAttachedProject)">
<h3>getSharedModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getSharedModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
<div class="block">Return a list of shared module <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a> from specified module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedProject</code> - an <code>IAttachedProject</code></dd>
<dt>Returns:</dt>
<dd>a list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModuleList()">
<h3>getModuleList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getModuleList</span>()</div>
<div class="block">Get list of used local modules excluding auxiliary resource in the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of used server and local <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModuleList(boolean)">
<h3>getModuleList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getModuleList</span><wbr/><span class="parameters">(boolean includeAuxiliary)</span></div>
<div class="block">Get list of used server and local modules in the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeAuxiliary</code> - if true, the auxiliary resources will be included. <br/>Default value is False.</dd>
<dt>Returns:</dt>
<dd>list of used server and local <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getServerModule()">
<h3>getServerModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getServerModule</span>()</div>
<div class="block">Get list of used server modules in the project exclude auxiliary resource.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of used server modules <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getServerModule(boolean)">
<h3>getServerModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getServerModule</span><wbr/><span class="parameters">(boolean includeAuxiliary)</span></div>
<div class="block">Get list of used server modules in the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeAuxiliary</code> - if true, the auxiliary resources will be included. <br/>Default value is False.</dd>
<dt>Returns:</dt>
<dd>list of used server <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalModule()">
<h3>getLocalModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getLocalModule</span>()</div>
<div class="block">Get list of used local modules in the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of used local <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalModule(boolean)">
<h3>getLocalModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getLocalModule</span><wbr/><span class="parameters">(boolean includeAuxiliary)</span></div>
<div class="block">Get list of used local modules in the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeAuxiliary</code> - if true, the auxiliary resources will be included. <br/>Default value is False.</dd>
<dt>Returns:</dt>
<dd>list of used local <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAuxiliaryResource()">
<h3>getAuxiliaryResource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectModule</a>&gt;</span> <span class="element-name">getAuxiliaryResource</span>()</div>
<div class="block">Get list of auxiliary resource modules in the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of <a href="ProjectModule.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectModule</code></a> that are auxiliary resources.</dd>
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
