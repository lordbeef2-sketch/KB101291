# JAVA OPENAPI: Project (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/Project.html
- source_path: `com/nomagic/magicdraw/core/Project.html`
- source_sha256: `c9be27305aa9f17834ff40e8bdd8dfb6d87ee2bf19044e9fd303669608fc3c4e`
- captured_utc: `2026-07-14T16:51:15.094123+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class Project

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
com.nomagic.magicdraw.core.Project

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`, `com.dassault_systemes.modeler.foundation.project.ModelElementProject`, `[BaseElement](../uml/BaseElement.html)`, `[MDElement](../uml/MDElement.html)`, `com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`, `com.nomagic.uml2.project.ElementProject`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`

@OpenApipublic classProject
extends com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
implements com.nomagic.uml2.project.ElementProject, [MDElement](../uml/MDElement.html)

The `Project` class represents main storage of all project data like: main package,
 all diagrams and diagram windows.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMMAND_EXECUTED](#COMMAND_EXECUTED)`
The any command (adding object, deleting object, changing specifications)
 executing event type and naming.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ACTIVATED](#DIAGRAM_ACTIVATED)`
The diagram focus on event type and naming.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_CLOSED](#DIAGRAM_CLOSED)`
The diagram window closing event type and naming.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_EDITED](#DIAGRAM_EDITED)`
Deprecated.
not used anymore
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_OPENED](#DIAGRAM_OPENED)`
The diagram window opening event type and naming.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_WINDOW_ACTIVATED](#DIAGRAM_WINDOW_ACTIVATED)`
The diagram window focus on event type and naming.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SELECTION_CHANGED](#SELECTION_CHANGED)`
Deprecated.
now SelectionProvider fires selection changed,
 use [`SelectionProvider.SelectionChangedListener`](../ui/SelectionProvider.SelectionChangedListener.html)
 The diagram objects selecting event type and naming.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addToProjectRepository](#addToProjectRepository(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Adds element into this project repository and removes it from previous
 project repository.
`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getActiveDiagram](#getActiveDiagram())()`
Returns currently active diagram.
`[Browser](../ui/browser/Browser.html)`
`[getBrowser](#getBrowser())()`
Get browser.
`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getDiagram](#getDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagramElement)`
Returns diagram presentation element for specified diagram model element.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagrams](#getDiagrams())()`
Returns all existing diagrams stored in this Project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)>`
`[getDiagrams](#getDiagrams(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Returns existing diagrams of given type stored in Project.
`[StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html)`
`[getDirtyType](#getDirtyType())()`
Returns project dirty type if project is dirty, otherwise - null.
`[BaseElement](../uml/BaseElement.html)`
`[getElementByID](#getElementByID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Return the element with given id.
`[ElementsFactory](../../uml2/impl/ElementsFactory.html)`
`[getElementsFactory](#getElementsFactory())()`
Provides UML elements factory
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileName](#getFileName())()`
Method returns file name of this project.
`[Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html)`
`[getModel](#getModel())()`
Deprecated.
deprecated because of ambiguity with historical API evolution
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getModels](#getModels())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns project name.
`[ProjectOptions](options/ProjectOptions.html)`
`[getOptions](#getOptions())()`
Getter for project options.
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getPrimaryModel](#getPrimaryModel())()`
Returns a primary model of this project.
`com.nomagic.ci.persistence.IPrimaryProject`
`[getPrimaryProject](#getPrimaryProject())()`
Primary project of MagicDraw project.
`static [Project](Project.html)`
`[getProject](#getProject(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Returns Project for given element
`static [Project](Project.html)`
`[getProject](#getProject(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> elements)`
Returns Project from first given element
`[ProxyManager](proxy/ProxyManager.html)`
`[getProxyManager](#getProxyManager())()`

`[AbstractRepository](../../uml2/ext/jmi/reflect/AbstractRepository.html)`
`[getRepository](#getRepository())()`
Get project repository.
`[RepositoryListenerRegistry](../../uml2/ext/jmi/RepositoryListenerRegistry.html)`
`[getRepositoryListenerRegistry](#getRepositoryListenerRegistry())()`
Return listener registry for repository.
`[SmartEventSupport](../../uml2/ext/jmi/smartlistener/SmartEventSupport.html)`
`[getSmartEventSupport](#getSmartEventSupport())()`
Returns registry that allows to register smart listener configurations by element type.
`[StateChangeHandler](../utils/StateChangeHandler.html)`
`[getStateChangeHandler](#getStateChangeHandler())()`

`[SymbolElementMap](../uml/symbols/SymbolElementMap.html)`
`[getSymbolElementMap](#getSymbolElementMap())()`
Get element symbol map.
`boolean`
`[isDirty](#isDirty())()`
Returns true if this project was modified after last save/load.
`boolean`
`[isDisposed](#isDisposed(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Check if given element is unregistered from project.
`static boolean`
`[isElementDisposed](#isElementDisposed(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Check if given element is unregistered from project.
`boolean`
`[isEsiProject](#isEsiProject())()`
Determines whether this is an ESI project
`boolean`
`[isRemote](#isRemote())()`
Returns the remote or not remote state of the project.
`void`
`[reSetDirty](#reSetDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(boolean dirty,
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)`
Marks this project modified and sets modification type without checking previous project's dirty type.
`void`
`[setDirty](#setDirty(boolean))(boolean dirty)`
Deprecated.
Use `[setDirty(boolean dirty, DirtyType dirtyType)](#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))`.
`void`
`[setDirty](#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(boolean dirty,
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)`
Marks this project modified and sets modification type depending on previous type.
Methods inherited from class com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
`getOptionalService, getService, getServiceProvider`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../uml/BaseElement.html)
`[canAdd](../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.project.ModelElementProject
`getOptionalService, getService, getServiceProvider`

============ FIELD DETAIL =========== 
Field Details
COMMAND_EXECUTED
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMMAND_EXECUTED
The any command (adding object, deleting object, changing specifications)
 executing event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.COMMAND_EXECUTED)
SELECTION_CHANGED
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SELECTION_CHANGED
Deprecated.
now SelectionProvider fires selection changed,
 use [`SelectionProvider.SelectionChangedListener`](../ui/SelectionProvider.SelectionChangedListener.html)
 The diagram objects selecting event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.SELECTION_CHANGED)
DIAGRAM_OPENED
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_OPENED
The diagram window opening event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_OPENED)
DIAGRAM_CLOSED
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_CLOSED
The diagram window closing event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_CLOSED)
DIAGRAM_EDITED
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_EDITED
Deprecated.
not used anymore
Any diagram properties editing event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_EDITED)
DIAGRAM_ACTIVATED
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ACTIVATED
The diagram focus on event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_ACTIVATED)
DIAGRAM_WINDOW_ACTIVATED
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_WINDOW_ACTIVATED
The diagram window focus on event type and naming.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_WINDOW_ACTIVATED)
 ============ METHOD DETAIL ========== 
Method Details
getProxyManager
@OpenApipublic [ProxyManager](proxy/ProxyManager.html) getProxyManager()
Returns:
proxy manager of the project
getBrowser
@OpenApipublic [Browser](../ui/browser/Browser.html) getBrowser()
Get browser.
Returns:
browser.
getOptions
@OpenApipublic [ProjectOptions](options/ProjectOptions.html) getOptions()
Getter for project options.
Returns:
project options
getActiveDiagram
@CheckForNull
@OpenApipublic [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) getActiveDiagram()
Returns currently active diagram.
Returns:
currently active diagram presentation element.
See Also:
[`DiagramPresentationElement`](../uml/symbols/DiagramPresentationElement.html)
getDiagrams
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> getDiagrams()
Returns all existing diagrams stored in this Project.
Returns:
all existing DiagramPresentationElements. The collection is unmodifiable.
See Also:
[`DiagramPresentationElement`](../uml/symbols/DiagramPresentationElement.html)
getDiagrams
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)> getDiagrams(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Returns existing diagrams of given type stored in Project.
Parameters:
`type` - the given diagrams type. Returns all diagrams if type is null.
Returns:
collection of all diagram views.
See Also:
[`DiagramPresentationElement`](../uml/symbols/DiagramPresentationElement.html)
getDiagram
@CheckForNull
@OpenApipublic [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) getDiagram([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagramElement)
Returns diagram presentation element for specified diagram model element.
Parameters:
`diagramElement` - diagram model element
Returns:
diagram presentation element.
getFileName
@CheckForNull
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileName()
Method returns file name of this project. If file name is undefined returns project name.
Returns:
file name of this project.
isRemote
@OpenApipublic boolean isRemote()
Returns the remote or not remote state of the project.
Returns:
true if project is a remote project, false otherwise.
isEsiProject
@OpenApipublic boolean isEsiProject()
Determines whether this is an ESI project
Returns:
`true` if ESI project, `false` otherwise
isDirty
@OpenApipublic boolean isDirty()
Returns true if this project was modified after last save/load.
Returns:
true if this project was modified after last save/load.
setDirty
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic void setDirty(boolean dirty)
Deprecated.
Use `[setDirty(boolean dirty, DirtyType dirtyType)](#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))`.
Marks this project modified.
Parameters:
`dirty` - new dirty flag.
setDirty
@OpenApipublic void setDirty(boolean dirty,
 @CheckForNull
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)
Marks this project modified and sets modification type depending on previous type.
Parameters:
`dirty` - new dirty flag.
`dirtyType` - specifies how much dirty is project.
 
If `dirtyType == null`, then default dirtyType
 value (`DirtyType.HARD_DIRTY`) is set.
 
If `dirty == true && dirtyType == DirtyType.SOFT_DIRTY` and
 project is already in state 
 `dirty == true && dirtyType == DirtyType.HARD_DIRTY`,
 then project's state is not going to be changed.
getDirtyType
@CheckForNull
@OpenApipublic [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) getDirtyType()
Returns project dirty type if project is dirty, otherwise - null.
Returns:
project dirty type
reSetDirty
@OpenApipublic void reSetDirty(boolean dirty,
 @CheckForNull
 [StateChangeHandler.DirtyType](../utils/StateChangeHandler.DirtyType.html) dirtyType)
Marks this project modified and sets modification type without checking previous project's dirty type.
Parameters:
`dirty` - new dirty flag.
`dirtyType` - specifies how much dirty is project.
 If `dirtyType == null`, then default dirtyType
 value (`DirtyType.HARD_DIRTY`) is set.
addToProjectRepository
@OpenApipublic void addToProjectRepository([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Adds element into this project repository and removes it from previous
 project repository. If element does not have an ID then it will be
 created. 
After this operation element can be retrieved from project by [`getElementByID(String)`](#getElementByID(java.lang.String)).
Parameters:
`element` - any element
getElementByID
@OpenApi
@CheckForNullpublic [BaseElement](../uml/BaseElement.html) getElementByID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Return the element with given id.
Specified by:
`getElementByID` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
Parameters:
`id` - the id of the element.
Returns:
the element with given id or null if element with such id is not registered in the project.
isElementDisposed
@OpenApipublic static boolean isElementDisposed(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)
Check if given element is unregistered from project.
Parameters:
`element` - element
Returns:
true if element is disposed
isDisposed
@OpenApipublic boolean isDisposed([BaseElement](../uml/BaseElement.html) element)
Check if given element is unregistered from project.
Specified by:
`isDisposed` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRegistry`
Parameters:
`element` - element
Returns:
true if element is disposed
getStateChangeHandler
@OpenApipublic [StateChangeHandler](../utils/StateChangeHandler.html) getStateChangeHandler()
Returns:
StateChangeHandler for this project.
getRepository
@OpenApipublic [AbstractRepository](../../uml2/ext/jmi/reflect/AbstractRepository.html) getRepository()
Get project repository.
Specified by:
`getRepository` in interface `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Returns:
repository.
getElementsFactory
@OpenApipublic [ElementsFactory](../../uml2/impl/ElementsFactory.html) getElementsFactory()
Description copied from interface: `com.nomagic.uml2.project.ElementProject`
Provides UML elements factory
Specified by:
`getElementsFactory` in interface `com.nomagic.uml2.project.ElementProject`
Returns:
Class for creating uml model elements.
getSmartEventSupport
@OpenApipublic [SmartEventSupport](../../uml2/ext/jmi/smartlistener/SmartEventSupport.html) getSmartEventSupport()
Returns registry that allows to register smart listener configurations by element type.
Returns:
smart listener registry.
getModel
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [Model](../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html) getModel()
Deprecated.
deprecated because of ambiguity with historical API evolution
Returns root primary model - root container of all model structure.
 This method should not be called anymore for TWC projects,
 because the returned model does not include the root models of modules (attached projects).
 [`getModels()`](#getModels()) or [`getPrimaryModel()`](#getPrimaryModel()) should be used instead as needed.
Returns:
root model element
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - in case root element is not a Model, but a Package
getPrimaryModel
@OpenApipublic [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getPrimaryModel()
Description copied from interface: `com.nomagic.uml2.project.ElementProject`
Returns a primary model of this project. Other models comes from modules (attached projects).
Specified by:
`getPrimaryModel` in interface `com.nomagic.uml2.project.ElementProject`
Returns:
primary model
See Also:
`ElementProject.getModels()`
getModels
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getModels()
getSymbolElementMap
@OpenApipublic [SymbolElementMap](../uml/symbols/SymbolElementMap.html) getSymbolElementMap()
Get element symbol map.
Returns:
symbol element map
getRepositoryListenerRegistry
@OpenApipublic [RepositoryListenerRegistry](../../uml2/ext/jmi/RepositoryListenerRegistry.html) getRepositoryListenerRegistry()
Return listener registry for repository.
Returns:
listener registry for repository.
getProject
@OpenApipublic static [Project](Project.html) getProject(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> elements)
Returns Project from first given element
Parameters:
`elements` - project elements
Returns:
project in which first given element exists
getProject
@OpenApipublic static [Project](Project.html) getProject(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Returns Project for given element
Parameters:
`element` - project element.
Returns:
project in which given element exists.
See Also:
`ProjectProvider`
getPrimaryProject
@OpenApipublic com.nomagic.ci.persistence.IPrimaryProject getPrimaryProject()
Primary project of MagicDraw project.
Returns:
primary project.
getName
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns project name.
Specified by:
`[getName](../uml/MDElement.html#getName())` in interface `[MDElement](../uml/MDElement.html)`
Returns:
project name.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class Project">Class Project</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
<div class="inheritance">com.nomagic.magicdraw.core.Project</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code>, <code>com.dassault_systemes.modeler.foundation.project.ModelElementProject</code>, <code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code>, <code>com.nomagic.uml2.project.ElementProject</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Project</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl
implements com.nomagic.uml2.project.ElementProject, <a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></span></div>
<div class="block">The <code>Project</code> class represents main storage of all project data like: main package,
 all diagrams and diagram windows.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMMAND_EXECUTED">COMMAND_EXECUTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The any command (adding object, deleting object, changing specifications)
 executing event type and naming.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_ACTIVATED">DIAGRAM_ACTIVATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The diagram focus on event type and naming.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_CLOSED">DIAGRAM_CLOSED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The diagram window closing event type and naming.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_EDITED">DIAGRAM_EDITED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_OPENED">DIAGRAM_OPENED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The diagram window opening event type and naming.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_WINDOW_ACTIVATED">DIAGRAM_WINDOW_ACTIVATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The diagram window focus on event type and naming.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SELECTION_CHANGED">SELECTION_CHANGED</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">now SelectionProvider fires selection changed,
 use <a href="../ui/SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui"><code>SelectionProvider.SelectionChangedListener</code></a>
 The diagram objects selecting event type and naming.</div>
</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToProjectRepository(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addToProjectRepository</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds element into this project repository and removes it from previous
 project repository.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveDiagram()">getActiveDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns currently active diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowser()">getBrowser</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagram</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagramElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagram presentation element for specified diagram model element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagrams()">getDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all existing diagrams stored in this Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagrams(java.lang.String)">getDiagrams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns existing diagrams of given type stored in Project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirtyType()">getDirtyType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project dirty type if project is dirty, otherwise - null.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementByID(java.lang.String)">getElementByID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the element with given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsFactory()">getElementsFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides UML elements factory</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileName()">getFileName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns file name of this project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getModel()">getModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of ambiguity with historical API evolution</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModels()">getModels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for project options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimaryModel()">getPrimaryModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a primary model of this project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.IPrimaryProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrimaryProject()">getPrimaryProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Primary project of MagicDraw project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(com.nomagic.magicdraw.uml.BaseElement)">getProject</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns Project for given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(java.util.Collection)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns Project from first given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="proxy/ProxyManager.html" title="interface in com.nomagic.magicdraw.core.proxy">ProxyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProxyManager()">getProxyManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepository()">getRepository</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/RepositoryListenerRegistry.html" title="interface in com.nomagic.uml2.ext.jmi">RepositoryListenerRegistry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepositoryListenerRegistry()">getRepositoryListenerRegistry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return listener registry for repository.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/jmi/smartlistener/SmartEventSupport.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartEventSupport</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSmartEventSupport()">getSmartEventSupport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns registry that allows to register smart listener configurations by element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../utils/StateChangeHandler.html" title="class in com.nomagic.magicdraw.utils">StateChangeHandler</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateChangeHandler()">getStateChangeHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/SymbolElementMap.html" title="class in com.nomagic.magicdraw.uml.symbols">SymbolElementMap</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolElementMap()">getSymbolElementMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get element symbol map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty()">isDirty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if this project was modified after last save/load.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisposed(com.nomagic.magicdraw.uml.BaseElement)">isDisposed</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given element is unregistered from project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isElementDisposed(com.dassault_systemes.modeler.foundation.model.ModelElement)">isElementDisposed</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if given element is unregistered from project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEsiProject()">isEsiProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether this is an ESI project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the remote or not remote state of the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reSetDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">reSetDirty</a><wbr/>(boolean dirty,
 <a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks this project modified and sets modification type without checking previous project's dirty type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setDirty(boolean)">setDirty</a><wbr/>(boolean dirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <code><a href="#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)"><code>setDirty(boolean dirty, DirtyType dirtyType)</code></a></code>.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">setDirty</a><wbr/>(boolean dirty,
 <a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks this project modified and sets modification type depending on previous type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl">Methods inherited from class com.dassault_systemes.modeler.foundation.project.ModelElementProjectImpl</h3>
<code>getOptionalService, getService, getServiceProvider</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.ModelElementProject">Methods inherited from interface com.dassault_systemes.modeler.foundation.project.ModelElementProject</h3>
<code>getOptionalService, getService, getServiceProvider</code></div>
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
<section class="detail" id="COMMAND_EXECUTED">
<h3>COMMAND_EXECUTED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMMAND_EXECUTED</span></div>
<div class="block">The any command (adding object, deleting object, changing specifications)
 executing event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.COMMAND_EXECUTED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SELECTION_CHANGED">
<h3>SELECTION_CHANGED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SELECTION_CHANGED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">now SelectionProvider fires selection changed,
 use <a href="../ui/SelectionProvider.SelectionChangedListener.html" title="interface in com.nomagic.magicdraw.ui"><code>SelectionProvider.SelectionChangedListener</code></a>
 The diagram objects selecting event type and naming.</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.SELECTION_CHANGED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_OPENED">
<h3>DIAGRAM_OPENED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_OPENED</span></div>
<div class="block">The diagram window opening event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_OPENED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CLOSED">
<h3>DIAGRAM_CLOSED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_CLOSED</span></div>
<div class="block">The diagram window closing event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_CLOSED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_EDITED">
<h3>DIAGRAM_EDITED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_EDITED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used anymore</div>
</div>
<div class="block">Any diagram properties editing event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_EDITED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ACTIVATED">
<h3>DIAGRAM_ACTIVATED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ACTIVATED</span></div>
<div class="block">The diagram focus on event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_ACTIVATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_WINDOW_ACTIVATED">
<h3>DIAGRAM_WINDOW_ACTIVATED</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_WINDOW_ACTIVATED</span></div>
<div class="block">The diagram window focus on event type and naming.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Project.DIAGRAM_WINDOW_ACTIVATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="getProxyManager()">
<h3>getProxyManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="proxy/ProxyManager.html" title="interface in com.nomagic.magicdraw.core.proxy">ProxyManager</a></span> <span class="element-name">getProxyManager</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>proxy manager of the project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBrowser()">
<h3>getBrowser</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></span> <span class="element-name">getBrowser</span>()</div>
<div class="block">Get browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>browser.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></span> <span class="element-name">getOptions</span>()</div>
<div class="block">Getter for project options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveDiagram()">
<h3>getActiveDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getActiveDiagram</span>()</div>
<div class="block">Returns currently active diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>currently active diagram presentation element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagrams()">
<h3>getDiagrams</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getDiagrams</span>()</div>
<div class="block">Returns all existing diagrams stored in this Project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all existing DiagramPresentationElements. The collection is unmodifiable.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagrams(java.lang.String)">
<h3>getDiagrams</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a>&gt;</span> <span class="element-name">getDiagrams</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Returns existing diagrams of given type stored in Project.
 <p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the given diagrams type. Returns all diagrams if type is null.</dd>
<dt>Returns:</dt>
<dd>collection of all diagram views.
 <p></p></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagram</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getDiagram</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagramElement)</span></div>
<div class="block">Returns diagram presentation element for specified diagram model element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramElement</code> - diagram model element</dd>
<dt>Returns:</dt>
<dd>diagram presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileName()">
<h3>getFileName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
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
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span>()</div>
<div class="block">Returns the remote or not remote state of the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project is a remote project, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEsiProject()">
<h3>isEsiProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEsiProject</span>()</div>
<div class="block">Determines whether this is an ESI project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if ESI project, <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirty()">
<h3>isDirty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span>()</div>
<div class="block">Returns true if this project was modified after last save/load.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this project was modified after last save/load.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(boolean)">
<h3>setDirty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(boolean dirty)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <code><a href="#setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)"><code>setDirty(boolean dirty, DirtyType dirtyType)</code></a></code>.</div>
</div>
<div class="block">Marks this project modified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - new dirty flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">
<h3>setDirty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(boolean dirty,
 @CheckForNull
 <a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</span></div>
<div class="block">Marks this project modified and sets modification type depending on previous type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - new dirty flag.</dd>
<dd><code>dirtyType</code> - specifies how much dirty is project.
                  <br/>If <code>dirtyType == null</code>, then default dirtyType
                  value (<code>DirtyType.HARD_DIRTY</code>) is set.
                  <br/>If <code>dirty == true &amp;&amp; dirtyType == DirtyType.SOFT_DIRTY</code> and
                  project is already in state <br/> <code>dirty == true &amp;&amp; dirtyType == DirtyType.HARD_DIRTY</code>,
                  then project's state is not going to be changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirtyType()">
<h3>getDirtyType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></span> <span class="element-name">getDirtyType</span>()</div>
<div class="block">Returns project dirty type if project is dirty, otherwise - null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project dirty type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reSetDirty(boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">
<h3>reSetDirty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reSetDirty</span><wbr/><span class="parameters">(boolean dirty,
 @CheckForNull
 <a href="../utils/StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</span></div>
<div class="block">Marks this project modified and sets modification type without checking previous project's dirty type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - new dirty flag.</dd>
<dd><code>dirtyType</code> - specifies how much dirty is project.
                  If <code>dirtyType == null</code>, then default dirtyType
                  value (<code>DirtyType.HARD_DIRTY</code>) is set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToProjectRepository(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addToProjectRepository</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToProjectRepository</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Adds element into this project repository and removes it from previous
 project repository. If element does not have an ID then it will be
 created. <br/>After this operation element can be retrieved from project by <a href="#getElementByID(java.lang.String)"><code>getElementByID(String)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - any element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementByID(java.lang.String)">
<h3>getElementByID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElementByID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Return the element with given id.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getElementByID</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the element.</dd>
<dt>Returns:</dt>
<dd>the element with given id or null if element with such id is not registered in the project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isElementDisposed(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>isElementDisposed</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isElementDisposed</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Check if given element is unregistered from project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisposed(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isDisposed</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisposed</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Check if given element is unregistered from project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isDisposed</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRegistry</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateChangeHandler()">
<h3>getStateChangeHandler</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../utils/StateChangeHandler.html" title="class in com.nomagic.magicdraw.utils">StateChangeHandler</a></span> <span class="element-name">getStateChangeHandler</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>StateChangeHandler for this project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepository()">
<h3>getRepository</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/jmi/reflect/AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></span> <span class="element-name">getRepository</span>()</div>
<div class="block">Get project repository.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getRepository</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></dd>
<dt>Returns:</dt>
<dd>repository.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsFactory()">
<h3>getElementsFactory</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a></span> <span class="element-name">getElementsFactory</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.project.ElementProject</code></span></div>
<div class="block">Provides UML elements factory</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getElementsFactory</code> in interface <code>com.nomagic.uml2.project.ElementProject</code></dd>
<dt>Returns:</dt>
<dd>Class for creating uml model elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmartEventSupport()">
<h3>getSmartEventSupport</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/jmi/smartlistener/SmartEventSupport.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartEventSupport</a></span> <span class="element-name">getSmartEventSupport</span>()</div>
<div class="block">Returns registry that allows to register smart listener configurations by element type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>smart listener registry.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModel()">
<h3>getModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></span> <span class="element-name">getModel</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated because of ambiguity with historical API evolution</div>
</div>
<div class="block">Returns root primary model - root container of all model structure.
 This method should not be called anymore for TWC projects,
 because the returned model does not include the root models of modules (attached projects).
 <a href="#getModels()"><code>getModels()</code></a> or <a href="#getPrimaryModel()"><code>getPrimaryModel()</code></a> should be used instead as needed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root model element</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - in case root element is not a Model, but a Package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimaryModel()">
<h3>getPrimaryModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getPrimaryModel</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.project.ElementProject</code></span></div>
<div class="block">Returns a primary model of this project. Other models comes from modules (attached projects).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPrimaryModel</code> in interface <code>com.nomagic.uml2.project.ElementProject</code></dd>
<dt>Returns:</dt>
<dd>primary model</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><code>ElementProject.getModels()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModels()">
<h3>getModels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getModels</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSymbolElementMap()">
<h3>getSymbolElementMap</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/SymbolElementMap.html" title="class in com.nomagic.magicdraw.uml.symbols">SymbolElementMap</a></span> <span class="element-name">getSymbolElementMap</span>()</div>
<div class="block">Get element symbol map.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol element map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepositoryListenerRegistry()">
<h3>getRepositoryListenerRegistry</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/jmi/RepositoryListenerRegistry.html" title="interface in com.nomagic.uml2.ext.jmi">RepositoryListenerRegistry</a></span> <span class="element-name">getRepositoryListenerRegistry</span>()</div>
<div class="block">Return listener registry for repository.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>listener registry for repository.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.util.Collection)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elements)</span></div>
<div class="block">Returns Project from first given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - project elements</dd>
<dt>Returns:</dt>
<dd>project in which first given element exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns Project for given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - project element.</dd>
<dt>Returns:</dt>
<dd>project in which given element exists.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><code>ProjectProvider</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimaryProject()">
<h3>getPrimaryProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.IPrimaryProject</span> <span class="element-name">getPrimaryProject</span>()</div>
<div class="block">Primary project of MagicDraw project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>primary project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns project name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/MDElement.html#getName()">getName</a></code> in interface <code><a href="../uml/MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Returns:</dt>
<dd>project name.</dd>
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
